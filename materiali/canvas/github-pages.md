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
  .cols > .sc { flex: 1.6; }
  .sc img { max-height: 440px; max-width: 100%; border: 1px solid #e5e5e5; border-radius: 10px; display: block; margin: 0 auto; }
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
<div class="card"><h2>Pubblicata</h2><p>Ha un indirizzo fisso, si apre da qualsiasi browser, si stampa e si passa alle colleghe.</p></div>
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

<p class="note" style="text-align:center">La prima pagina si chiama index.html. Le altre, nello stesso repository, hanno un nome loro.</p>

---

### Prima di iniziare: pubblico vuol dire pubblico

- Chiunque abbia il link vede la pagina, e chiunque apra il repository ne legge il codice.
- Nelle pagine e nei nomi dei file **mai nomi, foto o disegni degli alunni**.
- **Mai chiavi o password** dentro una pagina.
- Lo username di GitHub compare nell'indirizzo: sceglietene uno che vi sta bene vedere in pubblico.

---

### Account 1 · Il modulo

<div class="cols">
<div>

1. Aprite **github.com** e cliccate **Sign up**.
2. Scrivete **email**, **password** e **username**.
3. **Your Country/Region**: Italy.
4. Cliccate **Create account**.

<p class="note">La password: almeno 15 caratteri, oppure almeno 8 con un numero e una lettera minuscola.</p>

</div>
<div class="sc"><img src="img/github/01-sign-up.png"></div>
</div>

---

### Account 2 · Lo username

- Solo **lettere, numeri e trattini**, senza spazi. Non può iniziare né finire con un trattino.
- Diventa l'inizio dell'indirizzo: **username**.github.io
- Si può cambiare dopo, ma i link già mandati alle colleghe smettono di funzionare.

<div class="check"><b>Cosa vedete:</b> nessuna scritta rossa sotto lo username. Se compare, il nome è già preso: aggiungete un numero o una parola.</div>

---

### Account 3 · La verifica

1. Se compare un piccolo rompicapo con le immagini, risolvetelo: serve a dimostrare che non siete un programma.
2. Aprite l'email: GitHub ha mandato un **codice**. Scrivetelo nella pagina.
3. Se GitHub fa domande su di voi, potete saltarle.

<div class="check"><b>Cosa vedete:</b> la pagina principale di GitHub, con la vostra immagine del profilo in alto a destra. L'account è pronto.</div>

---

### Repository 1 · Aprire il modulo

<div class="cols">
<div>

1. In alto a destra cliccate **+**.
2. Scegliete **New repository**.

<div class="check"><b>Cosa vedete:</b> il modulo "Create a new repository".</div>

</div>
<div class="sc"><img src="img/github/02-new-repository.png"></div>
</div>

---

### Repository 2 · Compilare il modulo

<div class="cols">
<div>

1. **Repository name**: un nome breve, in minuscolo, senza spazi. Per esempio `creazioni-canvas`.
2. **Choose visibility**: **Public**.
3. Tutto il resto lasciatelo com'è.
4. In fondo cliccate **Create repository**.

<p class="note">Il nome finisce nell'indirizzo: username.github.io/<b>creazioni-canvas</b>/</p>

</div>
<div class="sc"><img src="img/github/03-modulo-repository.png"></div>
</div>

---

### Repository 3 · Il repository vuoto

<div class="cols">
<div>

<div class="check"><b>Cosa vedete:</b> una pagina quasi vuota, con il riquadro azzurro "Quick setup" e il link <i>uploading an existing file</i>.</div>

**Non chiudete questa scheda**: ci torniamo tra poco, con il file della pagina.

</div>
<div class="sc"><img src="img/github/04-quick-setup.png"></div>
</div>

---

### Canvas 1 · Scaricare il codice

<div class="cols">
<div>

1. In un'altra scheda aprite la chat di Gemini con la pagina.
2. In alto, nel riquadro di Canvas, cliccate **Esporta**.
3. Scegliete **Scarica codice**.

<div class="check"><b>Cosa vedete:</b> nella cartella <b>Download</b> del computer un file nuovo, che finisce con .html.</div>

</div>
<div class="sc"><img src="img/github/05-canvas-scarica-codice.png"></div>
</div>

---

### Canvas 2 · Rinominare in index.html

<div class="cols">
<div>

1. Aprite la cartella **Download**.
2. Rinominate il file appena scaricato in `index.html`
Windows: tasto destro → **Rinomina**. Mac: cliccate il file e premete **Invio**.

<p class="note">Il nome è obbligatorio: index.html è la pagina che GitHub Pages apre per prima.</p>

</div>
<div class="sc"><img src="img/github/06-rinomina-index.png"></div>
</div>

<div class="warn">Windows spesso nasconde la parte finale .html. Se il nome che vedete non finisce con .html, scrivete solo <b>index</b>: altrimenti il file diventa index.html.html.</div>

---

### Caricare il file

<div class="cols">
<div>

1. Tornate alla scheda di GitHub e cliccate **uploading an existing file**.
2. Trascinate **index.html** dalla cartella Download nel riquadro.
3. Sotto **Commit changes** potete scrivere una frase che descrive la pagina.
4. Cliccate il pulsante verde **Commit changes**.

</div>
<div class="sc"><img src="img/github/07-upload.png"></div>
</div>

<div class="check"><b>Cosa vedete:</b> la pagina del repository con un solo file, index.html.</div>

---

### Pages 1 · Trovare le impostazioni

<div class="cols">
<div>

1. Nel repository cliccate **Settings** (l'ingranaggio, in alto a destra).
2. Nella colonna di sinistra, in fondo, cliccate **Pages**.

<div class="check"><b>Cosa vedete:</b> la pagina "GitHub Pages", con la sezione "Build and deployment".</div>

</div>
<div class="sc"><img src="img/github/08-pages.png"></div>
</div>

---

### Pages 2 · Accendere la pubblicazione

<div class="cols">
<div>

1. **Source**: Deploy from a branch.
2. **Branch**: cliccate **None** e scegliete **main**.
3. Cartella: **/ (root)**.
4. Cliccate **Save**.

</div>
<div class="sc"><img src="img/github/08-pages.png"></div>
</div>

---

### Pages 3 · La pagina è online

<div class="cols">
<div>

1. Aspettate un paio di minuti.
2. Ricaricate la pagina delle impostazioni.
3. In cima compare **Your site is live at...**: cliccate **Visit site**.

<div class="check"><b>Cosa vedete:</b> la vostra pagina, che funziona come in Canvas.</div>

<div class="warn">Errore 404? Pages non ha ancora finito: aspettate un altro minuto e ricaricate.</div>

</div>
<div class="sc"><img src="img/github/09-site-live.png"></div>
</div>

---

### Il collaudo

1. Copiate l'indirizzo: **username.github.io/creazioni-canvas/**
2. Provate la stampa del browser (**Ctrl+P** o **Cmd+P**): fuori da Canvas funziona.
3. Mandate il link a una collega e fatelo provare a lei.

<div class="check"><b>Cosa vedete:</b> la pagina si apre anche dal telefono e dal computer della collega.</div>

---

### Gli errori più frequenti

| Cosa vedete | Cosa fare |
|---|---|
| Errore 404 | Aspettate un minuto e ricaricate |
| Errore 404 anche dopo 5 minuti | Il file non si chiama esattamente index.html |
| Su GitHub il file si chiama index.html.html | Rinominatelo bene sul computer e caricatelo di nuovo |
| Vedete la versione vecchia | Ricaricate con **Ctrl+Shift+R** (**Cmd+Shift+R**) |
| Manca Pages nelle impostazioni | Il repository non è Public |

---

### Aggiornare la pagina

Si carica un file con **lo stesso nome**: GitHub sostituisce quello vecchio.

1. In Canvas chiedete la modifica, poi **Esporta → Scarica codice**.
2. Rinominate il file in **index.html**, come la prima volta.
3. Nel repository: **Add file → Upload files**, trascinate il file, **Commit changes**.
4. Aspettate un paio di minuti.

<p class="note">L'indirizzo resta lo stesso: il link già mandato alle colleghe mostra la versione nuova.</p>

---

### Un'altra pagina, nello stesso repository

<div class="cols">
<div>

1. In Canvas: **Esporta → Scarica codice**.
2. Rinominate il file con un nome **suo**, non index.html. Per esempio `ruota_dell_autunno.html`
3. Nel repository: **Add file → Upload files**, trascinate il file, **Commit changes**.

<div class="check"><b>Cosa vedete:</b> la pagina all'indirizzo username.github.io/creazioni-canvas/ruota_dell_autunno.html</div>

</div>
<div class="sc"><img src="img/github/07-upload.png"></div>
</div>

---

### I nomi dei file

| Sì | No |
|---|---|
| `ruota_dell_autunno.html` | `Ruota dell'autunno.html` |
| `tabella-caa.html` | `tabella-caa` (manca .html) |

- Lettere **minuscole**, parole separate da **trattini** o **trattini bassi** ( _ ).
- **Niente** spazi, accenti, apostrofi.
- Finisce sempre con **.html**.

<p class="note">Più avanti index.html diventerà la pagina indice che porta a tutte le altre: esercitazione <a href="il-mio-sito.html">Il mio sito</a>.</p>

---

### In più · Le proprie immagini

Le immagini si caricano allo stesso modo, con **Add file → Upload files**, accanto a index.html. Ognuna ha il suo indirizzo: **username.github.io/creazioni-canvas/riccio.png**.

Se i file hanno il nome della parola, Canvas costruisce l'indirizzo da solo:

```text
Per ogni parola mostra l'immagine
https://USERNAME.github.io/REPOSITORY/PAROLA.png
Se l'immagine non esiste, mostra un punto interrogativo.
```

---

### Da ricordare

- Un repository per tutte le pagine: la prima si chiama **index.html**, le altre hanno un nome loro.
- Da Canvas a GitHub: **Esporta → Scarica codice**, rinomina in index.html, carica.
- Pages si accende una volta sola: **Settings → Pages → main → Save**.
- Un file caricato con lo stesso nome sostituisce quello vecchio.
- Pubblico vuol dire pubblico: mai dati degli alunni.
