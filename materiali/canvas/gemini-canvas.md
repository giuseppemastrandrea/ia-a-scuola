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

# Gemini Canvas

<p class="meta">Giuseppe Mastrandrea</p>

---

### Che cos'è

Un **pannello di lavoro accanto alla chat**: Gemini ci scrive un documento o costruisce una pagina, e a ogni richiesta successiva modifica quello che c'è già.

Si attiva dalla barra del prompt: **Strumenti → Canvas**.

<p class="note">È disponibile anche nella versione gratuita di Gemini.</p>

---

### Chat o Canvas?

<div class="cols">
<div class="card"><h2>Chat</h2><p>Ogni risposta è un messaggio nuovo che scorre via. Per correggere, Gemini riscrive tutto.</p></div>
<div class="card"><h2>Canvas</h2><p>C'è un solo oggetto, sempre visibile a destra. Le richieste lo modificano un pezzo alla volta.</p></div>
</div>

---

### Due cose diverse

<div class="schema"><img src="../comune/schemi/canvas-modi.svg"></div>

---

### Il documento

```text
Ambito: scuola primaria, classe terza.
Compito: crea in Canvas una scheda di lettura sul riccio:
un testo di 10 righe e 5 domande di comprensione.
Voglio un documento di testo, non una pagina web.
```

Poi si lavora sul documento: "accorcia il testo", "aggiungi due domande vero/falso", "metti in grassetto le parole nuove".

---

### L'app

```text
Ambito: scuola dell'infanzia, routine del mattino.
Compito: crea una pagina per la LIM con 4 pulsanti grandi:
☀️ sole, 🌧️ pioggia, ☁️ nuvole, ❄️ neve.
Quando tocco un pulsante, la sua emoji compare grande al centro.
```

<p class="note">Se non si specifica, è Gemini a scegliere tra documento e app.</p>

---

### Anteprima e codice

<div class="cols">
<div>

Un'app ha due viste:
- **Anteprima**: la pagina da usare;
- **Codice**: il testo che la fa funzionare.

Il codice non serve leggerlo. Per portare la pagina fuori da Canvas c'è il pulsante **Scarica**.

</div>
<div><img src="img/canvas-codice-anteprima.png" style="width:100%;border:1px solid #e5e5e5;border-radius:10px"></div>
</div>

---

### Il metodo: una richiesta alla volta

<div class="cols">
<div class="card"><h2>Un passo per messaggio</h2><p>Ogni richiesta aggiunge una sola funzione o cambia una sola cosa.</p></div>
<div class="card"><h2>Provate subito</h2><p>Dopo ogni passo si tocca, si legge, si scarica: fa quello che avete chiesto?</p></div>
<div class="card"><h2>Descrivete il problema</h2><p>"Il pulsante non fa nulla" funziona meglio che riscrivere tutto il prompt.</p></div>
</div>

---

### Cosa si porta fuori

| In Canvas | Dove va |
|---|---|
| Documento | **Esporta in Documenti**, poi da Documenti in PDF, Word o Markdown |
| Presentazione | **Esporta in Presentazioni** o in PDF |
| App | **Scarica**: il file della pagina, da aprire nel browser o pubblicare<br>**Condividi**: un link che apre la pagina<br>**Copia contenuti**: il codice |
| Qualsiasi creazione | **Condividi in Classroom** |

<p class="note">Fonte: guida di Google "Create docs, apps & more with Canvas"; Classroom da giugno 2026 (Google Workspace Updates).</p>

---

### Scarica e condividi un'app

<div class="cols">
<div>

In alto nel pannello di un'app:
- **Scarica**: salva la pagina come file;
- l'icona di **condivisione**: **Condividi** crea il link, **Copia contenuti** copia il codice.

Il file scaricato si apre con Chrome, e lì la stampa funziona.

</div>
<div><img src="img/canvas-scarica-condividi.png" style="width:100%;border:1px solid #e5e5e5;border-radius:10px"></div>
</div>

---

### I limiti delle app

- **La stampa è bloccata**: l'anteprima gira in un riquadro protetto. Si chiede un pulsante **"Scarica PDF"**, oppure si scarica la pagina e la si stampa da Chrome.
- **Le risorse esterne** (immagini, dati) funzionano solo se il sito che le offre lo permette: ARASAAC e GitHub Pages sì, Google Drive no.
- **Nessun dato personale**: le app condivise con un link sono pubbliche.

---

### Il prompt unico

Alla fine, nella stessa chat:

```text
Scrivi un prompt unico che, incollato in una chat nuova con
Canvas attivo, ricrei questa pagina con tutte le funzioni.
Mettilo in un blocco di codice.
```

Si salva nel kit: la prossima volta si riparte da lì.

---

### Le esercitazioni

<div class="cols">
<div class="card"><h2>Che tempo fa oggi?</h2><p>Infanzia. Una pagina, quattro pulsanti: il primo contatto con le app.</p></div>
<div class="card"><h2>La mappa che parla</h2><p>Infanzia. Una mappa per la LIM costruita in 7 passi.</p></div>
<div class="card"><h2>La tabella CAA</h2><p>Primaria. Pittogrammi ARASAAC dall'API e pubblicazione su GitHub Pages.</p></div>
</div>

---

### Da ricordare

- Prima di scrivere il prompt, decidete se vi serve un **documento** o un'**app**, e scrivetelo.
- Una richiesta per messaggio, e dopo ogni richiesta si prova.
- Il documento si esporta in Documenti, l'app si scarica o si condivide con un link.
