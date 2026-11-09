---
marp: true
paginate: true
size: 16:9
title: Rischi degli LLM
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

  blockquote { border-left: 3px solid var(--accent); padding-left: 0.8em; color: var(--fg); font-size: 1.1em; font-style: italic; margin: 0; }
  cite { display: block; color: var(--muted); font-size: 0.6em; font-style: normal; margin-top: 1em; }
  .center { text-align: center; }
  img { max-width: 100%; }

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

  .hb { display: grid; grid-template-columns: 300px 1fr 70px; gap: 10px 14px; align-items: center; font-size: 0.68em; }
  .hb i { display: block; height: 22px; background: var(--accent); border-radius: 3px; }
  .hb i.me { background: #f59e0b; } .hb i.z { height: 4px; background: var(--line); }
  .hb b { font-weight: 800; }
  .vic { display: flex; gap: 28px; margin-top: 0.4em; }
  .vic > div { flex: 1; border: 1px solid var(--line); border-radius: 14px; padding: 18px 22px; }
  .vic b { display: block; font-weight: 600; margin-bottom: 0.4em; }
  .vic p { margin: 0; font-size: 0.7em; }
  section.mappa { padding-top: 40px; padding-bottom: 30px; }
  section.mappa h2 { margin-bottom: 0.3em; }
  .usa { position: relative; width: 1120px; height: 476px; }
  .usa .map { position: absolute; left: 0; top: 0; width: 760px; height: 476px; }
  .usa summary { position: absolute; width: 60px; height: 60px; margin: -30px 0 0 -30px; border-radius: 50%; background: #fff; border: 4px solid var(--accent); display: flex; align-items: center; justify-content: center; font-size: 28px; cursor: pointer; list-style: none; box-shadow: 0 3px 10px rgba(0,0,0,.18); z-index: 1; }
  .usa summary::-webkit-details-marker { display: none; }
  .usa summary:hover { transform: scale(1.1); }
  .usa .aria summary { border-color: #777; } .usa .voto summary { border-color: var(--ok); } .usa .si summary { border-color: #f59e0b; }
  .usa details[open] summary { background: #fff4d6; transform: scale(1.15); }
  .usa .hint, .usa .pop { position: absolute; left: 790px; top: 0; width: 330px; box-sizing: border-box; font-size: 0.56em; }
  .usa .hint { height: 476px; }
  .usa .hint { color: var(--muted); padding: 18px 0; }
  .usa .hint b { color: var(--fg); font-size: 1.3em; }
  .usa .dot { display: inline-block; width: 12px; height: 12px; border-radius: 50%; background: rgba(26,26,26,.55); vertical-align: middle; }
  .usa .dot.vuoto { background: #fff; border: 2px solid #1a1a1a; width: 9px; height: 9px; }
  .usa .pop { background: #fff; border-left: 4px solid var(--accent); padding: 14px 22px; z-index: 2; box-shadow: -6px 0 20px rgba(0,0,0,.06); }
  .usa .pop b { color: var(--muted); text-transform: uppercase; letter-spacing: .1em; font-size: .8em; }
  .usa .pop h4 { font-size: 1.5em; margin: .2em 0 .4em; }
  .usa .pop ul { padding-left: 1.1em; margin: 0; } .usa .pop li { margin: .35em 0; }
  .usa .pop .src { font-size: .8em; }
  .usa .x { position: absolute; right: 10px; top: 8px; border: 0; background: none; font-size: 28px; line-height: 1; cursor: pointer; color: var(--muted); }
  .tre { display: flex; gap: 28px; margin-top: 0.4em; }
  .tre > div { flex: 1; background: #fafbff; border-left: 4px solid var(--accent); padding: 18px 24px; }
  .tre b { display: block; font-size: 2.6em; font-weight: 800; color: var(--accent); line-height: 1; }
  .tre p { margin: 0.5em 0 0; font-size: 0.7em; }
  section.radar { padding-top: 36px; padding-bottom: 30px; }
  section.radar .src { margin-top: 0; }
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Rischi degli LLM

<p class="muted">Cosa può andare storto nel sistema</p>

---

### Rischi degli LLM

## Risultati non deterministici

- Gli LLM sono modelli linguistici statistici con una **componente casuale**
- **NON** possiamo avere la certezza che ci diano risposte riproducibili
- Questo ci porta a comportamenti non prevedibili che possono avere esiti anche **pericolosi**

---

### Rischi degli LLM

## Risultati non deterministici

![w:1100](img/image31.png)

<span class="src">La risposta di Gemini ad uno studente dopo una <a href="https://gemini.google.com/share/6d141b742a13">conversazione</a> apparentemente innocua</span>

---

### Rischi degli LLM

## Questioni di copyright: [New York Times vs. OpenAI](https://www.nytimes.com/2023/12/27/business/media/new-york-times-open-ai-microsoft-lawsuit.html)

- Secondo il NY Times OpenAI ha usato in maniera illegittima i suoi contenuti per addestrare ChatGPT
- Nella primavera 2025 un giudice ha respinto la richiesta di archiviazione di OpenAI

---

### Rischi degli LLM

## Questioni di copyright

![w:1000](img/image32.png)

<span class="src"><a href="https://help.nytimes.com/115014893428-Terms-of-Service">Estratto dai termini di utilizzo del New York Times</a></span>

---

### Rischi degli LLM

## Questioni di copyright: [class action contro Anthropic](https://www.anthropiccopyrightsettlement.com/)

- Nel **2024** tre autori fanno causa ad Anthropic sostenendo che ha addestrato Claude su libri coperti da copyright e scaricati illegalmente
- Nell'autunno **2025** Anthropic ha patteggiato un accordo di **1,5 miliardi di dollari** per risarcire gli autori dei libri, pur non ammettendo la colpa

---

### Rischi degli LLM

## Bias nei dati

**[Humans are biased: generative AI is even worse](https://www.bloomberg.com/graphics/2023-generative-ai-bias/)**

Nel 2023 Bloomberg conduce uno studio su una nota libreria di generazione di immagini scoprendo che le immagini generate perpetuano **stereotipi** di genere, razza, età, posizione sociale

---

### Rischi degli LLM · Sostenibilità

## Dov'è il vostro registro elettronico?

<div class="cols" style="align-items:flex-start">
<div class="small">

* In un **data center**, come Gmail, Classroom e YouTube. Non è una cosa nuova
* 1946: ENIAC occupa una stanza costruita apposta. Il nome «data center» si diffonde negli anni '90, con internet
* Dal 2017 i consumi dei data center crescono di circa il **12% l'anno**: cinque anni prima di ChatGPT

</div>
<div class="small">

* 2024: **415 TWh**, circa l'1,5% dell'elettricità mondiale
* 2030: circa **945 TWh**, poco più di quanto consuma oggi il Giappone
* Un data center tipico per l'IA consuma quanto **100.000 famiglie**; i più grandi in costruzione, 20 volte tanto

</div>
</div>

<span class="src">IEA, <a href="https://www.iea.org/reports/energy-and-ai/executive-summary">Energy and AI</a>, aprile 2025.</span>

---

### Rischi degli LLM · Sostenibilità

## Quanto consuma una domanda?

<div class="pa">
<div class="a"><b>Google, agosto 2025</b><h2>0,26 mL d'acqua</h2><p>0,24 Wh per la domanda mediana di testo a Gemini</p></div>
<div class="p"><b>Mistral, luglio 2025</b><h2>45 mL d'acqua</h2><p>Per una risposta di 400 token</p></div>
</div>

<span class="src">Google Cloud, <a href="https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference">Measuring the environmental impact of AI inference</a>, agosto 2025. Mistral AI, <a href="https://mistral.ai/news/our-contribution-to-a-global-environmental-standard-for-ai">Our contribution to a global environmental standard for AI</a>, luglio 2025.</span>

---

### Rischi degli LLM · Sostenibilità

## Chi vive accanto a un data center

<div class="vic">
<div><b>💧 Acqua di falda</b><p>Newton County, Georgia: pozzi pieni di sedimenti dall'inizio dei lavori di Meta. Quattro famiglie in causa</p></div>
<div><b>💧 Acqua potabile</b><p>Tucson, Arizona: il comune respinge 7 a 0 un data center che avrebbe usato l'acqua della città</p></div>
<div><b>🏭 Aria</b><p>Memphis, Tennessee: turbine a gas senza permesso per il supercomputer di xAI</p></div>
</div>

<p class="small" style="margin-top:1em">Data Center Watch conta <strong>130 miliardi di dollari</strong> di progetti bloccati o rinviati per opposizione locale nel solo primo trimestre 2026. Rinviati, non sempre cancellati.</p>

<span class="src">Data Center Watch, <a href="https://datacenterwatch.org/q1-2026">Q1 2026</a>. Le fonti dei singoli casi sono nella slide successiva.</span>

---

<!-- _class: mappa -->

### Rischi degli LLM · Sostenibilità

## Stati Uniti: dove si dice no

<div class="usa">
<img class="map" src="img/usa.svg" alt="Mappa degli Stati Uniti">
<div class="hint"><b>Tocca un cerchio</b><p>💧 acqua · 🏭 aria · 🗳️ voto</p><p>Il 3 novembre 2026 oltre 30 comuni in 9 stati hanno votato moratorie, divieti o vincoli sui data center. Uno solo ha votato a favore.</p><p><span class="dot"></span> 60 grandi data center per l'IA in funzione: più grande il punto, più potenza. <span class="dot vuoto"></span> 16 in costruzione.</p><p>Insieme, circa <strong>12.600 MW</strong>.</p><span class="src">Epoch AI, <a href="https://epoch.ai/data/ai-data-centers">Frontier Data Centers</a>, 6 novembre 2026, CC-BY. Posizioni ricavate dagli indirizzi.</span></div>
<details name="usa" class="acqua"><summary style="left:568px;top:317px" aria-label="Newton County, Georgia">💧</summary><div class="pop"><button class="x" type="button" onclick="this.closest('details').open=false" aria-label="Chiudi">×</button><b>Newton County, Georgia</b><h4>L'acqua dei pozzi</h4><ul><li>Dall'inizio dei lavori del data center di Meta, alcune famiglie trovano sedimenti nell'acqua dei pozzi</li><li>Beverly Morris al <i>New York Times</i>, luglio 2025: ha paura a bere l'acqua del rubinetto</li><li>Settembre 2026: 4 famiglie fanno causa a Meta. Meta: uno studio commissionato da lei non trova impatti</li><li>Quanta acqua usa? Per Meta il 2% di quella della contea, per l'ente idrico circa il 10%</li></ul><span class="src"><a href="https://www.ajc.com/news/2026/09/georgia-families-sue-meta-accuse-its-data-center-of-tainting-their-water/">AJC, settembre 2026</a></span></div></details>
<details name="usa" class="acqua"><summary style="left:166px;top:336px" aria-label="Tucson, Arizona">💧</summary><div class="pop"><button class="x" type="button" onclick="this.closest('details').open=false" aria-label="Chiudi">×</button><b>Tucson, Arizona</b><h4>Acqua nel deserto</h4><ul><li>Agosto 2025: il consiglio comunale respinge 7 a 0 Project Blue, un data center legato ad Amazon che avrebbe usato l'acqua della città</li><li>Il progetto va avanti fuori dal comune, con raffreddamento ad aria e pozzi propri</li><li>Aprile 2026: il comune revoca un allaccio idrico usato dal cantiere senza autorizzazione</li></ul><span class="src"><a href="https://azluminaria.org/2025/08/06/tucson-city-council-rejects-project-blue-amid-intense-community-pressure/">AZ Luminaria</a>, <a href="https://www.kjzz.org/fronteras-desk/2026-05-08/tucson-cuts-off-water-to-project-blue-data-center-construction-contractor">KJZZ</a></span></div></details>
<details name="usa" class="aria"><summary style="left:473px;top:299px" aria-label="Memphis, Tennessee">🏭</summary><div class="pop"><button class="x" type="button" onclick="this.closest('details').open=false" aria-label="Chiudi">×</button><b>Memphis, Tennessee</b><h4>L'aria</h4><ul><li>Colossus, il supercomputer di xAI (Elon Musk), è alimentato anche da turbine a gas</li><li>Aprile 2026: la NAACP fa causa per 27 turbine senza permesso nel sito di Southaven, appena a sud di Memphis</li><li>Secondo la denuncia, fino a 1.700 tonnellate l'anno di ossidi di azoto. Nessuna sentenza, per ora</li></ul><span class="src"><a href="https://earthjustice.org/press/2026/xai-sued-for-illegal-power-plant">Earthjustice, aprile 2026</a></span></div></details>
<details name="usa" class="voto"><summary style="left:709px;top:112px" aria-label="Wells, Maine">🗳️</summary><div class="pop"><button class="x" type="button" onclick="this.closest('details').open=false" aria-label="Chiudi">×</button><b>Wells, Maine</b><h4>Il voto</h4><ul><li>Primavera 2026: la governatrice del Maine mette il veto a una moratoria per tutto lo Stato. Si muovono i comuni</li><li>3 novembre 2026: l'82% (5.818 sì, 1.282 no) vota una moratoria di 180 giorni sui grandi data center</li><li>Lo stesso giorno oltre 30 comuni in 9 stati approvano moratorie, divieti o vincoli. Risultati non ancora ufficiali</li></ul><span class="src"><a href="https://www.route-fifty.com/infrastructure/2026/05/local-maine-officials-look-pause-data-center-development-after-state-moratorium-veto/413662/">Route Fifty, maggio 2026</a>, <a href="https://www.semafor.com/article/11/04/2026/us-voters-roundly-reject-data-centers-in-ballot-measures">Semafor, 4 novembre 2026</a></span></div></details>
<details name="usa" class="si"><summary style="left:378px;top:91px" aria-label="Harwood, North Dakota">🗳️</summary><div class="pop"><button class="x" type="button" onclick="this.closest('details').open=false" aria-label="Chiudi">×</button><b>Harwood, North Dakota</b><h4>L'unico sì</h4><ul><li>Accanto alla città Applied Digital costruisce un data center da 3 miliardi di dollari, approvato a settembre 2025</li><li>Novembre 2026: circa 3 elettori su 4 respingono una misura per rallentare lo sviluppo industriale</li><li>Un consigliere comunale: a rischio le entrate fiscali del data center</li></ul><span class="src"><a href="https://www.bloomberg.com/news/articles/2026-11-04/only-one-town-out-of-dozens-in-us-voted-in-favor-of-data-centers">Bloomberg, 4 novembre 2026</a></span></div></details>
</div>

---

### Rischi degli LLM

## Opacità e pubblicità

- Usare una IA come motore di ricerca **non ci dà il controllo delle fonti** consultate dall'IA
- Alcune società (OpenAI) stanno introducendo le **pubblicità** all'interno delle risposte di ChatGPT

---

### Rischi degli LLM · Opacità e pubblicità

> «Gli utenti interagiscono con una voce adattiva e conversazionale alla quale hanno rivelato i loro pensieri più intimi. Le persone confidano ai chatbot le proprie paure mediche, i problemi relazionali, le proprie credenze su Dio e sull'aldilà.»

<cite>Zoë Hitzig, <em><a href="https://www.nytimes.com/2026/02/11/opinion/openai-ads-chatgpt.html">OpenAI Is Making the Mistakes Facebook Made. I Quit.</a></em></cite>

---

<!-- _class: radar -->

### Rischi degli LLM · Lavoro

## Cosa l'IA potrebbe fare, cosa fa davvero

<div class="cols" style="margin-top:-30px">
<div style="flex:0 0 540px"><img src="img/radar-anthropic.png" style="width:540px;display:block"></div>
<div class="small">

* Per circa 800 mestieri negli USA, la quota di compiti che un LLM potrebbe svolgere (**blu**) e quella che risulta svolta con Claude nel lavoro reale (**rosso**)
* Informatica e matematica: **94%** in teoria, **33%** nell'uso reale
* Il **30%** dei lavoratori è a zero

</div>
</div>

<span class="src">M. Massenkoff, P. McCrory, <a href="https://www.anthropic.com/research/labor-market-impacts">Labor market impacts of AI: A new measure and early evidence</a>, Anthropic, 5 marzo 2026. Dati d'uso di agosto e novembre 2025.</span>

---

### Rischi degli LLM · Lavoro

## Quanti compiti di un mestiere fa già l'IA?

<div class="hb">
<span>Programmatori</span><i style="width:75%"></i><b>75%</b>
<span>Servizio clienti</span><i style="width:70%"></i><b>70%</b>
<span>Data entry</span><i style="width:67%"></i><b>67%</b>
<span>Insegnanti, superiori</span><i class="me" style="width:29%"></i><b>29%</b>
<span>Insegnanti, primaria</span><i class="me" style="width:10%"></i><b>10%</b>
<span>Cuochi, baristi, bagnini</span><i class="z"></i><b>0%</b>
</div>


<span class="src">M. Massenkoff, P. McCrory, <a href="https://www.anthropic.com/research/labor-market-impacts">Labor market impacts of AI: A new measure and early evidence</a>, Anthropic, 5 marzo 2026. Dati d'uso di agosto e novembre 2025.</span>

---

### Rischi degli LLM · Lavoro

## E noi? I compiti di un insegnante delle superiori

<table class="f">
<tr><th>Coperti dall'uso di Claude</th><th>A zero</th></tr>
<tr><td>Preparare e correggere le verifiche</td><td>Parlare con i genitori</td></tr>
<tr><td>Fissare obiettivi e percorsi del corso</td><td>Far rispettare regole e ordine in classe</td></tr>
<tr><td>Adattare metodi e materiali ai bisogni degli studenti</td><td>Orientare e consigliare gli studenti</td></tr>
<tr><td></td><td>Discutere dei singoli studenti con altri professionisti</td></tr>
</table>

<p class="small" style="margin-top:0.8em">Coperti 8 compiti su 31, tutti di scrittura. «Correggere i compiti a casa» però risulta a zero: la misura conta l'uso di Claude, non chi perde il lavoro.</p>

<span class="src">Elaborazione sui dati di Anthropic (<a href="https://huggingface.co/datasets/Anthropic/EconomicIndex">EconomicIndex, labor_market_impacts</a>) e sui compiti O*NET 30.0 per «Secondary School Teachers».</span>

---

### Rischi degli LLM · Lavoro

## Cosa è successo finora

<div class="small">

* **Disoccupazione**: negli USA, dalla fine del 2022, nessun aumento sistematico per i mestieri più esposti
* **Giovani dai 22 ai 25 anni**: nei mestieri esposti le assunzioni calano del **14%** rispetto al 2022. Risultato appena significativo: per gli autori è un indizio
* **Limiti**: solo Claude, solo USA, misura i compiti e non i posti di lavoro

</div>

<p style="margin-top:1em;font-weight:400">Se i compiti da principiante li fa l'IA, dove impara il principiante?</p>

<span class="src">M. Massenkoff, P. McCrory, <a href="https://www.anthropic.com/research/labor-market-impacts">Labor market impacts of AI</a>, Anthropic, 5 marzo 2026.</span>

---

### Rischi degli LLM

## Etica e misusi

<div class="cols">
<div>

- Molti (tutti) gli utenti tendono a rispondere agli LLM **come se fossero [esseri senzienti](https://www.youtube.com/watch?v=CyyL0yDhr7I)**
- Uno studio del Center for Democracy and Technology ha evidenziato come **un terzo** degli intervistati (studenti adolescenti) abbia usato l'IA generativa in cerca di relazioni romantiche

</div>
<div class="center">

![w:520](img/image33.jpeg)
<span class="src">Joaquin Phoenix si innamora di una IA in Her (2013)</span>

</div>
</div>

---

### Rischi degli LLM · Etica e misusi

## Una lettura

[Che cosa pensano dell'intelligenza artificiale gli studenti della scuola secondaria in Italia](https://www.indire.it/wp-content/uploads/2026/10/sintesi_indagine_studenti_IA_2026_INDIRE.pdf)

<p class="small muted">Sintesi dell'indagine INDIRE «Io e l'Intelligenza Artificiale», 2026</p>

---

### Rischi degli LLM · Etica e misusi

## Dati interessanti

<div class="tre">
<div><b>53%</b><p>ha usato l'IA almeno una volta per sfogarsi o affrontare un problema personale</p></div>
<div><b>10%</b><p>lo fa molte volte</p></div>
<div><b>20%</b><p>sono «intensivi relazionali»: usano molto l'IA per studiare e si confidano spesso con lei</p></div>
</div>

<p class="small" style="margin-top:1em">Lo fanno di più le studentesse e gli studenti delle medie.</p>

<span class="src">S. Calzone, S. Borri, R. Manna, <a href="https://www.indire.it/wp-content/uploads/2026/10/sintesi_indagine_studenti_IA_2026_INDIRE.pdf">Che cosa pensano dell'intelligenza artificiale gli studenti della scuola secondaria in Italia</a>, INDIRE, 2026. 5.342 studenti di medie e superiori, marzo-giugno 2026; campione di convenienza, non rappresentativo.</span>

---

### Rischi degli LLM · Etica e misusi

## Per la discussione

<div class="qs">

* Corrisponde a quello che vedete nelle vostre classi?
* Perché lo fanno di più le studentesse e gli studenti delle medie?
* Cosa può fare la scuola, e cosa non può fare?

</div>

---

### Rischi degli LLM · Etica e misusi

## Tre casi da ricostruire

Cause in corso fra aziende dell'IA e famiglie, con l'accusa di **istigazione al suicidio**:

<div class="cols" style="align-items:flex-start">
<div>

- [Adam Raine](https://www.theguardian.com/us-news/2025/aug/29/chatgpt-suicide-openai-sam-altman-adam-raine)
- [Sewell Setzer III](https://www.theguardian.com/technology/2024/oct/23/character-ai-chatbot-sewell-setzer-death)
- [Zane Shamblin](https://edition.cnn.com/2025/11/06/us/openai-chatgpt-suicide-lawsuit-invs-vis)

</div>
<div class="small">

**A gruppi, un caso per gruppo.** Con Gemini, ChatGPT, Claude o un altro strumento a scelta, ricostruite i fatti: chi era, quale chatbot usava, cosa sostiene la famiglia, cosa risponde l'azienda, a che punto è la causa.

Ogni fatto con fonte e data.

</div>
</div>

---

### Rischi degli LLM · Etica e misusi

## Sui tre casi

<div class="qs">

* Cosa è accertato, e cosa sostiene solo una delle parti?<span>La famiglia, l'azienda, i giornali</span>
* Gli strumenti che avete usato hanno dato le stesse informazioni?<span>Qualcuno ha sbagliato o inventato?</span>
* Di chi è la responsabilità?<span>L'azienda, chi ha progettato il chatbot, la famiglia, la scuola</span>

</div>

---


<!-- _class: lead -->
<!-- _paginate: false -->

### Rischi degli LLM

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

