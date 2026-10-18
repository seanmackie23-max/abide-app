/* The cathedral: what makes Rose Window feel like a great church rather than a page.
   Sound (a stone nave's echo, the bell, the doors, the hush), the great west doors you open each day, coloured light that moves
   through the hours, candles, sitting in silence, and your own rose window, filled one day at a time.
   Everything is drawn or synthesised on the device: no recordings, no images to download, nothing to license. */
var CATH = (function () {
  /* ---------- Sound ---------- */
  var ctx = null, master = null, verb = null, wet = null, dry = null;
  function soundOn() { try { return store.sound !== false; } catch (e) { return true; } }
  function ac() {
    if (ctx) { if (ctx.state === "suspended") ctx.resume(); return ctx; }
    var A = window.AudioContext || window.webkitAudioContext; if (!A) return null;
    ctx = new A(); master = ctx.createGain(); master.gain.value = .9; master.connect(ctx.destination);
    // a stone nave: about five seconds of echo, darker as it fades
    var len = Math.floor(ctx.sampleRate * 5.2), ir = ctx.createBuffer(2, len, ctx.sampleRate);
    for (var ch = 0; ch < 2; ch++) { var d = ir.getChannelData(ch), lp = 0;
      for (var i = 0; i < len; i++) { var t = i / ctx.sampleRate, k = .55 - .45 * Math.min(1, t / 4.5); lp = lp * k + (Math.random() * 2 - 1) * (1 - k); d[i] = lp * Math.pow(1 - i / len, 2.4) * (t < .02 ? t / .02 : 1); } }
    verb = ctx.createConvolver(); verb.buffer = ir; wet = ctx.createGain(); wet.gain.value = .9; dry = ctx.createGain(); dry.gain.value = .55;
    verb.connect(wet); wet.connect(master); dry.connect(master);
    return ctx;
  }
  function out(node, wetAmt) { var g1 = ctx.createGain(), g2 = ctx.createGain(); g1.gain.value = 1 - (wetAmt || .5) * .6; g2.gain.value = wetAmt || .5; node.connect(g1); g1.connect(dry); node.connect(g2); g2.connect(verb); }
  function noiseBuf(sec) { var b = ctx.createBuffer(1, Math.floor(ctx.sampleRate * sec), ctx.sampleRate), d = b.getChannelData(0), p = 0; for (var i = 0; i < d.length; i++) { p = .97 * p + .03 * (Math.random() * 2 - 1); d[i] = p * 6; } return b; }
  // the bell: a bronze bell's partials, ringing into the nave
  function bell(strength) {
    if (!soundOn() || !ac()) return; var now = ctx.currentTime, base = 293.66, s = strength || 1;
    [[0.5, .5], [1, .9], [1.183, .55], [1.506, .4], [2, .35], [2.514, .2], [2.662, .14], [3.011, .1]].forEach(function (p, i) {
      var o = ctx.createOscillator(), g = ctx.createGain(); o.type = "sine"; o.frequency.value = base * p[0];
      g.gain.setValueAtTime(0, now); g.gain.linearRampToValueAtTime(p[1] * .1 * s, now + .008); g.gain.exponentialRampToValueAtTime(.0001, now + 7 - i * .6);
      o.connect(g); out(g, .55); o.start(now); o.stop(now + 7.2); });
  }
  // the great doors: the latch, the slow swing of heavy oak, and the boom as the nave answers
  function doors() {
    if (!soundOn() || !ac()) return; var now = ctx.currentTime;
    var latch = ctx.createBufferSource(); latch.buffer = noiseBuf(.12); var lf = ctx.createBiquadFilter(); lf.type = "bandpass"; lf.frequency.value = 1400; lf.Q.value = 2;
    var lg = ctx.createGain(); lg.gain.setValueAtTime(.5, now); lg.gain.exponentialRampToValueAtTime(.001, now + .1); latch.connect(lf).connect(lg); out(lg, .6); latch.start(now);
    var cr = ctx.createOscillator(); cr.type = "sawtooth"; cr.frequency.setValueAtTime(118, now + .25); cr.frequency.linearRampToValueAtTime(84, now + 1.5);
    var cf = ctx.createBiquadFilter(); cf.type = "bandpass"; cf.frequency.value = 900; cf.Q.value = 7;
    var cg = ctx.createGain(); cg.gain.setValueAtTime(0, now); cg.gain.linearRampToValueAtTime(.05, now + .4); cg.gain.linearRampToValueAtTime(.035, now + 1.1); cg.gain.linearRampToValueAtTime(0, now + 1.55);
    var trem = ctx.createOscillator(), tg = ctx.createGain(); trem.frequency.value = 23; tg.gain.value = .025; trem.connect(tg).connect(cg.gain);
    cr.connect(cf).connect(cg); out(cg, .5); cr.start(now + .25); cr.stop(now + 1.6); trem.start(now + .25); trem.stop(now + 1.6);
    var air = ctx.createBufferSource(); air.buffer = noiseBuf(2.6); var af = ctx.createBiquadFilter(); af.type = "lowpass"; af.frequency.value = 500;
    var ag = ctx.createGain(); ag.gain.setValueAtTime(0, now + .3); ag.gain.linearRampToValueAtTime(.16, now + 1.2); ag.gain.linearRampToValueAtTime(0, now + 2.6); air.connect(af).connect(ag); out(ag, .7); air.start(now + .3);
    var th = ctx.createOscillator(); th.type = "sine"; th.frequency.setValueAtTime(70, now + 1.5); th.frequency.exponentialRampToValueAtTime(42, now + 1.9);
    var thg = ctx.createGain(); thg.gain.setValueAtTime(0, now + 1.5); thg.gain.linearRampToValueAtTime(.32, now + 1.52); thg.gain.exponentialRampToValueAtTime(.001, now + 2.1); th.connect(thg); out(thg, .8); th.start(now + 1.5); th.stop(now + 2.2);
  }
  // a match struck, for a candle
  function strike() {
    if (!soundOn() || !ac()) return; var now = ctx.currentTime, n = ctx.createBufferSource(); n.buffer = noiseBuf(.5);
    var f = ctx.createBiquadFilter(); f.type = "highpass"; f.frequency.value = 2200; var g = ctx.createGain(); g.gain.setValueAtTime(.0, now); g.gain.linearRampToValueAtTime(.25, now + .02); g.gain.exponentialRampToValueAtTime(.001, now + .45);
    n.connect(f).connect(g); out(g, .45); n.start(now);
  }
  // the sound of the nave: stillness with distance in it, a low held chord, as if far away someone were singing
  var ambientNodes = null;
  function ambient(on) {
    if (!on) { if (ambientNodes) { var t = ctx.currentTime; ambientNodes.g.gain.cancelScheduledValues(t); ambientNodes.g.gain.setTargetAtTime(0, t, .8); var ns = ambientNodes.nodes; setTimeout(function () { ns.forEach(function (x) { try { x.stop(); } catch (e) {} }); }, 4000); ambientNodes = null; } return; }
    if (!ac() || ambientNodes) return; var now = ctx.currentTime, g = ctx.createGain(), nodes = []; g.gain.value = 0; g.gain.setTargetAtTime(1, now, 2);
    var room = ctx.createBufferSource(); room.buffer = noiseBuf(4); room.loop = true; var rf = ctx.createBiquadFilter(); rf.type = "lowpass"; rf.frequency.value = 320; var rg = ctx.createGain(); rg.gain.value = .035; room.connect(rf).connect(rg).connect(g); room.start(); nodes.push(room);
    [73.42, 110, 146.83, 185, 220].forEach(function (f, i) { var o = ctx.createOscillator(), og = ctx.createGain(), l = ctx.createOscillator(), lg = ctx.createGain();
      o.type = i % 2 ? "triangle" : "sine"; o.frequency.value = f * (1 + (i - 2) * .0009); og.gain.value = .012 / (1 + i * .35);
      l.frequency.value = .05 + i * .021; lg.gain.value = .009 / (1 + i * .35); l.connect(lg).connect(og.gain); o.connect(og).connect(g); o.start(); l.start(); nodes.push(o, l); });
    out(g, .92); ambientNodes = { g: g, nodes: nodes };
  }

  /* ---------- The great west doors ---------- */
  // geometry in a 390 x 700 box: the doorway opening is 200 wide, springing at y 330, apex at y 169
  var OX0 = 95, OX1 = 295, OY = 690, SPR = 330, R = 180, APEX = 169;
  function archPath(off) { var x0 = OX0 - off, x1 = OX1 + off, r = R + off, ay = SPR - Math.sqrt(r * r - Math.pow(195 - (x0 + r), 2));
    return "M" + x0 + " " + OY + " L" + x0 + " " + SPR + " A" + r + " " + r + " 0 0 1 195 " + ay.toFixed(1) + " A" + r + " " + r + " 0 0 1 " + x1 + " " + SPR + " L" + x1 + " " + OY + "Z"; }
  function leafSVG(side) { // side: "l" or "r"; drawn for the left leaf and mirrored for the right
    var W = 100, H = OY - APEX, sp = SPR - APEX, id = "lf" + side;
    var top = "M0 " + H + " L0 " + sp + " A" + R + " " + R + " 0 0 1 100 0 L100 " + H + "Z";
    var planks = "", tones = ["#5B3A22", "#4E311C", "#63412A", "#553620", "#4A2E1A"];
    for (var i = 0; i < 5; i++) planks += '<rect x="' + i * 20 + '" y="0" width="20" height="' + H + '" fill="' + tones[i] + '"/><rect x="' + (i * 20) + '" y="0" width="1.2" height="' + H + '" fill="#1E120A" opacity=".85"/>';
    var straps = "";
    [70, 205, 340, 465].forEach(function (y) {
      straps += '<path d="M-2 ' + y + ' H64 C76 ' + y + ' 84 ' + (y - 4) + ' 84 ' + (y - 12) + ' C84 ' + (y - 20) + ' 74 ' + (y - 22) + ' 70 ' + (y - 16) + ' M64 ' + y + ' C76 ' + y + ' 84 ' + (y + 4) + ' 84 ' + (y + 12) + ' C84 ' + (y + 20) + ' 74 ' + (y + 22) + ' 70 ' + (y + 16) + '" fill="none" stroke="#1A1714" stroke-width="7" stroke-linecap="round"/>' +
        '<path d="M-2 ' + (y - 2.4) + ' H62" stroke="#5A544C" stroke-width="1" opacity=".55"/>';
      for (var s = 8; s < 62; s += 13) straps += '<circle cx="' + s + '" cy="' + y + '" r="2.1" fill="#2A2622"/><circle cx="' + (s - .6) + '" cy="' + (y - .7) + '" r=".8" fill="#8A8178" opacity=".7"/>';
    });
    var ring = '<circle cx="90" cy="' + (H * .56) + '" r="5" fill="#1A1714"/><circle cx="90" cy="' + (H * .56 + 13) + '" r="10" fill="none" stroke="#1A1714" stroke-width="3.2"/><circle cx="89.4" cy="' + (H * .56 + 12.2) + '" r="10" fill="none" stroke="#6E665C" stroke-width=".7" opacity=".6"/>';
    var body = '<defs><clipPath id="' + id + 'c"><path d="' + top + '"/></clipPath>' +
      '<filter id="' + id + 'w" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".9 .012" numOctaves="3" seed="' + (side === "l" ? 4 : 7) + '"/><feColorMatrix type="matrix" values="0 0 0 0 .08  0 0 0 0 .05  0 0 0 0 .02  0 0 0 .7 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>' +
      '<linearGradient id="' + id + 'l" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFE2B0" stop-opacity=".16"/><stop offset=".5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".35"/></linearGradient></defs>' +
      '<g clip-path="url(#' + id + 'c)">' + planks + '<rect width="100" height="' + H + '" fill="#000" filter="url(#' + id + 'w)"/>' +
      '<path d="M0 ' + (H * .5) + ' H100" stroke="#1E120A" stroke-width="2" opacity=".6"/>' + straps + ring + '<rect width="100" height="' + H + '" fill="url(#' + id + 'l)"/></g>' +
      '<path d="' + top + '" fill="none" stroke="#140C06" stroke-width="3"/>';
    var tf = side === "r" ? ' transform="translate(100 0) scale(-1 1)"' : "";
    return '<svg viewBox="0 0 100 ' + H + '" preserveAspectRatio="none" aria-hidden="true"><g' + tf + '>' + body + '</g></svg>';
  }
  function doorwaySVG() {
    var orders = "";
    [[66, "#3A332D", "#4D453D"], [44, "#433B34", "#575047"], [22, "#4B433B", "#62594F"]].forEach(function (o) {
      orders += '<path d="' + archPath(o[0]) + '" fill="url(#dwS' + o[0] + ')" stroke="#1C1814" stroke-width="1.6"/>' +
        '<linearGradient id="dwS' + o[0] + '" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="' + o[2] + '"/><stop offset="1" stop-color="' + o[1] + '"/></linearGradient>';
    });
    // voussoirs: the wedge stones of the outer arch
    var vous = ""; for (var a = -78; a <= 78; a += 13) { var rad = (a - 90) * Math.PI / 180; }
    // colonnettes in the jambs
    var cols = ""; [[OX0 - 55, 0], [OX0 - 33, 0], [OX0 - 11, 0], [OX1 + 11, 0], [OX1 + 33, 0], [OX1 + 55, 0]].forEach(function (c) {
      cols += '<rect x="' + (c[0] - 5) + '" y="' + SPR + '" width="10" height="' + (OY - SPR) + '" fill="url(#dwC)" stroke="#1C1814" stroke-width=".8"/><rect x="' + (c[0] - 7) + '" y="' + (SPR - 8) + '" width="14" height="10" rx="2" fill="#5E554B" stroke="#1C1814" stroke-width=".8"/>'; });
    return '<svg class="dw-stone" viewBox="0 0 390 700" aria-hidden="true"><defs>' +
      '<linearGradient id="dwC" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#3B342E"/><stop offset=".4" stop-color="#6A6156"/><stop offset="1" stop-color="#2E2823"/></linearGradient>' +
      '<filter id="dwT"><feTurbulence type="fractalNoise" baseFrequency=".75" numOctaves="2" seed="5"/><feColorMatrix type="matrix" values="0 0 0 0 .5  0 0 0 0 .46  0 0 0 0 .4  0 0 0 .18 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>' +
      '<radialGradient id="dwIn" cx="50%" cy="40%" r="70%"><stop offset="0" stop-color="#FFE7B0"/><stop offset=".35" stop-color="#C98A4A"/><stop offset="1" stop-color="#2A1A12"/></radialGradient></defs>' +
      orders + '<g filter="url(#dwT)">' + orders.replace(/url\(#dwS\d+\)/g, "#000") + '</g>' + cols +
      // the opening: warm light inside, seen when the doors swing back
      '<path class="dw-inside" d="' + archPath(0) + '" fill="url(#dwIn)"/>' +
      '<g class="dw-inside-rose" transform="translate(195 260) scale(.34)">' + (window.roseSVG ? roseSVG({ glass: true, halo: false }) : "") + '</g>' +
      '<text x="195" y="70" text-anchor="middle" class="dw-carved">ROSE WINDOW</text>' +
      '<path d="M40 ' + (OY + 2) + ' H350" stroke="#1C1814" stroke-width="3"/></svg>';
  }
  function doorsHTML() {
    var L = (OX0 / 390 * 100).toFixed(3), T = (APEX / 700 * 100).toFixed(3), W = (100 / 390 * 100).toFixed(3), H = ((OY - APEX) / 700 * 100).toFixed(3), L2 = ((OX0 + 100) / 390 * 100).toFixed(3);
    return '<div class="doorway"><div class="dw-frame">' + doorwaySVG() +
      '<div class="dw-leaf dw-l" style="left:' + L + '%;top:' + T + '%;width:' + W + '%;height:' + H + '%">' + leafSVG("l") + '</div>' +
      '<div class="dw-leaf dw-r" style="left:' + L2 + '%;top:' + T + '%;width:' + W + '%;height:' + H + '%">' + leafSVG("r") + '</div></div></div>';
  }

  /* ---------- Light through the day ---------- */
  // coloured light, as if through stained glass, drifting slowly across the stone; its colour and angle follow the hour
  function lightHTML() {
    var h = new Date().getHours() + new Date().getMinutes() / 60, phase = h < 5 ? "night" : h < 10 ? "morning" : h < 14 ? "midday" : h < 17.5 ? "afternoon" : h < 21 ? "evening" : "night";
    return '<div class="nave-bg ' + phase + '" aria-hidden="true"><div class="nave-stone"></div><div class="nave-arcade"></div>' +
      '<i class="glow g1"></i><i class="glow g2"></i><i class="glow g3"></i><i class="glow g4"></i></div>';
  }
  function parallax() {
    var a = document.querySelector(".nave-arcade"); if (!a) return; var tick = false;
    window.addEventListener("scroll", function () { if (tick) return; tick = true; requestAnimationFrame(function () { a.style.transform = "translate3d(0," + (-window.scrollY * .35) + "px,0)"; tick = false; }); }, { passive: true });
  }

  /* ---------- Candles ---------- */
  function flame(cls) { return '<span class="cflame ' + (cls || "") + '" aria-hidden="true"><i></i></span>'; }
  function todaysCandles() { try { return ((store.candles || {})[dayKey()] || []); } catch (e) { return []; } }
  function lightCandle(forWhom) { store.candles = store.candles || {}; var k = dayKey(); (store.candles[k] = store.candles[k] || []).push({ f: String(forWhom || "").slice(0, 80), t: Date.now() });
    // keep a year of candles at most
    Object.keys(store.candles).sort().slice(0, -366).forEach(function (d) { delete store.candles[d]; }); save(); strike(); }
  function candleCount(year) { var n = 0; Object.keys(store.candles || {}).forEach(function (d) { if (!year || d.indexOf(year) === 0) n += store.candles[d].length; }); return n; }
  function standHTML() { // an iron stand with tiers of votive candles; only yours are lit
    var mine = todaysCandles(), rows = [7, 8, 9], k = 0, html = '<div class="stand">';
    rows.forEach(function (n, ri) { html += '<div class="tier">'; for (var i = 0; i < n; i++) { var lit = k < mine.length; html += '<span class="votive' + (lit ? " lit" : "") + '" title="' + (lit && mine[k].f ? esc(mine[k].f) : "") + '">' + (lit ? flame() : "") + '<b></b></span>'; k++; } html += '</div>'; });
    return html + '<div class="stand-rail"></div></div>';
  }

  /* ---------- Your rose window: a pane for every day of the year ---------- */
  function yearWindowSVG(year, dayInfo) {
    // twelve lancets, one per month (January at the top, the year going round clockwise), two columns of sixteen panes: a pane a day
    var P = Math.PI, s = "", lead = "", r0 = 30, r1 = 92, rows = 16, today = dayKey();
    for (var m = 0; m < 12; m++) {
      var dim = new Date(+year, m + 1, 0).getDate(), a = m * 30 - 90, half = 11.5;
      for (var d = 1; d <= 32; d++) {
        var row = Math.floor((d - 1) / 2), col = (d - 1) % 2, ra = r0 + (r1 - r0) * row / rows, rb = r0 + (r1 - r0) * (row + 1) / rows;
        var w0 = col ? 0 : -half, w1 = col ? half : 0, taper = function (r) { return r < 40 ? .6 + .4 * (r - r0) / 10 : 1; };
        var pt = function (r, w) { var t = (a + w * taper(r)) * P / 180; return (r * Math.cos(t)).toFixed(2) + " " + (r * Math.sin(t)).toFixed(2); };
        var path = "M" + pt(ra, w0) + " L" + pt(rb, w0) + " L" + pt(rb, w1) + " L" + pt(ra, w1) + "Z";
        var key = year + "-" + String(m + 1).padStart(2, "0") + "-" + String(d).padStart(2, "0"), fill, cls = "";
        if (d > dim) fill = "#1B1714";
        else { var inf = dayInfo(key);
          if (key > today || inf.before) fill = "#26201C";
          else if (inf.church) fill = "#FFF1C4";
          else if (inf.read) fill = "hsl(42 92% " + (52 + (d % 3) * 4) + "%)";
          else if (inf.kept) fill = m % 2 ? "hsl(220 88% " + (44 + (d % 4) * 3) + "%)" : "hsl(350 80% " + (44 + (d % 4) * 3) + "%)";
          else fill = "rgba(214,207,195,.22)";
          if (key === today) cls = ' class="ywt"'; }
        s += '<path' + cls + ' d="' + path + '" fill="' + fill + '"/>'; lead += '<path d="' + path + '"/>';
      }
      lead += '<path d="M' + (r0 * Math.cos((a - half) * P / 180)).toFixed(2) + " " + (r0 * Math.sin((a - half) * P / 180)).toFixed(2) + ' L' + (r1 * Math.cos((a - half) * P / 180)).toFixed(2) + " " + (r1 * Math.sin((a - half) * P / 180)).toFixed(2) + '"/>';
    }
    return '<svg class="yearwin" viewBox="-104 -104 208 208" role="img" aria-label="Your rose window for ' + year + '"><defs><radialGradient id="ywc" r="28" cx="0" cy="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FFF6DA"/><stop offset="1" stop-color="#E7B04A"/></radialGradient>' +
      '<filter id="ywg" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="2.2"/></filter></defs>' +
      '<circle r="101" fill="#120E0C"/><g filter="url(#ywg)" opacity=".7">' + s + '</g><g>' + s + '</g>' +
      '<g fill="none" stroke="#120E0C" stroke-width="1.1" stroke-linejoin="round">' + lead + '</g>' +
      '<circle r="' + (r0 - 2) + '" fill="url(#ywc)" stroke="#120E0C" stroke-width="2"/><text y="4" text-anchor="middle" class="yw-year">' + year + '</text>' +
      '<circle r="96" fill="none" stroke="#120E0C" stroke-width="6"/><circle r="99" fill="none" stroke="#6B5A48" stroke-width=".8" opacity=".5"/></svg>';
  }

  return { bell: bell, doors: doors, strike: strike, ambient: ambient, doorsHTML: doorsHTML, lightHTML: lightHTML, parallax: parallax,
    flame: flame, todaysCandles: todaysCandles, lightCandle: lightCandle, candleCount: candleCount, standHTML: standHTML, yearWindowSVG: yearWindowSVG, unlock: function () { ac(); } };
})();
