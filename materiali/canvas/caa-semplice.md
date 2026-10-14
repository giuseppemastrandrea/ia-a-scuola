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
  .griglia { display: grid; grid-template-columns: repeat(4, 150px); gap: 10px; justify-content: center; }
  .griglia div { border: 1px solid var(--line); border-radius: 8px; text-align: center; font-size: 0.55em; font-weight: 600; padding: 6px; height: 128px; }
  .griglia img { height: 95px; display: block; margin: 0 auto 2px; }
  .griglia .vuota { color: #d00; display: flex; align-items: flex-end; justify-content: center; }
  a { color: inherit; text-decoration: underline; text-decoration-color: var(--accent); text-underline-offset: 3px; }
---

<!-- _class: lead -->
<!-- _paginate: false -->

### Canvas · Esercitazione, versione semplice

# Una tabella di pittogrammi

<p class="meta">Giuseppe Mastrandrea</p>

---

### Cosa facciamo

Una pagina dove si incolla una lista di parole e compare una **griglia di pittogrammi**, presi da un archivio gratuito. Poi la si porta su carta.

---

### Come lavoriamo

<div class="cols">
<div class="card"><h2>Un passo alla volta</h2><p>Ogni slide chiede una sola azione. Si passa alla slide successiva solo quando l'azione è riuscita.</p></div>
<div class="card"><h2>Il riquadro verde</h2><p>Dice cosa dovete vedere sullo schermo. Se vedete altro, alzate la mano.</p></div>
</div>

<div class="check"><b>Cosa vedete:</b> qui, in ogni slide, il controllo da fare.</div>

---

### Il risultato che vogliamo

<div class="griglia">
<div><img src="img/autunno/autunno.png">autunno</div>
<div><img src="img/autunno/foglia.png">foglia</div>
<div><img src="img/autunno/castagna.png">castagna</div>
<div><img src="img/autunno/pioggia.png">pioggia</div>
<div><img src="img/autunno/ombrello.png">ombrello</div>
<div><img src="img/autunno/fungo.png">fungo</div>
<div><img src="img/autunno/uva.png">uva</div>
<div class="vuota">xyzabc</div>
</div>

<p class="note" style="text-align:center">Una parola che l'archivio non conosce resta senza immagine, scritta in rosso.</p>

---

### Da dove vengono i pittogrammi

- **ARASAAC** è un archivio di oltre **10.000 pittogrammi**, cercabili in italiano.
- Si usano gratis a scuola, citando l'autore.
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
Crea una pagina web per costruire tabelle di comunicazione CAA.
- Un riquadro dove incollo una lista di parole, una per riga.
- Per ogni parola cerca il pittogramma con l'API di ARASAAC:
  https://api.arasaac.org/v1/pictograms/it/search/PAROLA,
  prendi il campo _id del primo risultato e mostra l'immagine
  https://static.arasaac.org/pictograms/ID/ID_500.png.
- Mostra una griglia a 4 colonne, con la parola scritta sotto ogni immagine.
- Se una parola non ha pittogramma, mostra la casella vuota
  con la scritta in rosso.
- Un pulsante "Stampa" che stampa solo la griglia.
```

</div>

<div class="check"><b>Cosa vedete:</b> a destra la pagina, con il riquadro per le parole e il pulsante Stampa.</div>

---

### Il collaudo

<div class="cols">
<div>

Incollate nel riquadro:

```text
autunno
foglia
castagna
pioggia
ombrello
fungo
uva
xyzabc
```

</div>
<div>

<div class="check"><b>Cosa vedete:</b> 7 caselle con il pittogramma e la parola sotto. La casella di <b>xyzabc</b> è vuota, con la scritta in rosso.</div>

</div>
</div>

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
sotto la casella e fammi cliccare quello che preferisco.
```

<div class="check"><b>Cosa vedete:</b> sotto "foglia" 4 miniature. Cliccate la foglia secca: l'immagine grande della casella cambia.</div>

---

### Proviamo a stampare

Premete il pulsante **Stampa**.

<div class="check"><b>Cosa vedete:</b> niente, oppure un messaggio di errore.</div>

<div class="warn">Non è colpa del prompt. Dentro Canvas la pagina gira in un riquadro protetto, e il riquadro blocca la stampa.</div>

---

### Correggere · Scarica PDF

Nella stessa chat:

```text
Il pulsante "Stampa" dentro Canvas non funziona.
Sostituiscilo con un pulsante "Scarica PDF" che salva solo la griglia,
con le librerie html2canvas e jsPDF.
Carica le immagini con crossOrigin="anonymous".
Nel PDF metti solo il pittogramma scelto, senza le miniature.
```

<div class="check"><b>Cosa vedete:</b> al posto di Stampa il pulsante Scarica PDF. Premetelo: parte un download. Aprite il file: dentro c'è la sola griglia, con i pittogrammi.</div>

---

### Se qualcosa non va

Descrivete a Gemini **cosa vedete**:

```text
Il PDF si scarica ma le caselle sono vuote, senza immagini.
```

<div class="warn">Una correzione per messaggio. Se dopo tre tentativi non funziona, alzate la mano.</div>

---

### Per chi finisce prima · Un'altra lista

Cancellate le parole nel riquadro e incollate:

```text
merenda
mela
pane
succo
biscotto
acqua
bere
tovagliolo
```

<div class="check"><b>Cosa vedete:</b> una nuova griglia, con i pittogrammi della merenda. Scaricate anche questa in PDF.</div>

---

### Da ricordare

- I pittogrammi arrivano da **ARASAAC**, non li disegna Gemini.
- Il primo risultato non è sempre quello giusto: si controlla ogni immagine e, se serve, si sceglie tra le miniature.
- Dentro Canvas la stampa è bloccata: si chiede un pulsante **Scarica PDF**.

---

### Crediti

<div class="credits">

Pittogrammi: autore Sergio Palao. Origine: ARASAAC (<a href="https://arasaac.org">arasaac.org</a>). Licenza: CC BY-NC-SA. Proprietà: Governo di Aragona (Spagna).

</div>
