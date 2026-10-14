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
  a { color: inherit; text-decoration: underline; text-decoration-color: var(--accent); text-underline-offset: 3px; }
---

<!-- _class: lead -->
<!-- _paginate: false -->

### Prompt e contesto · Esercitazione

# Costruire i profili

<p class="meta">Giuseppe Mastrandrea</p>

---

### Cosa facciamo

<div class="cols">
<div>

Con Gemini trasformiamo le vostre osservazioni su alcuni alunni in **profili descritti per come funzionano in classe**.

Diventano la prima fonte del **notebook di classe** (modulo NotebookLM) e la base del Gem e della skill (modulo Gem e skill).

<p class="meta">Tecniche: template, esempio guida, verifica dei bias</p>

</div>
</div>

---

### Prima di cominciare

## Come si descrive un alunno

Una lettera al posto del nome (profilo A, B, C…) e:

- **niente nome**
- **niente diagnosi**
- **niente dati del PEI**

Si descrive il bisogno, non la persona.

---

### Passo 1 · Il prompt con l'etichetta

```text
Ambito: insegnamento di sostegno nella primaria.
Descrivi un alunno dislessico di classe quarta.
```

<p class="note">Incollate il prompt in una chat nuova di Gemini e leggete la risposta.</p>

---

### Passo 1 · Cosa notiamo

<div class="cols">
<div class="card"><h2>Da manuale</h2><p>Descrive la dislessia in generale, non un bambino in una classe.</p></div>
<div class="card"><h2>Solo difficoltà</h2><p>I punti di forza mancano o stanno in una riga finale.</p></div>
<div class="card"><h2>Scelte non richieste</h2><p>Gemini può inventare un nome e decidere il genere.</p></div>
</div>

---

### Passo 2 · Il template

## Quattro voci fisse per ogni profilo

<div class="cols">
<div class="card"><h2>Punti di forza</h2><p>Cosa sa fare e cosa gli piace</p></div>
<div class="card"><h2>Difficoltà</h2><p>Cosa osserviamo in classe</p></div>
<div class="card"><h2>Cosa lo aiuta</h2><p>Strumenti e modi di lavorare</p></div>
<div class="card"><h2>Cosa lo ostacola</h2><p>Situazioni da evitare</p></div>
</div>

---

### Passo 2 · Il prompt (prima parte)

<div class="small">

```text
Ambito: insegnamento di sostegno nella primaria.
Compito: trasformare le mie osservazioni su alcuni alunni in profili per la progettazione didattica.
Vincoli: niente nomi, niente diagnosi, niente riferimenti a etnia o genere.
Descrivi solo il funzionamento in classe.
Formato: usa esattamente questa struttura, come nell'esempio.

Profilo A, classe quarta
Punti di forza: capisce i testi letti ad alta voce, ha un lessico ricco,
partecipa volentieri alle discussioni.
Difficoltà: legge lentamente e con fatica, confonde b/d e p/q,
dopo 10 righe perde il filo.
Cosa lo aiuta: testi brevi, ascolto in audio, schemi con parole chiave.
Cosa lo ostacola: pagine fitte, consegne lunghe scritte,
lettura ad alta voce davanti alla classe.
```

</div>

---

### Passo 2 · Il prompt (seconda parte)

Nello stesso messaggio, sotto l'esempio:

```text
Con la stessa struttura crea i profili B, C e D
a partire dalle mie osservazioni:
B: [cosa osservi in classe, senza nome né diagnosi]
C: [...]
D: [...]
```

<p class="note">Il profilo A fa da esempio guida: mostra a Gemini il livello di dettaglio che vogliamo. Le osservazioni scrivetele come le raccontereste a una collega: cosa fa, cosa gli riesce, quando si blocca.</p>

---

### Passo 2 · Confrontiamo

Rispetto al passo 1, il template:

- obbliga a scrivere **i punti di forza**
- rende i 4 profili **confrontabili** tra loro
- toglie a Gemini le scelte su **nome e genere**

---

### Passo 3 · La verifica delle esperte

Per ogni profilo, tre domande:

<div class="cols">
<div class="card"><h2>È fedele?</h2><p>Corrisponde a quello che osservate, o Gemini ha aggiunto cose che non avete scritto?</p></div>
<div class="card"><h2>È stereotipato?</h2><p>Dove le osservazioni erano scarse, Gemini ha riempito i vuoti con luoghi comuni?</p></div>
<div class="card"><h2>Si può usare?</h2><p>"Cosa lo aiuta" e "Cosa lo ostacola" bastano per decidere un adattamento?</p></div>
</div>

---

### Passo 3 · Correggere con un prompt

```text
Nel profilo B togli quello che non ho scritto io
e rendi più concrete le voci "Cosa lo aiuta".
```

<p class="note">Una correzione per volta: si vede subito cosa cambia.</p>

---

### Passo 4 · Salvare

<div class="cols">
<div>

Copiate i 4 profili finali in un Documento Google chiamato **Profili della classe**, nella cartella del kit.

È la prima fonte del notebook di classe.

</div>
</div>

---

<!-- _class: big -->

# Il template lo scrive la docente,
# Gemini lo riempie.
