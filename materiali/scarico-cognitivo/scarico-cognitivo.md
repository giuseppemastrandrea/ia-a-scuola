---
marp: true
paginate: true
size: 16:9
title: Scarico cognitivo e fatica desiderabile
style: |
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
  :root { --fg: #1a1a1a; --muted: #777; --accent: #2563eb; --line: #e5e5e5; --ok: #16a34a; --no: #dc2626; --soft: #e6eeff; }
  section { background: #fff; color: var(--fg); font-family: 'Inter', sans-serif; font-weight: 300; font-size: 28px; padding: 56px 80px; }
  h1 { font-weight: 800; font-size: 1.9em; letter-spacing: -0.02em; margin: 0 0 0.4em; }
  h2 { font-weight: 600; font-size: 1.25em; margin: 0 0 0.6em; }
  h3 { font-weight: 600; font-size: 0.6em; color: var(--muted); text-transform: uppercase; letter-spacing: 0.18em; margin: 0 0 0.8em; }
  strong { font-weight: 600; color: var(--accent); }
  li { margin: 0.3em 0; }
  .src { display: block; color: var(--muted); font-size: 0.5em; margin-top: 1em; }
  .src a { color: inherit; }
  a { color: inherit; text-decoration: underline; text-decoration-color: var(--accent); text-underline-offset: 3px; }
  section::after { color: #bbb; font-size: 0.5em; }
  section.lead { display: flex; flex-direction: column; justify-content: center; }
  section.lead h1 { font-size: 2.4em; }
  section.big { display: flex; flex-direction: column; justify-content: center; text-align: center; }
  section.big h1 { font-size: 1.8em; line-height: 1.25; }
  section.big p { color: var(--muted); }
  .cols { display: flex; gap: 48px; align-items: center; }
  .cols > * { flex: 1; }
  .small { font-size: 0.7em; } .muted { color: var(--muted); }
  [data-bespoke-marp-fragment=inactive] { visibility: visible; opacity: 0; transition: none; }
  [data-bespoke-marp-fragment=active] { opacity: 1; transition: opacity 0.6s ease; }

  .pa { display: flex; gap: 36px; }
  .pa > div { flex: 1; border-radius: 16px; padding: 24px 28px; }
  .pa .p { background: #fff4d6; } .pa .a { background: var(--soft); }
  .pa b { display: block; font-size: 0.6em; text-transform: uppercase; letter-spacing: 0.14em; color: var(--muted); }
  .pa h2 { margin: 0.2em 0 0.3em; }
  .pa p { margin: 0; font-size: 0.75em; }

  .chart { display: flex; gap: 60px; justify-content: center; margin-top: 0.4em; }
  .grp { text-align: center; }
  .grp > b { display: block; font-size: 0.75em; margin-top: 10px; }
  .grp > span { display: block; font-size: 0.55em; color: var(--muted); }
  .bars { display: flex; gap: 22px; align-items: center; height: 330px; position: relative; }
  .bars::after { content: ''; position: absolute; left: -12px; right: -12px; top: 230px; border-top: 2px solid var(--fg); }
  .bar { width: 90px; height: 330px; position: relative; }
  .bar i { position: absolute; left: 0; right: 0; border-radius: 4px; }
  .bar .v { position: absolute; left: 0; right: 0; font-weight: 800; font-size: 0.8em; }
  .bar .l { position: absolute; left: -10px; right: -10px; top: 300px; font-size: 0.5em; color: var(--muted); }
  .up i { bottom: 100px; background: #f59e0b; } .up .v { color: #b45309; }
  .dn i { top: 230px; background: var(--no); } .dn .v { color: var(--no); }
  .eq i { top: 228px; height: 4px; background: var(--ok); } .eq .v { color: var(--ok); top: 190px; }

  .step svg { display: block; }
  .step text { font-family: Inter, sans-serif; }

  table.f { border-collapse: collapse; width: 100%; font-size: 0.72em; }
  table.f th, table.f td { border: 0; border-bottom: 1px solid var(--line); padding: 10px 14px; text-align: left; background: none; vertical-align: top; }
  table.f th { font-size: 0.75em; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 600; border-bottom: 2px solid var(--fg); }
  table.f th:first-child { color: var(--ok); } table.f th:last-child { color: var(--muted); }
  table.f tr { background: none !important; }

  .qs ul { list-style: none; padding: 0; margin: 0; }
  .qs li { font-size: 0.95em; font-weight: 400; padding: 14px 0 14px 22px; border-left: 4px solid var(--accent); margin: 0 0 14px; background: #fafbff; }
  .qs li span { display: block; font-size: 0.65em; font-weight: 300; color: var(--muted); margin-top: 4px; }
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Scarico cognitivo e fatica desiderabile

Cosa deleghiamo all'IA, e cosa perdiamo delegando

---

<!-- _class: big -->

# Quanti numeri di telefono sapete a memoria?

E quante strade della vostra città sapreste fare senza navigatore?

---

### Scarico cognitivo

## Affidare a uno strumento un lavoro della mente

<div class="cols" style="align-items:flex-start">
<div>

* La lista della spesa, il calendario, la calcolatrice, il navigatore
* **Non è un male**: libera la mente per altro. Lo facciamo da sempre
* Il problema nasce quando si scarica **proprio il lavoro che serviva a imparare**

</div>
<div class="small muted">

Già nel 2011, prima dell'IA: quando sappiamo che un'informazione resterà disponibile online, ricordiamo meno l'informazione e di più **dove trovarla**.

<span class="src">B. Sparrow, J. Liu, D. Wegner, <a href="https://www.science.org/doi/10.1126/science.1207745">Google Effects on Memory</a>, Science, 2011.</span>

</div>
</div>

---

### Fatica desiderabile

<div class="pa">
<div class="p"><b>Prestazione</b><h2>Quanto va bene adesso</h2><p>Durante l'esercizio, con l'aiuto a portata di mano</p></div>
<div class="a"><b>Apprendimento</b><h2>Quanto resta dopo</h2><p>Quando l'aiuto non c'è più</p></div>
</div>

<div class="small" style="margin-top:1em">

* Spesso vanno in **direzioni opposte**: ciò che rende facile l'esercizio può far imparare meno
* Alcune difficoltà rallentano, ma fanno ricordare di più: sono le **fatiche desiderabili**

</div>

<span class="src">Robert A. Bjork ed Elizabeth L. Bjork, University of California, Los Angeles. N. Soderstrom, R. Bjork, Learning versus Performance, Perspectives on Psychological Science, 2015.</span>

---

### Un esperimento: matematica in un liceo turco

<div class="chart">
<div class="grp">
<div class="bars">
<div class="bar up"><i style="height:40px"></i><span class="v" style="bottom:144px">+48%</span><span class="l">esercizi</span></div>
<div class="bar dn"><i style="height:14px"></i><span class="v" style="top:250px">−17%</span><span class="l">verifica</span></div>
</div>
<b>ChatGPT libero</b><span>risponde a tutto</span>
</div>
<div class="grp">
<div class="bars">
<div class="bar up"><i style="height:105px"></i><span class="v" style="bottom:209px">+127%</span><span class="l">esercizi</span></div>
<div class="bar eq"><i></i><span class="v">≈ 0</span><span class="l">verifica</span></div>
</div>
<b>ChatGPT tutor</b><span>dà indizi, non soluzioni</span>
</div>
</div>

<p class="small" style="text-align:center;margin-top:0.6em">Circa mille studenti. Rispetto a chi non aveva l'IA: durante gli esercizi tutti meglio, nella verifica senza IA chi aveva ChatGPT libero <strong>peggio</strong>.</p>

<span class="src">H. Bastani e altri, <a href="https://www.pnas.org/doi/10.1073/pnas.2422633122">Generative AI without guardrails can harm learning</a>, PNAS, 2025.</span>

---

### Quando una fatica è desiderabile

<div class="cols">
<div class="step">
<svg width="520" height="300" viewBox="0 0 520 300">
<line x1="10" y1="260" x2="510" y2="260" stroke="#1a1a1a" stroke-width="3"/>
<rect x="60" y="200" width="140" height="60" fill="#dcfce7" stroke="#16a34a" stroke-width="3"/>
<text x="130" y="236" text-anchor="middle" font-size="18" font-weight="700" fill="#16a34a">superabile</text>
<rect x="320" y="40" width="140" height="220" fill="#fee2e2" stroke="#dc2626" stroke-width="3"/>
<text x="390" y="160" text-anchor="middle" font-size="18" font-weight="700" fill="#dc2626">un muro</text>
<text x="130" y="290" text-anchor="middle" font-size="18" fill="#777">fatica desiderabile</text>
<text x="390" y="290" text-anchor="middle" font-size="18" fill="#777">ostacolo</text>
</svg>
</div>
<div class="small">

* Una difficoltà è desiderabile **solo se lo studente riesce a superarla**
* Altrimenti è un ostacolo, e basta
* Qui l'IA può aiutare davvero: una barriera di lingua, una dislessia, una consegna scritta male

</div>
</div>

---

### Quale fatica stai togliendo?

<table class="f">
<tr><th>Da proteggere</th><th>Si può togliere</th></tr>
<tr><td>Recuperare dalla memoria, invece di rileggere</td><td>Cercare e raccogliere i materiali</td></tr>
<tr><td>Provare a rispondere prima di vedere la soluzione</td><td>Decifrare una consegna scritta male</td></tr>
<tr><td>Spiegare con parole proprie</td><td>Impaginare, formattare</td></tr>
<tr><td>Riprendere un argomento a distanza di tempo</td><td>Le barriere di accesso: lingua, dislessia, BES</td></tr>
<tr><td>Alternare esercizi di tipo diverso</td><td></td></tr>
</table>

---

### Cosa dicono gli altri studi, con cautela

<div class="small">

* **Lavoratori, Microsoft e Carnegie Mellon** (319 persone, 2025): più fiducia nell'IA va con meno pensiero critico; più fiducia in sé stessi, con più pensiero critico. È un'indagine: associazioni, non cause
* **«Your Brain on ChatGPT», MIT** (54 persone, 2025): chi scriveva con ChatGPT mostrava meno connettività cerebrale all'EEG. Campione piccolo, preprint: gli autori stessi chiedono di considerarlo preliminare
* Sui giornali questi studi diventano «l'IA ci rende stupidi». **Non dicono questo**

</div>

<span class="src">H.-P. Lee e altri, <a href="https://dl.acm.org/doi/10.1145/3706598.3713778">The Impact of Generative AI on Critical Thinking</a>, CHI 2025. N. Kosmyna e altri, <a href="https://www.media.mit.edu/projects/your-brain-on-chatgpt/overview/">Your Brain on ChatGPT</a>, MIT Media Lab, giugno 2025.</span>

---

<!-- _class: big -->

# Chi ha già le competenze usa l'IA meglio. Chi non le ha rischia di non costruirle

L'IA può allargare il divario che la scuola cerca di ridurre

---

### Spunti per la discussione

<div class="qs">

* Se uno studente con l'IA scrive un tema migliore, ha imparato di più?<span>Prestazione o apprendimento?</span>
* Chi decide quale fatica è inutile: lo studente, il docente, o chi ha progettato lo strumento?<span>Un'app pensata per farti tornare non è pensata per renderti autonomo</span>
* Per uno studente con DSA, l'IA toglie un ostacolo o una fatica?<span>La risposta può cambiare da studente a studente</span>
* E noi docenti? Se deleghiamo la correzione o la progettazione, cosa smettiamo di saper fare?

</div>

---

<!-- _class: big -->

# Non chiederti se usare l'IA. Chiediti **quale fatica** stai togliendo, e a chi

