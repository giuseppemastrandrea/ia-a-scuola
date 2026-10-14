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

# GitHub Pages

<p class="meta">Giuseppe Mastrandrea</p>

---

### Perché pubblicare

<div class="cols">
<div class="card"><h2>Dentro Canvas</h2><p>La pagina vive nella chat di Gemini, in un riquadro protetto che blocca la stampa. Per riusarla bisogna ritrovare la chat.</p></div>
<div class="card"><h2>Pubblicata</h2><p>Ha un indirizzo fisso, si apre da qualsiasi browser, si stampa e si passa alle colleghe. Lo stesso vale per le proprie immagini.</p></div>
</div>

---

### GitHub e GitHub Pages

- **GitHub** è un sito che conserva i file di un progetto insieme alla storia delle modifiche. Ogni progetto si chiama **repository**.
- **GitHub Pages** è un servizio di GitHub che pubblica come sito i file HTML di un repository pubblico.
- L'account base è gratuito, e Pages lo è per i repository pubblici.

<p class="note">L'interfaccia di GitHub è in inglese: nelle slide i nomi dei pulsanti sono quelli originali.</p>

---

### Il percorso

<div class="schema"><img src="../comune/schemi/pubblicazione.svg"></div>

<p class="note" style="text-align:center">Prima pubblichiamo una pagina di prova con una sola parola. Solo quando funziona carichiamo le pagine fatte con Canvas.</p>

---

### Prima di iniziare: pubblico vuol dire pubblico

- Chiunque abbia il link vede la pagina, e chiunque apra il repository ne legge il codice.
- Nelle pagine e nei nomi dei file **mai nomi, foto o disegni degli alunni**.
- **Mai chiavi o password** dentro una pagina.
- Lo username di GitHub compare nell'indirizzo: sceglietene uno che vi sta bene vedere in pubblico.

---

### Account 1 · Email e password

<div class="cols">
<div>

1. Aprite **github.com**.
2. Cliccate **Sign up**, in alto a destra.
3. Scrivete la vostra **email** e una **password**.

</div>
<div class="shot">Screenshot: la pagina Sign up di GitHub</div>
</div>

<div class="check"><b>Cosa vedete:</b> il modulo chiede ancora lo username. Fermatevi lì.</div>

---

### Account 2 · Lo username

- Solo **lettere minuscole, numeri e trattini**, senza spazi.
- Diventa l'inizio dell'indirizzo: **username**.github.io
- Si può cambiare dopo, ma i link già mandati alle colleghe smettono di funzionare.

<div class="check"><b>Cosa vedete:</b> un segno verde accanto allo username. Se è rosso, il nome è già preso: aggiungete un numero o una parola.</div>

---

### Account 3 · La verifica

1. Cliccate **Create account**.
2. Se compare un piccolo rompicapo con le immagini, risolvetelo: serve a dimostrare che non siete un programma.
3. Aprite l'email: GitHub ha mandato un **codice**. Scrivetelo nella pagina.
4. Se GitHub fa domande su di voi, potete saltarle.

<div class="check"><b>Cosa vedete:</b> la pagina principale di GitHub, con il vostro username in alto a destra. L'account è pronto.</div>

---

### Repository 1 · Aprire il modulo

<div class="cols">
<div>

1. In alto a destra cliccate **+**.
2. Scegliete **New repository**.

</div>
<div class="shot">Screenshot: il menu + con la voce New repository</div>
</div>

<div class="check"><b>Cosa vedete:</b> il modulo "Create a new repository".</div>

---

### Repository 2 · Il nome del repository

Il repository è il vostro **sito**: lì metterete tutte le pagine fatte con Canvas durante il corso.

Il nome va scritto esattamente così: il vostro username, poi `.github.io`

| Username | Nome del repository |
|---|---|
| `mrossi-scuola` | `mrossi-scuola.github.io` |

<div class="warn">Un solo carattere diverso, e GitHub tratta il repository come uno qualsiasi: l'indirizzo cambia.</div>

---

### Repository 3 · Compilare il modulo

<div class="cols">
<div>

1. **Repository name**: `username.github.io`, con il vostro username.
2. Visibilità: **Public**.
3. Tutto il resto lasciatelo com'è.
4. Cliccate **Create repository**.

</div>
<div class="shot">Screenshot: il modulo compilato</div>
</div>

<div class="check"><b>Cosa vedete:</b> una pagina quasi vuota, con il titolo "Quick setup" e il link <i>creating a new file</i>.</div>

---

### Prova generale 1 · Un file di una riga

<div class="cols">
<div>

1. Cliccate **creating a new file**.
2. Nome del file: `index.html`
3. Nel riquadro grande scrivete:
`<h1>Ciao</h1>`

Questa sarà la pagina principale del sito. Per ora dice solo "Ciao".

</div>
<div class="shot">Screenshot: il file index.html con la riga di prova</div>
</div>

<p class="note">Il nome index.html è obbligatorio: è il file che GitHub Pages apre per primo.</p>

---

### Prova generale 2 · Salvare

1. Cliccate **Commit changes...** in alto a destra.
2. Si apre una finestra: cliccate di nuovo **Commit changes**.

<p class="note">"Commit" vuol dire salvare una versione. GitHub le conserva tutte.</p>

<div class="check"><b>Cosa vedete:</b> la pagina del repository con un solo file, index.html.</div>

---

### Pages 1 · Trovare le impostazioni

<div class="cols">
<div>

1. Nel repository cliccate **Settings** (l'ingranaggio, in alto).
2. Nella colonna di sinistra cliccate **Pages**.

</div>
<div class="shot">Screenshot: Settings con la voce Pages a sinistra</div>
</div>

<div class="check"><b>Cosa vedete:</b> la pagina "GitHub Pages" con la sezione "Build and deployment".</div>

---

### Pages 2 · Controllare la pubblicazione

<div class="cols">
<div>

Con un nome come `username.github.io`, di solito GitHub accende la pubblicazione da solo. Controllate:

1. **Source**: Deploy from a branch.
2. **Branch**: da None scegliete **main**.
3. Cartella: **/ (root)**.
4. Se avete cambiato qualcosa, cliccate **Save**.

</div>
<div class="shot">Screenshot: Branch main e cartella root</div>
</div>

---

### Pages 3 · Aspettare e controllare

1. Aspettate un paio di minuti.
2. Ricaricate la pagina delle impostazioni.
3. In cima compare **Your site is live at...**: cliccate **Visit site**.

<p class="note">L'indirizzo è username.github.io, senza altro dopo.</p>

<div class="check"><b>Cosa vedete:</b> una pagina bianca con la scritta grande <b>Ciao</b>. La pubblicazione funziona.</div>

<div class="warn">Errore 404? Pages non ha ancora finito: aspettate un altro minuto e ricaricate.</div>

---

### Perché la pagina di prova

<div class="cols">
<div class="card"><h2>Se "Ciao" compare</h2><p>Account, repository e Pages sono a posto. Ogni problema successivo sta nel codice della pagina.</p></div>
<div class="card"><h2>Se "Ciao" non compare</h2><p>Il problema sta nella pubblicazione, e lo cerchiamo senza la confusione di una pagina lunga.</p></div>
</div>

---

<!-- _class: big -->

# Pubblicare una pagina fatta con Canvas

---

### Pagina 1 · Scaricare da Canvas

<div class="cols">
<div>

1. Aprite la chat di Gemini con la pagina.
2. In alto, nel riquadro di Canvas, cliccate **Scarica**.

</div>
<div><img src="img/canvas-scarica-condividi.png" style="width:100%;border:1px solid #e5e5e5;border-radius:10px"></div>
</div>

<div class="check"><b>Cosa vedete:</b> nella cartella <b>Download</b> del computer un file nuovo, che finisce con .html.</div>

---

### I nomi dei file

Il nome del file diventa parte dell'indirizzo:

| Sì | No |
|---|---|
| `tabella-caa.html` | `Tabella CAA.html` |
| `ruota_dell_autunno.html` | `ruota_dell_autunno` (manca .html) |

- Lettere **minuscole**, parole separate da **trattini** o **trattini bassi** ( _ ).
- **Niente** spazi, accenti, apostrofi.
- Finisce sempre con **.html**.

---

### Pagina 2 · Rinominare il file

1. Aprite la cartella **Download**.
2. Rinominate il file appena scaricato con il nome scelto.
Windows: tasto destro → **Rinomina**. Mac: cliccate il file e premete **Invio**.

<div class="warn">Windows spesso nasconde la parte finale .html. Se il nome che vedete non finisce con .html, non aggiungetelo: altrimenti il file diventa NOME.html.html.</div>

<div class="check"><b>Cosa vedete:</b> nella cartella Download il file con il nome nuovo.</div>

---

### Pagina 3 · Caricare il file su GitHub

<div class="cols">
<div>

1. Su GitHub, nel repository: **Add file → Upload files**.
2. Trascinate il file dalla cartella Download nel riquadro.
3. Aspettate che il nome del file compaia sotto il riquadro.
4. In fondo alla pagina cliccate **Commit changes**.

</div>
<div class="shot">Screenshot: la finestra Upload files con il file trascinato</div>
</div>

<div class="check"><b>Cosa vedete:</b> nel repository il file nuovo, accanto a index.html.</div>

---

### Pagina 4 · Il collaudo

1. Aspettate un paio di minuti.
2. Aprite **username.github.io/** seguito dal nome del file.
3. Provate anche la stampa del browser (**Ctrl+P** o **Cmd+P**): fuori da Canvas funziona.

<div class="check"><b>Cosa vedete:</b> la pagina che funziona come in Canvas.</div>

---

### Le proprie immagini

Le immagini si caricano allo stesso modo, con **Upload files**, e ognuna ha il suo indirizzo: **username.github.io/riccio.png**.

Se i file hanno il nome della parola, Canvas costruisce l'indirizzo da solo:

```text
Per ogni parola mostra l'immagine
https://USERNAME.github.io/PAROLA.png
Se l'immagine non esiste, mostra un punto interrogativo.
```

<p class="note">GitHub Pages permette a qualsiasi pagina di usare i suoi file: funzionano anche nel PDF generato da Canvas.</p>

---

### Gli errori più frequenti

| Cosa vedete | Cosa fare |
|---|---|
| Errore 404 | Aspettate un minuto e ricaricate |
| Errore 404 solo su una pagina | Il nome del file è diverso dall'indirizzo: maiuscole, spazi, .html mancante |
| Vedete la versione vecchia | Ricaricate con **Ctrl+Shift+R** (**Cmd+Shift+R**) |
| Su GitHub il file si chiama NOME.html.html | Rinominatelo bene sul computer e caricatelo di nuovo |
| L'indirizzo username.github.io non esiste | Il nome del repository non è esattamente username.github.io |
| Manca Pages nelle impostazioni | Il repository non è Public |
| Intorno a un'immagine c'è un riquadro bianco | Il PNG non è trasparente |

---

### Aggiornare una pagina

Si carica un file con **lo stesso nome**: GitHub sostituisce quello vecchio.

1. In Canvas chiedete la modifica, poi **Scarica**.
2. Rinominate il file con lo stesso nome della prima volta.
3. Su GitHub: **Add file → Upload files**, trascinate il file, **Commit changes**.
4. Aspettate un paio di minuti.

<p class="note">L'indirizzo resta lo stesso: il link già mandato alle colleghe mostra la versione nuova.</p>

---

### Da ricordare

- Un repository **username.github.io** è il vostro sito: ci vanno tutte le pagine fatte con Canvas.
- Da Canvas a GitHub sempre in tre mosse: **Scarica**, rinomina, **Upload files**.
- Nomi dei file in minuscolo, senza spazi né accenti, con **.html** alla fine.
- Un file caricato con lo stesso nome sostituisce quello vecchio.
- Pubblico vuol dire pubblico: mai dati degli alunni.
