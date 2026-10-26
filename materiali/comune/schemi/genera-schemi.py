import os
OUT=os.path.dirname(os.path.abspath(__file__))
INK='#111'; BLUE='#2f54ff'; LIME='#e4f75a'; GREEN='#2fff6a'; LILAC='#c39bff'; ORANGE='#ff7a2f'; PINK='#ff8af7'; SKY='#d6f0ff'; GREY='#9a9a9a'; PAPER='#ffffff'
FONT="font-family=\"Inter, Helvetica, Arial, sans-serif\""
def svg(w,h,body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" {FONT}>\n<defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="{INK}"/></marker></defs>\n{body}\n</svg>\n'
def T(x,y,s,size=22,w=600,fill=INK,anchor='middle'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}">{s}</text>'
def box(x,y,w,h,fill=PAPER,r=16,sw=3,dash=False):
    d=' stroke-dasharray="10 8"' if dash else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{INK}" stroke-width="{sw}"{d}/>'
def arrow(x1,y1,x2,y2,dash=False):
    d=' stroke-dasharray="8 7"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{INK}" stroke-width="3"{d} marker-end="url(#ar)"/>'
def doc(x,y,s=1,fill=PAPER):
    w,h=44*s,56*s; f=14*s
    return (f'<path d="M{x} {y} h{w-f} l{f} {f} v{h-f} h{-w} z" fill="{fill}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
            + ''.join(f'<line x1="{x+8*s}" y1="{y+(22+i*10)*s}" x2="{x+w-8*s}" y2="{y+(22+i*10)*s}" stroke="{INK}" stroke-width="2.5"/>' for i in range(3)))
def check(x,y,on=True):
    if on: return f'<rect x="{x}" y="{y}" width="30" height="30" rx="6" fill="{BLUE}" stroke="{INK}" stroke-width="3"/><path d="M{x+7} {y+15} l6 6 l11 -12" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
    return f'<rect x="{x}" y="{y}" width="30" height="30" rx="6" fill="#fff" stroke="{INK}" stroke-width="3"/>'
def person(x,y,fill=LILAC):
    return f'<circle cx="{x}" cy="{y}" r="16" fill="{fill}" stroke="{INK}" stroke-width="3"/><path d="M{x-28} {y+52} q0 -30 28 -30 q28 0 28 30 z" fill="{fill}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
def gear(cx,cy,r=26,fill=LIME):
    teeth=''.join(f'<rect x="{cx-6}" y="{cy-r-10}" width="12" height="16" rx="3" fill="{fill}" stroke="{INK}" stroke-width="3" transform="rotate({a} {cx} {cy})"/>' for a in range(0,360,45))
    return teeth+f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{INK}" stroke-width="3"/><circle cx="{cx}" cy="{cy}" r="{r*0.38}" fill="#fff" stroke="{INK}" stroke-width="3"/>'
def bubble(x,y,w,h,fill=GREEN):
    return f'<path d="M{x+14} {y} h{w-28} q14 0 14 14 v{h-28} q0 14 -14 14 h{-(w-60)} l-18 18 v-18 h-10 q-14 0 -14 -14 v{-(h-28)} q0 -14 14 -14 z" fill="{fill}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
def bucket(x,y,w,h,layers,clip):
    # layers: list of (fraction_height, color, label) from bottom
    top=x; inset=w*0.12
    path=f'M{x} {y} L{x+w} {y} L{x+w-inset} {y+h} L{x+inset} {y+h} Z'
    out=f'<defs><clipPath id="{clip}"><path d="{path}"/></clipPath></defs><g clip-path="url(#{clip})">'
    cur=y+h; labels=''
    for frac,col,lab in layers:
        hh=h*frac; cur-=hh
        out+=f'<rect x="{x-5}" y="{cur}" width="{w+10}" height="{hh}" fill="{col}"/>'
        if lab: labels+=T(x+w/2,cur+hh/2+7,lab,18,700,'#fff' if col==BLUE else INK)
    out+='</g>'+labels
    out+=f'<path d="{path}" fill="none" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>'
    out+=f'<path d="M{x} {y} Q{x+w/2} {y-70} {x+w} {y}" fill="none" stroke="{INK}" stroke-width="3"/>'
    return out

files={}
# 1 notebook di classe
b=''
srcs=[(LILAC,'Profili (4)'),(ORANGE,'Scheda di scienze'),(LIME,'Programmazione 4ª')]
for i,(c,l) in enumerate(srcs):
    y=50+i*165
    b+=box(30,y,370,120)+f'<circle cx="92" cy="{y+60}" r="40" fill="{c}" stroke="{INK}" stroke-width="3"/>'+doc(70,y+32,0.9)
    b+=T(150,y+68,l,21,600,anchor='start')+check(352,y+45)
    b+=arrow(405,y+60,505,310)
b+=box(515,170,300,280,BLUE,24)
b+=f'<path d="M600 245 q65 -22 65 0 v110 q-65 -22 -65 0 z M730 245 q-65 -22 -65 0 v110 q65 -22 65 0 z" fill="#fff" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
b+=T(665,405,'Notebook di classe',24,800,'#fff')+T(665,432,'Gemini Notebook',17,500,'#fff')
b+=arrow(820,310,905,310)
b+=box(915,170,265,280)
for i,wd in enumerate([200,170,210,140]): b+=f'<rect x="945" y="{205+i*38}" width="{wd}" height="14" rx="7" fill="#ddd"/>'
b+=f'<circle cx="960" cy="385" r="18" fill="{LIME}" stroke="{INK}" stroke-width="3"/>'+T(960,392,'1',18,800)
b+=f'<circle cx="1005" cy="385" r="18" fill="{LIME}" stroke="{INK}" stroke-width="3"/>'+T(1005,392,'2',18,800)
b+=T(1047,480,'Risposta con citazioni',20,600)
for i,c in enumerate([LILAC,GREEN,PINK]): b+=person(605+i*60,540,c)
b+=T(665,622,'condiviso con il team',19,500,GREY)
files['notebook-classe.svg']=svg(1210,640,b)

# 2 percorso: tre secchi
b=''
specs=[('1 · Gemini Notebook','le fonti',[(0.22,ORANGE,'scheda'),(0.22,LILAC,'profili'),(0.22,LIME,'programma')]),
       ('2 · Gem','istruzioni sempre dentro',[(0.25,LIME,'istruzioni'),(0.22,LILAC,'conoscenza'),(0.18,GREEN,'richiesta')]),
       ('3 · Skill','istruzioni solo quando servono',[(0.18,GREEN,'richiesta'),(0.22,BLUE,'istruzioni')])]
for i,(t,c,lay) in enumerate(specs):
    x=40+i*390
    b+=T(x+150,40,t,26,800)
    b+=bucket(x,140,300,300,lay,f'k{i}')
    b+=T(x+150,490,c,20,500,GREY)
# skill tags on rim of 3rd
for j,(lab,col) in enumerate([('adatta-schede',BLUE),('lessico-caa','#fff'),('suoni-gn-gl','#fff')]):
    tx=795+j*122
    b+=f'<line x1="{tx+56}" y1="122" x2="{tx+56}" y2="140" stroke="{INK}" stroke-width="2"/>'
    b+=f'<rect x="{tx}" y="84" width="112" height="38" rx="8" fill="{col}" stroke="{INK}" stroke-width="2.5"/>'
    b+=T(tx+56,109,lab,14,700,'#fff' if col==BLUE else INK)
files['percorso.svg']=svg(1200,520,b)

# 3 gem: cosa entra a ogni risposta
b=''
b+=box(40,40,330,150)+gear(115,115,26)+T(170,110,'Istruzioni',24,800,anchor='start')+T(170,140,'scritte una volta',18,400,GREY,'start')
b+=box(435,40,330,150)+f'<circle cx="510" cy="115" r="42" fill="{LILAC}" stroke="{INK}" stroke-width="3"/>'+doc(490,88,0.9)+T(570,110,'Conoscenza',24,800,anchor='start')+T(570,140,'file dei profili',18,400,GREY,'start')
b+=box(830,40,330,150)+bubble(870,80,80,60)+T(970,110,'Richiesta',24,800,anchor='start')+T(970,140,'scritta ogni volta',18,400,GREY,'start')
for cx in (205,600,995): b+=arrow(cx,195,cx,290)
b+=box(40,300,1120,110,PAPER,18)
b+=f'<rect x="56" y="316" width="430" height="78" rx="10" fill="{LIME}" stroke="{INK}" stroke-width="2.5"/>'+T(271,363,'istruzioni',21,700)
b+=f'<rect x="494" y="316" width="430" height="78" rx="10" fill="{LILAC}" stroke="{INK}" stroke-width="2.5"/>'+T(709,363,'conoscenza',21,700)
b+=f'<rect x="932" y="316" width="212" height="78" rx="10" fill="{GREEN}" stroke="{INK}" stroke-width="2.5"/>'+T(1038,363,'richiesta',21,700)
b+=T(600,450,'Il contesto a ogni risposta: tutto il Gem entra sempre',20,500,GREY)
files['gem.svg']=svg(1200,480,b)

# 4 skill: tre livelli
b=''
b+=bucket(70,190,320,300,[(0.2,GREEN,'richiesta'),(0.25,BLUE,'istruzioni')],'sk')
tags=[('adatta-schede',BLUE),('lessico-caa','#fff'),('suoni-gn-gl','#fff'),('rubrica-voti','#fff')]
for j,(lab,col) in enumerate(tags):
    tx=20+j*112
    b+=f'<rect x="{tx}" y="60" width="104" height="38" rx="8" fill="{col}" stroke="{INK}" stroke-width="2.5"/>'+T(tx+52,85,lab,13,700,'#fff' if col==BLUE else INK)
    b+=f'<line x1="{tx+52}" y1="98" x2="{min(max(tx+52,90),370)}" y2="186" stroke="{INK}" stroke-width="2" stroke-dasharray="5 5"/>'
b+=doc(400,330,1.1,PAPER).replace('stroke-width="3"','stroke-width="3" stroke-dasharray="7 6"',1)+T(425,420,'file',17,600,GREY)
b+=arrow(398,350,365,350,True)
lv=[('1','Nome e descrizione','sempre, per tutte le skill'),('2','Istruzioni complete','solo se la skill serve'),('3','File allegati','solo quando servono')]
for i,(n,a,c) in enumerate(lv):
    y=90+i*140
    b+=f'<circle cx="600" cy="{y+40}" r="30" fill="{[LIME,BLUE,SKY][i]}" stroke="{INK}" stroke-width="3"/>'+T(600,y+49,n,26,800,'#fff' if i==1 else INK)
    b+=T(655,y+35,a,26,800,anchor='start')+T(655,y+68,c,20,400,GREY,'start')
files['skill.svg']=svg(1100,520,b)

# 5 caa: architettura della pagina
b=''
b+=box(30,120,220,250)+T(140,165,'Lista',22,800)
for i,w in enumerate(['voglio','ancora','bere','succo']): b+=T(60,215+i*40,w,20,500,anchor='start')
b+=arrow(255,245,330,245)
b+=box(340,90,330,310)+f'<rect x="340" y="90" width="330" height="44" rx="16" fill="{SKY}" stroke="{INK}" stroke-width="3"/>'
for i,c in enumerate(['#ff5f57','#febc2e','#28c840']): b+=f'<circle cx="{368+i*22}" cy="112" r="7" fill="{c}" stroke="{INK}" stroke-width="1.5"/>'
b+=T(505,200,'Pagina Canvas',24,800)+T(505,232,'scritta da Gemini',18,400,GREY)
for i in range(2):
    for j in range(3): b+=f'<rect x="{395+j*75}" y="{270+i*55}" width="60" height="44" rx="6" fill="{[LIME,ORANGE,LILAC,GREEN,PINK,SKY][i*3+j]}" stroke="{INK}" stroke-width="2"/>'
b+=box(340,470,330,120,LIME)+T(505,520,'API ARASAAC',24,800)+T(505,552,'parola → pittogramma',18,500)
b+=arrow(460,405,460,465)+arrow(550,465,550,405)
b+=T(440,440,'cerca',16,600,GREY,'end')+T(570,440,'immagine',16,600,GREY,'start')
b+=arrow(675,245,760,245)
b+=box(770,120,190,250)
for i in range(2):
    for j in range(2): b+=f'<rect x="{795+j*75}" y="{150+i*95}" width="65" height="80" rx="6" fill="#fff" stroke="{INK}" stroke-width="2.5"/>'
b+=T(865,355,'Griglia',20,800)
b+=arrow(965,245,1035,245)
b+=doc(1048,205,1.4,'#fff')+T(1079,320,'PDF',22,800)
files['caa.svg']=svg(1140,610,b)

for k,v in files.items(): open(os.path.join(OUT,k),'w').write(v)
print(list(files))

# 6 api: due domande, due risposte
MONO='font-family="JetBrains Mono, Menlo, monospace"'
def browser(x,y,w,h,title):
    o=box(x,y,w,h)+f'<path d="M{x} {y+16} q0 -16 16 -16 h{w-32} q16 0 16 16 v28 h{-w} z" fill="{SKY}" stroke="{INK}" stroke-width="3"/>'
    o+=''.join(f'<circle cx="{x+26+i*22}" cy="{y+22}" r="7" fill="{c}" stroke="{INK}" stroke-width="1.5"/>' for i,c in enumerate(['#ff5f57','#febc2e','#28c840']))
    return o+T(x+w/2,y+h/2+20,title,24,800)
def apple(cx,cy,r=34):
    return (f'<path d="M{cx} {cy-r*0.55} C{cx-r*1.3} {cy-r*1.25} {cx-r*1.45} {cy+r*0.9} {cx-r*0.35} {cy+r} C{cx-r*0.1} {cy+r*1.05} {cx+r*0.1} {cy+r*1.05} {cx+r*0.35} {cy+r} C{cx+r*1.45} {cy+r*0.9} {cx+r*1.3} {cy-r*1.25} {cx} {cy-r*0.55} Z" fill="#ff4d4d" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
            f'<path d="M{cx} {cy-r*0.55} q2 -{r*0.5} {r*0.25} -{r*0.7}" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
            f'<path d="M{cx+r*0.12} {cy-r*0.95} q{r*0.55} -{r*0.4} {r*0.8} -{r*0.05} q-{r*0.45} {r*0.35} -{r*0.8} {r*0.05} z" fill="{GREEN}" stroke="{INK}" stroke-width="2.5"/>')
b=''
b+=browser(30,40,250,480,'La pagina')
b+=box(920,40,250,480,LIME)+T(1045,270,'ARASAAC',26,800)+T(1045,302,'server',18,500)
def chip(x,y,w,txt,size=15,fill=PAPER):
    return f'<rect x="{x}" y="{y}" width="{w}" height="40" rx="10" fill="{fill}" stroke="{INK}" stroke-width="2.5"/><text x="{x+w/2}" y="{y+26}" font-size="{size}" font-weight="600" fill="{INK}" text-anchor="middle" {MONO}>{txt}</text>'
b+=T(600,72,'1 · Domanda: cerca "mela"',19,700)
b+=arrow(290,105,905,105)+chip(330,118,540,'api.arasaac.org/v1/pictograms/it/search/mela',14)
b+=arrow(910,215,295,215)+chip(400,228,400,'[{"_id": 2462, … "keyword": "mela" …}]',14,SKY)
b+=T(600,292,'risposta: testo con i dati',16,500,GREY)
b+=T(600,342,"2 · Domanda: l'immagine numero 2462",19,700)
b+=arrow(290,375,905,375)+chip(355,388,490,'static.arasaac.org/pictograms/2462/2462_500.png',13)
b+=arrow(910,470,295,470)+apple(600,470,22).replace('','')
b+=T(600,515,"risposta: l'immagine",16,500,GREY)
files={'api.svg':svg(1200,540,b)}

# 7 pubblicazione su GitHub Pages
b=''
steps=[('Canvas','Esporta → Scarica codice',SKY),('GitHub','un repository con index.html',LILAC),('GitHub Pages','pubblica il file come sito',GREEN),('Indirizzo','da condividere e stampare',LIME)]
for i,(t,c,col) in enumerate(steps):
    x=30+i*292
    b+=box(x,60,250,250)+f'<circle cx="{x+125}" cy="140" r="48" fill="{col}" stroke="{INK}" stroke-width="3"/>'
    b+=T(x+125,240,t,24,800)+T(x+125,272,c,16,500,GREY)
    if i<3: b+=arrow(x+256,185,x+286,185)
# icone
b+=f'<text x="155" y="152" font-size="30" font-weight="800" text-anchor="middle" {MONO}>&lt;/&gt;</text>'
b+=f'<path d="M418 118 h28 l8 10 h34 v42 h-70 z" fill="#fff" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
b+=f'<circle cx="739" cy="140" r="26" fill="#fff" stroke="{INK}" stroke-width="3"/><ellipse cx="739" cy="140" rx="11" ry="26" fill="none" stroke="{INK}" stroke-width="2.5"/><line x1="713" y1="140" x2="765" y2="140" stroke="{INK}" stroke-width="2.5"/>'
b+=f'<rect x="990" y="127" width="70" height="26" rx="13" fill="#fff" stroke="{INK}" stroke-width="3"/><circle cx="1004" cy="140" r="5" fill="{INK}"/>'
b+=chip(330,340,540,'username.github.io/creazioni-canvas/',17)
b+=T(600,410,"L'indirizzo della pagina pubblicata",17,500,GREY)
files['pubblicazione.svg']=svg(1200,430,b)
for k,v in files.items(): open(os.path.join(OUT,k),'w').write(v)
print(list(files))

# 8 canvas: documento e app
b=''
b+=T(300,40,'Documento',28,800)+T(900,40,'App',28,800)
b+=box(150,70,300,220)
for i,wd in enumerate([220,240,200,230,150]): b+=f'<rect x="185" y="{105+i*32}" width="{wd}" height="14" rx="7" fill="#ddd"/>'
b+=f'<rect x="185" y="105" width="140" height="18" rx="6" fill="{INK}"/>'
b+=browser(750,70,300,220,'')
for i in range(2):
    for j in range(3): b+=f'<rect x="{790+j*78}" y="{150+i*62}" width="62" height="48" rx="8" fill="{[LIME,ORANGE,LILAC,GREEN,PINK,SKY][i*3+j]}" stroke="{INK}" stroke-width="2"/>'
b+=T(300,325,'testo da leggere e modificare',18,500,GREY)+T(900,325,'pagina che si usa: tocchi, giochi, calcoli',18,500,GREY)
for i,(t,col) in enumerate([('Esporta in Documenti',SKY),('Presentazioni o PDF',SKY),('Copia contenuti',SKY)]):
    y=360+i*58; b+=arrow(300,y-12 if i==0 else y-14,300,y-2) if False else ''
    b+=f'<rect x="150" y="{y}" width="300" height="44" rx="12" fill="{col}" stroke="{INK}" stroke-width="2.5"/>'+T(300,y+29,t,18,700)
for i,(t,col) in enumerate([('Link di condivisione',LIME),('Classroom',LIME),('Codice → GitHub Pages',LIME)]):
    y=360+i*58
    b+=f'<rect x="750" y="{y}" width="300" height="44" rx="12" fill="{col}" stroke="{INK}" stroke-width="2.5"/>'+T(900,y+29,t,18,700)
b+=f'<line x1="600" y1="20" x2="600" y2="520" stroke="{INK}" stroke-width="2" stroke-dasharray="8 8"/>'
files={'canvas-modi.svg':svg(1200,540,b)}
for k,v in files.items(): open(os.path.join(OUT,k),'w').write(v)
print(list(files))

# 9 il mio sito: indice e pagine
b=''
b+=browser(40,40,420,440,'')
b+=chip(60,100,380,'username.github.io/creazioni-canvas/',14,SKY)
b+=T(250,180,'index.html',22,800)+T(250,206,'la pagina indice',16,500,GREY)
cards=[('Memory dell\'autunno',LIME),('Ruota dell\'autunno',LILAC),('…',PAPER)]
for i,(t,col) in enumerate(cards):
    y=235+i*72
    b+=f'<rect x="90" y="{y}" width="320" height="56" rx="12" fill="{col}" stroke="{INK}" stroke-width="2.5"/>'+T(250,y+36,t,19,700)
pages=[('memory_dell_autunno.html',LIME,90),('ruota_dell_autunno.html',LILAC,300)]
for i,(f,col,y) in enumerate(pages):
    b+=browser(740,y,420,170,'')+T(950,y+110,f,20,800)
    b+=f'<rect x="770" y="{y+130}" width="360" height="12" rx="6" fill="{col}"/>'
    b+=arrow(415,263+i*72,732,y+95)
b+=T(950,530,'un file per ogni pagina fatta con Canvas',17,500,GREY)
b+=T(250,530,"l'indice porta alle pagine",17,500,GREY)
files={'sito.svg':svg(1200,560,b)}
for k,v in files.items(): open(os.path.join(OUT,k),'w').write(v)
print(list(files))
