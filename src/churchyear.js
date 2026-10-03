// The church year: Easter, the seasons and the theme for any day. Shared by the app (inlined by build.mjs)
// and the daily email (daily.mjs). Expects CAL (content/calendar.json) in scope.
function easter(y) {
  const a = y % 19, b = Math.floor(y / 100), c = y % 100, d = Math.floor(b / 4), e = b % 4, f = Math.floor((b + 8) / 25), g = Math.floor((b - f + 1) / 3),
    h = (19 * a + b - d - g + 15) % 30, i = Math.floor(c / 4), k = c % 4, l = (32 + 2 * e + 2 * i - h - k) % 7, m = Math.floor((a + 11 * h + 22 * l) / 451),
    month = Math.floor((h + l - 7 * m + 114) / 31), day = ((h + l - 7 * m + 114) % 31) + 1;
  return new Date(y, month - 1, day);
}
const addDays = (x, n) => { const r = new Date(x); r.setDate(r.getDate() + n); return r; };
const daysBetween = (a, b) => Math.round((b - a) / 864e5);
function season(d = new Date()) {
  const y = d.getFullYear(), t = new Date(y, d.getMonth(), d.getDate()), E = easter(y);
  const xmas = new Date(y, 11, 25), advent = addDays(xmas, -((xmas.getDay() || 7) + 21));
  const S = (name, color, note) => ({ name, color, note });
  if (t <= new Date(y, 0, 5)) return S("Christmas", "#C9A227", "Twelve days of celebration");
  if (t >= addDays(E, -46) && t < addDays(E, -7)) return S("Lent", "#6B4A9E", "Forty days of simplicity and renewal");
  if (t >= addDays(E, -7) && t < E) return S("Holy Week", "#A33A3A", "The most important week of the old year");
  if (t >= E && t < addDays(E, 49)) return S("Easter", "#C9A227", "Fifty days of new life");
  if (+t === +addDays(E, 49)) return S("Pentecost", "#A33A3A", "Fire and new beginnings");
  if (t >= advent && t < xmas) return S("Advent", "#3B4FA0", "A season of waiting and hope");
  if (t >= xmas) return S("Christmas", "#C9A227", "Twelve days of celebration");
  return S("Ordinary Time", "#3E7A55", "The long green season of growth");
}
function themeFor(d = new Date()) {
  const y = d.getFullYear(), t = new Date(y, d.getMonth(), d.getDate()), E = easter(y);
  const movables = [[-46, "ash-wednesday"], [-7, "palm-sunday"], [-3, "maundy-thursday"], [-2, "good-friday"], [-1, "holy-saturday"], [0, "easter"], [39, "ascension"], [49, "pentecost"], [56, "trinity"]];
  for (const [n, k] of movables) if (+t === +addDays(E, n)) return CAL.movable[k];
  const key = String(t.getMonth() + 1).padStart(2, "0") + "-" + String(t.getDate()).padStart(2, "0");
  if (CAL.fixed[key]) return CAL.fixed[key];
  if (t > addDays(E, -7) && t < addDays(E, -3)) return CAL.holyweek;
  if (t > E && t < addDays(E, 7)) return CAL.easterweek;
  const xmas = new Date(y, 11, 25), advent = addDays(xmas, -((xmas.getDay() || 7) + 21));
  if (t >= advent && t < xmas) return CAL.advent[Math.min(3, Math.floor(daysBetween(advent, t) / 7))];
  if (t > xmas || t <= new Date(y, 0, 5)) return CAL.christmastide;
  if (t > addDays(E, -46) && t < addDays(E, -7)) return CAL.lent[t.getDay()];
  return weeklyFor(t);
}
/* Ordinary weeks: each weekday rotates through its own set of ideas, so a day's idea returns only every five to seven weeks */
const dayNumber = d => Math.floor(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()) / 864e5);
const weekNumber = d => Math.floor((dayNumber(d) + 4) / 7);
function weeklyFor(t) {
  const d = t.getDay(), pool = [CAL.weekly[d], ...((CAL.variants || {})[d] || [])];
  return pool[weekNumber(t) % pool.length];
}
