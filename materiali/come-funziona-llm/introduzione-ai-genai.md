---
marp: true
paginate: true
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
  :root { --fg: #1a1a1a; --muted: #777; --accent: #2563eb; --line: #e5e5e5; }
  section { background: #fff; color: var(--fg); font-family: 'Inter', sans-serif; font-weight: 300; font-size: 28px; padding: 60px 80px; }
  h1 { font-weight: 800; font-size: 1.9em; letter-spacing: -0.02em; margin: 0 0 0.4em; }
  h2 { font-weight: 600; font-size: 1.25em; margin: 0 0 0.6em; }
  h3 { font-weight: 600; font-size: 0.6em; color: var(--muted); text-transform: uppercase; letter-spacing: 0.18em; margin: 0 0 0.8em; }
  strong { font-weight: 600; color: var(--accent); }
  ul { padding-left: 1.1em; } li { margin: 0.25em 0; }
  blockquote { border-left: 3px solid var(--accent); padding-left: 0.8em; color: var(--fg); font-size: 1.1em; font-style: italic; margin: 0; }
  cite, .src { display: block; color: var(--muted); font-size: 0.6em; font-style: normal; margin-top: 1em; }
  section::after { color: #bbb; font-size: 0.5em; }
  section.lead { display: flex; flex-direction: column; justify-content: center; }
  section.lead h1 { font-size: 2.4em; }
  section.big { display: flex; flex-direction: column; justify-content: center; text-align: center; }
  section.big h1 { font-size: 1.8em; line-height: 1.25; }
  .cols { display: flex; gap: 48px; align-items: center; }
  .cols > * { flex: 1; }
  .card { border: 1px solid var(--line); border-radius: 10px; padding: 20px 24px; }
  .card h2 { margin-bottom: 0.3em; }
  .card p { color: var(--muted); font-size: 0.8em; margin: 0; }
  .center { text-align: center; }
  img { max-width: 100%; }
  .tok { display: flex; flex-wrap: wrap; gap: 8px; margin: 0.4em 0 0.9em; }
  .tok span { font-family: ui-monospace, monospace; font-size: 0.85em; padding: 8px 12px; border-radius: 8px; background: #eef1ff; border: 1px solid #c9d3ff; }
  .tok span:nth-child(even) { background: #fff4e0; border-color: #ffd89a; }
  .tok-row { display: flex; align-items: center; gap: 24px; }
  .tok-row > b { flex: 0 0 300px; font-weight: 400; font-size: 0.85em; }
  .tok-row > em { font-style: normal; color: var(--muted); font-size: 0.7em; }
  table.geo { border-collapse: collapse; font-size: 0.85em; }
  table.geo th { text-align: left; font-weight: 600; font-size: 0.7em; text-transform: uppercase; letter-spacing: 0.12em; color: var(--muted); border-bottom: 2px solid var(--fg); padding: 8px 18px; background: none; }
  table.geo td { border: 0; border-bottom: 1px solid var(--line); padding: 12px 18px; background: none; }
  table.geo tr { background: none !important; }
  .eco { border-left: 3px solid var(--accent); padding: 10px 16px; background: #f6f8ff; font-size: 0.85em; margin-top: 1em; }
  section.dart { padding-top: 40px; }
  .faces ul { list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: repeat(3, 1fr); column-gap: 28px; row-gap: 34px; }
  .faces li { margin: 0; display: flex; gap: 18px; align-items: center; }
  .faces img { width: 130px; height: 130px; border-radius: 50%; object-fit: cover; display: block; flex: 0 0 130px; }
  .faces .nm { display: block; font-weight: 600; font-size: 0.8em; color: var(--fg); }
  .faces .yr { display: block; font-size: 0.55em; color: var(--muted); margin-bottom: 6px; }
  .faces .tx { display: block; font-size: 0.6em; line-height: 1.35; color: var(--fg); }
  .faces .tx b { color: var(--accent); font-weight: 600; }
  .others ul { list-style: none; padding: 0; margin: 18px 0 0; }
  .others li { font-size: 0.55em; color: var(--muted); }
  section.dart .src { font-size: 0.4em; margin-top: 10px; }
  [data-bespoke-marp-fragment=inactive] { visibility: visible; opacity: 0; transition: none; }
  [data-bespoke-marp-fragment=active] { opacity: 1; transition: opacity 0.6s ease; }
  section.move { padding-top: 40px; }
  section.move h2 { margin-bottom: 0.2em; }
  .tok span.last { background: #f59e0b; border-color: #d97706; color: #fff; font-weight: 600; }
  .space .w circle { fill: #bbb; } .space .w text { font-size: 17px; fill: #777; font-family: Inter, sans-serif; }
  .space .w.fin text { fill: #aaa; }
  .space .cap { font-size: 13px; fill: #aaa; font-family: Inter, sans-serif; }
  .space .ghost { fill: #f59e0b; opacity: 0; transition: opacity 0.6s; }
  #dot { transform: translate(150px,92px); opacity: 0; transition: transform 1.2s cubic-bezier(.4,0,.2,1), opacity 0.4s; }
  #dot circle { fill: #f59e0b; stroke: #fff; stroke-width: 3; }
  #dot text { font-size: 22px; font-weight: 700; fill: #b45309; font-family: Inter, sans-serif; }
  section.move:has(.steps li:nth-child(1)[data-bespoke-marp-fragment=active]) #dot { opacity: 1; }
  section.move:has(.steps li:nth-child(1)[data-bespoke-marp-fragment=active]) #dot { transform: translate(150px,92px); }
  section.move:has(.steps li:nth-child(2)[data-bespoke-marp-fragment=active]) #dot { transform: translate(300px,160px); }
  section.move:has(.steps li:nth-child(3)[data-bespoke-marp-fragment=active]) #dot { transform: translate(420px,250px); }
  section.move:has(.steps li:nth-child(4)[data-bespoke-marp-fragment=active]) #dot { transform: translate(515px,332px); }
  section.move:has(.steps li:nth-child(2)[data-bespoke-marp-fragment=active]) .ghost.g1 { opacity: 0.35; }
  section.move:has(.steps li:nth-child(3)[data-bespoke-marp-fragment=active]) .ghost.g2 { opacity: 0.35; }
  section.move:has(.steps li:nth-child(4)[data-bespoke-marp-fragment=active]) .ghost.g3 { opacity: 0.35; }
  section.move:has(.steps li:nth-child(5)[data-bespoke-marp-fragment=active]) .space .w.agg text { fill: #2563eb; font-weight: 700; font-size: 20px; }
  section.move:has(.steps li:nth-child(5)[data-bespoke-marp-fragment=active]) .space .w.agg circle { fill: #2563eb; }
  .tok.att span { background: #f4f4f4; border-color: #ddd; color: #1a1a1a; transition: background 0.5s, color 0.5s, border-color 0.5s; }
  .tok.att span.last { background: #f59e0b; border-color: #d97706; color: #fff; }
  section.move:has(.steps li:nth-child(2)[data-bespoke-marp-fragment=active]):not(:has(.steps li:nth-child(3)[data-bespoke-marp-fragment=active])) .tok.att .tk-la { background: rgba(107,114,128,0.08); border-color: #6b7280; color: #1a1a1a; }
  section.move:has(.steps li:nth-child(2)[data-bespoke-marp-fragment=active]):not(:has(.steps li:nth-child(3)[data-bespoke-marp-fragment=active])) .tok.att .tk-banca { background: rgba(147,51,234,0.55); border-color: #9333ea; color: #fff; }
  section.move:has(.steps li:nth-child(2)[data-bespoke-marp-fragment=active]):not(:has(.steps li:nth-child(3)[data-bespoke-marp-fragment=active])) .tok.att .tk-del { background: rgba(13,148,136,0.1); border-color: #0d9488; color: #1a1a1a; }
  section.move:has(.steps li:nth-child(2)[data-bespoke-marp-fragment=active]):not(:has(.steps li:nth-child(3)[data-bespoke-marp-fragment=active])) .tok.att .tk-fiume { background: rgba(37,99,235,0.55); border-color: #2563eb; color: #fff; }
  section.move:has(.steps li:nth-child(3)[data-bespoke-marp-fragment=active]):not(:has(.steps li:nth-child(4)[data-bespoke-marp-fragment=active])) .tok.att .tk-la { background: rgba(107,114,128,0.08); border-color: #6b7280; color: #1a1a1a; }
  section.move:has(.steps li:nth-child(3)[data-bespoke-marp-fragment=active]):not(:has(.steps li:nth-child(4)[data-bespoke-marp-fragment=active])) .tok.att .tk-banca { background: rgba(147,51,234,0.55); border-color: #9333ea; color: #fff; }
  section.move:has(.steps li:nth-child(3)[data-bespoke-marp-fragment=active]):not(:has(.steps li:nth-child(4)[data-bespoke-marp-fragment=active])) .tok.att .tk-del { background: rgba(13,148,136,0.1); border-color: #0d9488; color: #1a1a1a; }
  section.move:has(.steps li:nth-child(3)[data-bespoke-marp-fragment=active]):not(:has(.steps li:nth-child(4)[data-bespoke-marp-fragment=active])) .tok.att .tk-fiume { background: rgba(37,99,235,0.55); border-color: #2563eb; color: #fff; }
  section.move:has(.steps li:nth-child(4)[data-bespoke-marp-fragment=active]):not(:has(.steps li:nth-child(5)[data-bespoke-marp-fragment=active])) .tok.att .tk-la { background: rgba(107,114,128,0.08); border-color: #6b7280; color: #1a1a1a; }
  section.move:has(.steps li:nth-child(4)[data-bespoke-marp-fragment=active]):not(:has(.steps li:nth-child(5)[data-bespoke-marp-fragment=active])) .tok.att .tk-banca { background: rgba(147,51,234,0.55); border-color: #9333ea; color: #fff; }
  section.move:has(.steps li:nth-child(4)[data-bespoke-marp-fragment=active]):not(:has(.steps li:nth-child(5)[data-bespoke-marp-fragment=active])) .tok.att .tk-del { background: rgba(13,148,136,0.1); border-color: #0d9488; color: #1a1a1a; }
  section.move:has(.steps li:nth-child(4)[data-bespoke-marp-fragment=active]):not(:has(.steps li:nth-child(5)[data-bespoke-marp-fragment=active])) .tok.att .tk-fiume { background: rgba(37,99,235,0.55); border-color: #2563eb; color: #fff; }
  .steps { font-size: 0.62em; }
  .steps ul { list-style: none; padding: 0; margin: 0; }
  .steps li { margin: 0 0 14px; padding-left: 12px; border-left: 3px solid var(--line); }
  .steps li b { display: block; font-size: 0.75em; text-transform: uppercase; letter-spacing: 0.12em; color: var(--accent); }
  section.samp { padding-top: 40px; }
  .ptab { position: relative; }
  .ptab .r { display: grid; grid-template-columns: 170px 1fr 70px; align-items: center; gap: 14px; height: 54px; padding: 0 12px; position: relative; z-index: 1; transition: opacity 0.5s; }
  .ptab .t { font-family: ui-monospace, monospace; font-size: 0.8em; }
  .ptab .b { height: 20px; background: #eee; border-radius: 4px; overflow: hidden; }
  .ptab .b i { display: block; height: 100%; width: 0; background: var(--accent); transition: width 0.9s ease; }
  .ptab .p { text-align: right; font-size: 0.7em; color: var(--muted); opacity: 0; transition: opacity 0.5s; }
  .ptab .more { font-size: 0.5em; color: var(--muted); padding: 10px 12px 0; opacity: 0; transition: opacity 0.5s; }
  .ptab .pick { position: absolute; left: 0; right: 0; top: 0; height: 54px; background: #fde7b0; border-radius: 8px; opacity: 0; }
  .newtok { opacity: 0; transition: opacity 0.6s; }
  section.samp:has(.steps li:nth-child(1)[data-bespoke-marp-fragment=active]) .ptab .b i { width: var(--w); }
  section.samp:has(.steps li:nth-child(1)[data-bespoke-marp-fragment=active]) .ptab .p, section.samp:has(.steps li:nth-child(1)[data-bespoke-marp-fragment=active]) .ptab .more { opacity: 1; }
  section.samp:has(.steps li:nth-child(2)[data-bespoke-marp-fragment=active]) .ptab .r5, section.samp:has(.steps li:nth-child(2)[data-bespoke-marp-fragment=active]) .ptab .r6, section.samp:has(.steps li:nth-child(2)[data-bespoke-marp-fragment=active]) .ptab .more { opacity: 0.25; }
  section.samp:has(.steps li:nth-child(3)[data-bespoke-marp-fragment=active]) .ptab .pick { opacity: 1; animation: roulette 2.6s cubic-bezier(.2,.6,.3,1) forwards; }
  section.samp:has(.steps li:nth-child(3)[data-bespoke-marp-fragment=active]) .ptab .r2 .t { font-weight: 700; }
  section.samp:has(.steps li:nth-child(4)[data-bespoke-marp-fragment=active]) .newtok { opacity: 1; }
  @keyframes roulette {
    0% { top: 0; } 8% { top: 54px; } 16% { top: 108px; } 24% { top: 162px; } 32% { top: 0; }
    42% { top: 54px; } 52% { top: 108px; } 62% { top: 162px; } 74% { top: 0; } 100% { top: 54px; }
  }
  section.emb { padding-top: 40px; }
  .egrid { display: flex; gap: 10px; justify-content: space-between; margin-top: 6px; }
  .ec { flex: 1; display: flex; flex-direction: column; align-items: center; gap: 8px; }
  .ec .et { font-family: ui-monospace, monospace; font-size: 0.8em; padding: 6px 10px; border-radius: 8px; background: #eef1ff; border: 1px solid #c9d3ff; white-space: pre; }
  .ec:nth-child(even) .et { background: #fff4e0; border-color: #ffd89a; }
  .ec .ev { display: flex; flex-direction: column; width: 100%; max-width: 110px; border: 1px solid #ddd; border-radius: 6px; overflow: hidden; max-height: 0; opacity: 0; transition: max-height 0.7s ease, opacity 0.4s; transition-delay: calc(var(--k) * 0.15s); }
  .ec .pos { font-size: 0.45em; font-weight: 600; color: #fff; background: var(--accent); border-radius: 999px; padding: 2px 10px; opacity: 0; transform: scale(0.6); transition: opacity 0.4s, transform 0.4s; transition-delay: calc(var(--k) * 0.1s); }
  .ec .ev span { position: relative; font-family: ui-monospace, monospace; font-size: 0.5em; text-align: center; padding: 4px 0; color: #1a1a1a; background: var(--a); transition: background 0.8s; transition-delay: calc(var(--k) * 0.1s); }
  .ec .ev span i { font-style: normal; transition: opacity 0.6s; transition-delay: calc(var(--k) * 0.1s); }
  .ec .ev span i.v2 { position: absolute; left: 0; right: 0; opacity: 0; }
  .ec .ev em { font-style: normal; text-align: center; font-size: 0.6em; color: var(--muted); }
  section.emb:has(.esteps li:nth-child(1)[data-bespoke-marp-fragment=active]) .ec .ev { max-height: 260px; opacity: 1; }
  section.emb:has(.esteps li:nth-child(2)[data-bespoke-marp-fragment=active]) .ec .pos { opacity: 1; transform: none; }
  section.emb:has(.esteps li:nth-child(2)[data-bespoke-marp-fragment=active]) .ec .ev span { background: var(--b); }
  section.emb:has(.esteps li:nth-child(2)[data-bespoke-marp-fragment=active]) .ec .ev span i.v1 { opacity: 0; }
  section.emb:has(.esteps li:nth-child(2)[data-bespoke-marp-fragment=active]) .ec .ev span i.v2 { opacity: 1; }
  section.emb:has(.esteps li:nth-child(3)[data-bespoke-marp-fragment=active]) .egrid { outline: 3px dashed var(--accent); outline-offset: 8px; border-radius: 6px; }
  .esteps { margin-top: 22px; font-size: 0.62em; }
  .esteps ul { list-style: none; padding: 0; margin: 0; display: flex; gap: 26px; }
  .esteps li { flex: 1; margin: 0; padding-left: 12px; border-left: 3px solid var(--line); }
  .esteps li b { display: block; font-size: 0.8em; text-transform: uppercase; letter-spacing: 0.12em; color: var(--accent); }
  section.emb .src { font-size: 0.45em; }
  section.vocab { padding-top: 40px; }
  .vbig { white-space: nowrap; font-size: 2.2em; font-weight: 800; color: var(--accent); margin: 0; line-height: 1; }
  .vsub { font-size: 0.7em; color: var(--muted); margin: 0.4em 0 0; }
  .vgroups { flex: 1; display: grid; grid-template-columns: 1fr 1fr; gap: 14px 28px; }
  .vgroups b { display: block; font-size: 0.55em; text-transform: uppercase; letter-spacing: 0.12em; color: var(--muted); }
  .vgroups .tok { margin: 0.3em 0 0; gap: 6px; }
  .vgroups .tok span, .vcomp .tok span { font-size: 0.7em; padding: 5px 9px; }
  .vcomp { margin-top: 18px; }
  .vcomp p { font-size: 0.72em; margin: 0 0 6px; font-weight: 600; }
  .vcomp ul { list-style: none; padding: 0; margin: 0; display: flex; gap: 36px; }
  .vcomp li { display: flex; align-items: center; gap: 10px; margin: 0; }
  .vcomp .w { font-size: 0.75em; font-weight: 600; }
  .vcomp .w::after { content: ' →'; color: var(--muted); font-weight: 300; }
  .vcomp .tok { display: inline-flex; margin: 0; gap: 4px; }
  section.vocab .src { font-size: 0.45em; margin-top: 12px; }
  section.fit { padding-top: 40px; }
  .mlrow { display: flex; gap: 36px; align-items: center; }
  .mlrow .mlc { height: 420px; }
  .plot { width: 560px; }
  .plot .eq { position: relative; height: 46px; font-family: ui-monospace, monospace; font-size: 0.85em; }
  .plot .eq span { position: absolute; left: 0; top: 0; opacity: 0; transition: opacity 0.4s; white-space: nowrap; }
  .plot .eq b { font-weight: 700; padding: 0 4px; border-radius: 6px; transition: background 0.5s; }
  .plot svg text { font-family: Inter, sans-serif; font-size: 15px; fill: #777; }
  .plot .pts circle { fill: #2563eb; }
  .plot .ln { fill: none; stroke: #dc2626; stroke-width: 4; stroke-linecap: round; opacity: 0; d: path("M60,80.0 L540,280.0"); transition: d 1s ease, opacity 0.4s, stroke 0.5s; }
  .plot .res { fill: none; stroke: #dc2626; stroke-width: 2; stroke-dasharray: 4 4; opacity: 0; d: path("M220.5,181.0 L220.5,146.9 M107.1,223.1 L107.1,99.6 M316.2,169.5 L316.2,186.7 M303.4,160.7 L303.4,181.4 M91.3,276.1 L91.3,93.0 M115.3,250.0 L115.3,103.1 M265.9,178.4 L265.9,165.8 M175.1,240.9 L175.1,128.0 M357.5,106.4 L357.5,204.0 M253.4,204.1 L253.4,160.6 M205.1,196.4 L205.1,140.4 M139.5,224.5 L139.5,113.1 M442.6,87.2 L442.6,239.4 M155.9,273.3 L155.9,120.0 M242.4,217.4 L242.4,156.0 M321.5,150.4 L321.5,189.0 M167.3,226.8 L167.3,124.7 M381.4,156.1 L381.4,213.9 M338.6,140.9 L338.6,196.1 M278.9,196.1 L278.9,171.2 M389.8,78.1 L389.8,217.4 M184.5,255.6 L184.5,131.9 M469.3,108.9 L469.3,250.5 M403.5,142.4 L403.5,223.1 M127.7,167.4 L127.7,108.2 M263.1,186.2 L263.1,164.6"); transition: d 1s ease, opacity 0.4s, stroke 0.5s; }
  .plot .err { display: flex; align-items: center; gap: 12px; height: 30px; font-size: 0.55em; color: var(--muted); opacity: 0; transition: opacity 0.4s; }
  .plot .err i { display: block; height: 14px; width: 240px; background: #dc2626; border-radius: 4px; transition: width 1s ease, background 0.5s; }
  .plot .err .ev { position: relative; width: 90px; height: 1.2em; }
  .plot .err em { position: absolute; left: 0; font-style: normal; font-weight: 600; color: var(--fg); opacity: 0; transition: opacity 0.4s; }
  .fsteps { position: relative; height: 40px; font-size: 0.62em; margin-top: 8px; }
  .fsteps ul { list-style: none; padding: 0; margin: 0; }
  .fsteps li { position: absolute; left: 0; top: 0; margin: 0; }
  .fsteps li:has(+ li[data-bespoke-marp-fragment=active]) { opacity: 0; }
  section.fit:not(:has(.fsteps li:nth-child(1)[data-bespoke-marp-fragment=active])) .eq .e0, section.fit:has(.fsteps li:nth-child(1)[data-bespoke-marp-fragment=active]):not(:has(.fsteps li:nth-child(3)[data-bespoke-marp-fragment=active])) .eq .e1, section.fit:has(.fsteps li:nth-child(3)[data-bespoke-marp-fragment=active]):not(:has(.fsteps li:nth-child(4)[data-bespoke-marp-fragment=active])) .eq .e2, section.fit:has(.fsteps li:nth-child(4)[data-bespoke-marp-fragment=active]):not(:has(.fsteps li:nth-child(5)[data-bespoke-marp-fragment=active])) .eq .e3, section.fit:has(.fsteps li:nth-child(5)[data-bespoke-marp-fragment=active]) .eq .e4 { opacity: 1; }
  section.fit:has(.fsteps li:nth-child(1)[data-bespoke-marp-fragment=active]) .ln { opacity: 1; }
  section.fit:has(.fsteps li:nth-child(2)[data-bespoke-marp-fragment=active]) .res { opacity: 0.8; }
  section.fit:has(.fsteps li:nth-child(2)[data-bespoke-marp-fragment=active]) .err { opacity: 1; }
  section.fit:has(.fsteps li:nth-child(2)[data-bespoke-marp-fragment=active]):not(:has(.fsteps li:nth-child(3)[data-bespoke-marp-fragment=active])) .err .m1, section.fit:has(.fsteps li:nth-child(3)[data-bespoke-marp-fragment=active]):not(:has(.fsteps li:nth-child(4)[data-bespoke-marp-fragment=active])) .err .m2, section.fit:has(.fsteps li:nth-child(4)[data-bespoke-marp-fragment=active]):not(:has(.fsteps li:nth-child(5)[data-bespoke-marp-fragment=active])) .err .m3, section.fit:has(.fsteps li:nth-child(5)[data-bespoke-marp-fragment=active]) .err .m4 { opacity: 1; }
  section.fit:has(.fsteps li:nth-child(3)[data-bespoke-marp-fragment=active]) .ln { d: path("M60,180.0 L540,180.0"); }
  section.fit:has(.fsteps li:nth-child(3)[data-bespoke-marp-fragment=active]) .res { d: path("M220.5,181.0 L220.5,180.0 M107.1,223.1 L107.1,180.0 M316.2,169.5 L316.2,180.0 M303.4,160.7 L303.4,180.0 M91.3,276.1 L91.3,180.0 M115.3,250.0 L115.3,180.0 M265.9,178.4 L265.9,180.0 M175.1,240.9 L175.1,180.0 M357.5,106.4 L357.5,180.0 M253.4,204.1 L253.4,180.0 M205.1,196.4 L205.1,180.0 M139.5,224.5 L139.5,180.0 M442.6,87.2 L442.6,180.0 M155.9,273.3 L155.9,180.0 M242.4,217.4 L242.4,180.0 M321.5,150.4 L321.5,180.0 M167.3,226.8 L167.3,180.0 M381.4,156.1 L381.4,180.0 M338.6,140.9 L338.6,180.0 M278.9,196.1 L278.9,180.0 M389.8,78.1 L389.8,180.0 M184.5,255.6 L184.5,180.0 M469.3,108.9 L469.3,180.0 M403.5,142.4 L403.5,180.0 M127.7,167.4 L127.7,180.0 M263.1,186.2 L263.1,180.0"); }
  section.fit:has(.fsteps li:nth-child(3)[data-bespoke-marp-fragment=active]) .err i { width: 126px; }
  section.fit:has(.fsteps li:nth-child(4)[data-bespoke-marp-fragment=active]) .ln { d: path("M60,240.0 L540,120.0"); }
  section.fit:has(.fsteps li:nth-child(4)[data-bespoke-marp-fragment=active]) .res { d: path("M220.5,181.0 L220.5,199.9 M107.1,223.1 L107.1,228.2 M316.2,169.5 L316.2,176.0 M303.4,160.7 L303.4,179.2 M91.3,276.1 L91.3,232.2 M115.3,250.0 L115.3,226.2 M265.9,178.4 L265.9,188.5 M175.1,240.9 L175.1,211.2 M357.5,106.4 L357.5,165.6 M253.4,204.1 L253.4,191.7 M205.1,196.4 L205.1,203.7 M139.5,224.5 L139.5,220.1 M442.6,87.2 L442.6,144.3 M155.9,273.3 L155.9,216.0 M242.4,217.4 L242.4,194.4 M321.5,150.4 L321.5,174.6 M167.3,226.8 L167.3,213.2 M381.4,156.1 L381.4,159.7 M338.6,140.9 L338.6,170.3 M278.9,196.1 L278.9,185.3 M389.8,78.1 L389.8,157.6 M184.5,255.6 L184.5,208.9 M469.3,108.9 L469.3,137.7 M403.5,142.4 L403.5,154.1 M127.7,167.4 L127.7,223.1 M263.1,186.2 L263.1,189.2"); }
  section.fit:has(.fsteps li:nth-child(4)[data-bespoke-marp-fragment=active]) .err i { width: 76px; }
  section.fit:has(.fsteps li:nth-child(5)[data-bespoke-marp-fragment=active]) .ln { d: path("M60,272.0 L540,60.0"); }
  section.fit:has(.fsteps li:nth-child(5)[data-bespoke-marp-fragment=active]) .res { d: path("M220.5,181.0 L220.5,201.1 M107.1,223.1 L107.1,251.2 M316.2,169.5 L316.2,158.8 M303.4,160.7 L303.4,164.5 M91.3,276.1 L91.3,258.2 M115.3,250.0 L115.3,247.6 M265.9,178.4 L265.9,181.0 M175.1,240.9 L175.1,221.2 M357.5,106.4 L357.5,140.6 M253.4,204.1 L253.4,186.6 M205.1,196.4 L205.1,207.9 M139.5,224.5 L139.5,236.9 M442.6,87.2 L442.6,103.0 M155.9,273.3 L155.9,229.6 M242.4,217.4 L242.4,191.4 M321.5,150.4 L321.5,156.5 M167.3,226.8 L167.3,224.6 M381.4,156.1 L381.4,130.0 M338.6,140.9 L338.6,148.9 M278.9,196.1 L278.9,175.3 M389.8,78.1 L389.8,126.3 M184.5,255.6 L184.5,217.0 M469.3,108.9 L469.3,91.2 M403.5,142.4 L403.5,120.3 M127.7,167.4 L127.7,242.1 M263.1,186.2 L263.1,182.3"); }
  section.fit:has(.fsteps li:nth-child(5)[data-bespoke-marp-fragment=active]) .err i { width: 59px; }
  section.fit:has(.fsteps li:nth-child(5)[data-bespoke-marp-fragment=active]) .ln, section.fit:has(.fsteps li:nth-child(5)[data-bespoke-marp-fragment=active]) .res { stroke: #16a34a; }
  section.fit:has(.fsteps li:nth-child(5)[data-bespoke-marp-fragment=active]) .err i { background: #16a34a; }
  section.fit:has(.fsteps li:nth-child(6)[data-bespoke-marp-fragment=active]) .eq b { background: #fde7b0; }
  section.npar { padding-top: 40px; }
  .nrow { display: flex; gap: 40px; align-items: center; margin-top: 30px; }
  .nrow .nl { flex: 1; }
  table.ds { border-collapse: collapse; font-size: 0.95em; }
  table.ds th, table.ds td { border: 0; border-bottom: 1px solid var(--line); padding: 12px 26px; text-align: center; background: none; font-family: ui-monospace, monospace; }
  table.ds tr { background: none !important; }
  table.ds th { font-family: Inter, sans-serif; font-weight: 600; font-size: 0.8em; border-bottom: 2px solid var(--fg); }
  table.ds .ft { color: var(--accent); } table.ds .lb { color: #b45309; background: #fff4e0; }
  table.ds tr.kind td { font-family: Inter, sans-serif; font-size: 0.6em; text-transform: uppercase; letter-spacing: 0.12em; border: 0; padding-bottom: 2px; }
  table.ds .k2, table.ds .k3, table.ds .kn { display: none; animation: pop 0.6s ease; }
  @keyframes pop { from { opacity: 0; } to { opacity: 1; } }
  section.npar:has(.fsteps li:nth-child(1)[data-bespoke-marp-fragment=active]) table.ds .k2, section.npar:has(.fsteps li:nth-child(2)[data-bespoke-marp-fragment=active]) table.ds .k3, section.npar:has(.fsteps li:nth-child(3)[data-bespoke-marp-fragment=active]) table.ds .kn { display: table-cell; }
  .neq { position: relative; height: 50px; margin-top: 34px; font-family: ui-monospace, monospace; font-size: 0.95em; }
  .neq .s4 { font-family: Inter, sans-serif; font-weight: 400; }
  .neq span, .ncount span { position: absolute; left: 0; top: 0; opacity: 0; transition: opacity 0.5s; white-space: nowrap; }
  .neq b { font-weight: 700; color: var(--accent); }
  .ncount { flex: 0 0 340px; text-align: center; }
  .ncount .nn { position: relative; height: 1.2em; font-size: 4em; font-weight: 800; color: var(--accent); line-height: 1.2; }
  .ncount .nn span { left: 0; right: 0; }
  .ncount p { margin: 0; color: var(--muted); font-size: 0.8em; }
  section.npar:not(:has(.fsteps li:nth-child(1)[data-bespoke-marp-fragment=active])) .s0, section.npar:has(.fsteps li:nth-child(1)[data-bespoke-marp-fragment=active]):not(:has(.fsteps li:nth-child(2)[data-bespoke-marp-fragment=active])) .s1, section.npar:has(.fsteps li:nth-child(2)[data-bespoke-marp-fragment=active]):not(:has(.fsteps li:nth-child(3)[data-bespoke-marp-fragment=active])) .s2, section.npar:has(.fsteps li:nth-child(3)[data-bespoke-marp-fragment=active]):not(:has(.fsteps li:nth-child(4)[data-bespoke-marp-fragment=active])) .s3, section.npar:has(.fsteps li:nth-child(4)[data-bespoke-marp-fragment=active]) .s4 { opacity: 1; }
  section.npar:has(.fsteps li:nth-child(4)[data-bespoke-marp-fragment=active]) .ncount .nn { font-size: 2.6em; }
  section.npar .fsteps { font-size: 0.8em; margin-top: 30px; }
  a { color: inherit; text-decoration: underline; text-decoration-color: var(--accent); text-underline-offset: 3px; }
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Introduzione all'IA e all'IA generativa

<p style="color:var(--muted)">Come fa una macchina a scrivere come Eco?</p>

---

### Agenda

1. IA: definizioni generali
2. Classificazione dei sistemi di IA
3. IA generativa: introduzione agli LLM
4. Etica nei sistemi di IA
5. Successi e fallimenti dell'IA

---

### Definizioni generali

> «Un problema fondamentale della definizione di "Intelligenza artificiale" è che nessuno sa cosa sia realmente l'intelligenza.»

<cite>Shane Legg, Marcus Hutter, <em><a href="https://arxiv.org/abs/0712.3329">Universal Intelligence: A Definition of Machine Intelligence</a></em></cite>

---

### Definizioni generali

> In computer science, artificial intelligence (AI) […] is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans.

<cite>Definizione di Intelligenza Artificiale di Wikipedia fino al 2020</cite>

---

<!-- _class: big -->

### La proposta, 31 agosto 1955

# «Si cercherà di scoprire come far sì che le macchine **usino il linguaggio**, formino astrazioni e concetti, risolvano problemi oggi riservati agli esseri umani»

<span class="src">J. McCarthy, M. Minsky, N. Rochester, C. Shannon, <em>A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence</em>. Richiesta: due mesi, dieci persone</span>

---

<!-- _class: dart -->

### Hanover, New Hampshire · estate 1956

<div class="faces">

* <img src="img/dartmouth-mccarthy.jpg"><span class="cap"><b class="nm">John McCarthy</b><span class="yr">1927-2011</span><span class="tx">Conia <b>intelligenza artificiale</b>, inventa il LISP</span></span>
* <img src="img/dartmouth-minsky.jpg"><span class="cap"><b class="nm">Marvin Minsky</b><span class="yr">1927-2016</span><span class="tx">Fonda il laboratorio di IA del MIT, consulente per <b>HAL 9000</b></span></span>
* <img src="img/dartmouth-shannon.jpg"><span class="cap"><b class="nm">Claude Shannon</b><span class="yr">1916-2001</span><span class="tx">Padre della <b>teoria dell'informazione</b></span></span>
* <img src="img/dartmouth-simon.jpg"><span class="cap"><b class="nm">Herbert Simon</b><span class="yr">1916-2001</span><span class="tx"><b>Logic Theorist</b>, Nobel per l'economia 1978</span></span>
* <img src="img/dartmouth-selfridge.jpg"><span class="cap"><b class="nm">Oliver Selfridge</b><span class="yr">1926-2008</span><span class="tx"><b>Pandemonium</b>, riconoscimento di forme</span></span>
* <img src="img/dartmouth-nash.jpg"><span class="cap"><b class="nm">John Nash</b><span class="yr">1928-2015</span><span class="tx"><b>Equilibrio di Nash</b>, Nobel 1994, <i>A Beautiful Mind</i></span></span>

</div>

<div class="others">

* E poi Nathaniel Rochester (IBM), Allen Newell, Arthur Samuel, Ray Solomonoff, Warren McCulloch e altri

</div>


---

### Definizioni generali

> Ai fini presenti, il problema dell'intelligenza artificiale viene considerato come quello di far comportare una macchina in modi che verrebbero definiti intelligenti se fosse un essere umano a comportarsi così.

<cite>John McCarthy, nota alla lista dei partecipanti al <em><a href="http://www-formal.stanford.edu/jmc/history/dartmouth/dartmouth.html">Dartmouth Summer Research Project on Artificial Intelligence</a></em>, dopo l'estate 1956</cite>

---

<!-- _class: big -->

# Una lavatrice può essere definita intelligente?

---

### Definizioni

- La definizione originaria **non ha niente a che fare col pensiero**
- È più legata al **comportamento** (behavior)
- Alan Turing giunse alle stesse conclusioni quando sviluppò il **Test di Turing**

---

### Definizioni generali

> «La domanda se un computer possa pensare non è più interessante della domanda se un sottomarino possa nuotare»

<cite>Edsger Dijkstra</cite>

---

### Definizioni

La domanda «Un computer può pensare?» è semplicemente **mal posta**

**Keypoints:**

- non fissarsi su analogie fuorvianti
- è più utile studiare **cosa** fa un computer e **come** lo fa

---

### Cosa stiamo misurando?

## Due anime nell'Intelligenza Artificiale

<div class="cols">
<div class="card"><h2>Ingegneristica</h2><p>Aspetto rilevante: eseguire con successo un compito</p></div>
<div style="flex:0 0 120px"><img src="img/image10.png" style="width:120px"></div>
<div class="card"><h2>Cognitiva</h2></div>
</div>

---

### Cosa stiamo misurando?

<div class="cols">
<div class="card center"><img src="img/image11.png" style="height:130px"><h2>Task Focused AI</h2><p>oppure IA debole, IA stretta</p></div>
<div class="card center"><img src="img/image12.png" style="height:130px"><h2>Process Focused AI</h2><p>oppure IA cognitiva, IA forte, AGI</p></div>
</div>

---

<!-- _class: lead -->
<!-- _paginate: false -->

### Parte 2

# Classificazione dei sistemi di IA

---

<!-- _class: big -->

### AI simbolica

![h:460](img/image13.png)

---

### AI simbolica

- Sistemi che seguono un **set di regole predefinite**
- Logica proposizionale
- Se tutto è regola, tutto è deducibile
- Esempio: [un algoritmo che gioca a Tris](https://gabri-sh.github.io/tris/tris-nes.css%20ai/indexAI.html)

---

<!-- _class: fit -->

### Machine Learning

<div class="mlrow">
<img class="mlc" src="img/ml-cerchi.png">
<div class="plot">
<div class="eq"><span class="e0">voto = <b>a</b> · ore + <b>b</b></span><span class="e1">voto = <b>−0,5</b> · ore + <b>9</b></span><span class="e2">voto = <b>0</b> · ore + <b>6,5</b></span><span class="e3">voto = <b>0,3</b> · ore + <b>5</b></span><span class="e4">voto = <b>0,53</b> · ore + <b>4,2</b></span></div>
<svg viewBox="0 0 560 420" width="560" height="420"><line x1="60" y1="20" x2="60" y2="360" stroke="#1a1a1a" stroke-width="2"/><line x1="60" y1="360" x2="550" y2="360" stroke="#1a1a1a" stroke-width="2"/><line x1="60" y1="360" x2="60" y2="366" stroke="#bbb"/><text x="60" y="384" text-anchor="middle">0</text><line x1="156" y1="360" x2="156" y2="366" stroke="#bbb"/><text x="156" y="384" text-anchor="middle">2</text><line x1="252" y1="360" x2="252" y2="366" stroke="#bbb"/><text x="252" y="384" text-anchor="middle">4</text><line x1="348" y1="360" x2="348" y2="366" stroke="#bbb"/><text x="348" y="384" text-anchor="middle">6</text><line x1="444" y1="360" x2="444" y2="366" stroke="#bbb"/><text x="444" y="384" text-anchor="middle">8</text><line x1="540" y1="360" x2="540" y2="366" stroke="#bbb"/><text x="540" y="384" text-anchor="middle">10</text><line x1="54" y1="360" x2="60" y2="360" stroke="#bbb"/><text x="46" y="365" text-anchor="end">2</text><line x1="54" y1="280" x2="60" y2="280" stroke="#bbb"/><text x="46" y="285" text-anchor="end">4</text><line x1="54" y1="200" x2="60" y2="200" stroke="#bbb"/><text x="46" y="205" text-anchor="end">6</text><line x1="54" y1="120" x2="60" y2="120" stroke="#bbb"/><text x="46" y="125" text-anchor="end">8</text><line x1="54" y1="40" x2="60" y2="40" stroke="#bbb"/><text x="46" y="45" text-anchor="end">10</text><text x="550" y="410" text-anchor="end">ore di studio a settimana</text><text x="70" y="26">voto</text><text x="550" y="26" text-anchor="end" font-size="12">dati inventati</text><path class="res" d="M220.5,181.0 L220.5,146.9 M107.1,223.1 L107.1,99.6 M316.2,169.5 L316.2,186.7 M303.4,160.7 L303.4,181.4 M91.3,276.1 L91.3,93.0 M115.3,250.0 L115.3,103.1 M265.9,178.4 L265.9,165.8 M175.1,240.9 L175.1,128.0 M357.5,106.4 L357.5,204.0 M253.4,204.1 L253.4,160.6 M205.1,196.4 L205.1,140.4 M139.5,224.5 L139.5,113.1 M442.6,87.2 L442.6,239.4 M155.9,273.3 L155.9,120.0 M242.4,217.4 L242.4,156.0 M321.5,150.4 L321.5,189.0 M167.3,226.8 L167.3,124.7 M381.4,156.1 L381.4,213.9 M338.6,140.9 L338.6,196.1 M278.9,196.1 L278.9,171.2 M389.8,78.1 L389.8,217.4 M184.5,255.6 L184.5,131.9 M469.3,108.9 L469.3,250.5 M403.5,142.4 L403.5,223.1 M127.7,167.4 L127.7,108.2 M263.1,186.2 L263.1,164.6"/><g class="pts"><circle cx="220.5" cy="181.0" r="6"/><circle cx="107.1" cy="223.1" r="6"/><circle cx="316.2" cy="169.5" r="6"/><circle cx="303.4" cy="160.7" r="6"/><circle cx="91.3" cy="276.1" r="6"/><circle cx="115.3" cy="250.0" r="6"/><circle cx="265.9" cy="178.4" r="6"/><circle cx="175.1" cy="240.9" r="6"/><circle cx="357.5" cy="106.4" r="6"/><circle cx="253.4" cy="204.1" r="6"/><circle cx="205.1" cy="196.4" r="6"/><circle cx="139.5" cy="224.5" r="6"/><circle cx="442.6" cy="87.2" r="6"/><circle cx="155.9" cy="273.3" r="6"/><circle cx="242.4" cy="217.4" r="6"/><circle cx="321.5" cy="150.4" r="6"/><circle cx="167.3" cy="226.8" r="6"/><circle cx="381.4" cy="156.1" r="6"/><circle cx="338.6" cy="140.9" r="6"/><circle cx="278.9" cy="196.1" r="6"/><circle cx="389.8" cy="78.1" r="6"/><circle cx="184.5" cy="255.6" r="6"/><circle cx="469.3" cy="108.9" r="6"/><circle cx="403.5" cy="142.4" r="6"/><circle cx="127.7" cy="167.4" r="6"/><circle cx="263.1" cy="186.2" r="6"/></g><path class="ln" d="M60,80.0 L540,280.0"/></svg>
<div class="err"><span>errore medio</span><i></i><span class="ev"><em class="m1">2,1 voti</em><em class="m2">1,1 voti</em><em class="m3">0,7 voti</em><em class="m4">0,5 voti</em></span></div>
<div class="fsteps">

* **Si parte a caso.** Più studi, peggio vai: sbagliatissima
* **Si misura l'errore:** quanto dista ogni punto dalla retta
* **Si correggono a e b**, di poco, per ridurre l'errore
* **E si ripete.** L'errore scende ancora
* **La retta migliore** per questi dati
* **a e b sono i parametri.** Trovarli è l'addestramento

</div>
</div>
</div>

---

<!-- _class: npar -->

### Machine Learning

## Più caratteristiche, più parametri

<div class="nrow">
<div class="nl">
<table class="ds"><tr class="kind"><td class="ft" colspan="1">feature</td><td class="k2"></td><td class="k3"></td><td class="kn"></td><td class="lb">label</td></tr><tr><th class="ft">ore di studio</th><th class="ft k2">ore di sonno</th><th class="ft k3">assenze</th><th class="ft kn">… xₙ</th><th class="lb">voto</th></tr><tr><td>2</td><td class="k2">6</td><td class="k3">10</td><td class="kn">…</td><td class="lb">5</td></tr><tr><td>5</td><td class="k2">7</td><td class="k3">4</td><td class="kn">…</td><td class="lb">6,5</td></tr><tr><td>8</td><td class="k2">8</td><td class="k3">1</td><td class="kn">…</td><td class="lb">8</td></tr></table>
<div class="neq"><span class="s0">voto = <b>a</b>·ore + <b>b</b></span><span class="s1">voto = <b>a₁</b>·ore + <b>a₂</b>·sonno + <b>b</b></span><span class="s2">voto = <b>a₁</b>·ore + <b>a₂</b>·sonno + <b>a₃</b>·assenze + <b>b</b></span><span class="s3">voto = <b>a₁</b>·x₁ + <b>a₂</b>·x₂ + … + <b>aₙ</b>·xₙ + <b>b</b></span><span class="s4">stesso gioco: indovinare, misurare l'errore, correggere</span></div>
</div>
<div class="ncount"><div class="nn"><span class="s0">2</span><span class="s1">3</span><span class="s2">4</span><span class="s3">n + 1</span><span class="s4">70 miliardi</span></div><p>parametri</p></div>
</div>
<div class="fsteps">

* **Una caratteristica in più:** le ore di sonno. Un parametro in più
* **E un'altra:** le assenze
* **n caratteristiche:** n + 1 parametri
* **Un LLM, Llama 2 70B:** 70 miliardi di parametri. Il gioco è lo stesso

</div>

---

### Machine Learning

- Un sistema che fa **predizioni su base statistica**
- Introduzione del concetto di **addestramento**
- La logica lascia spazio alla **probabilità**
- L'algoritmo «impara» osservando le correlazioni senza essere cosciente

---

### Machine Learning

## L'importanza dei dati nell'epoca dei big data

Tutto quello che facciamo è sorgente di dati che sono utilizzati dai provider di servizi per:

- vendita dei dati
  - [Ottobre 2026](https://www.repubblica.it/economia/2026/10/10/news/spirit_airlines_fallisce_google_compra_100_milioni_di_email_rivolta_tra_i_parlamentari_usa-425638929/): Spirit Airlines fallisce e Google offre **10 milioni di dollari** per i suoi archivi, circa **100 milioni di email**, per addestrare l'AI. Oltre 120 parlamentari USA protestano: secondo loro i dipendenti non hanno mai autorizzato quell'uso
- addestramento diretto di modelli

Esistono **dataset pubblici** praticamente per [qualsiasi cosa](https://www.kaggle.com/datasets/rounakbanik/pokemon)

---

<!-- _class: big -->

### Deep Learning

![h:460](img/image15.png)

---

### Deep Learning

- Principi identici al machine learning ma con modelli di **reti neurali**
- **Costosi** da addestrare (tempo e denaro)
- **Difficili da spiegare** (bassa explainability)
- **Efficacissimi** in determinati scenari
- Un esempio: [la guida autonoma](https://www.youtube.com/watch?v=u_eZoOS5bFc)

---

### Deep Learning

<div class="cols">
<div>

- Oltre ai dati si creano enormi possibilità per i **produttori di chip**
- Possedere GPU diventa il must have
- [Il successo di **nVidia**](https://www.forbes.com/sites/tylerroush/2025/07/15/nvidia-shares-hit-all-time-high-as-trump-administration-backs-china-chip-sales/)

</div>
<div class="center">

![h:380](img/image16.jpeg)
<span class="src">Jensen Huang, CEO di Nvidia</span>

</div>
</div>

---

### Deep Learning

<div class="cols">
<div>

- Oltre ai dati si creano enormi possibilità per i **produttori di chip**
- Possedere GPU diventa il must have
- [**AlphaGo – The Movie**](https://www.youtube.com/watch?v=WXuK6gekU1Y)

</div>
<div class="center">

![w:560](img/image17.jpeg)
<span class="src">Lee Se-Dol durante il match contro AlphaGo</span>

</div>
</div>

---

<!-- _class: big -->

### Generative AI

![h:460](img/image18.png)

---

### Generative AI

- Dal **2014** le deep neural networks sono utilizzate per creare contenuti «originali» basandosi sui dati di addestramento
- [this-person-does-not-exist.com](https://this-person-does-not-exist.com/)

**Ma è dal 2017 che cambia tutto…**

---

### Generative AI

<div class="cols">
<div>

…quando Google pubblica il paper **«[Attention is all you need](https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)»**

Nel paper si introduce una nuova architettura di reti neurali chiamata **transformer**:

- specializzati nell'elaborazione del linguaggio naturale (NLP)

</div>
<div class="center" style="flex:0 0 320px">

![h:440](img/image19.png)
<span class="src">Schema dell'architettura Transformer</span>

</div>
</div>

---

### Generative AI

<div class="cols">
<div>

- Originariamente nati per la **traduzione automatica**
- Sono la base degli attuali **Large Language Models**

</div>
<div class="center" style="flex:0 0 320px">

![h:440](img/image19.png)
<span class="src">Schema dell'architettura Transformer</span>

</div>
</div>

---

<!-- _class: lead -->
<!-- _paginate: false -->

### Parte 3

# Large Language Models

---

### Recap – Da dove partiamo

<div class="cols">
<div>

L'IA generativa è un sottoinsieme dell'Intelligenza Artificiale che si concentra sullo sviluppo di sistemi e modelli capaci di **creare contenuti originali** a partire da **dati esistenti**.

</div>
<div class="center" style="flex:0 0 300px">

![w:300](img/image20.png)

</div>
</div>

---

### Recap – Da dove partiamo

<div class="cols">
<div class="card"><h2>Modelli</h2><p>Software</p></div>
<div class="card"><h2>Creare contenuti originali</h2><p>Creare contenuti molto probabilmente inesistenti</p></div>
<div class="card"><h2>A partire da testi esistenti</h2><p>«Copiando» testi già noti al software (dati di addestramento)</p></div>
</div>

---

### Large Language Models

Si tratta di **modelli matematici** in grado di codificare informazioni statistiche su uno o più linguaggi, ossia **quanto è probabile che una parola appaia** in una determinata frase.

![w:1000](img/image21.png)

---

### Punti chiave

- Il processo di generazione avviene in maniera **sequenziale**
- La generazione avviene su **base statistica**
- Le statistiche sono calcolate in base ai **dati di addestramento**
- I contenuti generati sono scelti da un **vocabolario**

---

### Addestramento

## La benzina sono i dati

- Libri, siti, enciclopedie, codice, conversazioni: **miliardi di parole**
- Il modello non memorizza i testi: ne ricava **le regolarità** (quali parole stanno insieme, in quale ordine, in quale contesto)
- Sa solo ciò che c'era nei dati, con **gli stessi squilibri e gli stessi stereotipi**

---

### Addestramento

## Quanto è grande la benzina?

<div class="center" style="margin-top:1.4em">

# 15 milioni di siti web

<p style="color:var(--muted)">in uno solo dei dataset di addestramento</p>

<p style="font-size:1.1em;margin-top:1.4em"><a href="https://www.washingtonpost.com/technology/interactive/2023/ai-chatbot-learning/">Apriamo l'inchiesta del Washington Post</a></p>

</div>

<cite>Kevin Schaul, Szu Yu Chen, Nitasha Tiku, <em>Inside the secret list of websites that make AI like ChatGPT sound smart</em>, The Washington Post, 19 aprile 2023</cite>

---

### Addestramento

## Un archivio zip che perde i dettagli

<div class="cols" style="align-items:flex-start">
<div class="card"><h2>Lo zip</h2><p>Comprime i file e li restituisce identici</p></div>
<div class="card"><h2>Il modello</h2><p>Comprime miliardi di testi <b>perdendo dettagli</b>: quando "decomprime" ricostruisce ciò che è plausibile, non ciò che c'era</p></div>
</div>

<cite>Ted Chiang, <em><a href="https://www.newyorker.com/tech/annals-of-technology/chatgpt-is-a-blurry-jpeg-of-the-web">ChatGPT Is a Blurry JPEG of the Web</a></em>, The New Yorker, 9 febbraio 2023</cite>

---

<!-- _class: vocab -->

### LLM – Come generano i contenuti?

## Il vocabolario del modello

<div class="cols" style="align-items:flex-start;gap:44px">
<div style="flex:0 0 330px">
<p class="vbig">≈ 200.000</p>
<p class="vsub">pezzi di testo nel vocabolario di GPT-4o. Il modello non conosce altro: ogni testo che legge o scrive è fatto con questi pezzi</p>
<p class="vsub" style="margin-top:0.8em">GPT-2, nel 2019, ne aveva 50.257</p>
</div>
<div class="vgroups">
<div><b>Parole intere</b><div class="tok"><span>·the</span><span>·vita</span><span>·casa</span><span>·scuola</span><span>·docente</span><span>·Bari</span></div></div>
<div><b>Pezzi di parola</b><div class="tok"><span>mente</span><span>zione</span><span>issime</span><span>ing</span></div></div>
<div><b>Simboli e cifre</b><div class="tok"><span>!</span><span>,</span><span>↵</span><span>202</span></div></div>
<div><b>Altre lingue ed emoji</b><div class="tok"><span>ción</span><span>ção</span><span>的</span><span>😀</span></div></div>
</div>
</div>

<div class="vcomp">

<p>E le parole che non ci sono? Si compongono con i pezzi:</p>

* <span class="w">docenti</span><span class="tok"><span>·doc</span><span>enti</span></span>
* <span class="w">intelligenza</span><span class="tok"><span>·int</span><span>elligen</span><span>za</span></span>
* <span class="w">Bitetto</span><span class="tok"><span>·Bit</span><span>etto</span></span>

</div>

<span class="src">Token reali del tokenizzatore di GPT-4o (o200k_base). Il punto · indica lo spazio, ↵ l'a capo</span>

---

### LLM – Come generano i contenuti?

Si parte dall'input dell'utente (**prompt**) e si **tokenizza**

![w:1100](img/image22.png)

---

### LLM – Come generano i contenuti?

## Raymond Queneau (1903-1976)

<div class="cols" style="align-items:flex-start;gap:40px">
<div style="flex:0 0 430px">

<img src="img/queneau-sonetti.jpg" style="width:430px;border-radius:8px">

<span class="src"><em>Cent mille milliards de poèmes</em>, 1961</span>

</div>
<div style="font-size:0.9em">

- **10 sonetti** di 14 versi, ogni verso su una **striscia** che si sfoglia da sola
- Ogni verso si combina con quelli degli altri sonetti: rima e grammatica tornano sempre
- 10<sup>14</sup> combinazioni: **centomila miliardi di poesie**. Per leggerle tutte, stima Queneau, circa **200 milioni di anni**

</div>
</div>

<div class="eco"><b>Come i token:</b> pochi pezzi, combinazioni quasi infinite. Ma Queneau costruisce i versi perché ogni combinazione funzioni; il modello sceglie, un pezzo alla volta, in base alla probabilità.</div>

---

### LLM – Come generano i contenuti?

## Pezzi di parole

<div class="tok-row"><b>Nel mezzo del cammin di nostra vita</b><div class="tok"><span>Nel</span><span>·mezzo</span><span>·del</span><span>·cam</span><span>min</span><span>·di</span><span>·nostra</span><span>·vita</span></div></div>
<div class="tok-row"><b>poeta</b><div class="tok"><span>po</span><span>eta</span></div></div>
<div class="tok-row"><b>Il poeta</b><div class="tok"><span>Il</span><span>·poeta</span></div></div>
<div class="tok-row"><b>precipitevolissimevolmente</b><div class="tok"><span>prec</span><span>ip</span><span>ite</span><span>vol</span><span>issime</span><span>vol</span><span>mente</span></div></div>

<span class="src">Tokenizzatore di GPT-4o (o200k_base). Il punto · indica lo spazio. Ogni modello ha il suo tokenizzatore.</span>

---

<!-- _class: emb -->

### LLM – Come generano i contenuti?

## Dai token ai vettori

<div class="egrid"><div class="ec" style="--k:0"><span class="et">Nel</span><span class="pos">posizione 1</span><span class="ev"><span style="--a:rgba(245,158,11,0.26);--b:rgba(245,158,11,0.36)"><i class="v1">-0,33</i><i class="v2">-0,45</i></span><span style="--a:rgba(245,158,11,0.69);--b:rgba(245,158,11,0.78)"><i class="v1">-0,86</i><i class="v2">-0,98</i></span><span style="--a:rgba(245,158,11,0.67);--b:rgba(245,158,11,0.73)"><i class="v1">-0,84</i><i class="v2">-0,91</i></span><span style="--a:rgba(245,158,11,0.10);--b:rgba(245,158,11,0.18)"><i class="v1">-0,13</i><i class="v2">-0,23</i></span><span style="--a:rgba(37,99,235,0.07);--b:rgba(245,158,11,0.07)"><i class="v1">+0,10</i><i class="v2">-0,09</i></span><span style="--a:rgba(245,158,11,0.57);--b:rgba(245,158,11,0.70)"><i class="v1">-0,71</i><i class="v2">-0,87</i></span><em>⋮</em></span></div><div class="ec" style="--k:1"><span class="et">·mezzo</span><span class="pos">posizione 2</span><span class="ev"><span style="--a:rgba(37,99,235,0.11);--b:rgba(37,99,235,0.01)"><i class="v1">+0,16</i><i class="v2">+0,01</i></span><span style="--a:rgba(245,158,11,0.16);--b:rgba(245,158,11,0.22)"><i class="v1">-0,20</i><i class="v2">-0,27</i></span><span style="--a:rgba(37,99,235,0.48);--b:rgba(37,99,235,0.57)"><i class="v1">+0,68</i><i class="v2">+0,81</i></span><span style="--a:rgba(37,99,235,0.06);--b:rgba(37,99,235,0.16)"><i class="v1">+0,08</i><i class="v2">+0,23</i></span><span style="--a:rgba(37,99,235,0.24);--b:rgba(37,99,235,0.14)"><i class="v1">+0,35</i><i class="v2">+0,20</i></span><span style="--a:rgba(37,99,235,0.18);--b:rgba(37,99,235,0.24)"><i class="v1">+0,26</i><i class="v2">+0,34</i></span><em>⋮</em></span></div><div class="ec" style="--k:2"><span class="et">·del</span><span class="pos">posizione 3</span><span class="ev"><span style="--a:rgba(37,99,235,0.28);--b:rgba(37,99,235,0.17)"><i class="v1">+0,40</i><i class="v2">+0,24</i></span><span style="--a:rgba(245,158,11,0.01);--b:rgba(37,99,235,0.12)"><i class="v1">-0,01</i><i class="v2">+0,17</i></span><span style="--a:rgba(245,158,11,0.06);--b:rgba(37,99,235,0.03)"><i class="v1">-0,07</i><i class="v2">+0,05</i></span><span style="--a:rgba(245,158,11,0.38);--b:rgba(245,158,11,0.52)"><i class="v1">-0,48</i><i class="v2">-0,65</i></span><span style="--a:rgba(245,158,11,0.39);--b:rgba(245,158,11,0.28)"><i class="v1">-0,49</i><i class="v2">-0,35</i></span><span style="--a:rgba(37,99,235,0.50);--b:rgba(37,99,235,0.57)"><i class="v1">+0,71</i><i class="v2">+0,82</i></span><em>⋮</em></span></div><div class="ec" style="--k:3"><span class="et">·cam</span><span class="pos">posizione 4</span><span class="ev"><span style="--a:rgba(37,99,235,0.64);--b:rgba(37,99,235,0.54)"><i class="v1">+0,91</i><i class="v2">+0,77</i></span><span style="--a:rgba(245,158,11,0.51);--b:rgba(245,158,11,0.45)"><i class="v1">-0,64</i><i class="v2">-0,56</i></span><span style="--a:rgba(245,158,11,0.02);--b:rgba(245,158,11,0.18)"><i class="v1">-0,02</i><i class="v2">-0,23</i></span><span style="--a:rgba(245,158,11,0.64);--b:rgba(245,158,11,0.55)"><i class="v1">-0,80</i><i class="v2">-0,69</i></span><span style="--a:rgba(245,158,11,0.22);--b:rgba(245,158,11,0.10)"><i class="v1">-0,28</i><i class="v2">-0,13</i></span><span style="--a:rgba(245,158,11,0.06);--b:rgba(245,158,11,0.23)"><i class="v1">-0,08</i><i class="v2">-0,29</i></span><em>⋮</em></span></div><div class="ec" style="--k:4"><span class="et">min</span><span class="pos">posizione 5</span><span class="ev"><span style="--a:rgba(245,158,11,0.04);--b:rgba(245,158,11,0.10)"><i class="v1">-0,05</i><i class="v2">-0,12</i></span><span style="--a:rgba(37,99,235,0.27);--b:rgba(37,99,235,0.34)"><i class="v1">+0,38</i><i class="v2">+0,49</i></span><span style="--a:rgba(245,158,11,0.18);--b:rgba(245,158,11,0.13)"><i class="v1">-0,22</i><i class="v2">-0,16</i></span><span style="--a:rgba(245,158,11,0.06);--b:rgba(245,158,11,0.18)"><i class="v1">-0,07</i><i class="v2">-0,23</i></span><span style="--a:rgba(245,158,11,0.01);--b:rgba(245,158,11,0.15)"><i class="v1">-0,01</i><i class="v2">-0,19</i></span><span style="--a:rgba(245,158,11,0.56);--b:rgba(245,158,11,0.66)"><i class="v1">-0,70</i><i class="v2">-0,82</i></span><em>⋮</em></span></div><div class="ec" style="--k:5"><span class="et">·di</span><span class="pos">posizione 6</span><span class="ev"><span style="--a:rgba(37,99,235,0.55);--b:rgba(37,99,235,0.60)"><i class="v1">+0,79</i><i class="v2">+0,86</i></span><span style="--a:rgba(245,158,11,0.08);--b:rgba(37,99,235,0.07)"><i class="v1">-0,10</i><i class="v2">+0,10</i></span><span style="--a:rgba(37,99,235,0.43);--b:rgba(37,99,235,0.55)"><i class="v1">+0,61</i><i class="v2">+0,78</i></span><span style="--a:rgba(37,99,235,0.64);--b:rgba(37,99,235,0.69)"><i class="v1">+0,92</i><i class="v2">+0,99</i></span><span style="--a:rgba(245,158,11,0.53);--b:rgba(245,158,11,0.59)"><i class="v1">-0,66</i><i class="v2">-0,74</i></span><span style="--a:rgba(37,99,235,0.21);--b:rgba(37,99,235,0.11)"><i class="v1">+0,30</i><i class="v2">+0,16</i></span><em>⋮</em></span></div><div class="ec" style="--k:6"><span class="et">·nostra</span><span class="pos">posizione 7</span><span class="ev"><span style="--a:rgba(37,99,235,0.12);--b:rgba(37,99,235,0.20)"><i class="v1">+0,17</i><i class="v2">+0,28</i></span><span style="--a:rgba(245,158,11,0.54);--b:rgba(245,158,11,0.41)"><i class="v1">-0,67</i><i class="v2">-0,51</i></span><span style="--a:rgba(245,158,11,0.27);--b:rgba(245,158,11,0.41)"><i class="v1">-0,34</i><i class="v2">-0,51</i></span><span style="--a:rgba(37,99,235,0.02);--b:rgba(245,158,11,0.08)"><i class="v1">+0,03</i><i class="v2">-0,10</i></span><span style="--a:rgba(37,99,235,0.49);--b:rgba(37,99,235,0.57)"><i class="v1">+0,70</i><i class="v2">+0,82</i></span><span style="--a:rgba(245,158,11,0.16);--b:rgba(245,158,11,0.03)"><i class="v1">-0,20</i><i class="v2">-0,04</i></span><em>⋮</em></span></div><div class="ec" style="--k:7"><span class="et">·vita</span><span class="pos">posizione 8</span><span class="ev"><span style="--a:rgba(245,158,11,0.66);--b:rgba(245,158,11,0.79)"><i class="v1">-0,83</i><i class="v2">-0,99</i></span><span style="--a:rgba(245,158,11,0.09);--b:rgba(245,158,11,0.18)"><i class="v1">-0,11</i><i class="v2">-0,22</i></span><span style="--a:rgba(245,158,11,0.68);--b:rgba(245,158,11,0.79)"><i class="v1">-0,85</i><i class="v2">-0,99</i></span><span style="--a:rgba(37,99,235,0.05);--b:rgba(37,99,235,0.16)"><i class="v1">+0,07</i><i class="v2">+0,23</i></span><span style="--a:rgba(245,158,11,0.66);--b:rgba(245,158,11,0.78)"><i class="v1">-0,82</i><i class="v2">-0,98</i></span><span style="--a:rgba(245,158,11,0.54);--b:rgba(245,158,11,0.37)"><i class="v1">-0,67</i><i class="v2">-0,46</i></span><em>⋮</em></span></div></div>

<div class="esteps">

* <b>1 · Un vettore</b> ogni token diventa una lista di numeri, presa dalla tabella del modello: l'embedding
* <b>2 · + la posizione</b> si somma l'informazione sulla posizione: cambiano tutti i numeri. «del» in terza posizione non è uguale a «del» in sesta
* <b>3 · Una tabella</b> 8 token × migliaia di numeri: è questo che il modello elabora davvero

</div>

<span class="src">Token reali del tokenizzatore di GPT-4o. Valori illustrativi: in un modello vero sono migliaia per token (in GPT-3, 12.288)</span>

---

### LLM – Come generano i contenuti?

## Embedding come coordinate

<div class="cols" style="align-items:center;gap:40px">
<div style="flex:0 0 560px">

<img src="img/mappa-palo-bitetto-parigi.svg" style="width:560px">

</div>
<div style="font-size:0.9em">

- Palo e Bitetto: coordinate simili, **3,7 km**. Tante cose in comune
- Palo e Parigi: **circa 1.420 km**. Molto meno in comune
- Gli embedding fanno lo stesso con le parole, ma con **migliaia di coordinate** invece di due

</div>
</div>

---

<!-- _class: move -->

### LLM – Come generano i contenuti?

## È l'ultimo token a spostarsi

<div class="tok-row" style="margin-bottom:10px"><div class="tok att"><span class="tk-la">La</span><span class="tk-banca">·banca</span><span class="tk-del">·del</span><span class="tk-fiume">·fiume</span><span class="last tk-e">·è</span></div></div>

<div class="cols" style="align-items:flex-start;gap:32px">
<div style="flex:0 0 700px">

<svg class="space" viewBox="0 0 700 460" width="700" height="460"><rect width="700" height="460" rx="14" fill="#f7f9fc"/><text x="20" y="444" class="cap">Spazio degli embedding, semplificato in 2 dimensioni. Pesi illustrativi</text><g class="w verbo"><circle cx="70" cy="62" r="5"/><text x="80" y="68">era</text></g><g class="w verbo"><circle cx="165" cy="50" r="5"/><text x="175" y="56">sono</text></g><g class="w verbo"><circle cx="95" cy="128" r="5"/><text x="105" y="134">sta</text></g><g class="w verbo"><circle cx="190" cy="118" r="5"/><text x="200" y="124">ha</text></g><g class="w fin"><circle cx="90" cy="360" r="5"/><text x="100" y="366">conto</text></g><g class="w fin"><circle cx="175" cy="410" r="5"/><text x="185" y="416">mutuo</text></g><g class="w fin"><circle cx="60" cy="400" r="5"/><text x="70" y="406">denaro</text></g><g class="w fin"><circle cx="190" cy="340" r="5"/><text x="200" y="346">prestito</text></g><g class="w nat"><circle cx="390" cy="95" r="5"/><text x="400" y="101">riva</text></g><g class="w nat"><circle cx="470" cy="140" r="5"/><text x="480" y="146">argine</text></g><g class="w nat"><circle cx="520" cy="80" r="5"/><text x="530" y="86">acqua</text></g><g class="w nat"><circle cx="410" cy="185" r="5"/><text x="420" y="191">rapide</text></g><g class="w agg"><circle cx="470" cy="300" r="5"/><text x="480" y="306">ripida</text></g><g class="w agg"><circle cx="555" cy="355" r="5"/><text x="565" y="361">rocciosa</text></g><g class="w agg"><circle cx="480" cy="405" r="5"/><text x="490" y="411">piena</text></g><g class="w agg"><circle cx="560" cy="265" r="5"/><text x="570" y="271">scivolosa</text></g><circle class="ghost g1" cx="150" cy="92" r="9"/><circle class="ghost g2" cx="300" cy="160" r="9"/><circle class="ghost g3" cx="420" cy="250" r="9"/><g id="dot"><circle r="13"/><text x="18" y="7">è</text></g></svg>

</div>
<div class="steps">

* <b>Partenza</b> il vettore di «è» preso dalla tabella: vicino agli altri verbi
* <b>Primo strato</b> «è» guarda tutti i token insieme: «banca» e «fiume» pesano di più e lo spingono verso l'acqua
* <b>Strati intermedi</b> lo stesso meccanismo, strato dopo strato: il vettore si allontana dalla finanza
* <b>Ultimo strato</b> arriva vicino a «ripida», «rocciosa», «piena»
* <b>Proiezione</b> i token più vicini sono i più probabili

</div>
</div>

---

<!-- _class: samp -->

### LLM – Come generano i contenuti?

## Dalla posizione alla parola

<div class="tok-row" style="margin-bottom:12px"><div class="tok att"><span>La</span><span>·banca</span><span>·del</span><span>·fiume</span><span>·è</span><span class="last newtok">·rocciosa</span></div></div>

<div class="cols" style="align-items:flex-start;gap:36px">
<div style="flex:0 0 640px">
<div class="ptab">
<div class="pick"></div>
<div class="r r1"><span class="t">·ripida</span><span class="b"><i style="--w:81.6%"></i></span><span class="p">34%</span></div><div class="r r2"><span class="t">·rocciosa</span><span class="b"><i style="--w:64.8%"></i></span><span class="p">27%</span></div><div class="r r3"><span class="t">·piena</span><span class="b"><i style="--w:38.4%"></i></span><span class="p">16%</span></div><div class="r r4"><span class="t">·scivolosa</span><span class="b"><i style="--w:26.4%"></i></span><span class="p">11%</span></div><div class="r r5"><span class="t">·chiusa</span><span class="b"><i style="--w:9.6%"></i></span><span class="p">4%</span></div><div class="r r6"><span class="t">·fallita</span><span class="b"><i style="--w:2.4%"></i></span><span class="p">1%</span></div>
<div class="more">… e tutti gli altri token del vocabolario, con probabilità vicina a zero</div>
</div>
</div>
<div class="steps">

* <b>Proiezione</b> il vettore di «è» diventa una probabilità per ogni token
* <b>Top-k</b> restano in gara solo i 4 più probabili
* <b>Campionamento</b> un'estrazione casuale, pesata sulle probabilità: non vince per forza il primo
* <b>E si ricomincia</b> il token scelto si aggiunge alla frase

</div>
</div>

---

<!-- _class: big -->

### LLM – Come generano i contenuti?

# Proviamo: un token alla volta

<p style="font-size:1.1em;margin-top:1em"><a href="next-token.html" target="_blank">Apri la simulazione</a></p>

<span class="src">«Il mio colore preferito è…»: probabilità, campionamento, temperatura</span>

---

### Recap – Da dove partiamo

<div class="cols">
<div>

Generano contenuti:

- con un processo **iterativo**
- su **base statistica** con una **componente casuale**

</div>
<div class="center" style="flex:0 0 300px">

![w:300](img/image27.png)

</div>
</div>

---

<!-- _class: big -->

# I Large Language Models non modellano la **conoscenza**, ma il **linguaggio**

---

### LLM – Limiti invalicabili

<div class="cols">
<div class="card center"><img src="img/image28.png" style="height:90px"><h2>Knowledge cutoff</h2><p>Non conoscono fatti avvenuti dopo il loro addestramento</p></div>
<div class="card center"><img src="img/image30.png" style="height:90px"><h2>Hallucinations</h2><p>La loro creatività può ritorcersi loro contro producendo risposte false o errate</p></div>
<div class="card center"><img src="img/image29.png" style="height:90px"><h2>Conoscenza di dominio assente</h2><p>Non sanno rispondere a domande che richiedono informazioni specifiche</p></div>
</div>

---

### LLM – Limiti invalicabili

## Hallucinations: lo dice anche il falso Eco

- Nel falso: **Teofrasto di Melitene**, filosofo bizantino mai esistito, con trattato, manoscritto e segnatura
- Nella realtà: **Tribunale di Firenze, 14 marzo 2025**, un atto cita sentenze della Cassazione inventate da ChatGPT
- Il modello produce ciò che è **plausibile**: la verità non è un criterio del calcolo

<div class="eco">«Si obietterà che una successione plausibile di parole non è pensiero.» Dalla finta Bustina</div>

---

<!-- _class: big -->

### Hands on

> «L'autolavaggio è a 40 metri da casa. Devo lavare la macchina. Dovrei andarci a piedi o in macchina?»

---

### Mitigazioni

- **Prompt Engineering:** chiedere le cose nel miglior modo possibile
- **Retrieval:** inviare dei file o della conoscenza «esterna» per l'analisi durante la conversazione
- **Fine tuning:** ri-addestrare il modello aggiungendo fra i dati di addestramento altre informazioni (altri testi)

---

### Oltre gli LLM – Agenti AI

Le piattaforme più blasonate di IA generativa possono interagire con moduli terzi per:

- fare ricerche sul web
- analizzare e leggere contenuti da file
- generare grafici anche interattivi

Quando un'applicazione che fa uso di LLM può interagire con altri componenti e **riesce a capire quando farlo** si parla di **agente AI**

---

<!-- _class: lead -->
<!-- _paginate: false -->

### Parte 4

# Rischi dei Large Language Models

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

### Rischi degli LLM

## Sostenibilità

L'IA generativa ha un elevatissimo **consumo energetico** in termini di:

- uso di modelli
- costruzione di data center

L'impatto più immediato e preoccupante è sul **[consumo di acqua](https://www.forbes.com/sites/cindygordon/2024/02/25/ai-is-accelerating-the-loss-of-our-scarcest-natural-resource-water/)** legato all'uso di modelli di IA

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

### Rischi degli LLM

## Etica e misconception

Cause in corso fra aziende operanti nell'AI e famiglie per accuse legate ad **istigazione al suicidio**:

- [Adam Raine](https://www.theguardian.com/us-news/2025/aug/29/chatgpt-suicide-openai-sam-altman-adam-raine)
- [Sewell Setzer III](https://www.theguardian.com/technology/2024/oct/23/character-ai-chatbot-sewell-setzer-death)
- [Zane Shamblin](https://edition.cnn.com/2025/11/06/us/openai-chatgpt-suicide-lawsuit-invs-vis)

---

<!-- _class: lead -->
<!-- _paginate: false -->

### Parte 5

# Use case e scenari efficaci

---

### LLM – Sono da buttare via?

<div class="cols" style="align-items:flex-start">
<div>

- Customer Service di nuova generazione
- Personalizzazione del marketing
- Supporto nell'automazione di processi aziendali
- Revisione di documentazione

</div>
<div>

- Creazione di corpus di documenti
- Creatività
- Estrazione dati strutturati da documenti non strutturati

</div>
</div>

---

<!-- _class: big -->
<!-- _paginate: false -->

# …domande?
