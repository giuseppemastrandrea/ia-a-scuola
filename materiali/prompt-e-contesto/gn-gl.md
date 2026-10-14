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

# La storia con GN e GL

<p class="meta">Giuseppe Mastrandrea</p>

---

### Cosa facciamo

Chiediamo a Gemini un racconto con un **vincolo ortografico** (10 parole con GN, 5 con GL), poi lo controlliamo a mano.


<p class="meta" style="text-align:center">Tecnica: verificare l'output</p>

---

### Il prompt

```text
Ambito: insegnamento dell'italiano nella primaria, classe seconda.
Compito: scrivi un racconto di 120 parole con almeno 10 parole
che contengono GN e 5 che contengono GL.
```

---

### Ora contate voi

<div class="cols">
<div>

1. Copiate il racconto in un Documento Google.
2. Evidenziate in verde le parole con **GN** e in azzurro quelle con **GL**.
3. Contate le parole totali: menu **Strumenti → Conteggio parole**.

</div>
</div>

---

### Cosa controllare

<div class="cols">
<div class="card"><h2>GN e GL</h2><p>Sono almeno 10 e 5? Ci sono parole contate due volte?</p></div>
<div class="card"><h2>Lunghezza</h2><p>Il racconto ha davvero circa 120 parole?</p></div>
<div class="card"><h2>Classe seconda</h2><p>Il lessico e la lunghezza delle frasi vanno bene per bambini di 7 anni?</p></div>
</div>

---

### Secondo tentativo: Gemini si controlla

```text
Elenca le parole con GN e con GL che hai usato nel racconto.
```

Confrontate l'elenco con il testo. Cercate parole che **nel racconto non ci sono** e parole che **l'elenco salta**.

---

### Perché succede

Gemini non legge lettera per lettera: lavora su **pezzi di parola** (token).

Per questo, quando deve contare lettere, sillabe o parole, può sbagliare anche se il testo scorre bene.

---

### La regola

Quando il vincolo è **il cuore dell'esercizio** (un suono, una lunghezza, un numero di parole), il controllo si fa a mano.

<p class="note">Chiedere a Gemini l'elenco delle parole usate aiuta il controllo, ma non lo sostituisce.</p>
