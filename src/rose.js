/* Rose Window's mark: a gothic rose of twelve lancets, a ring of twelve small round lights and a centre with a cross.
   roseSVG({glass:true}) is the lit glass (the icon, the opening); roseSVG({glass:false}) is the line drawing (the small mark).
   Shared by the app, the church portal, the daily pictures and the icon script. Returns SVG content for a viewBox of -102 -102 204 204
   (glass adds a soft halo that reaches further out; give it a larger viewBox to show it). */
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
