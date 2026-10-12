// Test video: dati e spiegazioni.
// Fonte: Stuart A. Thompson, "A.I. Videos Have Never Been Better. Can You Tell What's Real?",
// The New York Times, 29 giugno 2025. I video AI sono stati generati dal NYT con Google Veo 3.
window.QUIZ = window.QUIZ || {};
window.QUIZ.video = {
  titolo: 'Reale o AI? I video',
  tipo: 'video',
  nome: 'Video',
  istruzioni: 'Dieci video brevi, alcuni reali e alcuni generati con l\'intelligenza artificiale. Attiva l\'audio: quasi tutti hanno dialoghi. Per ogni video scegli AI oppure Reale. Le soluzioni arrivano alla fine.',
  fonte: 'Video e soluzioni: Stuart A. Thompson, «A.I. Videos Have Never Been Better. Can You Tell What\'s Real?», The New York Times, 29 giugno 2025.',
  lezioni: [
    'Ogni video falso ha richiesto pochi minuti: un prompt breve e, a volte, un copione di massima. Persone, vestiti, luci, voci ed effetti sonori li ha decisi il modello.',
    'Il testo dentro l\'immagine resta un punto debole: scritte storpiate o illeggibili sono uno degli indizi più affidabili, per ora.',
    'La bassa qualità aiuta il falso: un video sgranato "da cellulare" nasconde i difetti e sembra più spontaneo.',
    'I difetti si correggono ripetendo la richiesta: l\'occhio umano non è un metodo di verifica. Serve risalire alla fonte.'
  ],
  items: [
    {
      file: 'media/video/video-01.mp4', poster: 'media/video/video-01.jpg',
      domanda: 'Una conferenza',
      risposta: 'AI',
      spiegazione: [
        'Generato con Google Veo 3 a partire da un prompt di una decina di righe che descriveva tutto: un uomo sui 40 anni con barba e occhiali, un po\' nervoso, abito color cammello senza cravatta, fondo nero e cerchio rosso sul pavimento.',
        'Anche il discorso è scritto nel prompt: parla del sonno e di come il cervello riordina i ricordi. La voce e l\'eco della sala sono generate.',
        'Lo stile TED è facile da imitare perché è presentissimo nei dati di addestramento: inquadratura, luci e gesti sono sempre gli stessi.'
      ],
      prompt: 'In un prompt di circa 10 righe: età, aspetto, abito, scenografia, tono un po\' nervoso e argomento del discorso.'
    },
    {
      file: 'media/video/video-02.mp4', poster: 'media/video/video-02.jpg',
      domanda: 'Una modella con i palloncini',
      risposta: 'Reale',
      spiegazione: [
        'Video reale, pubblicato su Instagram da Gökhan Ergin, fotografo di Istanbul.',
        'Una scena molto curata e "da cartolina" può sembrare artificiale, ma non lo è: la perfezione estetica non è un indizio di AI.'
      ]
    },
    {
      file: 'media/video/video-03.mp4', poster: 'media/video/video-03.jpg',
      domanda: 'Un telegiornale',
      risposta: 'AI',
      spiegazione: [
        'Telegiornale inventato: i nomi dei due conduttori e la notizia del crollo delle borse sono stati scritti nel prompt.',
        'Indizio: nel 2025 le clip di Veo duravano pochi secondi, quindi il video si interrompe prima che la conduttrice finisca di dare la notizia scritta nel prompt.',
        'È il caso che preoccupa di più chi si occupa di disinformazione: un notiziario credibile, con studio, grafiche e conduttori, si produce in pochi minuti.'
      ],
      prompt: 'Lo studio di un telegiornale nazionale, due conduttori sui 40 anni, le loro battute parola per parola.'
    },
    {
      file: 'media/video/video-04.mp4', poster: 'media/video/video-04.jpg',
      domanda: 'Un influencer in cammino',
      risposta: 'AI',
      spiegazione: [
        'Imita una serie YouTube vera, quella di un ragazzo che va a piedi dal Regno Unito al Vietnam.',
        'Il prompt chiedeva apposta un video "ultrarealistico, di bassa qualità, girato con l\'iPhone, verticale per TikTok". La qualità bassa è una scelta: rende il video più spontaneo e nasconde i difetti.',
        'Anche il modo di parlare, enfatico come quello di un influencer, era descritto nel prompt.'
      ],
      prompt: 'Un ragazzo sui 20 anni che si riprende col cellulare mentre cammina su una strada sterrata, accento britannico, tatuaggio sul braccio sinistro, sole forte.'
    },
    {
      file: 'media/video/video-05.mp4', poster: 'media/video/video-05.jpg',
      domanda: 'Un video notturno',
      risposta: 'Reale',
      spiegazione: [
        'Video reale, girato da Romualdas Šapoka, youtuber lituano, durante un\'escursione di tre giorni nella foresta amazzonica.',
        'Buio, inquadratura instabile e immagine sgranata fanno pensare a un falso, ma sono semplicemente le condizioni di ripresa. Gli stessi indizi possono valere in un senso e nell\'altro.'
      ]
    },
    {
      file: 'media/video/video-06.mp4', poster: 'media/video/video-06.jpg',
      domanda: 'L\'intervista a un cestista',
      risposta: 'AI',
      spiegazione: [
        'Imita alla perfezione un\'intervista sportiva: pubblico che esce, allenatori, un giocatore sudato che risponde a fatica.',
        'Guardando con attenzione emergono i difetti: alcune persone sullo sfondo compaiono e scompaiono, e le lettere sulla maglia del giocatore sono storpiate.',
        'Il testo dentro l\'immagine è ancora uno dei punti deboli dei generatori. È lo stesso errore della falsa Bustina di Eco: la stringa senza senso sotto la M.'
      ],
      prompt: 'Un\'intervista televisiva a un cestista universitario alto più di due metri, con il pubblico che lascia l\'arena e la sua risposta già scritta.'
    },
    {
      file: 'media/video/video-07.mp4', poster: 'media/video/video-07.jpg',
      domanda: 'Un tutorial di trucco',
      risposta: 'AI',
      spiegazione: [
        'Il prompt era una sola frase: «Una giovane donna fa un tutorial di trucco». Viso, prodotti, stanza, voce e parole li ha decisi il modello, pescando da ciò che ha visto nei dati di addestramento.',
        'Nelle prime versioni il fard "brillava" sul viso. Ripetendo la richiesta il difetto è sparito: i segni del falso non sono una garanzia.',
        'Il rischio, secondo il NYT: social pieni di influencer artificiali, un po\' troppo perfetti.'
      ],
      prompt: 'A young woman gives a makeup tutorial.'
    },
    {
      file: 'media/video/video-08.mp4', poster: 'media/video/video-08.jpg',
      domanda: 'Un video di moda',
      risposta: 'Reale',
      spiegazione: [
        'Video reale, di Ivy Thompson, che sul canale YouTube «The Sewlo Artist» pubblica video su abiti vintage.',
        'Formato verticale, luce morbida, ragazza che parla in camera: è lo stesso stile dei video generati, perché i generatori imparano proprio da video come questo.'
      ]
    },
    {
      file: 'media/video/video-09.mp4', poster: 'media/video/video-09.jpg',
      domanda: 'Consigli sulle criptovalute',
      risposta: 'Reale',
      spiegazione: [
        'Video reale, di Alex Becker, youtuber che parla di investimenti in criptovalute.',
        'Il NYT lo ha incluso per un motivo: il mondo delle cripto è un bersaglio ideale per truffe con l\'AI, con finti testimonial e falso sostegno sui social. In Italia è successo con i video falsi di Meloni e Mentana.'
      ]
    },
    {
      file: 'media/video/video-10.mp4', poster: 'media/video/video-10.jpg',
      domanda: 'La diretta di un videogioco',
      risposta: 'AI',
      spiegazione: [
        'Tutto è generato: sia il videogioco, in stile seconda guerra mondiale, sia il ragazzo nel riquadro in basso.',
        'Nessun copione: il prompt chiedeva solo che il ragazzo parlasse della sua strategia. Le battute le ha inventate il modello.',
        'Il modello ha messo insieme elementi diversi (gioco, riquadro, voce, espressione annoiata) in modo coerente.'
      ],
      prompt: 'La diretta di un videogioco di guerra con lo streamer in un riquadro in basso a destra: un ragazzino annoiato che risponde alle domande sulla sua strategia.'
    },
    {
      // Clip di Zach King, tagliata dal file originale (01-fonti-esterne/assets/zachking.mov)
      attivo: true,
      file: 'media/video/video-11.mp4', poster: 'media/video/video-11.jpg',
      domanda: 'Una partita a minigolf',
      risposta: 'Reale',
      spiegazione: [
        'Nessuna intelligenza artificiale: è un video di Zach King, filmmaker statunitense diventato famoso su Vine, e poi su YouTube, Instagram e TikTok, per la sua "magia digitale".',
        'Le riprese sono reali: le palline da golf che si rompono come uova e diventano pulcini sono il risultato di oggetti diversi, tagli di montaggio nascosti dietro i movimenti ed effetti aggiunti dopo. Pochi secondi di video richiedono pianificazione, prove, riprese e post-produzione.',
        'Reale non vuol dire vero: il video è manipolato quanto uno generato. La differenza è nel lavoro e nella competenza necessari, ed è la stessa domanda della linea del tempo dei falsi: cosa serviva per farlo?'
      ]
    },
    {
      // Clip dal file originale 01-fonti-esterne/assets/redbull.mov (registrazione di un reel)
      file: 'media/video/video-12.mp4', poster: 'media/video/video-12.jpg',
      domanda: 'Un volo in galleria',
      risposta: 'Reale',
      spiegazione: [
        'Video reale: il 4 settembre 2021 il pilota acrobatico italiano Dario Costa ha attraversato in volo le due gallerie di Çatalca, sull\'autostrada vicino a Istanbul, con un aereo da corsa modificato. Il volo è durato circa 43 secondi.',
        'Ha stabilito il record Guinness per la galleria più lunga attraversata in aereo. Dietro c\'è più di un anno di preparazione con un team Red Bull.',
        'Sembra generato perché è straordinario: dopo anni di contenuti AI tendiamo a sospettare anche del vero. Chi crea falsi ci guadagna due volte, perché anche le immagini autentiche diventano contestabili.',
        'La scritta in sovrimpressione l\'ha aggiunta chi ha ripubblicato il video, senza citare la fonte: il primo passo della verifica resta risalire all\'originale.'
      ]
    }
  ]
};
