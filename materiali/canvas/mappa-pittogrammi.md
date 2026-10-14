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
  .mappa { display: grid; grid-template-columns: repeat(3, 150px); gap: 8px 70px; justify-content: center; }
  .mappa div { text-align: center; font-size: 0.6em; font-weight: 600; padding: 4px; }
  .mappa img { height: 90px; display: block; margin: 0 auto 2px; }
  .mappa .c { border: 3px solid var(--accent); border-radius: 12px; }
  a { color: inherit; text-decoration: underline; text-decoration-color: var(--accent); text-underline-offset: 3px; }
---

<!-- _class: lead -->
<!-- _paginate: false -->

### Canvas · Esercitazione, mappa concettuale

# Una mappa di pittogrammi

<p class="meta">Giuseppe Mastrandrea</p>

---

### Cosa facciamo

Una pagina con un argomento al centro e, intorno, le parole collegate. Ogni parola ha il suo **pittogramma**, preso da un archivio gratuito.

Nient'altro: niente tabelle, niente PDF, niente pubblicazione.

---

### Il risultato che vogliamo

<div class="mappa">
<div><img src="img/autunno/foglia.png">FOGLIA</div>
<div><img src="img/autunno/castagna.png">CASTAGNA</div>
<div><img src="img/autunno/pioggia.png">PIOGGIA</div>
<div><img src="img/autunno/ombrello.png">OMBRELLO</div>
<div class="c"><img src="img/autunno/autunno.png">AUTUNNO</div>
<div><img src="img/autunno/fungo.png">FUNGO</div>
<div><img src="img/autunno/uva.png">UVA</div>
<div><img src="img/autunno/vento.png">VENTO</div>
<div><img src="img/autunno/scoiattolo.png">SCOIATTOLO</div>
</div>

<p class="note" style="text-align:center">Nella pagina le parole saranno collegate al centro da linee.</p>

---

### Da dove vengono i pittogrammi

- **ARASAAC** è un archivio di oltre **10.000 pittogrammi**, cercabili in italiano.
- Si usano gratis a scuola.
- Gemini **non li disegna**: la pagina li va a prendere da ARASAAC, parola per parola.


<p class="note">Come funziona un'API e come si prova dal browser: deck <a href="api.html">Le API</a>, da fare prima di questa esercitazione.</p>

---

### Aprire Canvas

1. Aprite Gemini in una **chat nuova**.
2. Cliccate **Strumenti** sotto la casella del prompt.
3. Scegliete **Canvas**.

<div class="check"><b>Cosa vedete:</b> la voce Canvas evidenziata vicino alla casella del prompt.</div>

---

### Il prompt

<div class="small">

```text
Ambito: scuola primaria, materiali con i pittogrammi.
Compito: crea una pagina web per creare mappe concettuali.
Bisogna prevedere una casella di testo con il concetto centrale
e un altro campo di testo multi riga.

Per ciascuna delle parole (sia nel campo di testo che nelle singole
righe dell'altro campo) bisogna:
cercare il pittogramma con l'API di ARASAAC:
https://api.arasaac.org/v1/pictograms/it/search/PAROLA
prendere il campo _id del primo risultato e mostrare l'immagine
https://static.arasaac.org/pictograms/ID/ID_500.png.

Es.
Al centro la parola "autunno". Intorno, in cerchio, queste parole:
foglia, castagna, pioggia, ombrello, fungo, uva, vento, scoiattolo.
Ogni parola è collegata al centro con una linea.

Per ogni parola visualizza il pittogramma e la parola in maiuscolo.
```

</div>

---

### Il collaudo

<div class="cols">
<div>

1. Nella casella del concetto centrale scrivete **autunno**.
2. Nel campo grande, una per riga:

```text
foglia
castagna
pioggia
ombrello
fungo
uva
vento
scoiattolo
```

</div>
<div>

<div class="check"><b>Cosa vedete:</b> AUTUNNO al centro, 8 parole in maiuscolo intorno, ognuna con il suo pittogramma e una linea verso il centro.</div>

</div>
</div>

---

### Se qualcosa non va

Descrivete a Gemini **cosa vedete**:

```text
Le immagini non compaiono: al loro posto c'è un'icona rotta.
```

<div class="warn">Una correzione per messaggio. Se dopo tre tentativi non funziona, alzate la mano.</div>

---

### Guardate la foglia

Per "foglia" ARASAAC restituisce **4 pittogrammi**. La pagina prende sempre il primo.

<div class="cols">
<div class="card" style="text-align:center"><img src="img/autunno/foglia-5077.png" style="height:120px"><p>1° · quella che prende la pagina</p></div><div class="card" style="text-align:center"><img src="img/autunno/foglia-3114.png" style="height:120px"><p>2°</p></div><div class="card" style="text-align:center"><img src="img/autunno/foglia-5076.png" style="height:120px"><p>3° · la foglia secca</p></div><div class="card" style="text-align:center"><img src="img/autunno/foglia-38396.png" style="height:120px"><p>4° · un insetto</p></div>
</div>

<p class="note">Prova del 13 ottobre 2026. Per l'autunno servirebbe il terzo: la scelta deve restare a voi.</p>

---

### Scegliere il pittogramma

Nella stessa chat:

```text
Quando una parola ha più pittogrammi, mostrali in piccolo
sotto la parola e fammi cliccare quello che preferisco.
```

<div class="check"><b>Cosa vedete:</b> sotto "foglia" 4 miniature. Cliccate la foglia secca: il pittogramma grande cambia.</div>

---

### Un altro argomento

Non serve un prompt nuovo: cambiate le parole nella pagina.

1. Concetto centrale: **merenda**.
2. Nel campo grande, una per riga: mela, pane, succo, biscotto, acqua, bere, mangiare, tovagliolo.

<div class="check"><b>Cosa vedete:</b> la nuova mappa, con i pittogrammi della merenda.</div>

---

### Portarla fuori da Canvas

1. In alto, nel riquadro di Canvas, cliccate **Scarica**.
2. Aprite il file scaricato con **Chrome**.
3. Per stamparla: **Ctrl+P** (sul Mac **Cmd+P**).

<p class="note">Dentro Canvas la stampa è bloccata. Fuori funziona.</p>

---

### Da ricordare

- I pittogrammi arrivano da **ARASAAC**, non li disegna Gemini.
- Il primo risultato non è sempre quello giusto: si controlla ogni immagine.
