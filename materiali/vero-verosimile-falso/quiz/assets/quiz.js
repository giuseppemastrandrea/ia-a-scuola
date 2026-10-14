// Motore comune: carica i dati del test indicato in ?test=, poi avvia la pagina richiesta.
(function () {
  var TESTS = ['video'];

  function param(name) {
    return new URLSearchParams(location.search).get(name);
  }

  function el(tag, attrs, children) {
    var n = document.createElement(tag);
    Object.keys(attrs || {}).forEach(function (k) {
      if (k === 'text') n.textContent = attrs[k];
      else if (k === 'class') n.className = attrs[k];
      else n.setAttribute(k, attrs[k]);
    });
    (children || []).forEach(function (c) { if (c) n.appendChild(c); });
    return n;
  }

  function loadTest(name, cb) {
    if (TESTS.indexOf(name) === -1) { cb(null); return; }
    var s = document.createElement('script');
    s.src = 'data/' + name + '.js';
    s.onload = function () {
      var data = window.QUIZ && window.QUIZ[name];
      // Gli elementi con attivo: false restano nei dati ma non entrano nel test
      if (data) data.items = data.items.filter(function (it) { return it.attivo !== false; });
      cb(data);
    };
    s.onerror = function () { cb(null); };
    document.head.appendChild(s);
  }

  function media(data, item, controls) {
    if (data.tipo === 'video') {
      var v = el('video', { src: item.file, poster: item.poster || '', preload: 'metadata', playsinline: '' });
      if (controls) v.controls = true;
      return el('div', { class: 'media' }, [v]);
    }
    return el('div', { class: 'media' }, [el('img', { src: item.file, alt: '' })]);
  }

  function notFound(root) {
    root.innerHTML = '';
    root.appendChild(el('h1', { text: 'Test non trovato' }));
    root.appendChild(el('p', {}, [el('a', { href: 'index.html', text: 'Torna alla pagina iniziale' })]));
  }

  // Pagina del quiz
  function runQuiz(root, name, data) {
    var answers = [];
    var i = 0;
    var total = data.items.length;
    document.title = data.titolo;

    function intro() {
      root.innerHTML = '';
      root.appendChild(el('p', { class: 'label', text: total + ' ' + (data.tipo === 'video' ? 'video' : 'immagini') }));
      root.appendChild(el('h1', { text: data.titolo }));
      root.appendChild(el('p', { class: 'lead', text: data.istruzioni }));
      var start = el('button', { class: 'btn primary', type: 'button', text: 'Inizia' });
      start.style.font = 'inherit';
      start.style.fontWeight = '600';
      start.style.cursor = 'pointer';
      start.addEventListener('click', step);
      root.appendChild(el('div', { class: 'actions' }, [start]));
    }

    function step() {
      if (i >= total) {
        location.href = 'risultati.html?test=' + name + '&a=' + answers.join('');
        return;
      }
      var item = data.items[i];
      root.innerHTML = '';
      root.appendChild(el('p', { class: 'label', text: data.nome + ' ' + (i + 1) + ' di ' + total }));
      var bar = el('div', { class: 'progress' }, [el('div', {})]);
      bar.firstChild.style.width = (i / total * 100) + '%';
      root.appendChild(bar);
      root.appendChild(el('h2', { text: item.domanda }));
      root.appendChild(media(data, item, true));
      if (data.tipo === 'video') root.appendChild(el('p', { class: 'small hint', text: 'Attiva l\'audio. Puoi rivederlo quante volte vuoi.' }));
      var ai = el('button', { type: 'button', text: 'AI' });
      var real = el('button', { type: 'button', text: 'Reale' });
      ai.addEventListener('click', function () { answer('A'); });
      real.addEventListener('click', function () { answer('R'); });
      root.appendChild(el('div', { class: 'choices' }, [ai, real]));
      window.scrollTo(0, 0);
    }

    function answer(a) {
      var v = root.querySelector('video');
      if (v) v.pause();
      answers.push(a);
      i++;
      step();
    }

    intro();
  }

  // Pagina dei risultati
  function runResults(root, name, data) {
    var a = (param('a') || '').toUpperCase();
    var total = data.items.length;
    document.title = 'Risultati: ' + data.titolo;
    if (a.length !== total || /[^AR]/.test(a)) {
      root.innerHTML = '';
      root.appendChild(el('h1', { text: 'Nessun risultato' }));
      root.appendChild(el('p', { text: 'Per vedere i risultati bisogna completare il test.' }));
      root.appendChild(el('div', { class: 'actions' }, [el('a', { class: 'btn primary', href: 'quiz.html?test=' + name, text: 'Fai il test' })]));
      return;
    }

    var ok = 0, aiTot = 0, aiOk = 0, realTot = 0, realOk = 0;
    data.items.forEach(function (it, k) {
      var right = (it.risposta === 'AI' ? 'A' : 'R') === a[k];
      if (right) ok++;
      if (it.risposta === 'AI') { aiTot++; if (right) aiOk++; } else { realTot++; if (right) realOk++; }
    });

    root.innerHTML = '';
    root.appendChild(el('p', { class: 'label', text: 'Risultati' }));
    root.appendChild(el('h1', { text: data.titolo }));
    var score = el('p', { class: 'score' });
    score.appendChild(document.createTextNode(ok));
    score.appendChild(el('span', { text: ' su ' + total }));
    root.appendChild(score);
    root.appendChild(el('div', { class: 'breakdown' }, [
      el('div', {}, [el('b', { text: aiOk + ' su ' + aiTot }), document.createTextNode('falsi riconosciuti')]),
      el('div', {}, [el('b', { text: realOk + ' su ' + realTot }), document.createTextNode('reali riconosciuti')])
    ]));

    data.items.forEach(function (it, k) {
      var mine = a[k] === 'A' ? 'AI' : 'Reale';
      var right = mine === it.risposta;
      var box = el('section', { class: 'item' });
      box.appendChild(el('div', { class: 'item-head' }, [
        el('h2', { text: (k + 1) + '. ' + it.domanda }),
        el('span', { class: 'verdict ' + (it.risposta === 'AI' ? 'ai' : 'real'), text: it.risposta === 'AI' ? 'Generato con AI' : 'Reale' })
      ]));
      box.appendChild(media(data, it, true));
      box.appendChild(el('p', { class: 'mine ' + (right ? 'ok' : 'ko'), text: (right ? 'Giusto: ' : 'Sbagliato: ') + 'hai risposto ' + mine + '.' }));
      box.appendChild(el('ul', {}, it.spiegazione.map(function (s) { return el('li', { text: s }); })));
      if (it.prompt) box.appendChild(el('p', { class: 'prompt', text: 'Il prompt: ' + it.prompt }));
      root.appendChild(box);
    });

    if (data.lezioni && data.lezioni.length) {
      root.appendChild(el('section', { class: 'lessons' }, [
        el('h2', { text: 'Cosa ci insegna' }),
        el('ul', {}, data.lezioni.map(function (s) { return el('li', { text: s }); }))
      ]));
    }

    root.appendChild(el('div', { class: 'actions' }, [
      el('a', { class: 'btn', href: 'quiz.html?test=' + name, text: 'Rifai il test' }),
      el('a', { class: 'btn primary', href: 'index.html', text: 'Torna ai test' })
    ]));
    if (data.fonte) root.appendChild(el('footer', {}, [el('p', { class: 'small', text: data.fonte })]));

    // Un solo video alla volta
    root.addEventListener('play', function (e) {
      root.querySelectorAll('video').forEach(function (v) { if (v !== e.target) v.pause(); });
    }, true);
  }

  // Home: disattiva i test ancora vuoti
  function runHome() {
    document.querySelectorAll('[data-test]').forEach(function (card) {
      var name = card.getAttribute('data-test');
      loadTest(name, function (data) {
        var n = card.querySelector('[data-count]');
        if (!data || !data.items.length) {
          card.classList.add('off');
          card.removeAttribute('href');
          if (n) n.textContent = 'In preparazione';
        } else if (n) {
          n.textContent = data.items.length + ' ' + (data.tipo === 'video' ? 'video' : 'immagini');
        }
      });
    });
  }

  window.startPage = function (page) {
    var root = document.getElementById('app');
    if (page === 'home') { runHome(); return; }
    var name = param('test');
    loadTest(name, function (data) {
      if (!data || !data.items.length) { notFound(root); return; }
      if (page === 'quiz') runQuiz(root, name, data);
      else runResults(root, name, data);
    });
  };
})();
