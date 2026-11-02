"""Controlla le domande di un quiz e monta lo script di Google Apps Script.

Uso:
    python3 controlla_quiz.py domande.json [-o genera-form.js] [--modello percorso.js]

Il file domande.json ha questa forma:
    {"config": {"titolo": "...", "descrizione": "..."},
     "domande": [ {...}, {...} ]}

Lo script controlla la FORMA delle domande (tipi, indici, opzioni, punti).
Non controlla che le risposte siano giuste: quella revisione resta al docente.
Se non trova errori, inserisce CONFIG e DOMANDE nel modello
assets/genera-form-quiz.js e scrive lo script completo da incollare
su script.google.com. Usa solo la libreria standard e non va in rete.
"""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

TIPI = {
    "text", "paragraph", "multipleChoice", "list", "checkbox", "scale",
    "grid", "checkboxGrid", "sectionHeader", "pageBreak", "image", "video",
}
SCELTA_SINGOLA = {"multipleChoice", "list"}
CHIAVI = {
    "tipo", "titolo", "descrizione", "obbligatoria", "punti", "opzioni",
    "rispostaCorretta", "feedback", "min", "max", "etichettaMin",
    "etichettaMax", "righe", "colonne", "url",
}
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
TELEFONO = re.compile(r"\b(?:\+39\s?)?3\d{2}[\s.-]?\d{3}[\s.-]?\d{3,4}\b")
MODELLO = Path(__file__).resolve().parent.parent / "assets" / "genera-form-quiz.js"


def testo_valido(x):
    return isinstance(x, str) and x.strip() != ""


def controlla_feedback(fb, dove, errori):
    if fb is None:
        return
    if not isinstance(fb, dict):
        errori.append(f"{dove}: 'feedback' deve essere un oggetto con corretto, errato o generale.")
        return
    for chiave, valore in fb.items():
        if chiave not in {"corretto", "errato", "generale"}:
            errori.append(f"{dove}: nel feedback la chiave '{chiave}' non esiste (usa corretto, errato, generale).")
            continue
        if not isinstance(valore, dict) or not testo_valido(valore.get("testo")):
            errori.append(f"{dove}: feedback.{chiave} deve avere un campo 'testo' non vuoto.")


def controlla_domanda(i, d, errori, avvisi):
    dove = f"Voce {i + 1}"
    if not isinstance(d, dict):
        errori.append(f"{dove}: non è un oggetto.")
        return
    tipo = d.get("tipo")
    if tipo not in TIPI:
        errori.append(f"{dove}: tipo '{tipo}' non ammesso. Tipi ammessi: {', '.join(sorted(TIPI))}.")
        return
    dove = f"Voce {i + 1} ({tipo})"

    for chiave in d:
        if chiave not in CHIAVI:
            avvisi.append(f"{dove}: la chiave '{chiave}' non è usata dallo script e verrà ignorata.")

    if tipo not in {"image", "video"} and not testo_valido(d.get("titolo")):
        errori.append(f"{dove}: manca il titolo.")

    punti = d.get("punti", 0)
    if not isinstance(punti, int) or isinstance(punti, bool) or punti < 0:
        errori.append(f"{dove}: 'punti' deve essere un numero intero da 0 in su.")
        punti = 0

    if "obbligatoria" in d and not isinstance(d["obbligatoria"], bool):
        errori.append(f"{dove}: 'obbligatoria' deve essere true o false.")

    controlla_feedback(d.get("feedback"), dove, errori)

    if tipo in SCELTA_SINGOLA or tipo == "checkbox":
        opzioni = d.get("opzioni")
        if not isinstance(opzioni, list) or len(opzioni) < 2 or not all(testo_valido(o) for o in opzioni):
            errori.append(f"{dove}: servono almeno 2 opzioni, tutte con un testo.")
            return
        normali = [o.strip().lower() for o in opzioni]
        if len(set(normali)) != len(normali):
            errori.append(f"{dove}: ci sono opzioni ripetute.")
        corretta = d.get("rispostaCorretta")
        indici = corretta if tipo == "checkbox" and isinstance(corretta, list) else [corretta]
        if corretta is None:
            if punti > 0:
                errori.append(f"{dove}: ha {punti} punti ma nessuna 'rispostaCorretta'.")
        elif not all(isinstance(k, int) and not isinstance(k, bool) and 0 <= k < len(opzioni) for k in indici):
            errori.append(
                f"{dove}: 'rispostaCorretta' deve essere un indice da 0 a {len(opzioni) - 1} "
                f"(0 è la prima opzione){'; per checkbox una lista di indici' if tipo == 'checkbox' else ''}."
            )
        elif tipo == "checkbox" and len(set(indici)) != len(indici):
            errori.append(f"{dove}: in 'rispostaCorretta' c'è un indice ripetuto.")
        elif tipo in SCELTA_SINGOLA:
            giusta = len(opzioni[corretta])
            altre = [len(o) for k, o in enumerate(opzioni) if k != corretta]
            if altre and giusta > 1.5 * (sum(altre) / len(altre)):
                avvisi.append(f"{dove}: la risposta corretta è molto più lunga delle altre, e si indovina.")
        if punti > 0 and not (d.get("feedback") or {}).get("errato"):
            avvisi.append(f"{dove}: manca il feedback per chi sbaglia.")

    elif tipo == "scale":
        lo, hi = d.get("min", 1), d.get("max", 5)
        if lo not in (0, 1) or not isinstance(hi, int) or not 3 <= hi <= 10:
            errori.append(f"{dove}: in Moduli la scala parte da 0 o 1 e arriva a un valore da 3 a 10.")

    elif tipo in {"grid", "checkboxGrid"}:
        for chiave in ("righe", "colonne"):
            v = d.get(chiave)
            if not isinstance(v, list) or not v or not all(testo_valido(x) for x in v):
                errori.append(f"{dove}: '{chiave}' deve essere una lista di testi non vuota.")

    elif tipo in {"image", "video"}:
        url = d.get("url")
        if not (isinstance(url, str) and url.startswith(("http://", "https://"))):
            errori.append(f"{dove}: serve un 'url' che inizi con https://.")


def controlla(dati):
    errori, avvisi = [], []
    if not isinstance(dati, dict):
        return ["Il file deve contenere un oggetto con 'config' e 'domande'."], []
    config = dati.get("config")
    if not isinstance(config, dict) or not testo_valido(config.get("titolo")):
        errori.append("Manca config.titolo, il titolo del Modulo.")
    domande = dati.get("domande")
    if not isinstance(domande, list) or not domande:
        errori.append("La lista 'domande' è vuota o manca.")
        return errori, avvisi

    for i, d in enumerate(domande):
        controlla_domanda(i, d, errori, avvisi)

    titoli = Counter(d.get("titolo", "").strip().lower() for d in domande
                     if isinstance(d, dict) and d.get("tipo") not in {"pageBreak", "sectionHeader", "image", "video"})
    for t, n in titoli.items():
        if t and n > 1:
            avvisi.append(f"La domanda «{t[:60]}» compare {n} volte.")

    singole = [d for d in domande if isinstance(d, dict) and d.get("tipo") in SCELTA_SINGOLA
               and isinstance(d.get("rispostaCorretta"), int)]
    if len(singole) >= 4:
        conta = Counter(d["rispostaCorretta"] for d in singole)
        indice, quante = conta.most_common(1)[0]
        if quante / len(singole) > 0.6:
            avvisi.append(
                f"In {quante} domande su {len(singole)} la risposta giusta è l'opzione {indice + 1}: "
                "conviene mescolare l'ordine."
            )

    if not any(isinstance(d, dict) and isinstance(d.get("punti"), int) and d.get("punti", 0) > 0 for d in domande):
        avvisi.append("Nessuna domanda ha punti: il Modulo sarà un questionario senza correzione automatica.")

    testo = json.dumps(dati, ensure_ascii=False)
    if EMAIL.search(testo) or TELEFONO.search(testo):
        errori.append("Il quiz contiene un indirizzo email o un numero di telefono: toglilo prima di procedere.")

    return errori, avvisi


def monta(dati, modello):
    codice = modello.read_text(encoding="utf-8")
    if "const CONFIG = __CONFIG__;" not in codice or "const DOMANDE = __DOMANDE__;" not in codice:
        raise ValueError("Il modello non contiene le righe con i segnaposto __CONFIG__ e __DOMANDE__.")
    config = {"titolo": dati["config"]["titolo"], "descrizione": dati["config"].get("descrizione", "")}
    codice = codice.replace("const CONFIG = __CONFIG__;",
                            "const CONFIG = " + json.dumps(config, ensure_ascii=False, indent=2) + ";")
    return codice.replace("const DOMANDE = __DOMANDE__;",
                          "const DOMANDE = " + json.dumps(dati["domande"], ensure_ascii=False, indent=2) + ";")


def main():
    p = argparse.ArgumentParser(description="Controlla un quiz e monta lo script per Google Moduli.")
    p.add_argument("domande", help="file JSON con config e domande")
    p.add_argument("-o", "--output", default="genera-form.js", help="file dello script completo")
    p.add_argument("--modello", default=str(MODELLO), help="modello dello script Apps Script")
    a = p.parse_args()

    try:
        dati = json.loads(Path(a.domande).read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"ERRORE: il file non è JSON valido (riga {e.lineno}, colonna {e.colno}): {e.msg}")
        return 1

    errori, avvisi = controlla(dati)
    domande = dati.get("domande") or []
    print(f"Voci controllate: {len(domande)}")
    for e in errori:
        print(f"ERRORE: {e}")
    for w in avvisi:
        print(f"AVVISO: {w}")
    if errori:
        print("Script non generato: correggi gli errori e riprova.")
        return 1

    Path(a.output).write_text(monta(dati, Path(a.modello)), encoding="utf-8")
    print(f"OK: script completo scritto in {a.output}")
    print("Ricorda: lo script controlla la forma, non la correttezza delle risposte.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
