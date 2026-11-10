"""La spia: mostra in diretta quali file tocca Antigravity mentre lavora.

Uso (in un terminale, lasciandolo aperto accanto ad Antigravity):
    python3 spia.py                      solo ~/.gemini
    python3 spia.py ~/antigravity-corso  ~/.gemini e la cartella del progetto

Su Windows: py spia.py  oppure  python spia.py
Ctrl+C per fermarla: stampa il riepilogo dei file toccati.

Legge soltanto: non modifica niente. Il contenuto dei token e delle chiavi
non viene mai mostrato.
"""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

GEMINI = Path.home() / ".gemini"
SALTA = {"bin", "cache", "crashes", "node_modules", ".git"}  # rumore o file enormi
RIPETIZIONE = 8  # secondi: lo stesso file modificato di continuo si stampa una volta
SEGRETI = ("token", "secret", "password", "key", "credential", "oauth", "chiave")

COLORI = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None
def c(testo, codice):
    return f"\033[{codice}m{testo}\033[0m" if COLORI else testo

# Da percorso (relativo a ~/.gemini) a spiegazione. Vince la prima che combacia.
ETICHETTE = [
    ("config/projects/", "cartelle e permessi del progetto"),
    ("config/sidecars/", "Automazioni"),
    ("jetski/sidecars/", "Automazioni (copia interna)"),
    ("config/mcp_config.json", "strumenti esterni (MCP)"),
    ("config/config.json", "impostazioni generali"),
    ("config/skills/", "skill per tutti i progetti"),
    ("config/rules/", "regole per tutti i progetti"),
    ("config/GEMINI.md", "istruzioni per tutti i progetti"),
    ("config/hooks.json", "hook"),
    ("config/plugins/", "plugin"),
    ("antigravity/conversations/", "la conversazione, salvata in locale"),
    ("antigravity/conversation_summaries.db", "riassunti delle conversazioni"),
    ("antigravity/brain/", "area di lavoro dell'agente"),
    ("antigravity/annotations/", "note sulla conversazione"),
    ("antigravity/presence/", "conversazione aperta in questo momento"),
    ("antigravity/builtin/", "skill predefinite"),
    ("antigravity/", "stato dell'app"),
    ("sandbox/", "sandbox dei comandi"),
    ("jetski-standalone-oauth-token", "token di accesso all'account"),
]

DETTAGLI_BRAIN = [
    ("logs/transcript", "trascrizione della conversazione"),
    ("/steps/", "il risultato di un'azione, che poi rilegge"),
    ("/scratch/", "appunti e file di prova"),
    (".user_uploaded/", "file che gli avete dato"),
]


def etichetta(percorso: Path, progetto: Path | None) -> str:
    if progetto and percorso.is_relative_to(progetto):
        rel = percorso.relative_to(progetto).as_posix()
        if rel.startswith(".agents/") or rel in ("AGENTS.md", "GEMINI.md"):
            return "personalizzazioni del progetto"
        return "file del progetto"
    rel = percorso.relative_to(GEMINI).as_posix()
    for prefisso, testo in ETICHETTE:
        if rel.startswith(prefisso):
            if prefisso == "antigravity/brain/":
                for pezzo, dettaglio in DETTAGLI_BRAIN:
                    if pezzo in rel:
                        return f"{testo}: {dettaglio}"
            return testo
    return "altro"


def fotografa(radici):
    foto = {}
    for radice in radici:
        if not radice.exists():
            continue
        for cartella, sottocartelle, file in os.walk(radice):
            sottocartelle[:] = [d for d in sottocartelle if d not in SALTA]
            for nome in file:
                p = Path(cartella) / nome
                try:
                    s = p.stat()
                except OSError:
                    continue
                foto[p] = (s.st_mtime_ns, s.st_size)
    return foto


def segreto(p: Path) -> bool:
    nome = p.name.lower()
    return nome.endswith(".env") or any(s in nome for s in SEGRETI)


def mostra_json(p: Path):
    """Per i file di configurazione piccoli stampa il contenuto, chiavi segrete oscurate."""
    if p.suffix != ".json" or segreto(p) or not p.is_relative_to(GEMINI / "config"):
        return
    try:
        dati = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return

    def oscura(x):
        if isinstance(x, dict):
            return {k: ("***" if any(s in k.lower() for s in SEGRETI) else oscura(v))
                    for k, v in x.items()}
        if isinstance(x, list):
            return [oscura(v) for v in x]
        return x

    testo = json.dumps(oscura(dati), indent=2, ensure_ascii=False)
    righe = testo.splitlines()
    for r in righe[:25]:
        print(c("      │ ", "90") + r)
    if len(righe) > 25:
        print(c(f"      │ ... altre {len(righe) - 25} righe", "90"))


def breve(p: Path, progetto: Path | None) -> str:
    if progetto and p.is_relative_to(progetto):
        return f"[progetto]/{p.relative_to(progetto).as_posix()}"
    return f"~/.gemini/{p.relative_to(GEMINI).as_posix()}"


def main():
    progetto = Path(sys.argv[1]).expanduser().resolve() if len(sys.argv) > 1 else None
    radici = [GEMINI] + ([progetto] if progetto else [])
    if not GEMINI.exists():
        print("Non trovo ~/.gemini: Antigravity è installato e l'avete aperto almeno una volta?")
        return

    print(c("La spia è attiva.", "1") + " Guardo:")
    for r in radici:
        print("  ", r)
    print("Lavorate in Antigravity e guardate qui. Ctrl+C per il riepilogo.\n")

    prima = fotografa(radici)
    ultima_stampa: dict[Path, float] = {}
    conteggio: dict[Path, int] = {}
    nuovi: set[Path] = set()

    try:
        while True:
            time.sleep(1)
            dopo = fotografa(radici)
            eventi = [(p, "NUOVO") for p in dopo.keys() - prima.keys()]
            eventi += [(p, "MODIFICATO") for p in dopo.keys() & prima.keys() if dopo[p] != prima[p]]
            eventi += [(p, "CANCELLATO") for p in prima.keys() - dopo.keys()]
            ora = time.time()
            for p, tipo in sorted(eventi, key=lambda e: str(e[0])):
                conteggio[p] = conteggio.get(p, 0) + 1
                if tipo == "NUOVO":
                    nuovi.add(p)
                if tipo == "MODIFICATO" and ora - ultima_stampa.get(p, 0) < RIPETIZIONE:
                    continue
                ultima_stampa[p] = ora
                colore = {"NUOVO": "32", "MODIFICATO": "33", "CANCELLATO": "31"}[tipo]
                print(f"{time.strftime('%H:%M:%S')}  {c(tipo.ljust(10), colore)}  "
                      f"{c(etichetta(p, progetto), '1')}")
                print(f"      {breve(p, progetto)}")
                if segreto(p):
                    print(c("      │ contenuto non mostrato: è un segreto", "90"))
                elif tipo != "CANCELLATO":
                    mostra_json(p)
            prima = dopo
    except KeyboardInterrupt:
        pass

    print("\n" + c("Riepilogo", "1"))
    if not conteggio:
        print("Nessun file toccato.")
        return
    gruppi: dict[str, list[Path]] = {}
    for p in conteggio:
        gruppi.setdefault(etichetta(p, progetto), []).append(p)
    for nome, file in sorted(gruppi.items(), key=lambda g: -sum(conteggio[p] for p in g[1])):
        volte = sum(conteggio[p] for p in file)
        nuovi_qui = sum(1 for p in file if p in nuovi)
        print(f"  {nome}: {len(file)} file ({nuovi_qui} nuovi), {volte} modifiche")
    passi = {p.parent for p in nuovi if p.parent.parent.name == "steps"}
    if passi:
        print(c(f"\n  Azioni con un risultato salvato: {len(passi)}", "1"))


if __name__ == "__main__":
    main()
