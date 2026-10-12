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
  .schema { display: flex; justify-content: center; } .schema img { max-height: 470px; }
  a { color: inherit; text-decoration: underline; text-decoration-color: var(--accent); text-underline-offset: 3px; }
---

<!-- _class: lead -->
<!-- _paginate: false -->

### Strumenti

# API e GitHub Pages

<p class="meta">Giuseppe Mastrandrea</p>

---

### Di cosa parliamo

<div class="cols">
<div class="card"><h2>API</h2><p>Come una pagina fatta con Canvas prende dati e immagini da altri siti.</p></div>
<div class="card"><h2>GitHub Pages</h2><p>Come mettere online le proprie pagine e le proprie immagini, gratis e con un indirizzo fisso.</p></div>
</div>

---

<!-- _class: big -->

# Parte 1 · Le API

---

### Che cos'è un'API

- Un'**API** è un indirizzo web pensato per essere letto da un programma, non da una persona.
- Il programma scrive la domanda **dentro l'indirizzo**: una parola da cercare, una città, un numero.
- La risposta arriva in un **formato fisso**, che il programma sa leggere senza ambiguità.

---

### Un'API all'opera: due domande

<div class="schema"><img src="img/schemi/api.svg"></div>

<p class="note" style="text-align:center">Esempio con ARASAAC, l'archivio gratuito di pittogrammi: prima si cerca la parola, poi si chiede l'immagine.</p>

---

### Provate dal browser

<div class="cols">
<div>

1. In una scheda nuova aprite
`api.arasaac.org/v1/pictograms/it/search/mela`
2. Cercate nel testo **"_id": 2462**: è il numero del pittogramma.
3. Ora aprite
`static.arasaac.org/pictograms/2462/2462_500.png`
4. Ripetete con un'altra parola.

</div>
<div class="shot">Screenshot: la risposta dell'API aperta nel browser</div>
</div>

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

<!-- _class: big -->

# Parte 2 · GitHub Pages

---

### Perché pubblicare

<div class="cols">
<div class="card"><h2>Una pagina fatta con Canvas</h2><p>Dentro Canvas la stampa è bloccata e la pagina va ritrovata nella chat. Pubblicata ha un indirizzo fisso e si apre da qualsiasi browser.</p></div>
<div class="card"><h2>Le proprie immagini</h2><p>Immagini generate o disegnate, con un indirizzo che Canvas può usare come usa un'API.</p></div>
</div>

---

### GitHub e GitHub Pages

- **GitHub** è un sito che conserva i file di un progetto insieme alla storia delle modifiche. Ogni progetto si chiama **repository**.
- **GitHub Pages** pubblica come sito i file di un repository pubblico.
- L'account base è gratuito, e Pages lo è per i repository pubblici.

<p class="note">L'interfaccia di GitHub è in inglese: nelle slide i nomi dei pulsanti sono quelli originali.</p>

---

### Il percorso

<div class="schema"><img src="img/schemi/pubblicazione.svg"></div>

---

### Creare l'account

<div class="cols">
<div>

1. Aprite **github.com** e cliccate **Sign up**.
2. Email, password e **username**.
3. Inserite il codice di verifica arrivato per email.

Lo username finisce in tutti gli indirizzi: sceglietene uno che vi sta bene vedere in pubblico.

</div>
<div class="shot">Screenshot: la pagina Sign up di GitHub</div>
</div>

---

### Creare un repository

<div class="cols">
<div>

1. In alto a destra **+ → New repository**.
2. Un nome breve, in minuscolo, senza spazi: **immagini**, **tabella-caa**.
3. Visibilità **Public**.
4. **Create repository**.

</div>
<div class="shot">Screenshot: il modulo New repository</div>
</div>

---

### Caso 1 · Caricare file

<div class="cols">
<div>

1. Nel repository: **Add file → Upload files**.
2. Trascinate le immagini nella finestra.
3. **Commit changes**.

Il nome del file diventa parte dell'indirizzo: **riccio.png**, non **Riccio (1).PNG**.

</div>
<div class="shot">Screenshot: la finestra Upload files con le immagini trascinate</div>
</div>

---

### Caso 2 · Pubblicare una pagina

<div class="cols">
<div>

1. In Canvas: **Scarica**. Rinominate il file in **index.html**.
2. Nel repository: **Add file → Upload files**, trascinate il file.
3. **Commit changes**.

Oppure: **Copia contenuti**, poi **Add file → Create new file**, nome **index.html**, incollate.

</div>
<div class="shot">Screenshot: il file index.html appena creato</div>
</div>

---

### Attivare GitHub Pages

<div class="cols">
<div>

1. Nel repository: **Settings → Pages**.
2. Source: **Deploy from a branch**.
3. Branch: **main**, cartella **/ (root)**, poi **Save**.
4. Dopo un paio di minuti, in cima alla stessa pagina compare l'indirizzo.

</div>
<div class="shot">Screenshot: la sezione Pages con l'indirizzo pubblicato</div>
</div>

---

### Gli indirizzi

| Cosa | Indirizzo |
|---|---|
| La pagina (`index.html`) | `nomeutente.github.io/repository/` |
| Un file | `nomeutente.github.io/repository/riccio.png` |

Prima di usarli altrove, apriteli nel browser: se compare l'immagine o la pagina, funziona.

---

### Il vostro magazzino come un'API

Se i file hanno il nome della parola, Canvas costruisce l'indirizzo da solo:

```text
Per ogni parola mostra l'immagine
https://NOMEUTENTE.github.io/immagini/PAROLA.png
Se l'immagine non esiste, mostra un punto interrogativo.
```

<p class="note">GitHub Pages permette a qualsiasi pagina di usare i suoi file: funzionano anche nel PDF generato da Canvas.</p>

---

### Gli errori più frequenti

| Problema | Causa probabile |
|---|---|
| L'immagine non compare | Maiuscole, spazi, accenti o "(1)" nel nome del file |
| L'indirizzo dà errore 404 | Pages non è ancora attivo, o mancano un paio di minuti |
| Il file nuovo non cambia | Il browser mostra la versione vecchia: ricaricate la pagina |
| Intorno alla figura c'è un riquadro bianco | Il PNG non è trasparente |

---

### Aggiornare

- **Sostituire un'immagine**: caricate il file nuovo con **lo stesso nome**. L'indirizzo resta uguale.
- **Modificare la pagina**: aprite **index.html**, cliccate la matita, incollate il codice nuovo, **Commit changes**.
- Dopo ogni modifica servono un paio di minuti.

---

### Pubblico vuol dire pubblico

- Chiunque abbia l'indirizzo vede pagine e immagini, e chiunque apra il repository ne legge il contenuto.
- Mai nomi, foto o disegni degli alunni.
- Mai chiavi o password dentro una pagina.

---

### Da ricordare

- Un'API è un indirizzo che risponde a un programma: prima si prova dal browser, poi si usa in Canvas.
- Su GitHub Pages un file caricato diventa un indirizzo fisso.
- Nomi dei file in minuscolo, senza spazi né accenti.
