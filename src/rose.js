/* Rose Window's mark: a carved stone rose window of eight petals, small round lights between them, and a cross in the centre.
   roseSVG({glass:true}) is the lit window: cream stone tracery in front of ruby and blue glass, light from the centre
   (the app icon, the brand mark, the opening portal, the daily pictures, the welcome film).
   roseSVG({glass:false}) is the line drawing in one colour (the small mark on buttons and seals).
   Shared by the app, the church portal, the daily pictures and the welcome film. Returns SVG content for a viewBox of -102 -102 204 204
   (glass adds a soft halo that reaches further out unless halo:false; give it a larger viewBox to show it).
   The app icon in public/icons is drawn by tools/logo/rose-icon.mjs from the same geometry. */
var roseSVG = (function () {
  var N = 8, W = 68, TIP = 78, C = 300 - W, OC = 78, QR = 276, QS = 17, n = 0;
  var R = function (d) { return d * Math.PI / 180; }, f = function (v) { return v.toFixed(1); };
  var rot = function (x, y, a) { return [x * Math.cos(R(a)) - y * Math.sin(R(a)), x * Math.sin(R(a)) + y * Math.cos(R(a))]; };
  var pt = function (x, y, a) { var p = rot(x, y, a); return f(p[0]) + " " + f(p[1]); };
  var petal = function (a) {
    return "M" + pt(TIP, 0, a) + " C" + pt(TIP + 30, -W * .5, a) + " " + pt(C - 80, -W, a) + " " + pt(C, -W, a) + " A" + W + " " + W + " 0 0 1 " + pt(C, W, a) +
      " C" + pt(C - 80, W, a) + " " + pt(TIP + 30, W * .5, a) + " " + pt(TIP, 0, a) + "Z";
  };
  var circ = function (x, y, r) { return "M" + f(x + r) + " " + f(y) + "A" + r + " " + r + " 0 1 0 " + f(x - r) + " " + f(y) + "A" + r + " " + r + " 0 1 0 " + f(x + r) + " " + f(y) + "Z"; };
  var petals = [], lights = [], leads = [];
  for (var i = 0; i < N; i++) {
    var a = i * 360 / N - 90, b = a + 180 / N, q = rot(QR, 0, b);
    petals.push(petal(a));
    lights.push(circ(q[0], q[1], QS));
    leads.push("M" + pt(TIP + 20, 0, a) + "L" + pt(320, 0, a) + "M" + pt(C - 40, -90, a) + "Q" + pt(C - 6, 0, a) + " " + pt(C - 40, 90, a));
  }
  var S = 100 / 352; // the design is drawn at radius 352; the mark is radius 100
  var grad = function (id, c) { return '<radialGradient id="' + id + '" cx="0" cy="0" r="305" gradientUnits="userSpaceOnUse"><stop offset=".18" stop-color="' + c[0] + '"/><stop offset=".38" stop-color="' + c[1] + '"/><stop offset=".7" stop-color="' + c[2] + '"/><stop offset="1" stop-color="' + c[3] + '"/></radialGradient>'; };

  return function (o) {
    o = o || {};
    if (o.glass === false) {
      var sw = (o.sw || 7) / S, c = o.stroke || "currentColor", cross = o.cross || c;
      return '<g transform="scale(' + S.toFixed(4) + ')" fill="none" stroke="' + c + '" stroke-width="' + f(sw) + '" stroke-linejoin="round"><circle r="' + f(352 - sw / 2) + '"/>' +
        petals.map(function (d) { return '<path d="' + d + '"/>'; }).join("") + '<circle r="' + OC + '"/>' +
        lights.map(function (d) { return '<path d="' + d + '" stroke-width="' + f(sw * .7) + '"/>'; }).join("") +
        '<path d="M0 -50V50M-50 0H50" stroke="' + cross + '" stroke-width="' + f(sw * 1.2) + '" stroke-linecap="round"/></g>';
    }
    var id = "rw" + (n++), u = function (k) { return "url(#" + id + k + ")"; }, stone = "#EFE5D1";
    var tracery = function (col) {
      return '<g fill="none" stroke="' + col + '" stroke-linejoin="round"><circle r="320" stroke-width="40"/>' +
        petals.map(function (d) { return '<path d="' + d + '" stroke-width="24"/>'; }).join("") + '<circle r="' + OC + '" stroke-width="24"/>' +
        lights.map(function (d) { return '<path d="' + d + '" stroke-width="9"/>'; }).join("") +
        '<path d="M0 ' + -OC + 'V' + OC + 'M' + -OC + ' 0H' + OC + '" stroke-width="16"/></g>';
    };
    var defs = '<defs>' + grad(id + "p0", ["#FFF1C2", "#E8A23A", "#B3202E", "#4A0716"]) + grad(id + "p1", ["#FFF1C2", "#E8B04A", "#2A57C4", "#0A1A4D"]) +
      '<radialGradient id="' + id + 'sp" cx="0" cy="0" r="320" gradientUnits="userSpaceOnUse"><stop offset=".3" stop-color="#3B6FD8"/><stop offset=".75" stop-color="#16307A"/><stop offset="1" stop-color="#0A1638"/></radialGradient>' +
      '<radialGradient id="' + id + 'q0" r=".6"><stop offset="0" stop-color="#C8F2B8"/><stop offset="1" stop-color="#1F7A45"/></radialGradient>' +
      '<radialGradient id="' + id + 'q1" r=".6"><stop offset="0" stop-color="#FFE3A0"/><stop offset="1" stop-color="#C9861E"/></radialGradient>' +
      '<radialGradient id="' + id + 'core" cx="0" cy="0" r="' + OC + '" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".55" stop-color="#FFF2C8"/><stop offset="1" stop-color="#FFC861"/></radialGradient>' +
      '<radialGradient id="' + id + 'bloom" cx="0" cy="0" r="300" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FFF8E0" stop-opacity=".9"/><stop offset=".3" stop-color="#FFE3A0" stop-opacity=".35"/><stop offset=".6" stop-color="#FFC070" stop-opacity="0"/></radialGradient>' +
      '<radialGradient id="' + id + 'warm" cx="0" cy="0" r="330" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FFC56E"/><stop offset=".55" stop-color="#FFE7BE"/><stop offset="1" stop-color="#FFFFFF"/></radialGradient>' +
      '<linearGradient id="' + id + 'tile" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FAF5EC"/><stop offset=".6" stop-color="#EFE6D6"/><stop offset="1" stop-color="#E0D3BE"/></linearGradient>' +
      '<radialGradient id="' + id + 'h" r=".5"><stop offset=".55" stop-color="#FFC27A" stop-opacity=".55"/><stop offset=".8" stop-color="#C23A5A" stop-opacity=".18"/><stop offset="1" stop-color="#2353B8" stop-opacity="0"/></radialGradient>' +
      '<filter id="' + id + 'grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="3" seed="4"/><feColorMatrix values="0 0 0 0 .42  0 0 0 0 .35  0 0 0 0 .25  0 0 0 .09 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>' +
      '<filter id="' + id + 'tex" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency=".022" numOctaves="3" seed="11" result="n"/><feColorMatrix in="n" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -.9 .55" result="dk"/><feComposite in="dk" in2="SourceGraphic" operator="in" result="dki"/><feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="dki"/></feMerge></filter>' +
      '<filter id="' + id + 'bevel" x="-5%" y="-5%" width="110%" height="110%"><feGaussianBlur in="SourceAlpha" stdDeviation="2.2" result="b"/>' +
      '<feSpecularLighting in="b" surfaceScale="3.5" specularConstant=".7" specularExponent="22" lighting-color="#FFFFFF" result="s"><feDistantLight azimuth="225" elevation="40"/></feSpecularLighting><feComposite in="s" in2="SourceAlpha" operator="in" result="s2"/>' +
      '<feDiffuseLighting in="b" surfaceScale="3.5" diffuseConstant="1.12" lighting-color="#FFFFFF" result="d"><feDistantLight azimuth="225" elevation="50"/></feDiffuseLighting>' +
      '<feComposite in="SourceGraphic" in2="d" operator="arithmetic" k1="1" result="lit"/><feComposite in="s2" in2="lit" operator="arithmetic" k2=".5" k3="1" result="out"/><feComposite in="out" in2="SourceAlpha" operator="in"/></filter>' +
      '<filter id="' + id + 'drop" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur in="SourceAlpha" stdDeviation="6"/><feOffset dx="6" dy="8"/><feColorMatrix values="0 0 0 0 .02  0 0 0 0 .01  0 0 0 0 .04  0 0 0 .75 0"/></filter>' +
      '<filter id="' + id + 'recess" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur in="SourceAlpha" stdDeviation="9"/><feOffset dx="-8" dy="-10"/><feComposite in2="SourceAlpha" operator="arithmetic" k2="-1" k3="1"/><feColorMatrix values="0 0 0 0 .25  0 0 0 0 .2  0 0 0 0 .14  0 0 0 .5 0"/></filter>' +
      '<clipPath id="' + id + 'win"><circle r="312"/></clipPath></defs>';
    return defs + (o.halo === false ? "" : '<circle class="rw-halo" r="150" fill="' + u("h") + '"/>') +
      '<g transform="scale(' + S.toFixed(4) + ')"><circle r="352" fill="' + u("tile") + '" filter="' + u("bevel") + '"/>' +
      '<circle r="336" fill="#000" opacity=".9" filter="' + u("recess") + '"/>' +
      '<g class="rw-glass" clip-path="' + u("win") + '"><g filter="' + u("tex") + '"><circle r="312" fill="' + u("sp") + '"/>' +
      petals.map(function (d, i) { return '<path d="' + d + '" fill="' + u("p" + (i % 2)) + '"/>'; }).join("") +
      lights.map(function (d, i) { return '<path d="' + d + '" fill="' + u("q" + (i % 2)) + '"/>'; }).join("") +
      '<circle r="' + OC + '" fill="' + u("core") + '"/></g>' +
      '<g fill="none" stroke="#1A1424" stroke-width="3.2" opacity=".8">' + petals.map(function (d, i) {
        return '<clipPath id="' + id + "c" + i + '"><path d="' + d + '"/></clipPath><path clip-path="' + u("c" + i) + '" d="' + leads[i] + '"/>'; }).join("") + '</g>' +
      '<circle r="300" fill="' + u("bloom") + '"/><g filter="' + u("drop") + '">' + tracery(stone) + '</g></g>' +
      '<g filter="' + u("bevel") + '">' + tracery(stone) + '</g>' +
      '<g style="mix-blend-mode:multiply" opacity=".55">' + tracery(u("warm")) + '</g>' +
      '<g filter="' + u("grain") + '">' + tracery("#000") + '</g></g>';
  };
})();
if (typeof module !== "undefined") module.exports = roseSVG;
