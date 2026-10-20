// The Rose Window app icon: a carved stone rose window (eight petals, a cross in the centre) with lit glass behind.
// node tools/logo/rose-icon.mjs out.svg '{"sw":24,"bb":2.2,"ss":3.5,"cw":16,"oc":78,"tip":78}'  (the chosen settings). The PNGs in public/icons were rendered from it with Playwright.
import fs from "node:fs";
const R = d => d * Math.PI / 180, f = n => n.toFixed(1);
const rot = (x, y, a) => [x * Math.cos(R(a)) - y * Math.sin(R(a)), x * Math.sin(R(a)) + y * Math.cos(R(a))];
const o = JSON.parse(process.argv[3] || "{}");
const N = o.n || 8, W = o.w || 68, TIP = o.tip || 74, C = 300 - W;
function petal(a) {
  const pts = [[TIP,0],[TIP+30,-W*.5],[C-80,-W],[C,-W],[C,W],[C-80,W],[TIP+30,W*.5]].map(([x,y]) => rot(x,y,a).map(f).join(" "));
  return `M${pts[0]} C${pts[1]} ${pts[2]} ${pts[3]} A${W} ${W} 0 0 1 ${pts[4]} C${pts[5]} ${pts[6]} ${pts[0]}Z`;
}
const circ = (x, y, r) => `M${f(x+r)} ${f(y)}A${r} ${r} 0 1 0 ${f(x-r)} ${f(y)}A${r} ${r} 0 1 0 ${f(x+r)} ${f(y)}Z`;
function quatre(cx, cy, r, a) { let s = ""; for (let k = 0; k < 4; k++) { const [x, y] = rot(r*.5, 0, a + k*90); s += circ(cx+x, cy+y, r*.52); } return s; }
const petals = [], quats = [], quatC = [];
for (let i = 0; i < N; i++) petals.push(petal(i*360/N - 90));
for (let i = 0; i < N; i++) { const a = i*360/N - 90 + 180/N; const [x, y] = rot(o.qr || 276, 0, a); quats.push(circ(x, y, o.qs || 17)); quatC.push([x,y]); }
const OC = o.oc || 66;
const leads = petals.map((d,i)=>{ const a=i*360/N-90; const L=(x1,y1,x2,y2,cx,cy)=>{const p=rot(x1,y1,a),q=rot(x2,y2,a),c=rot(cx,cy,a);return `M${f(p[0])} ${f(p[1])}Q${f(c[0])} ${f(c[1])} ${f(q[0])} ${f(q[1])}`;};
 return `<clipPath id="pc${i}"><path d="${d}"/></clipPath><g clip-path="url(#pc${i})">`+
 `<path d="${L(TIP+20,0,320,0,200,0)}${L(C-40,-90,C-40,90,C-6,0)}"/></g>`; }).join("");
// colours
const cols = o.cols || [["#FFF1C2","#E8A23A","#B3202E","#4A0716"],["#FFF1C2","#E8B04A","#2A57C4","#0A1A4D"]];
const grad = (id, c) => `<radialGradient id="${id}" cx="0" cy="0" r="305" gradientUnits="userSpaceOnUse"><stop offset=".18" stop-color="${c[0]}"/><stop offset=".38" stop-color="${c[1]}"/><stop offset=".7" stop-color="${c[2]}"/><stop offset="1" stop-color="${c[3]}"/></radialGradient>`;
const stoneCol = o.stone || "#EFE5D1";
const tracery = `<g fill="none" stroke="${stoneCol}" stroke-linejoin="round">
 <circle r="320" stroke-width="40"/>
 ${petals.map(d=>`<path d="${d}" stroke-width="${o.sw||17}"/>`).join("")}
 <circle r="${OC}" stroke-width="${o.sw||17}"/>
 ${quats.map(d=>`<path d="${d}" stroke-width="9"/>`).join("")}
 <path d="M0 ${-OC}V${OC}M${-OC} 0H${OC}" stroke-width="${o.cw||12}"/>
</g>`;
const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
<defs>
${grad("p0", cols[0])}${grad("p1", cols[1])}
<radialGradient id="sp" cx="0" cy="0" r="320" gradientUnits="userSpaceOnUse"><stop offset=".3" stop-color="#3B6FD8"/><stop offset=".75" stop-color="#16307A"/><stop offset="1" stop-color="#0A1638"/></radialGradient>
<radialGradient id="q0" r=".6"><stop offset="0" stop-color="#C8F2B8"/><stop offset="1" stop-color="#1F7A45"/></radialGradient>
<radialGradient id="q1" r=".6"><stop offset="0" stop-color="#FFE3A0"/><stop offset="1" stop-color="#C9861E"/></radialGradient>
<radialGradient id="core" cx="0" cy="0" r="${OC}" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".55" stop-color="#FFF2C8"/><stop offset="1" stop-color="#FFC861"/></radialGradient>
<radialGradient id="bloom" cx="0" cy="0" r="300" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FFF8E0" stop-opacity=".9"/><stop offset=".3" stop-color="#FFE3A0" stop-opacity=".35"/><stop offset=".6" stop-color="#FFC070" stop-opacity="0"/></radialGradient>
<radialGradient id="warm" cx="0" cy="0" r="330" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FFC56E"/><stop offset=".55" stop-color="#FFE7BE"/><stop offset="1" stop-color="#FFFFFF"/></radialGradient>
<linearGradient id="tile" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FAF5EC"/><stop offset=".6" stop-color="#EFE6D6"/><stop offset="1" stop-color="#E0D3BE"/></linearGradient>
<filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="3" seed="4"/><feColorMatrix values="0 0 0 0 .42  0 0 0 0 .35  0 0 0 0 .25  0 0 0 .09 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>
<filter id="glassTex" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency=".022" numOctaves="3" seed="11" result="n"/><feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -.9 .55" result="dk"/><feComposite in="dk" in2="SourceGraphic" operator="in" result="dki"/><feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="dki"/></feMerge></filter>
<filter id="bevel" x="-5%" y="-5%" width="110%" height="110%">
 <feGaussianBlur in="SourceAlpha" stdDeviation="${o.bb||3.5}" result="b"/>
 <feSpecularLighting in="b" surfaceScale="${o.ss||6}" specularConstant=".7" specularExponent="22" lighting-color="#FFFFFF" result="s"><feDistantLight azimuth="225" elevation="40"/></feSpecularLighting>
 <feComposite in="s" in2="SourceAlpha" operator="in" result="s2"/>
 <feDiffuseLighting in="b" surfaceScale="${o.ss||6}" diffuseConstant="1.12" lighting-color="#FFFFFF" result="d"><feDistantLight azimuth="225" elevation="50"/></feDiffuseLighting>
 <feComposite in="SourceGraphic" in2="d" operator="arithmetic" k1="1" result="lit"/>
 <feComposite in="s2" in2="lit" operator="arithmetic" k2=".5" k3="1" result="out"/>
 <feComposite in="out" in2="SourceAlpha" operator="in"/>
</filter>
<filter id="drop" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur in="SourceAlpha" stdDeviation="6"/><feOffset dx="6" dy="8"/><feColorMatrix values="0 0 0 0 .02  0 0 0 0 .01  0 0 0 0 .04  0 0 0 .75 0"/></filter>
<filter id="glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="14"/></filter>
<filter id="tileShadow" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur in="SourceAlpha" stdDeviation="16"/><feOffset dy="12"/><feColorMatrix values="0 0 0 0 .3  0 0 0 0 .24  0 0 0 0 .18  0 0 0 .32 0"/><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="recess" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur in="SourceAlpha" stdDeviation="9"/><feOffset dx="-8" dy="-10"/><feComposite in2="SourceAlpha" operator="arithmetic" k2="-1" k3="1"/><feColorMatrix values="0 0 0 0 .25  0 0 0 0 .2  0 0 0 0 .14  0 0 0 .5 0"/></filter>
<clipPath id="win"><circle r="312"/></clipPath>
</defs>
<rect x="56" y="48" width="912" height="912" rx="208" fill="url(#tile)" filter="url(#tileShadow)"/>
<rect x="56" y="48" width="912" height="912" rx="208" fill="#000" filter="url(#grain)"/>
<g transform="translate(512 504)">
 <circle r="352" fill="url(#tile)" filter="url(#bevel)"/>
 <circle r="336" fill="#000" opacity=".9" filter="url(#recess)"/>
 
 <g clip-path="url(#win)">
  <g filter="url(#glassTex)">
   <circle r="312" fill="url(#sp)"/>
   ${petals.map((d,i)=>`<path d="${d}" fill="url(#p${i%2})"/>`).join("")}
   ${quats.map((d,i)=>`<path d="${d}" fill="url(#q${i%2})"/>`).join("")}
   <circle r="${OC}" fill="url(#core)"/>
  </g>
  <g fill="none" stroke="#1A1424" stroke-width="3.2" opacity=".8">${leads}</g>
  <circle r="300" fill="url(#bloom)"/>
  <g filter="url(#drop)">${tracery}</g>
 </g>
 <g filter="url(#bevel)">${tracery}</g>
<g style="mix-blend-mode:multiply" opacity=".55">${tracery.replaceAll(`stroke="${stoneCol}"`, 'stroke="url(#warm)"')}</g>
 <g filter="url(#grain)">${tracery.replaceAll(`stroke="${stoneCol}"`, 'stroke="#000"')}</g>
</g>
</svg>`;
fs.writeFileSync(process.argv[2], svg);
