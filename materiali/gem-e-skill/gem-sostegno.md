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

### Gem e skill · Esercitazione

# Il mio Gem di sostegno

<p class="meta">Giuseppe Mastrandrea</p>

---

### Cosa facciamo

<div class="cols">
<div>

Raccogliamo in un **Gem** le regole delle esercitazioni precedenti, così non vanno riscritte a ogni prompt.

Il notebook dice al modello **cosa sa**, il Gem dice **come lavora**.

<p class="meta">Tecnica: istruzioni salvate e riutilizzabili</p>

</div>
</div>

---

### Gem: due livelli di prompt

<div class="cols">
<div class="card"><h2>Istruzioni del Gem</h2><p>Scritte una volta, valgono per ogni conversazione: ambito, regole, formato, file di riferimento.</p></div>
<div class="card"><h2>Richiesta del momento</h2><p>Quello che scrivete ogni volta: "adatta questa scheda", "prepara il vocabolario per la palestra".</p></div>
</div>

---

### Cosa entra nel contesto

<div class="schema"><img src="../comune/schemi/gem.svg"></div>

<p class="note" style="text-align:center">Istruzioni e conoscenza del Gem occupano spazio a ogni risposta, anche quando non servono.</p>

---

### Creare il Gem

1. Da browser apri **Gemini**.
2. Menu a sinistra: **Esplora Gem → Nuovo Gem**.
3. Dai un nome, per esempio **Sostegno primaria**.
4. Incolla le istruzioni della slide successiva.
5. In **Conoscenza** allega il Documento **Profili della classe**.

<div class="shot" style="height:200px">Screenshot: editor del Gem con istruzioni e conoscenza</div>

---

### Le istruzioni del Gem

<div class="small">

```text
Ambito: insegnamento di sostegno nella primaria.
Compito: aiutarmi a preparare materiali adattati per alunni con bisogni diversi.
Riferimenti: usa i profili del file allegato. Quando proponi
un adattamento, indica per quale profilo.

Regole:
- L'obiettivo di apprendimento resta uguale per tutti. Se lo abbassi, dimmelo.
- Per ogni adattamento spiega cosa hai cambiato e perché.
- Se ti chiedo testi con vincoli su parole, lettere o suoni, alla fine
  elenca le parole usate, così posso controllarle.
- Per la CAA non generare immagini: proponi le parole da cercare su ARASAAC.
- Non chiedere mai nome, diagnosi o dati degli alunni.
  Se li scrivo io, ricordami di toglierli.

Formato: frasi brevi; una tabella quando confronti più versioni.
```

</div>

---

### Ritroviamo le esercitazioni

<div class="cols">
<div class="card"><h2>I profili</h2><p>I profili diventano il file di riferimento.</p></div>
<div class="card"><h2>Il notebook di classe</h2><p>Obiettivo invariato e "cosa ho cambiato e perché", come nel notebook.</p></div>
<div class="card"><h2>La storia con GN e GL</h2><p>L'elenco delle parole da controllare.</p></div>
<div class="card"><h2>La tabella CAA</h2><p>I simboli da ARASAAC, non generati.</p></div>
</div>

---

### Mettere alla prova il Gem

Tre richieste, una per volta:

```text
Adatta questa breve consegna di matematica per il profilo C: [incolla].
```

```text
Scrivi 5 frasi con almeno 3 parole con GN per il profilo A.
```

```text
Prepara il vocabolario per una tabella CAA per la palestra.
```

<p class="note">Dopo ogni risposta, se una regola non è stata rispettata, correggete le istruzioni del Gem.</p>

---

### Prova di resistenza

Scambiatevi il Gem con la collega accanto. Provate a fargli rompere una regola:

- scrivete un nome e una diagnosi inventati nel prompt
- chiedete di generare i simboli come immagini
- chiedete di "semplificare" abbassando l'obiettivo

Se il Gem cede, aggiungete una regola alle istruzioni.

---

### Il prodotto

Un Gem **Sostegno primaria** con il file dei profili, provato con 3 richieste e una prova di resistenza.

Salvate il link del Gem nella cartella del kit.


---

### Prossimo passo

## I Gem diventeranno skill

- Nelle scuole le skill arrivano nell'app Gemini tra il **13 ottobre** e metà novembre 2026; per un periodo Gem e skill convivono.
- Non prima del **1° giugno 2027** i Gem si spengono, anche in Classroom, e diventano skill in bozza.

<p class="note">Fonte: Google Workspace Help, "About the transition from Gems to skills".</p>
