---
marp: true
paginate: true
size: 16:9
title: Il modello nudo
style: |
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
  :root { --fg: #1a1a1a; --muted: #777; --accent: #2563eb; --line: #e5e5e5; --pick: #f59e0b; --sys: #0d9488; --sys-soft: #ccfbf1; --mod-soft: #e6eeff; --no: #dc2626; }
  section { background: #fff; color: var(--fg); font-family: 'Inter', sans-serif; font-weight: 300; font-size: 28px; padding: 56px 80px; }
  h1 { font-weight: 800; font-size: 1.9em; letter-spacing: -0.02em; margin: 0 0 0.4em; }
  h2 { font-weight: 600; font-size: 1.25em; margin: 0 0 0.6em; }
  h3 { font-weight: 600; font-size: 0.6em; color: var(--muted); text-transform: uppercase; letter-spacing: 0.18em; margin: 0 0 0.8em; }
  strong { font-weight: 600; color: var(--accent); }
  ul, ol { padding-left: 1.1em; } li { margin: 0.25em 0; }
  .src { display: block; color: var(--muted); font-size: 0.5em; font-style: normal; margin-top: 1em; }
  .src a { color: inherit; }
  section::after { color: #bbb; font-size: 0.5em; }
  section.lead { display: flex; flex-direction: column; justify-content: center; }
  section.lead h1 { font-size: 2.6em; }
  section.big { display: flex; flex-direction: column; justify-content: center; text-align: center; }
  section.big h1 { font-size: 1.9em; line-height: 1.25; }
  section.big p { color: var(--muted); }
  .cols { display: flex; gap: 48px; align-items: center; }
  .cols > * { flex: 1; }
  .muted { color: var(--muted); }
  .small { font-size: 0.7em; }
  a { color: inherit; text-decoration: underline; text-decoration-color: var(--accent); text-underline-offset: 3px; }
  [data-bespoke-marp-fragment=inactive] { visibility: visible; opacity: 0; transition: none; }
  [data-bespoke-marp-fragment=active] { opacity: 1; transition: opacity 0.6s ease; }
  .plain ul, .plain ol { list-style: none; padding: 0; }

  /* attività */
  .temi ol { columns: 1; font-size: 0.95em; }
  .temi li { padding: 6px 0; border-bottom: 1px solid var(--line); }
  .tag { display: inline-block; font-size: 0.5em; font-weight: 600; text-transform: uppercase; letter-spacing: 0.14em; padding: 4px 10px; border-radius: 6px; background: var(--mod-soft); color: var(--accent); }
  .tag.sys { background: var(--sys-soft); color: var(--sys); }

  /* un solo obiettivo */
  .masked { font-size: 1.35em; font-weight: 400; margin: 0.2em 0 0.8em; }
  .masked .gap { display: inline-block; min-width: 150px; border-bottom: 4px dashed var(--accent); color: var(--accent); font-weight: 600; text-align: center; }
  .loop { display: flex; align-items: center; gap: 18px; font-size: 0.85em; }
  .loop span { white-space: nowrap; padding: 10px 18px; border-radius: 10px; background: var(--mod-soft); font-weight: 600; }
  .loop i { font-style: normal; color: var(--muted); }
  .loop .x { background: none; color: var(--accent); font-weight: 800; font-size: 1.1em; }
  .check { display: flex; gap: 28px; margin: 1.2em 0 1em; }
  .check > div { flex: 1; border-radius: 12px; padding: 16px 22px; font-size: 0.8em; }
  .check .yes { background: #ecfdf5; border: 2px solid #16a34a; }
  .check .no { background: #fef2f2; border: 2px dashed var(--no); }
  .check b { display: block; font-size: 0.7em; text-transform: uppercase; letter-spacing: 0.14em; margin-bottom: 4px; }
  .check .yes b { color: #16a34a; } .check .no b { color: var(--no); }

  /* il testo non ci sta */
  .sq { display: flex; align-items: flex-end; gap: 70px; margin-top: 0.4em; }
  .sq .a { width: 400px; height: 400px; background: repeating-linear-gradient(0deg, #dbe4ff 0 3px, #eef2ff 3px 9px); border: 2px solid var(--accent); border-radius: 6px; position: relative; }
  .sq .b { width: 48px; height: 48px; background: var(--accent); border-radius: 4px; }
  .sq .lab { font-size: 0.75em; margin-top: 10px; }
  .sq .lab b { display: block; font-size: 1.5em; font-weight: 800; color: var(--accent); }
  .sq .txt { flex: 1; font-size: 0.85em; }

  /* la scala della frequenza */
  .scale { display: flex; flex-direction: column; gap: 18px; margin-top: 0.3em; }
  .scale .r { display: grid; grid-template-columns: 250px 1fr 300px; align-items: center; gap: 24px; }
  .scale .f { font-size: 0.65em; font-weight: 600; text-transform: uppercase; letter-spacing: 0.12em; color: var(--muted); }
  .scale .f em { display: block; font-style: normal; font-weight: 300; text-transform: none; letter-spacing: 0; font-size: 1.15em; color: var(--fg); }
  .scale .q { font-family: Georgia, serif; font-size: 0.95em; padding: 14px 20px; background: #fafafa; border-radius: 10px; border: 1px solid var(--line); }
  .scale .r1 .q { filter: blur(5px); }
  .scale .r2 .q { filter: blur(1.6px); }
  .scale .k { font-size: 0.7em; }
  .scale .k b { color: var(--accent); font-weight: 600; }

  /* frequente non vuol dire vero */
  .wall { position: relative; height: 330px; overflow: hidden; border-radius: 12px; background: #fafafa; border: 1px solid var(--line); padding: 14px 18px; }
  .wall p { margin: 0; font-size: 0.55em; line-height: 1.75; color: #9aa3b5; white-space: nowrap; }
  .wall p b { color: #6b7280; font-weight: 600; }
  .one { border-left: 4px solid var(--fg); padding: 10px 18px; font-size: 0.75em; background: #fff; }
  .one b { display: block; font-size: 0.7em; text-transform: uppercase; letter-spacing: 0.14em; color: var(--muted); }

  /* il verso */
  .rev svg { display: block; margin: 0 auto; }
  .rev text { font-family: Inter, sans-serif; }

  /* xerox */
  .plan { display: flex; gap: 40px; justify-content: center; margin-top: 0.4em; }
  .plan figure { margin: 0; text-align: center; }
  .plan .room { width: 330px; height: 210px; border: 6px solid #333; display: flex; align-items: center; justify-content: center; font-family: 'Courier New', monospace; font-size: 1.5em; font-weight: 700; background: #fff; }
  .plan .room.bad { color: var(--no); }
  .plan figcaption { font-size: 0.6em; color: var(--muted); margin-top: 10px; text-transform: uppercase; letter-spacing: 0.14em; font-weight: 600; }
  .vs { display: flex; gap: 30px; margin-top: 1em; font-size: 0.75em; }
  .vs > div { flex: 1; }
  .blurimg { display: inline-block; filter: blur(1.1px); font-weight: 700; }

  /* due memorie */
  .mem { display: flex; gap: 40px; }
  .mem > div { flex: 1; border-radius: 16px; padding: 24px 28px; }
  .mem .p { background: #f4f4f5; }
  .mem .c { background: var(--mod-soft); }
  .mem h2 { margin: 0.3em 0 0.4em; }
  .mem ul { list-style: none; padding: 0; margin: 0; font-size: 0.72em; }
  .mem li { padding: 6px 0; border-top: 1px solid rgba(0,0,0,0.08); }
  .mem li b { display: inline-block; width: 160px; color: var(--muted); font-weight: 600; font-size: 0.85em; text-transform: uppercase; letter-spacing: 0.08em; }
  .mem svg { display: block; height: 110px; }

  /* il secchio del contesto */
  .buckets { display: flex; gap: 70px; justify-content: center; align-items: flex-end; }
  .buckets figure { margin: 0; text-align: center; }
  .buckets figcaption { font-weight: 600; font-size: 0.8em; margin-top: 8px; white-space: nowrap; }
  .buckets figcaption span { display: block; font-weight: 300; font-size: 0.75em; color: var(--muted); }
  .bk text { font-family: Inter, sans-serif; font-size: 17px; font-weight: 600; }
  .layer { opacity: 0; transition: opacity 0.6s; }
  section.fill:has(.fsteps li:nth-child(1)[data-bespoke-marp-fragment=active]) .l1,
  section.fill:has(.fsteps li:nth-child(2)[data-bespoke-marp-fragment=active]) .l2,
  section.fill:has(.fsteps li:nth-child(3)[data-bespoke-marp-fragment=active]) .l3,
  section.fill:has(.fsteps li:nth-child(4)[data-bespoke-marp-fragment=active]) .l4 { opacity: 1; }
  .layer.l0 { opacity: 1; }
  .fsteps { font-size: 0.6em; }
  .fsteps ul { list-style: none; padding: 0; margin: 0; }
  .fsteps li { margin: 0 0 12px; padding-left: 12px; border-left: 3px solid var(--sys); }

  /* AI Overviews */
  .ov { display: flex; gap: 40px; align-items: center; }
  .ov .card { flex: 1; border: 1px solid var(--line); border-radius: 14px; padding: 18px 22px; font-size: 0.72em; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
  .ov .card .h { font-size: 0.75em; color: var(--muted); font-weight: 600; margin-bottom: 6px; }
  .ov .card .h::before { content: '✦ '; color: var(--accent); }
  .ov .card q { font-family: Georgia, serif; }
  .ov .from { font-size: 0.75em; margin-top: 10px; padding-top: 10px; border-top: 1px dashed var(--line); color: var(--muted); }
  .ov .from b { color: var(--fg); font-weight: 600; }

  /* modello e sistema */
  .rings { display: flex; gap: 50px; align-items: center; }
  .rings svg text { font-family: Inter, sans-serif; }
  .legend { flex: 1; font-size: 0.72em; }
  .legend p { margin: 0 0 14px; }

  /* rilettura */
  table.sort { border-collapse: collapse; width: 100%; font-size: 0.72em; }
  table.sort td, table.sort th { border: 0; border-bottom: 1px solid var(--line); padding: 10px 14px; background: none; text-align: left; }
  table.sort th { font-size: 0.75em; text-transform: uppercase; letter-spacing: 0.12em; color: var(--muted); font-weight: 600; border-bottom: 2px solid var(--fg); }
  table.sort tr { background: none !important; }
  /* xerox: il perché */
  .jb { display: flex; align-items: center; gap: 18px; margin: 0.2em 0 0.8em; }
  .jb > i { font-style: normal; font-size: 1.4em; color: var(--muted); }
  .jb .st { flex: 1; text-align: center; }
  .jb .st b { display: block; font-size: 0.6em; text-transform: uppercase; letter-spacing: 0.14em; color: var(--accent); margin-bottom: 8px; }
  .jb .st p { font-size: 0.6em; margin: 8px 0 0; }
  .tiles { display: flex; justify-content: center; gap: 6px; }
  .tiles span { font-family: 'Courier New', monospace; font-weight: 700; font-size: 1.2em; width: 46px; height: 60px; display: flex; align-items: center; justify-content: center; border: 2px dashed #999; border-radius: 6px; background: #fff; }
  .tiles span.g { border: 2px solid var(--accent); background: var(--mod-soft); }
  .tiles.bad span { border-style: solid; border-color: #333; }
  .tiles.w span { width: auto; padding: 0 10px; font-size: 1em; }
  .tiles span.x { color: #bbb; text-decoration: line-through; }
  .tiles.bad span:first-child { color: var(--no); }
  .cmp { display: flex; gap: 22px; }
  .cmp > div { flex: 1; border: 1px solid var(--line); border-radius: 12px; padding: 12px 16px; font-size: 0.65em; }
  .cmp > div.llm { border-color: var(--accent); background: var(--mod-soft); }
  .cmp b { display: block; font-size: 0.8em; text-transform: uppercase; letter-spacing: 0.12em; color: var(--muted); margin-bottom: 6px; }
  .cmp p { margin: 6px 0 0; color: var(--muted); }
  .crisp { font-weight: 700; }
  .cmp .blurimg { filter: blur(2.2px); }
  /* AI Overviews: il flusso */
  .flow ul { list-style: none; padding: 0; margin: 0.2em 0 0.6em; display: flex; gap: 16px; }
  .flow li { flex: 1; margin: 0; }
  .fq { height: 100%; box-sizing: border-box; border: 1px solid var(--line); border-top: 4px solid var(--sys); border-radius: 12px; padding: 14px 16px; font-size: 0.62em; }
  .fq b { display: block; font-size: 0.8em; text-transform: uppercase; letter-spacing: 0.12em; color: var(--sys); margin-bottom: 8px; }
  .fq.ans { border-top-color: var(--accent); background: var(--mod-soft); }
  .fq.ans b { color: var(--accent); }
  .fq q { font-family: Georgia, serif; font-size: 1.1em; }
  .search { display: block; border: 1px solid #ccc; border-radius: 14px; padding: 8px 14px; font-size: 1em; }
  .search::before { content: '🔍 '; }
---

<!-- _class: lead -->
<!-- _paginate: false -->

### Modulo · Il modello nudo

# Il modello nudo

Cosa fa un LLM quando non ha niente intorno

---

<!-- _class: temi -->

### Caccia all'allucinazione

## Prima su LM Arena, poi su Gemini, ChatGPT o Claude

Fate generare a un modello **almeno un'allucinazione** su uno di questi temi:

1. Argomento disciplinare
2. Notizie di attualità
3. Citazione esatta di un testo
4. Personaggi storici o presunti tali
5. Allucinazione logica

<span class="src">LM Arena: <a href="https://lmarena.ai">lmarena.ai</a>, modalità Direct Chat. Niente dati personali: le conversazioni sono pubbliche.</span>

---

<!-- _class: big -->

# Che giorno è oggi?

Chiedetelo, tutti, al modello che avete davanti su LM Arena

---

<!-- _class: big -->

### Parte 1 · Compressione con perdita

# Perché il modello ha inventato, invece di dire «non lo so»?

---

### Come impara

<p class="masked">Il Colosseo si trova a <span class="gap">?</span></p>

<div class="loop"><span>indovina la parola</span><i>→</i><span>confronta con il testo</span><i>→</i><span>regola i parametri</span><span class="x">× migliaia di miliardi</span></div>

<div class="check">
<div class="yes"><b>Viene premiato</b>indovinare la parola che c'era nel testo</div>
<div class="no"><b>Nessuno controlla</b>se quella parola è vera</div>
</div>

<p class="small muted">I <strong>parametri</strong> sono miliardi di numeri che lavorano tutti insieme: non c'è un numero per ogni parola o per ogni frase.</p>

---

<!-- _class: big -->

# L'addestramento ha **un solo obiettivo**: prevedere come continua un testo

La correttezza non è un obiettivo. È un effetto collaterale, che funziona solo dove i testi letti erano frequenti e corretti.

---

### Il testo non ci sta

<div class="sq">
<div><div class="a"></div><p class="lab"><b>~10 TB</b>di testo letto</p></div>
<div><div class="b"></div><p class="lab"><b>140 GB</b>di parametri</p></div>
<div class="txt">

Llama 2 70B, il modello che Karpathy usa come esempio: circa **cento volte** più piccolo dei testi da cui viene.

Non può essere un archivio. È una **compressione con perdita**.

</div>
</div>

<span class="src">Andrej Karpathy, <a href="https://www.youtube.com/watch?v=zjkBMFhNj_g">Intro to Large Language Models</a>, novembre 2023. Aree dei quadrati in proporzione.</span>

---

### Cosa resta dipende da quanto compare

<div class="scale">
<div class="r r1"><div class="f">Raramente<em>un fatto locale</em></div><div class="q">Nel 1987 il preside del liceo di Bitetto era…</div><div class="k">Si perde: il modello <b>ricostruisce</b>, cioè inventa</div></div>
<div class="r r2"><div class="f">Spesso<em>un fatto noto</em></div><div class="q">La Costituzione italiana entra in vigore il 1° gennaio 1948</div><div class="k">Resta <b>il senso</b>, i fatti principali</div></div>
<div class="r r3"><div class="f">Moltissime volte<em>un incipit famoso</em></div><div class="q">Nel mezzo del cammin di nostra vita / mi ritrovai per una selva oscura</div><div class="k">Resta <b>anche la lettera</b></div></div>
</div>

<p class="small muted">La citazione esatta è la prima a cedere: basta una parola sbagliata su trenta.</p>

---

### Frequente non vuol dire vero

<div class="cols" style="align-items:flex-start">
<div class="wall">
<p><b>Maria Antonietta</b>: «Che mangino brioche!» · «S'ils n'ont pas de pain, qu'ils mangent de la brioche»</p>
<p>La regina rispose: «Che mangino brioche» · Maria Antonietta e la famosa frase sulle brioche</p>
<p>«Se non hanno pane, che mangino brioche» disse <b>Maria Antonietta</b> · citazioni celebri</p>
<p>La frase di <b>Maria Antonietta</b> che costò la testa · «Che mangino brioche!»</p>
<p>Le 10 frasi storiche più famose: «Che mangino brioche» (<b>Maria Antonietta</b>)</p>
<p>«Qu'ils mangent de la brioche» · <b>Marie-Antoinette</b> · Let them eat cake</p>
<p>Perché <b>Maria Antonietta</b> disse «che mangino brioche»? · storia per ragazzi</p>
<p>Frasi celebri della Rivoluzione francese: «Che mangino brioche»</p>
<p>«Let them eat cake» · <b>Marie Antoinette</b> · quote · famous quotes</p>
<p>La regina e le brioche: la frase di <b>Maria Antonietta</b> spiegata</p>
</div>
<div>

* Su ogni pagina che il modello ha letto
* <div class="one"><b>Una sola fonte</b>Rousseau, <em>Confessioni</em>, libro VI (scritto intorno al 1765): la frase è di «una grande principessa». Maria Antonietta era una bambina, a Vienna.</div>
* Un errore che circola molto, il modello lo impara **bene quanto un fatto**

</div>
</div>

---

### Il sapere ha un verso

<div class="rev">
<svg width="1000" height="300" viewBox="0 0 1000 300">
  <defs>
    <marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#2563eb"/></marker>
    <marker id="ag" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#bbb"/></marker>
  </defs>
  <rect x="20" y="105" width="230" height="90" rx="14" fill="#e6eeff" stroke="#2563eb" stroke-width="2"/>
  <text x="135" y="158" text-anchor="middle" font-size="26" font-weight="700">Tom Cruise</text>
  <rect x="750" y="105" width="230" height="90" rx="14" fill="#f4f4f5" stroke="#999" stroke-width="2"/>
  <text x="865" y="147" text-anchor="middle" font-size="22" font-weight="700">Mary Lee</text>
  <text x="865" y="175" text-anchor="middle" font-size="22" font-weight="700">Pfeiffer</text>
  <path d="M260 120 C 420 40, 580 40, 740 120" fill="none" stroke="#2563eb" stroke-width="12" marker-end="url(#ah)"/>
  <text x="500" y="38" text-anchor="middle" font-size="22">«Chi è la madre di Tom Cruise?»</text>
  <text x="500" y="128" text-anchor="middle" font-size="30" font-weight="800" fill="#2563eb">79%</text>
  <path d="M740 180 C 580 260, 420 260, 260 180" fill="none" stroke="#bbb" stroke-width="3" stroke-dasharray="10 8" marker-end="url(#ag)"/>
  <text x="500" y="200" text-anchor="middle" font-size="30" font-weight="800" fill="#999">33%</text>
  <text x="500" y="284" text-anchor="middle" font-size="22" fill="#777">«Chi è il figlio di Mary Lee Pfeiffer?»</text>
</svg>
</div>

Sul web si scrive «la madre di Tom Cruise è…», quasi mai il contrario. Il modello impara **come continua il testo**, nel verso in cui è scritto.

<span class="src">GPT-4 su coppie genitore e figlio famoso. L. Berglund e altri, <a href="https://arxiv.org/abs/2309.12288">The Reversal Curse</a>, settembre 2023. Provatelo su LM Arena con un personaggio famoso e un genitore poco noto.</span>

---

### Una scansione, 2013

<div class="cols" style="align-items:center">
<div class="plan" style="flex:0 0 auto">
<figure><div class="room">21,11 m²</div><figcaption>La planimetria</figcaption></figure>
<figure><div class="room bad">14,13 m²</div><figcaption>La scansione</figcaption></figure>
</div>
<div class="small">

* David Kriesel, informatico tedesco, scansiona la planimetria di un edificio con una multifunzione **Xerox**
* Nella copia la stanza da 21,11 m² diventa da **14,13 m²**, come un'altra stanza
* La copia è **perfettamente nitida**: niente fa sospettare un errore

</div>
</div>

<span class="src">WorkCentre 7535 e 7556. <a href="https://www.computerworld.com/article/1396837/xerox-scanners-found-to-sometimes-alter-numbers.html">Computerworld</a>, agosto 2013.</span>

---

### Perché: comprimere riusando i pezzi

<div class="jb">
<div class="st"><b>1 · Taglia</b><div class="tiles w"><span>21,11</span><span>14,13</span></div><p>la pagina in pezzetti. Qui, le etichette di due stanze</p></div>
<i>→</i>
<div class="st"><b>2 · Accorpa</b><div class="tiles w"><span class="x">21,11</span><span class="g">14,13</span></div><p>si somigliano abbastanza: ne tiene <strong>uno solo</strong> e lo riusa</p></div>
<i>→</i>
<div class="st"><b>3 · Ricompone</b><div class="tiles w bad"><span>14,13</span><span>14,13</span></div><p>una pagina nitida, con un numero sbagliato</p></div>
</div>

<div class="cmp">
<div><b>JPEG compresso troppo</b><span class="blurimg">21,11 m²</span><p>Si vede che è rovinato: diffidi</p></div>
<div><b>Scanner Xerox</b><span class="crisp">14,13 m²</span><p>Nitido e falso</p></div>
<div class="llm"><b>LLM</b><span class="crisp">«Nel 1987 il preside del liceo di Bitetto era il prof. Rossi»</span><p>Nitido e, se il dato era raro, inventato</p></div>
</div>

<span class="src">Xerox ha attribuito il difetto alla compressione JBIG2 e ha distribuito una correzione. Ted Chiang usa questo caso in <a href="https://www.newyorker.com/tech/annals-of-technology/chatgpt-is-a-blurry-jpeg-of-the-web">ChatGPT Is a Blurry JPEG of the Web</a>, The New Yorker, 9 febbraio 2023.</span>

---

<!-- _class: big -->

# Il modello ricorda meglio ciò che è stato scritto più spesso

Non ciò che è vero, e quasi mai parola per parola.

---

<!-- _class: big -->

### Parte 2 · Due memorie

# La data giusta poteva essere nei parametri?

L'addestramento è finito mesi fa

---

### Due memorie

<div class="mem">
<div class="p">
<svg viewBox="0 0 160 110"><rect x="30" y="18" width="100" height="80" rx="6" fill="#71717a"/><rect x="38" y="18" width="6" height="80" fill="#52525b"/><g filter="url(#bl)"><rect x="56" y="40" width="58" height="6" rx="3" fill="#d4d4d8"/><rect x="56" y="54" width="44" height="6" rx="3" fill="#d4d4d8"/></g><defs><filter id="bl"><feGaussianBlur stdDeviation="2.5"/></filter></defs></svg>
<span class="tag">Memoria lunga</span>
<h2>I parametri</h2>
<ul>
<li><b>Viene</b> dall'addestramento, mesi fa</li>
<li><b>Com'è</b> compressa, sfocata</li>
<li><b>Dura</b> finché non si riaddestra</li>
<li><b>Come</b> un libro letto anni fa</li>
</ul>
</div>
<div class="c">
<svg viewBox="0 0 160 110"><path d="M80 30 C 60 20, 30 20, 12 26 L12 96 C 30 90, 60 90, 80 100 Z" fill="#fff" stroke="#2563eb" stroke-width="3"/><path d="M80 30 C 100 20, 130 20, 148 26 L148 96 C 130 90, 100 90, 80 100 Z" fill="#fff" stroke="#2563eb" stroke-width="3"/><rect x="24" y="42" width="44" height="5" rx="2" fill="#2563eb"/><rect x="24" y="56" width="38" height="5" rx="2" fill="#2563eb"/><rect x="24" y="70" width="44" height="5" rx="2" fill="#2563eb"/><rect x="92" y="42" width="44" height="5" rx="2" fill="#2563eb"/><rect x="92" y="56" width="40" height="5" rx="2" fill="#2563eb"/></svg>
<span class="tag">Memoria di lavoro</span>
<h2>Il contesto</h2>
<ul>
<li><b>Viene</b> dalla conversazione, adesso</li>
<li><b>Com'è</b> esatta, parola per parola</li>
<li><b>Dura</b> fino alla fine della chat</li>
<li><b>Come</b> il libro aperto sul tavolo</li>
</ul>
</div>
</div>

<p class="small muted" style="margin-top:0.8em">Il contesto è tutto ciò che il modello ha davanti: il prompt, la conversazione, i file caricati.</p>

---

<!-- _class: big -->

### A libro aperto · su LM Arena, stesso modello

# «Oggi è [la data di oggi]. Che giorno della settimana sarà fra dieci giorni?»

Il modello non è cambiato. È cambiato il contesto.

---

### Il limite del libro aperto

<div class="cols">
<div>

* Rifate l'**analisi logica** di prima, incollando la definizione dei complementi dal manuale
* Migliora? Forse. Il testo lo scrive comunque **il modello**, con quello che ha compresso
* Il contesto aiuta sui **fatti**. Non corregge come il modello costruisce le frasi

</div>
<div class="center">
<svg viewBox="0 0 360 230" width="440"><rect x="0" y="0" width="360" height="100" rx="16" fill="#ecfdf5" stroke="#16a34a" stroke-width="2"/><text x="180" y="45" text-anchor="middle" font-family="Inter" font-size="22" font-weight="600" fill="#16a34a">I fatti nel contesto</text><text x="180" y="78" text-anchor="middle" font-family="Inter" font-size="18" fill="#1a1a1a">la data, le fonti, le definizioni</text><rect x="0" y="125" width="360" height="100" rx="16" fill="#f4f4f5" stroke="#999" stroke-width="2" stroke-dasharray="8 6"/><text x="180" y="170" text-anchor="middle" font-family="Inter" font-size="22" font-weight="600" fill="#555">La scrittura</text><text x="180" y="203" text-anchor="middle" font-family="Inter" font-size="18" fill="#1a1a1a">resta del modello</text></svg>
</div>
</div>

---

<!-- _class: big -->

### Parte 3 · Il sistema

# Gemini sa che giorno è. È più intelligente, o qualcuno gliel'ha detto?

---

<!-- _class: fill -->

### Il secchio del contesto

<div class="cols" style="align-items:flex-end">
<div class="buckets">
<figure>
<svg class="bk" width="250" height="300" viewBox="0 0 250 300"><path d="M15 20 L235 20 L210 290 L40 290 Z" fill="#fff" stroke="#111" stroke-width="3"/><g class="layer l0"><path d="M38.4 240 L211.6 240 L207 290 L43 290 Z" fill="#e6eeff"/><text x="125" y="272" text-anchor="middle">la tua domanda</text></g></svg>
<figcaption>LM Arena<span>il modello nudo</span></figcaption>
</figure>
<figure>
<svg class="bk" width="250" height="300" viewBox="0 0 250 300"><path d="M15 20 L235 20 L210 290 L40 290 Z" fill="#fff" stroke="#111" stroke-width="3"/>
<g class="layer l1"><path d="M38.4 240 L211.6 240 L207 290 L43 290 Z" fill="#ccfbf1"/><text x="125" y="272" text-anchor="middle">istruzioni</text></g>
<g class="layer l2"><path d="M33.8 190 L216.2 190 L211.6 240 L38.4 240 Z" fill="#99f6e4"/><text x="125" y="222" text-anchor="middle">la data di oggi</text></g>
<g class="layer l3"><path d="M29.3 140 L220.7 140 L216.2 190 L33.8 190 Z" fill="#5eead4"/><text x="125" y="172" text-anchor="middle">risultati della ricerca</text></g>
<g class="layer l4"><path d="M24.7 90 L225.3 90 L220.7 140 L29.3 140 Z" fill="#e6eeff"/><text x="125" y="122" text-anchor="middle">la tua domanda</text></g>
</svg>
<figcaption>Gemini, interfaccia web<span>il modello dentro un sistema</span></figcaption>
</figure>
</div>
<div class="fsteps">

* **Istruzioni**: il testo dell'azienda, prima di tutto. Tono, regole, cosa non dire
* **La data**: scritta lì dal sistema
* **La ricerca**: la fa il sistema, poi incolla i risultati
* **La tua domanda** arriva per ultima. Con le app collegate, nel secchio possono finire anche email, calendario, documenti

</div>
</div>

---

### AI Overviews, maggio 2024

<div class="flow">

* <div class="fq"><b>La domanda</b><span class="search">come non far scivolare il formaggio dalla pizza</span></div>
* <div class="fq"><b>Il sistema cerca</b>e trova una discussione su Reddit. Dentro, una <strong>battuta</strong> di circa dieci anni prima</div>
* <div class="fq"><b>La mette nel secchio</b>insieme alla domanda</div>
* <div class="fq ans"><b>Il modello scrive</b><q>Puoi aggiungere circa 1/8 di tazza di colla non tossica alla salsa, per renderla più appiccicosa.</q></div>

</div>

<p class="small muted">Le AI Overviews sono il riassunto scritto da Gemini in cima ai risultati di Google, a partire dalle pagine trovate.</p>

---

### Lo stesso mese: i sassi

<div class="cols" style="align-items:flex-start">
<div>
<div class="ov"><div class="card"><div class="h">AI Overview · «quanti sassi dovrei mangiare?»</div><q>Secondo i geologi di UC Berkeley, si dovrebbe mangiare almeno un piccolo sasso al giorno.</q><div class="from">Dal secchio: <b>un articolo satirico</b> di The Onion (2021), ripubblicato sul sito di un'azienda di software geologico</div></div></div>
</div>
<div class="small">

* **La spiegazione di Google**: su domande così insolite le pagine serie sono pochissime. Il sistema ha preso quelle che c'erano: satira e battute
* La ricerca ha fatto il suo lavoro. Il modello ha scritto bene. **Il testo di partenza era sbagliato**
* La ricerca porta nel contesto **ciò che è scritto, non ciò che è vero**: la regola della brioche, di nuovo

</div>
</div>

<span class="src">Liz Reid, responsabile della ricerca di Google, <a href="https://blog.google/products/search/ai-overviews-update-may-2024/">AI Overviews: About last week</a>, 30 maggio 2024. Risposte tradotte dall'inglese.</span>

---

<!-- _class: big -->

# Il sistema **riduce** alcune allucinazioni. Non le **elimina**.

La data, la ricerca, le fonti entrano nel contesto. La scrittura resta del modello.

---

<!-- _class: big -->

### Parte 4 · Modelli diversi

# Quando dite «ChatGPT è meglio di Gemini», cosa state confrontando?

---

### Cosa cambia fra un modello e l'altro

<div class="rings">
<svg width="470" height="470" viewBox="0 0 470 470">
<circle cx="235" cy="235" r="225" fill="#ccfbf1" stroke="#0d9488" stroke-width="3"/>
<circle cx="235" cy="235" r="130" fill="#e6eeff" stroke="#2563eb" stroke-width="3"/>
<text x="235" y="200" text-anchor="middle" font-size="30" font-weight="800" fill="#2563eb">MODELLO</text>
<text x="235" y="236" text-anchor="middle" font-size="18">parametri · dati</text>
<text x="235" y="262" text-anchor="middle" font-size="18">addestramento finale</text>
<text x="235" y="288" text-anchor="middle" font-size="18">memoria di lavoro</text>
<text x="235" y="58" text-anchor="middle" font-size="26" font-weight="800" fill="#0d9488">SISTEMA</text>
<text x="235" y="88" text-anchor="middle" font-size="18">istruzioni</text>
<text x="235" y="400" text-anchor="middle" font-size="18">strumenti · app collegate</text>
<text x="235" y="426" text-anchor="middle" font-size="18">memoria fra le chat</text>
</svg>
<div class="legend">

<p><span class="tag">Modello</span></p>

<p><b>Parametri</b>: quanto dettaglio conserva la memoria lunga. <b>Dati</b>: cosa ha letto e fino a quando. <b>Addestramento finale</b>: come risponde, quando rifiuta. <b>Memoria di lavoro</b>: quanto testo riesce a tenere davanti.</p>

<p><span class="tag sys">Sistema</span></p>

<p><b>Istruzioni</b>, <b>strumenti</b> (ricerca, immagini, codice), <b>app collegate</b>, <b>memoria</b> fra una chat e l'altra.</p>

<p class="muted">Quanti parametri hanno Gemini e GPT, e con quali dati sono addestrati, non è pubblico.</p>

</div>
</div>

---

### Rimettiamo in ordine quello che avete visto

<table class="sort">
<tr><th>Cosa avete visto</th><th>Da dove viene</th></tr>
<tr><td>La data sbagliata su LM Arena</td><td><span class="tag">Modello</span> dati fermi al passato</td></tr>
<tr><td>La data giusta su Gemini</td><td><span class="tag sys">Sistema</span> istruzioni</td></tr>
<tr><td>La brioche di Maria Antonietta</td><td><span class="tag">Modello</span> dati</td></tr>
<tr><td>Il figlio di Mary Lee Pfeiffer</td><td><span class="tag">Modello</span> parametri</td></tr>
<tr><td>L'analisi logica sbagliata</td><td><span class="tag">Modello</span> dati e parametri</td></tr>
<tr><td>La notizia di ieri trovata da Gemini</td><td><span class="tag sys">Sistema</span> strumenti</td></tr>
<tr><td>La colla sulla pizza</td><td><span class="tag sys">Sistema</span> strumenti, che portano testi sbagliati</td></tr>
</table>

---

<!-- _class: big -->

# Un LLM è affidabile sulla **forma**, non sui fatti rari

I fatti mettiamoli noi nel contesto. Il modello lavori sulla forma.
