/* Rose Window's mark: a gothic rose of twelve lancets, a ring of twelve small round lights and a centre with a cross.
   roseSVG({glass:true}) is the lit glass, drawn as real leaded glass (deep cobalt and ruby, hand-made unevenness, light glowing through, dark stone tracery); roseSVG({glass:true, flat:true}) is the earlier flat version (the icon, the opening); roseSVG({glass:false}) is the line drawing (the small mark).
   Shared by the app, the church portal, the daily pictures and the icon script. Returns SVG content for a viewBox of -102 -102 204 204
   (glass adds a soft halo that reaches further out; give it a larger viewBox to show it). */
// The lit window, drawn as real glass: stone tracery, many small leaded pieces of uneven hand-made glass, light that glows and falls off.
var realRose = (function () {
  var rad = function (a) { return a * Math.PI / 180; };
  var P = function (r, a) { return (r * Math.cos(rad(a))).toFixed(2) + " " + (r * Math.sin(rad(a))).toFixed(2); };
  var seed = 7; var rnd = function () { seed = (seed * 16807) % 2147483647; return seed / 2147483647; };
  // Chartres-like palette: cobalt dominant, ruby, a little gold, green and murrey
  var COL = { blue: [219, 95, 47], blue2: [226, 90, 42], ruby: [350, 92, 45], gold: [40, 96, 55], green: [150, 70, 36], violet: [292, 55, 40], white: [42, 80, 70] };
  var hsl = function (c, dl, ds) { return "hsl(" + (c[0] + (rnd() - .5) * 10).toFixed(0) + " " + Math.max(20, Math.min(95, c[1] + (ds || 0) + (rnd() - .5) * 14)).toFixed(0) + "% " + Math.max(8, Math.min(92, c[2] + (dl || 0) + (rnd() - .5) * 12)).toFixed(0) + "%)"; };
  var n = 0;
  return function (o) {
    o = o || {}; seed = 7; var id = "rr" + (n++);
    var lead = "#120F0C", s = "";
    var defs = '<defs>' +
      // hand-made glass: mottling, seeds and streaks, multiplied into the colour
      '<filter id="' + id + 'g" x="-10%" y="-10%" width="120%" height="120%" color-interpolation-filters="sRGB">' +
      '<feTurbulence type="fractalNoise" baseFrequency=".055" numOctaves="3" seed="3" result="m"/>' +
      '<feTurbulence type="fractalNoise" baseFrequency=".02 .35" numOctaves="2" seed="9" result="st"/>' +
      '<feColorMatrix in="m" type="matrix" values="1.1 0 0 0 0  1.1 0 0 0 0  1.1 0 0 0 0  0 0 0 0 1" result="m2"/>' +
      '<feComposite in="SourceGraphic" in2="m2" operator="arithmetic" k1="1.75" k2="0" k3="0" k4="0" result="a"/>' +
      '<feColorMatrix in="st" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 .25 0 0 -.16" result="st2"/>' +
      '<feComposite in="st2" in2="SourceGraphic" operator="in" result="st3"/>' +
      '<feBlend in="a" in2="st3" mode="screen" result="b"/>' +
      '<feComposite in="b" in2="SourceGraphic" operator="in"/></filter>' +
      // bloom: light spilling over the lead
      '<filter id="' + id + 'sh" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="1.6"/></filter>' +
      '<filter id="' + id + 'b2" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="2.2"/></filter>' +
      '<filter id="' + id + 'b" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="3.2"/></filter>' +
      // light falls off towards the rim; brightest at the centre
      '<radialGradient id="' + id + 'v" r="100" cx="0" cy="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#000" stop-opacity="0"/><stop offset=".6" stop-color="#000" stop-opacity=".05"/><stop offset="1" stop-color="#000" stop-opacity=".38"/></radialGradient>' +
      '<radialGradient id="' + id + 'sun" r="95" cx="-28" cy="-34" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FFE7B8" stop-opacity=".2"/><stop offset=".5" stop-color="#FFE2A8" stop-opacity=".06"/><stop offset="1" stop-color="#FFE2A8" stop-opacity="0"/></radialGradient>' +
      '<clipPath id="' + id + 'k"><circle r="96"/></clipPath>' +
      '<radialGradient id="' + id + 'c" r="34" cx="0" cy="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FFF1C4"/><stop offset=".5" stop-color="#F2B94A"/><stop offset="1" stop-color="#A8681C"/></radialGradient>' +
      // stone: warm limestone, lit faintly by the glass
      '<radialGradient id="' + id + 's" r="104" cx="0" cy="0" gradientUnits="userSpaceOnUse"><stop offset=".3" stop-color="#1F1915"/><stop offset=".85" stop-color="#15110E"/><stop offset="1" stop-color="#0D0B09"/></radialGradient>' +
      '<filter id="' + id + 't"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="2"/><feColorMatrix type="matrix" values="0 0 0 0 .32  0 0 0 0 .27  0 0 0 0 .22  0 0 0 .22 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>' +
      '<radialGradient id="' + id + 'h" r=".5"><stop offset=".5" stop-color="#E9B46A" stop-opacity=".42"/><stop offset=".72" stop-color="#7A2A4A" stop-opacity=".16"/><stop offset="1" stop-color="#1E3FA0" stop-opacity="0"/></radialGradient>' +
      '</defs>';
    // the glass pieces
    var pieces = "";
    // twelve lancets, each in panes: a pointed head and three panels split down the middle
    for (var i = 0; i < 12; i++) {
      var a = i * 30, h = 10.5, rows = [[37, 49], [49, 60], [60, 69]];
      rows.forEach(function (rw, k) {
        [[-h, 0], [0, h]].forEach(function (side, j) {
          var r0 = rnd(), c = k === 1 ? (r0 < .45 ? COL.ruby : COL.blue) : (r0 < .12 ? COL.ruby : r0 < .17 ? COL.green : COL.blue);
          pieces += '<path transform="rotate(' + a + ')" d="M' + P(rw[0], side[0] * (k ? 1 : .92)) + ' L' + P(rw[1], side[0]) + ' L' + P(rw[1], side[1]) + ' L' + P(rw[0], side[1] * (k ? 1 : .92)) + 'Z" fill="' + hsl(c) + '"/>';
        });
      });
      // the pointed head
      pieces += '<path transform="rotate(' + a + ')" d="M' + P(69, -h) + ' Q' + P(76, -h * .6) + ' ' + P(81, 0) + ' Q' + P(76, h * .6) + ' ' + P(69, h) + 'Z" fill="' + hsl(i % 3 === 0 ? COL.gold : COL.ruby, -2) + '"/>';
    }
    // twelve small round lights, each in four pieces
    for (var i2 = 0; i2 < 12; i2++) {
      var a2 = i2 * 30 + 15, cc = [COL.green, COL.violet, COL.blue2][i2 % 3];
      for (var q = 0; q < 4; q++) pieces += '<path transform="rotate(' + a2 + ') translate(85 0) rotate(' + (q * 90 + 45) + ')" d="M0 0 L7.5 0 A7.5 7.5 0 0 1 0 7.5Z" fill="' + hsl(cc, 10) + '"/>';
    }
    // the centre: eight pieces of pale gold round a ruby cross
    for (var k2 = 0; k2 < 8; k2++) pieces += '<path transform="rotate(' + (k2 * 45) + ')" d="M0 0 L' + P(31, -22.5) + ' A31 31 0 0 1 ' + P(31, 22.5) + 'Z" fill="url(#' + id + 'c)"/>';
    // lead: the dark lines between every piece
    var leads = "";
    for (var i3 = 0; i3 < 12; i3++) {
      var a3 = i3 * 30, h3 = 10.5;
      leads += '<path transform="rotate(' + a3 + ')" d="M' + P(37, -h3 * .92) + ' L' + P(69, -h3) + ' Q' + P(76, -h3 * .6) + ' ' + P(81, 0) + ' Q' + P(76, h3 * .6) + ' ' + P(69, h3) + ' L' + P(37, h3 * .92) + ' A37 37 0 0 0 ' + P(37, -h3 * .92) + 'Z M' + P(37, 0) + ' L' + P(69, 0) + ' M' + P(49, -h3) + ' L' + P(49, h3) + ' M' + P(60, -h3) + ' L' + P(60, h3) + ' M' + P(69, -h3) + ' L' + P(69, h3) + '"/>';
      leads += '<g transform="rotate(' + (a3 + 15) + ') translate(85 0)"><circle r="7.5"/><path d="M-5.3 -5.3L5.3 5.3M-5.3 5.3L5.3 -5.3"/></g>';
    }
    for (var k3 = 0; k3 < 8; k3++) leads += '<path transform="rotate(' + (k3 * 45 + 22.5) + ')" d="M0 0 L31 0"/>';
    leads += '<circle r="31"/>';
    // the painted cross (glass paint, not lead)
    var cross = '<path d="M0 -19V19M-12.5 -6H12.5" stroke="#7E0F22" stroke-width="7" stroke-linecap="butt"/><path d="M0 -19V19M-12.5 -6H12.5" stroke="#B3203A" stroke-width="4.2"/>';
    s += defs;
    if (o.halo !== false) s += '<circle class="rw-halo" r="160" fill="url(#' + id + 'h)"/>';
    // stone tracery
    s += '<circle r="101" fill="url(#' + id + 's)"/><circle r="101" fill="#000" filter="url(#' + id + 't)" opacity=".7"/>';
    // glass, its glow, its texture
    s += '<g filter="url(#' + id + 'b)" opacity=".8">' + pieces + '</g>';
    s += '<g filter="url(#' + id + 'g)">' + pieces + '</g>';
    s += '<g clip-path="url(#' + id + 'k)" style="mix-blend-mode:screen">' + pieces.replace(/fill="[^"]*"/g, 'fill="url(#' + id + 'sun)"') + '</g>';
    s += '<g filter="url(#' + id + 'b2)" opacity=".38" style="mix-blend-mode:screen">' + pieces + '</g>';
    s += cross;
    s += '<g fill="none" stroke="#000" stroke-width="6.5" stroke-linejoin="round" opacity=".55" filter="url(#' + id + 'sh)">' + leads + '</g>';
    s += '<g fill="none" stroke="' + lead + '" stroke-width="2.8" stroke-linejoin="round">' + leads + '</g>';
    s += '<g fill="none" stroke="#7A6A58" stroke-width=".45" stroke-linejoin="round" opacity=".35" transform="translate(-.4 -.4)">' + leads + '</g>';
    s += '<circle r="100" fill="url(#' + id + 'v)" style="mix-blend-mode:multiply" pointer-events="none"/>';
    // the stone rim, with a lit inner edge
    s += '<circle r="98" fill="none" stroke="#0F0C0A" stroke-width="7"/><circle r="94.5" fill="none" stroke="#6B5A48" stroke-width=".7" opacity=".45"/><circle r="101.5" fill="none" stroke="#3A3129" stroke-width="1"/>';
    return s;
  };
})();

var roseSVG = (function () {
  var RUBY = ["#FF6B6B", "#C21F3A", "#5E0A1C"], LAPIS = ["#7FB2FF", "#2353B8", "#0B1E52"], GOLD = ["#FFE7A3", "#E0A526", "#7A4A08"], GREEN = ["#9FE0A8", "#2F8F55", "#0E3B22"], VIOLET = ["#C9A6FF", "#6B3FB8", "#26104E"];
  var rad = function (a) { return a * Math.PI / 180; };
  var P = function (r, a) { return (r * Math.cos(rad(a))).toFixed(2) + " " + (r * Math.sin(rad(a))).toFixed(2); };
  var lancet = function (r1, r2, tip, h) { return "M" + P(r1, -h) + " L" + P(r2, -h) + " Q" + P((r2 + tip) / 2 + 2, -h * .55) + " " + P(tip, 0) + " Q" + P((r2 + tip) / 2 + 2, h * .55) + " " + P(r2, h) + " L" + P(r1, h) + " A" + r1 + " " + r1 + " 0 0 0 " + P(r1, -h) + "Z"; };
  var L = lancet(36, 66, 80, 11), n = 0;
  var each = function (k, f) { var s = ""; for (var i = 0; i < k; i++) s += f(i, i * 360 / k); return s; };
  return function (o) {
    o = o || {};
    var cross = o.cross || "#8E2B2B";
    if (o.glass === false) {
      var sw = o.sw || 7, c = o.stroke || "currentColor";
      return '<g fill="none" stroke="' + c + '" stroke-width="' + sw + '" stroke-linejoin="round"><circle r="96"/><circle r="30"/>' +
        each(12, function (i, a) { return '<path transform="rotate(' + a + ')" d="' + L + '"/>'; }) +
        each(12, function (i, a) { return '<circle transform="rotate(' + (a + 15) + ') translate(84 0)" r="7.5"/>'; }) +
        '<path d="M0 -17V17M-11 -5H11" stroke="' + cross + '" stroke-width="' + (sw * 1.5) + '" stroke-linecap="round"/></g>';
    }
    if (!o.flat) return realRose(o);
    var id = "rw" + (n++), lead = o.lead || "#0B0B10", scheme = [RUBY, LAPIS, GOLD, LAPIS];
    var grad = function (k, c) { return '<radialGradient id="' + id + k + '" cx="0" cy="0" r="100" gradientUnits="userSpaceOnUse"><stop offset=".25" stop-color="' + c[0] + '"/><stop offset=".62" stop-color="' + c[1] + '"/><stop offset="1" stop-color="' + c[2] + '"/></radialGradient>'; };
    return '<defs>' + scheme.map(function (c, i) { return grad(i, c); }).join("") + grad("g", GREEN) + grad("v", VIOLET) +
      '<radialGradient id="' + id + 'c" r=".5"><stop offset="0" stop-color="#FFF8E6"/><stop offset=".7" stop-color="#FFD98A"/><stop offset="1" stop-color="#C9862A"/></radialGradient>' +
      '<radialGradient id="' + id + 'h" r=".5"><stop offset=".55" stop-color="#FFC27A" stop-opacity=".55"/><stop offset=".8" stop-color="#C23A5A" stop-opacity=".18"/><stop offset="1" stop-color="#2353B8" stop-opacity="0"/></radialGradient>' +
      '<filter id="' + id + 'b" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="5"/></filter></defs>' +
      (o.halo === false ? "" : '<circle class="rw-halo" r="150" fill="url(#' + id + 'h)"/>') +
      '<circle r="100" fill="' + lead + '"/><g class="rw-glass">' +
      '<g filter="url(#' + id + 'b)" opacity=".75">' + each(12, function (i, a) { return '<path transform="rotate(' + a + ')" d="' + L + '" fill="url(#' + id + (i % 4) + ')"/>'; }) + '</g>' +
      each(12, function (i, a) { return '<path transform="rotate(' + a + ')" d="' + L + '" fill="url(#' + id + (i % 4) + ')" stroke="' + lead + '" stroke-width="2.5"/><path transform="rotate(' + a + ')" d="M40 0H74" stroke="' + lead + '" stroke-width="1.6"/>'; }) +
      each(12, function (i, a) { return '<circle transform="rotate(' + (a + 15) + ') translate(84 0)" r="8" fill="url(#' + id + (i % 2 ? "g" : "v") + ')" stroke="' + lead + '" stroke-width="2.2"/>'; }) +
      '<circle r="31" fill="url(#' + id + 'c)" stroke="' + lead + '" stroke-width="3"/>' +
      '<path d="M0 -18V18M-12 -5.5H12" stroke="#9E1F33" stroke-width="5.5" stroke-linecap="round"/></g>' +
      '<circle r="97" fill="none" stroke="#3A3530" stroke-width="5"/><circle r="97" fill="none" stroke="#7A6A55" stroke-width="1.2" opacity=".7"/>';
  };
})();
if (typeof module !== "undefined") module.exports = roseSVG;
