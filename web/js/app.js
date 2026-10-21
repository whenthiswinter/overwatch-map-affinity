const MODES = ["Escort", "Hybrid", "Control", "Push", "Flashpoint"];
const ROLES = ["Tank", "Damage", "Support"];
const TIER_ORDER = { S: 0, A: 1, B: 2, C: 3, D: 4 };
const TIER_INNER = 1.2; // A/C line, see analysis/build_dataset.py

let data = null;

// View state, mirrored into the URL hash so a link opens the same view.
// Map and hero defaults are filled in once the data is loaded.
const DEFAULTS = { tab: "map", scope: "all", rank: "ALL", region: "ALL", map: "", role: "ALL", poolonly: "0", hero: "", prole: "ALL", pmode: "ALL" };
let state = { ...DEFAULTS };

// Hero slugs were renamed to match Blizzard's; carry saved pools over.
const LEGACY_SLUGS = { jetpackcat: "jetpack-cat", junkerqueen: "junker-queen", soldier76: "soldier-76", wreckingball: "wrecking-ball" };
let pool = new Set(JSON.parse(localStorage.getItem("owPool") || '["winston","tracer","ana"]').map((h) => LEGACY_SLUGS[h] || h));

const el = (id) => document.getElementById(id);
const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);
const fmt = (slug) => slug.replace(/-/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());
const heroName = (slug) => esc((data && data.hero_names && data.hero_names[slug]) || fmt(slug));
const mapName = (slug) => esc((data && data.map_names && data.map_names[slug]) || fmt(slug));
const signed = (v, digits = 2) => `${v > 0 ? "+" : ""}${v.toFixed(digits)}`;
const provTag = (e) => (e.provisional ? '<span class="prov-tag">Provisional</span>' : "");
const fmtDate = (iso) => new Date(`${iso}T00:00:00`).toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric" });

const CONTROLS = { scope: "scopeSelect", rank: "rankSelect", region: "regionSelect", map: "mapSelect", role: "roleSelect", hero: "heroSelect" };

function storageGet(key, fallback) {
  try { return localStorage.getItem(key) ?? fallback; } catch { return fallback; }
}

function storageSet(key, value) {
  try { localStorage.setItem(key, value); } catch { /* private mode */ }
}

function showStatus(message, isError = false) {
  el("status").textContent = message;
  el("status").classList.toggle("error", isError);
  el("status").classList.toggle("hidden", !message);
}

fetch("../data/web_data.json")
  .then((r) => {
    if (!r.ok) throw new Error(`HTTP ${r.status}`);
    return r.json();
  })
  .then((json) => {
    data = json;
    expandScopes();
    init();
  })
  .catch((err) => showStatus(`Couldn't load the data (${err.message}). Try refreshing the page in a minute.`, true));

// web_data.json stores each hero-map entry once per rank/region combo; rebuild
// the per-map and per-hero views the tabs read from.
function expandScopes() {
  Object.values(data.scopes).forEach((combos) => {
    Object.values(combos).forEach((combo) => {
      combo.maps = {};
      Object.entries(combo.heroes).forEach(([hero, h]) => {
        h.role = data.hero_roles[hero] || "Damage";
        h.maps = [];
      });
      combo.entries.forEach((e) => {
        e.role = data.hero_roles[e.hero] || "Damage";
        e.mode = data.map_modes[e.map] || "Other";
        (combo.maps[e.map] = combo.maps[e.map] || []).push(e);
        combo.heroes[e.hero].maps.push(e);
      });
    });
  });
}

function patchLabel(meta) {
  return `Season ${meta.season}${meta.is_midseason ? " midseason" : ""}`;
}

function renderFreshness() {
  const m = data.meta;
  let text = `Data through ${fmtDate(m.data_through)} · ${patchLabel(m)}, day ${m.days_into_patch}`;
  if (!m.mature) text += ` · counts fully from day ${m.maturity_days}`;
  el("freshness").textContent = text;
  el("scopeSelect").options[1].textContent = `This patch only (${patchLabel(m)})`;
}

function init() {
  renderFreshness();

  el("mapSelect").innerHTML = MODES.map((mode) => {
    const maps = data.map_list.filter((m) => data.map_modes[m] === mode)
      .sort((a, b) => data.map_names[a].localeCompare(data.map_names[b]));
    return `<optgroup label="${mode}">${maps.map((m) => `<option value="${m}">${mapName(m)}</option>`).join("")}</optgroup>`;
  }).join("");
  el("heroSelect").innerHTML = [...data.hero_list]
    .sort((a, b) => (data.hero_names[a] || a).localeCompare(data.hero_names[b] || b))
    .map((h) => `<option value="${h}">${heroName(h)}</option>`).join("");
  DEFAULTS.map = el("mapSelect").value;
  DEFAULTS.hero = el("heroSelect").value;

  const buckets = { Tank: el("chipsTank"), Damage: el("chipsDamage"), Support: el("chipsSupport") };
  data.hero_list.forEach((h) => {
    const chip = document.createElement("button");
    chip.type = "button";
    chip.className = "chip";
    chip.dataset.hero = h;
    chip.innerHTML = heroName(h);
    chip.onclick = () => togglePool(h);
    buckets[data.hero_roles[h] || "Damage"].appendChild(chip);
  });

  // Pool editor: open while the pool is empty, otherwise as the user last left it.
  el("poolEditor").open = pool.size === 0 || storageGet("owPoolEditorOpen", "0") === "1";
  el("poolStatsBox").open = storageGet("owPoolStatsOpen", "1") === "1";
  el("poolEditor").addEventListener("toggle", () => storageSet("owPoolEditorOpen", el("poolEditor").open ? "1" : "0"));
  el("poolStatsBox").addEventListener("toggle", () => storageSet("owPoolStatsOpen", el("poolStatsBox").open ? "1" : "0"));

  document.querySelectorAll("select, input").forEach((n) => { n.disabled = false; });
  showStatus("");
  bindEvents();
  readHash();
  applyState();
  render();
}

function readHash() {
  state = { ...DEFAULTS };
  new URLSearchParams(location.hash.slice(1)).forEach((value, key) => {
    if (key in DEFAULTS) state[key] = value;
  });
}

function writeHash() {
  const params = new URLSearchParams();
  Object.keys(DEFAULTS).forEach((k) => { if (state[k] !== DEFAULTS[k]) params.set(k, state[k]); });
  const hash = params.toString();
  history.replaceState(null, "", hash ? `#${hash}` : location.pathname + location.search);
}

// Push state into the controls, falling back to defaults for values that
// don't exist (an old link to a map that left the pool, a typo, ...).
function applyState() {
  Object.entries(CONTROLS).forEach(([key, id]) => {
    const select = el(id);
    if (![...select.options].some((o) => o.value === state[key])) state[key] = DEFAULTS[key];
    select.value = state[key];
  });
  if (!["map", "hero", "pool"].includes(state.tab)) state.tab = DEFAULTS.tab;
  el("onlyPoolCheck").checked = state.poolonly === "1";
  document.querySelectorAll("#poolRoleFilter .chip-toggle").forEach((b) => b.classList.toggle("active", b.dataset.role === state.prole));
  document.querySelectorAll("#poolModeFilter .chip-toggle").forEach((b) => b.classList.toggle("active", b.dataset.mode === state.pmode));
}

function bindEvents() {
  document.querySelectorAll(".tab").forEach((btn) => {
    btn.onclick = () => { state.tab = btn.dataset.tab; update(); };
  });

  document.querySelectorAll("#poolRoleFilter .chip-toggle").forEach((btn) => {
    btn.onclick = () => { state.prole = btn.dataset.role; applyState(); update(); };
  });

  document.querySelectorAll("#poolModeFilter .chip-toggle").forEach((btn) => {
    btn.onclick = () => { state.pmode = btn.dataset.mode; applyState(); update(); };
  });

  Object.entries(CONTROLS).forEach(([key, id]) => {
    el(id).addEventListener("change", () => { state[key] = el(id).value; update(); });
  });
  el("onlyPoolCheck").addEventListener("change", () => { state.poolonly = el("onlyPoolCheck").checked ? "1" : "0"; update(); });

  window.addEventListener("hashchange", () => { readHash(); applyState(); render(); });

  el("clearPoolBtn").onclick = () => {
    pool.clear();
    storageSet("owPool", "[]");
    render();
  };

  // Rows (tables and pool cards) open a details line; works with touch, mouse and keyboard.
  const toggleRow = (row) => {
    const detail = row.nextElementSibling;
    if (!detail || !detail.classList.contains("detail")) return;
    const open = detail.classList.toggle("hidden") === false;
    row.setAttribute("aria-expanded", open);
  };
  ["tableBody", "poolGrid"].forEach((id) => {
    el(id).addEventListener("click", (ev) => {
      const row = ev.target.closest(".expandable");
      if (row) toggleRow(row);
    });
    el(id).addEventListener("keydown", (ev) => {
      const row = ev.target.closest(".expandable");
      if (row && (ev.key === "Enter" || ev.key === " ")) {
        ev.preventDefault();
        toggleRow(row);
      }
    });
  });

  el("exportBtn").onclick = openExport;
  el("copyExportBtn").onclick = copyExport;
  el("closeExportBtn").onclick = () => el("exportDialog").close();

  el("legendBtn").onclick = () => el("legendDialog").showModal();
  el("closeLegendBtn").onclick = () => el("legendDialog").close();
}

function update() {
  writeHash();
  render();
}

function togglePool(hero) {
  if (pool.has(hero)) pool.delete(hero);
  else pool.add(hero);
  storageSet("owPool", JSON.stringify([...pool]));
  render();
}

function activeSlice() {
  return data.scopes[state.scope][`${state.rank}_${state.region}`] || { maps: {}, heroes: {} };
}

// Chance the shown tier is right (tier_p, from the calibrated noise model).
// High = at least 3 in 4, Medium = more likely right than wrong, Low = less.
function confidence(e) {
  if (e.tier_p >= 75) return { level: "High", cls: "high" };
  if (e.tier_p >= 50) return { level: "Medium", cls: "mid" };
  return { level: "Low", cls: "low" };
}

const sigmaText = (h) => (h.volatility_class.startsWith("Too early") ? "&sigma; &ndash;" : `&sigma; ${h.volatility.toFixed(2)}%`);

function confCell(e) {
  const c = confidence(e);
  return `<span class="conf conf-${c.cls}"><span class="conf-dot"></span><span class="conf-level">${c.level} </span>${e.tier_p}%</span> <span class="muted n-count">n=${e.sample_size}</span>`;
}

function deltaCell(e) {
  const low = confidence(e).cls === "low";
  return `<span class="delta ${e.delta_wr >= 0 ? "pos" : "neg"}${low ? " lowconf" : ""}">${signed(e.delta_wr)}%</span>`;
}

// Everything that used to live in hover-only tooltips.
function detailsHtml(e, { showHero, showMap }) {
  const c = confidence(e);
  const presenceLabel = e.presence.split(" (")[0];
  const lines = [
    `<b>${showHero ? heroName(e.hero) : ""}${showHero && showMap ? " on " : ""}${showMap ? mapName(e.map) : ""}</b> · ${e.role} · ${e.mode}`,
    `<b>Delta WR ${signed(e.delta_wr)}%</b> (tier ${e.tier}), adjusted for noise from a raw average of ${signed(e.raw_delta_wr)}% &plusmn;${e.ci.toFixed(1)} (95% range, ${e.sample_size} slice${e.sample_size === 1 ? "" : "s"}).`,
    `<b>${c.level} confidence:</b> ${e.tier_p}% chance the true value is in tier ${e.tier}.`,
    `<b>Picked ${signed(e.pr_lift, 0)}%</b> vs this hero's average map (${presenceLabel}) · <b>${e.archetype}</b>`,
  ];
  if (e.provisional) lines.push("<b>Provisional:</b> only current-patch data so far, still settling. Expect this to move.");
  return lines.map((l) => `<div>${l}</div>`).join("");
}

function renderPatchNotice() {
  const m = data.meta;
  const patchOnly = state.scope === "patch";
  el("patchNotice").classList.toggle("hidden", !patchOnly);
  if (patchOnly) {
    el("patchNotice").innerHTML = `<strong>${patchLabel(m)} only</strong>, ${m.days_into_patch} days in. These numbers come from the current patch alone (at most 8 slices per hero-map pair, 1 with a single rank and region picked), so they are much noisier than the all-seasons view${m.mature ? "" : " and still settling"}.`;
  }
}

function sortByTier(entries) {
  return [...entries].sort((a, b) => TIER_ORDER[a.tier] - TIER_ORDER[b.tier] || b.delta_wr - a.delta_wr);
}

function render() {
  if (!data) return;
  const tab = state.tab;
  document.querySelectorAll(".tab").forEach((b) => {
    b.classList.toggle("active", b.dataset.tab === tab);
    b.setAttribute("aria-selected", b.dataset.tab === tab);
  });
  ["map", "hero", "pool"].forEach((scope) => {
    document.querySelectorAll(`[data-scope="${scope}"]`).forEach((n) => n.classList.toggle("hidden", tab !== scope));
  });
  el("tableView").classList.toggle("hidden", tab === "pool");
  el("poolView").classList.toggle("hidden", tab !== "pool");
  el("heroSummary").classList.toggle("hidden", tab !== "hero");
  el("filterNotice").classList.toggle("hidden", state.rank === "ALL" && state.region === "ALL");
  renderPatchNotice();
  renderPoolEditor();

  const slice = activeSlice();
  if (tab === "map") renderMapTab(slice);
  else if (tab === "hero") renderHeroTab(slice);
  else renderPoolTab(slice);
}

function renderPoolEditor() {
  document.querySelectorAll(".chip").forEach((chip) => {
    const on = pool.has(chip.dataset.hero);
    chip.classList.toggle("selected", on);
    chip.setAttribute("aria-pressed", on);
  });
  const names = [...pool].map((h) => heroName(h));
  el("poolSummary").innerHTML = names.length ? `(${names.length}): ${names.join(", ")}` : "empty, tap to pick heroes";
}

function tableRows(entries, cols, { showHero, showMap }) {
  return entries.map((e) => `
    <tr class="expandable${e.provisional ? " is-prov" : ""}" tabindex="0" aria-expanded="false">${cols.map((col) => col.cell(e)).join("")}</tr>
    <tr class="detail hidden"><td colspan="${cols.length}"><div class="details">${detailsHtml(e, { showHero, showMap })}</div></td></tr>`).join("");
}

function renderTable(cols, entries, opts) {
  el("tableHead").innerHTML = `<tr>${cols.map((c) => `<th class="${c.cls || ""}">${c.label}</th>`).join("")}</tr>`;
  el("tableBody").innerHTML = entries.length
    ? tableRows(entries, cols, opts)
    : `<tr><td colspan="${cols.length}" class="empty-note">No entries for this view.</td></tr>`;
}

const COL = {
  tier: { label: "Tier", cell: (e) => `<td><span class="badge ${e.tier}">${e.tier}</span></td>` },
  hero: { label: "Hero", cell: (e) => `<td><strong>${heroName(e.hero)}</strong>${provTag(e)}</td>` },
  map: { label: "Map", cell: (e) => `<td><strong>${mapName(e.map)}</strong>${provTag(e)}</td>` },
  role: { label: "Role", cls: "col-wide", cell: (e) => `<td class="col-wide"><span class="role-tag ${e.role}">${e.role}</span></td>` },
  mode: { label: "Mode", cls: "col-wide", cell: (e) => `<td class="col-wide"><span class="mode-badge">${e.mode}</span></td>` },
  delta: { label: "Delta WR", cell: (e) => `<td>${deltaCell(e)}</td>` },
  presence: { label: "Presence", cls: "col-wide", cell: (e) => `<td class="col-wide muted">${esc(e.presence)}</td>` },
  archetype: { label: "Archetype", cls: "col-wide", cell: (e) => `<td class="col-wide">${e.archetype}</td>` },
  conf: { label: '<span class="lbl-long">Confidence</span><span class="lbl-short">Conf.</span>', cell: (e) => `<td>${confCell(e)}</td>` },
};

function renderMapTab(slice) {
  let entries = slice.maps[state.map] || [];
  const total = entries.length;
  if (state.role !== "ALL") entries = entries.filter((e) => e.role === state.role);
  if (state.poolonly === "1" && pool.size > 0) entries = entries.filter((e) => pool.has(e.hero));
  el("tableCaption").innerHTML = `<b>${mapName(state.map)}</b> · ${data.map_modes[state.map]} · ${entries.length === total ? `${total} heroes` : `${entries.length} of ${total} heroes`}`;
  renderTable([COL.tier, COL.hero, COL.role, COL.delta, COL.presence, COL.archetype, COL.conf], sortByTier(entries), { showHero: true, showMap: false });
}

function renderHeroTab(slice) {
  const hero = state.hero;
  const hData = slice.heroes[hero] || { role: data.hero_roles[hero] || "Damage", modes: {}, maps: [], volatility: 0, volatility_class: "no data in this view" };

  el("heroName").innerHTML = heroName(hero);
  el("heroRolePill").textContent = hData.role;
  el("heroRolePill").className = `role-pill ${hData.role}`;
  el("heroProv").innerHTML = hData.provisional ? provTag(hData) : "";
  el("heroVol").innerHTML = `Map sensitivity: <strong>${sigmaText(hData)}</strong> <span class="muted">(${hData.volatility_class})</span>`;

  el("modeGrid").innerHTML = MODES.map((m) => {
    const val = hData.modes[m];
    if (val === undefined) return `<div class="mode-card"><h4>${m}</h4><div class="val muted">&ndash;</div></div>`;
    const cls = val >= TIER_INNER ? "pos" : val <= -TIER_INNER ? "neg" : "";
    return `<div class="mode-card"><h4>${m}</h4><div class="val delta ${cls}">${signed(val)}%</div></div>`;
  }).join("");

  el("tableCaption").innerHTML = "";
  renderTable([COL.tier, COL.map, COL.mode, COL.delta, COL.presence, COL.archetype, COL.conf], sortByTier(hData.maps || []), { showHero: false, showMap: true });
}

function volClass(sigma) {
  if (sigma >= 3.0) return "vol-high";
  if (sigma >= TIER_INNER) return "vol-mid";
  return "vol-low";
}

function renderPoolTab(slice) {
  const grid = el("poolGrid");
  const stats = el("poolStats");

  if (pool.size === 0) {
    grid.innerHTML = `<p class="empty-note">Pick heroes in "Your pool" above to build your board.</p>`;
    stats.innerHTML = "";
    return;
  }

  stats.innerHTML = [...pool]
    .filter((h) => state.prole === "ALL" || (data.hero_roles[h] || "Damage") === state.prole)
    .map((h) => ({ hero: h, role: data.hero_roles[h] || "Damage", ...(slice.heroes[h] || { volatility: 0, volatility_class: "" }) }))
    .sort((a, b) => b.volatility - a.volatility)
    .map((h) => `
      <div class="pool-stat-chip">
        <span class="role-tag ${h.role}">${heroName(h.hero)}</span>
        <span class="sigma ${volClass(h.volatility)}">${sigmaText(h)}</span>
      </div>`).join("");

  const modesToShow = state.pmode === "ALL" ? MODES : [state.pmode];

  grid.innerHTML = modesToShow.map((mode) => {
    const maps = data.map_list.filter((m) => data.map_modes[m] === mode)
      .sort((a, b) => data.map_names[a].localeCompare(data.map_names[b]));

    const cards = maps.map((mapSlug) => {
      const entries = (slice.maps[mapSlug] || []).filter((e) => pool.has(e.hero));
      let body = "";

      ROLES.forEach((role) => {
        if (state.prole !== "ALL" && state.prole !== role) return;
        const roleEntries = entries.filter((e) => e.role === role).sort((a, b) => b.delta_wr - a.delta_wr);
        if (roleEntries.length === 0) return;

        body += `<p class="pick-role-label role-tag ${role}">${role}</p>`;
        body += roleEntries.map((e, idx) => {
          const isBest = idx === 0 && e.delta_wr > 0;
          return `
            <div class="pick-row expandable" tabindex="0" aria-expanded="false">
              <span class="name">
                <span class="badge badge-sm ${e.tier}">${e.tier}</span>
                ${heroName(e.hero)}${provTag(e)}
                ${isBest ? `<span class="best-tag ${role}">#1</span>` : ""}
              </span>
              <span class="pick-stats">
                <span class="pick-arch">${e.archetype}</span>
                ${deltaCell(e)}
              </span>
            </div>
            <div class="detail pick-detail hidden">${detailsHtml(e, { showHero: true, showMap: false })}</div>`;
        }).join("");
      });

      if (!body) body = `<p class="empty-note">No pool heroes here.</p>`;
      return `<div class="map-card"><h4>${mapName(mapSlug)}</h4>${body}</div>`;
    }).join("");

    return `<div class="mode-section"><h3>${mode}</h3><div class="map-grid">${cards}</div></div>`;
  }).join("");
}

function openExport() {
  const text = el("exportText");
  el("copyExportBtn").disabled = pool.size === 0;
  if (pool.size === 0) {
    text.value = "Your pool is empty. Pick some heroes on the My pool tab first.";
    el("exportDialog").showModal();
    return;
  }

  const slice = activeSlice();
  const plain = (s) => s.replace(/&#39;/g, "'").replace(/&amp;/g, "&");
  const byRole = { Tank: [], Damage: [], Support: [] };
  pool.forEach((h) => byRole[data.hero_roles[h] || "Damage"].push(plain(heroName(h))));

  let out = "OVERWATCH MAP AFFINITY - OFFLINE CHEAT SHEET\n";
  out += "=".repeat(50) + "\n\n";
  out += "ROSTER\n";
  if (byRole.Tank.length) out += `  Tank:    ${byRole.Tank.join(", ")}\n`;
  if (byRole.Damage.length) out += `  Damage:  ${byRole.Damage.join(", ")}\n`;
  if (byRole.Support.length) out += `  Support: ${byRole.Support.join(", ")}\n`;
  out += "\n";

  MODES.forEach((mode) => {
    out += "-".repeat(50) + "\n";
    out += `${mode.toUpperCase()}\n`;
    out += "-".repeat(50) + "\n";

    data.map_list.filter((m) => data.map_modes[m] === mode)
      .sort((a, b) => data.map_names[a].localeCompare(data.map_names[b]))
      .forEach((mapSlug) => {
        out += `[${plain(mapName(mapSlug))}]\n`;
        const entries = (slice.maps[mapSlug] || []).filter((e) => pool.has(e.hero));
        let any = false;

        ROLES.forEach((role) => {
          const roleEntries = entries.filter((e) => e.role === role).sort((a, b) => b.delta_wr - a.delta_wr);
          if (roleEntries.length === 0) return;
          any = true;
          const parts = roleEntries.map((e, idx) => {
            const tag = idx === 0 && e.delta_wr > 0 ? " [best]" : "";
            return `${plain(heroName(e.hero))}${e.provisional ? "*" : ""}${confidence(e).cls === "low" ? "?" : ""} (${signed(e.delta_wr, 1)}%, ${e.archetype})${tag}`;
          });
          out += `  ${role.padEnd(8)}: ${parts.join(" | ")}\n`;
        });

        if (!any) out += "  (no pool heroes with data here)\n";
        out += "\n";
      });
  });

  out += "* provisional: only current-patch data so far, still settling\n";
  out += "? low confidence: under 50% chance the tier is right\n";
  out += `Data through ${data.meta.data_through}, ${state.scope === "patch" ? patchLabel(data.meta) + " only" : "all seasons"}\n`;

  text.value = out;
  el("exportDialog").showModal();
}

function copyExport() {
  const btn = el("copyExportBtn");
  const done = (label) => {
    btn.textContent = label;
    setTimeout(() => { btn.textContent = "Copy"; }, 1500);
  };
  navigator.clipboard.writeText(el("exportText").value).then(
    () => done("Copied!"),
    () => {
      el("exportText").select();
      done("Press Ctrl+C");
    },
  );
}
