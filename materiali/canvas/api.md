---
marp: true
paginate: true
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=JetBrains+Mono:wght@400&display=swap');
  :root { --fg: #1a1a1a; --muted: #6b6b6b; --accent: #2563eb; --line: #e5e5e5; --soft: #f5f7fb; }
  section { background: #fff; color: var(--fg); font-family: 'Inter', sans-serif; font-weight: 300; font-size: 28px; padding: 60px 80px; }
  h1 { color: var(--fg); font-weight: 800; font-size: 1.9em; letter-spacing: -0.02em; margin: 0 0 0.4em; }
  h2 { font-weight: 600; font-size: 1.25em; margin: 0 0 0.6em; }
  h3 { font-weight: 600; font-size: 0.6em; color: var(--muted); text-transform: uppercase; letter-spacing: 0.18em; margin: 0 0 0.8em; }
  strong { font-weight: 600; color: var(--accent); }
  ul, ol { padding-left: 1.1em; } li { margin: 0.25em 0; }
  section::after { color: #bbb; font-size: 0.5em; }
  section.lead { display: flex; flex-direction: column; justify-content: center; }
  section.lead h1 { font-size: 2.4em; }
  section.big { display: flex; flex-direction: column; justify-content: center; text-align: center; }
  section.big h1 { font-size: 1.8em; line-height: 1.25; }
  .cols { display: flex; gap: 40px; align-items: flex-start; }
  .cols > * { flex: 1; }
  .card { border: 1px solid var(--line); border-radius: 10px; padding: 18px 22px; }
  .card h2 { font-size: 0.95em; margin-bottom: 0.3em; }
  .card p { color: var(--muted); font-size: 0.75em; margin: 0; }
  .picts { display: flex; gap: 28px; justify-content: center; margin-top: 0.6em; }
  .picts img { height: 150px; }
  .pict-s img { height: 110px; }
  .meta { color: var(--muted); font-size: 0.75em; }
  pre { background: var(--soft); border: 1px solid var(--line); border-left: 4px solid var(--accent); border-radius: 8px; padding: 16px 20px; white-space: pre-wrap; }
  pre code { font-family: 'JetBrains Mono', monospace; font-size: 0.68em; line-height: 1.5; color: var(--fg); background: none; }
  .small pre code { font-size: 0.56em; }
  .note { color: var(--muted); font-size: 0.7em; margin-top: 0.8em; }
  .credits { color: var(--muted); font-size: 0.65em; }
  img { max-width: 100%; }
  .shot { border: 2px dashed #c4c4c4; border-radius: 12px; background: #fafafa; color: #9a9a9a; display: flex; align-items: center; justify-content: center; text-align: center; height: 330px; font-size: 0.6em; padding: 0 40px; }
  .schema { display: flex; justify-content: center; } .schema img { width: 100%; max-height: 480px; object-fit: contain; }
  .check { border: 1px solid #b7e4c7; background: #f0fbf4; border-radius: 10px; padding: 12px 20px; font-size: 0.7em; margin-top: 0.8em; }
  .check b { color: #1b7f3b; font-weight: 600; }
  .warn { border: 1px solid #f3d19c; background: #fff8ec; border-radius: 10px; padding: 12px 20px; font-size: 0.7em; margin-top: 0.8em; }
  a { color: inherit; text-decoration: underline; text-decoration-color: var(--accent); text-underline-offset: 3px; }
---

<!-- _class: lead -->
<!-- _paginate: false -->

### Canvas · Introduzione

# Le API

<p class="meta">Giuseppe Mastrandrea</p>

---

### Di cosa parliamo

<div class="cols">
<div class="card"><h2>Cosa sono</h2><p>Indirizzi web pensati per un programma: una pagina fatta con Canvas li usa per prendere dati e immagini da altri siti.</p></div>
<div class="card"><h2>Dove servono</h2><p>Nella tabella CAA, nella mappa di pittogrammi, nella mappa con le emoji: le immagini non le disegna Gemini, le chiede a un archivio.</p></div>
</div>

---

### Che cos'è un'API

- Un'**API** è un indirizzo web pensato per essere letto da un programma, non da una persona.
- Il programma scrive la domanda **dentro l'indirizzo**: una parola da cercare, una città, un numero.
- La risposta arriva in un **formato fisso**, che il programma sa leggere senza ambiguità.

---

### Un'API all'opera: due domande

<div class="schema"><img src="../comune/schemi/api.svg"></div>

<p class="note" style="text-align:center">Esempio con ARASAAC, l'archivio gratuito di pittogrammi: prima si cerca la parola, poi si chiede l'immagine. Adesso facciamo a mano, dal browser, le stesse due domande.</p>

---

### Prova 1 · Fare la domanda

<div class="cols">
<div>

1. Aprite una **scheda nuova** del browser.
2. Nella barra degli indirizzi scrivete
`api.arasaac.org/v1/pictograms/it/search/mela`
3. Premete **Invio**.

</div>
<div class="shot">Screenshot: la risposta dell'API aperta nel browser</div>
</div>

<div class="check"><b>Cosa vedete:</b> un testo fitto, pieno di virgolette e parentesi graffe. È normale: è scritto per un programma, non per noi.</div>

---

### Prova 2 · Trovare il numero

1. Premete **Ctrl+F** (sul Mac **Cmd+F**) e cercate `_id`
2. Il primo risultato è **"_id": 2462**.
3. Quel numero è il **codice del pittogramma** della mela.

<div class="check"><b>Cosa vedete:</b> la scritta _id evidenziata, seguita da 2462.</div>

---

### Prova 3 · Chiedere l'immagine

1. Nella stessa scheda, nella barra degli indirizzi scrivete
`static.arasaac.org/pictograms/2462/2462_500.png`
2. Premete **Invio**.

<p class="note">Il numero compare due volte nell'indirizzo: tutte e due le volte va sostituito.</p>

<div class="check"><b>Cosa vedete:</b> il pittogramma della mela, su sfondo bianco o trasparente.</div>

---

### Prova 4 · Da soli

Ripetete le prove 1, 2 e 3 con la parola **gatto**:

1. cercate la parola;
2. copiate il numero dopo `_id`;
3. mettetelo, due volte, nell'indirizzo dell'immagine.

<div class="check"><b>Cosa vedete:</b> un gatto. Questi tre passaggi una pagina fatta con Canvas li fa da sola, per ogni parola di una lista.</div>

---

### JSON, il formato delle risposte

```text
{ "titolo": "Il riccio eurasiatico",
  "lingua": "it",
  "parole": ["riccio", "mammifero", "aculei"] }
```

- **Coppie nome-valore** tra graffe: `"lingua": "it"`.
- **Elenchi** tra parentesi quadre: `["riccio", "mammifero"]`.

Non serve saperlo scrivere: basta riconoscerlo e dire a Gemini quale campo usare.

---

### Tre API gratuite, senza registrazione

| API | Cosa dà | Esempio di indirizzo |
|---|---|---|
| **ARASAAC** | Pittogrammi per parola | `api.arasaac.org/v1/pictograms/it/search/mela` |
| **Open-Meteo** | Meteo attuale e previsioni | `api.open-meteo.com/v1/forecast?latitude=41.12&longitude=16.87&current=temperature_2m` |
| **Wikipedia** | Riassunto di una voce | `it.wikipedia.org/api/rest_v1/page/summary/Riccio_europeo` |

<p class="note">Verificate il 6 ottobre 2026: rispondono senza chiave e da qualsiasi pagina.</p>

---

### Usare un'API da Canvas

Il prompt deve dire **tre cose**: l'indirizzo, il campo da prendere, cosa farne.

```text
Per ogni parola della lista chiama l'API
https://api.arasaac.org/v1/pictograms/it/search/PAROLA
prendi il campo _id del primo risultato e mostra l'immagine
https://static.arasaac.org/pictograms/ID/ID_500.png
Se la parola non ha risultati, mostra la casella vuota in rosso.
```

---

### Quando un'API non funziona da Canvas

- **Il sito non lo permette**: alcune API rispondono solo ad altri siti autorizzati. Dal browser funzionano, dalla pagina no.
- **Serve una chiave**: un codice personale da inserire nell'indirizzo. Una chiave dentro una pagina pubblica la vede chiunque.
- **Il primo risultato è sbagliato**: per "ancora" ARASAAC restituisce prima l'àncora della nave. Il controllo resta umano.

<p class="note">Per capire cosa succede: "Mostrami nella pagina il messaggio di errore dell'API".</p>

---

### Da ricordare

- Un'API è un indirizzo che risponde a un programma: prima si prova dal browser, poi si usa in Canvas.
- La domanda sta dentro l'indirizzo, la risposta arriva in JSON.
- Nel prompt: l'indirizzo, il campo da prendere, cosa farne.
