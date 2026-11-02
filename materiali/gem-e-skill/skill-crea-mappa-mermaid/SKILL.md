---
name: crea-mappa-mermaid
description: Scrive in codice Mermaid mappe concettuali, mappe mentali, linee del tempo, diagrammi di flusso e schemi causa-effetto a partire da una lezione, un testo o un argomento. Da usare quando si chiede una mappa, uno schema, un diagramma o una linea del tempo da proiettare, stampare o modificare in draw.io.
---

# Crea una mappa in Mermaid

Ambito: materiali per la lezione, dalla primaria alle superiori. Il codice verrà incollato in draw.io (Arrange, Insert, Mermaid) oppure in mermaid.live per esportare l'immagine.

## Procedura

1. Scegli il tipo di diagramma dalla richiesta:
   - mappa concettuale (concetti legati da relazioni con un verbo): `flowchart TD` con etichette sulle frecce;
   - mappa mentale (un tema al centro e i suoi rami): `mindmap`;
   - linea del tempo (date o fasi in ordine): `timeline`;
   - diagramma di flusso (una procedura con scelte): `flowchart TD` con rombi per le domande;
   - schema causa-effetto (cause che portano a conseguenze): `flowchart LR`.
2. Se la richiesta non dice il tipo, scegli quello più adatto e scrivilo nella riga dopo il codice.
3. Se manca la classe o l'ordine di scuola, chiedilo prima di scrivere: la quantità di caselle dipende da quello.
4. Apri il file `modelli.md` e parti dal modello del tipo scelto.
5. Prima di rispondere, ripassa la sezione "Errori comuni" qui sotto, una regola alla volta.

## Regole per il contenuto

- Primaria: al massimo 8 caselle, al massimo 4 parole per casella.
- Secondaria di primo grado: al massimo 12 caselle, al massimo 6 parole per casella.
- Secondaria di secondo grado: al massimo 16 caselle, al massimo 8 parole per casella.
- Nelle mappe concettuali ogni freccia ha un verbo: "produce", "è formato da", "causa".
- Solo concetti presenti nel testo o nella lezione indicata. Se aggiungi qualcosa di tuo, dillo nella riga dopo il codice.
- Nessun nome di studenti o altri dati personali, anche se compaiono nel testo.

## Formato della risposta

1. Un solo blocco di codice Mermaid, senza commenti dentro.
2. Una riga con il tipo di diagramma e il numero di caselle.
3. Una riga: "Per modificarlo: draw.io, Arrange, Insert, Mermaid. Per l'immagine: mermaid.live".

Niente altre spiegazioni, a meno che non vengano chieste.

## Colori

Usa i colori solo nei diagrammi di flusso e negli schemi causa-effetto, e sempre questi tre:

```text
classDef inizio fill:#d9f2e6,stroke:#1b7f3b,color:#1a1a1a
classDef domanda fill:#fff4d6,stroke:#b7791f,color:#1a1a1a
classDef passo fill:#e6eefc,stroke:#2563eb,color:#1a1a1a
```

Nelle mappe mentali e nelle linee del tempo niente colori: draw.io li ignora.

## Errori comuni

- **Testo con caratteri speciali.** Nei flowchart metti sempre il testo della casella tra virgolette doppie: `A["Perché l'acqua evapora?"]`. Senza virgolette, parentesi, due punti, accenti e apostrofi rompono il diagramma.
- **Virgolette dentro il testo.** Dentro `["..."]` non usare altre virgolette doppie: sostituiscile con quelle basse « » o toglile.
- **ID ripetuti.** Ogni casella ha un ID breve e unico (A, B, C... oppure A1, A2). Lo stesso ID usato due volte unisce due caselle diverse.
- **Parole riservate.** Non usare `end` come ID o come testo senza virgolette: chiude il diagramma.
- **Due punti nella linea del tempo.** In `timeline` i due punti separano la data dagli eventi: nel testo degli eventi non metterli mai, e scrivi gli orari con il punto (8.30).
- **Rientri nella mappa mentale.** In `mindmap` il rientro decide chi sta sotto chi: usa sempre 2 spazi per livello, mai il tabulatore. Niente parentesi nel testo dei rami, perché le parentesi cambiano la forma del nodo.
- **Blocco di codice.** Il codice va dentro un solo blocco: le righe con i tre apici non vanno copiate in draw.io.
