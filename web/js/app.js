const MODES = ["Escort", "Hybrid", "Control", "Push", "Flashpoint"];
const ROLES = ["Tank", "Damage", "Support"];
const TIER_ORDER = { S: 0, A: 1, B: 2, C: 3, D: 4 };

let data = null;
let activeTab = "map";
let poolRoleFilter = "ALL";
let poolModeFilter = "ALL";
// Hero slugs were renamed to match Blizzard's; carry saved pools over.
const LEGACY_SLUGS = { jetpackcat: "jetpack-cat", junkerqueen: "junker-queen", soldier76: "soldier-76", wreckingball: "wrecking-ball" };
let pool = new Set(JSON.parse(localStorage.getItem("owPool") || '["winston","tracer","ana"]').map((h) => LEGACY_SLUGS[h] || h));

const el = (id) => document.getElementById(id);
const fmt = (slug) => slug.replace(/-/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());
const heroName = (slug) => (data && data.hero_names && data.hero_names[slug]) || fmt(slug);
const provTag = (e) => (e.provisional ? '<span class="prov-tag" title="Only current-patch data so far, which is still settling. Expect this to move.">Provisional</span>' : "");
const fmtDate = (iso) => new Date(`${iso}T00:00:00`).toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric" });

fetch("../data/web_data.json")
  .then((r) => r.json())
  .then((json) => {
    data = json;
    expandScopes();
    init();
  });

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
  el("mapSelect").innerHTML = data.map_list.map((m) => `<option value="${m}">${fmt(m)}</option>`).join("");
  el("heroSelect").innerHTML = data.hero_list.map((h) => `<option value="${h}">${heroName(h)}</option>`).join("");

  const buckets = { Tank: el("chipsTank"), Damage: el("chipsDamage"), Support: el("chipsSupport") };
  data.hero_list.forEach((h) => {
    const role = data.hero_roles[h] || "Damage";
    const chip = document.createElement("div");
    chip.className = "chip" + (pool.has(h) ? " selected" : "");
    chip.textContent = heroName(h);
    chip.onclick = () => togglePool(h, chip);
    buckets[role].appendChild(chip);
  });

  bindEvents();
  switchTab(activeTab);
}

function bindEvents() {
  document.querySelectorAll(".tab").forEach((btn) => {
    btn.onclick = () => switchTab(btn.dataset.tab);
  });

  document.querySelectorAll("#poolRoleFilter .chip-toggle").forEach((btn) => {
    btn.onclick = () => {
      poolRoleFilter = btn.dataset.role;
      document.querySelectorAll("#poolRoleFilter .chip-toggle").forEach((b) => b.classList.toggle("active", b === btn));
      render();
    };
  });

  document.querySelectorAll("#poolModeFilter .chip-toggle").forEach((btn) => {
    btn.onclick = () => {
      poolModeFilter = btn.dataset.mode;
      document.querySelectorAll("#poolModeFilter .chip-toggle").forEach((b) => b.classList.toggle("active", b === btn));
      render();
    };
  });

  ["scopeSelect", "rankSelect", "regionSelect", "mapSelect", "roleSelect", "heroSelect", "onlyPoolCheck"].forEach((id) => {
    el(id).addEventListener("change", render);
  });

  el("clearPoolBtn").onclick = () => {
    pool.clear();
    localStorage.removeItem("owPool");
    document.querySelectorAll(".chip").forEach((c) => c.classList.remove("selected"));
    render();
  };

  el("exportBtn").onclick = openExport;
  el("copyExportBtn").onclick = () => {
    navigator.clipboard.writeText(el("exportText").value);
  };
  el("closeExportBtn").onclick = () => el("exportDialog").close();

  el("legendBtn").onclick = () => el("legendDialog").showModal();
  el("closeLegendBtn").onclick = () => el("legendDialog").close();
}

function togglePool(hero, chipEl) {
  if (pool.has(hero)) {
    pool.delete(hero);
    chipEl.classList.remove("selected");
  } else {
    pool.add(hero);
    chipEl.classList.add("selected");
  }
  localStorage.setItem("owPool", JSON.stringify([...pool]));
  render();
}

function switchTab(tab) {
  activeTab = tab;
  document.querySelectorAll(".tab").forEach((b) => b.classList.toggle("active", b.dataset.tab === tab));
  document.querySelectorAll('[data-scope="map"]').forEach((n) => n.classList.toggle("hidden", tab !== "map"));
  document.querySelectorAll('[data-scope="hero"]').forEach((n) => n.classList.toggle("hidden", tab !== "hero"));
  document.querySelectorAll('[data-scope="pool"]').forEach((n) => n.classList.toggle("hidden", tab !== "pool"));
  el("tableView").classList.toggle("hidden", tab === "pool");
  el("poolView").classList.toggle("hidden", tab !== "pool");
  if (tab !== "hero") el("heroSummary").classList.add("hidden");
  render();
}

function activeSlice() {
  const key = `${el("rankSelect").value}_${el("regionSelect").value}`;
  return data.scopes[el("scopeSelect").value][key] || { maps: {}, heroes: {} };
}

// Chance the shown tier is right (tier_p, from the calibrated noise model).
// High = at least 3 in 4, Medium = more likely right than wrong, Low = less.
function confidence(e) {
  if (e.tier_p >= 75) return { level: "High", cls: "high" };
  if (e.tier_p >= 50) return { level: "Medium", cls: "mid" };
  return { level: "Low", cls: "low" };
}

function confTitle(e) {
  const c = confidence(e);
  const raw = `${e.raw_delta_wr > 0 ? "+" : ""}${e.raw_delta_wr.toFixed(2)}%`;
  return `${c.level} confidence: ${e.tier_p}% chance this hero's true value on this map is in tier ${e.tier}. Raw average ${raw} ±${e.ci.toFixed(1)} (95% range, ${e.sample_size} slice${e.sample_size === 1 ? "" : "s"}); the shown value is adjusted for that noise.`;
}

const sigmaText = (h) => (h.volatility_class.startsWith("Too early") ? "&sigma; &ndash;" : `&sigma; ${h.volatility.toFixed(2)}%`);

function confCell(e) {
  const c = confidence(e);
  return `<span class="conf conf-${c.cls}" title="${confTitle(e)}"><span class="conf-dot"></span>${c.level} ${e.tier_p}%</span> <span class="muted">n=${e.sample_size}</span>`;
}

function renderPatchNotice() {
  const m = data.meta;
  const patchOnly = el("scopeSelect").value === "patch";
  el("patchNotice").classList.toggle("hidden", !patchOnly);
  if (patchOnly) {
    el("patchNotice").innerHTML = `<strong>${patchLabel(m)} only</strong>, ${m.days_into_patch} days in. These numbers come from the current patch alone (at most 8 slices per hero-map pair, 1 with a single rank and region picked), so they are much noisier than the all-seasons view${m.mature ? "" : " and still settling"}.`;
  }
}

function renderFilterNotice() {
  const narrow = el("rankSelect").value !== "ALL" || el("regionSelect").value !== "ALL";
  el("filterNotice").classList.toggle("hidden", !narrow);
}

function deltaCell(v, e) {
  const cls = v >= 0 ? "pos" : "neg";
  const sign = v > 0 ? "+" : "";
  const low = e && confidence(e).cls === "low";
  return `<span class="delta ${cls}${low ? " lowconf" : ""}"${e ? ` title="${confTitle(e)}"` : ""}>${sign}${v.toFixed(2)}%</span>`;
}

function sortByTier(entries) {
  return [...entries].sort((a, b) => TIER_ORDER[a.tier] - TIER_ORDER[b.tier] || b.delta_wr - a.delta_wr);
}

function render() {
  if (!data) return;
  const slice = activeSlice();
  renderPatchNotice();
  renderFilterNotice();

  if (activeTab === "map") renderMapTab(slice);
  else if (activeTab === "hero") renderHeroTab(slice);
  else renderPoolTab(slice);
}

function renderMapTab(slice) {
  el("heroSummary").classList.add("hidden");

  const mapSlug = el("mapSelect").value;
  const mode = data.map_modes[mapSlug];
  const role = el("roleSelect").value;
  const onlyPool = el("onlyPoolCheck").checked;

  el("tableHead").innerHTML = `
    <tr>
      <th>Tier</th><th>Hero</th><th>Role</th><th>Mode</th>
      <th>Delta WR</th><th>Presence</th><th>Archetype</th><th>Confidence</th>
    </tr>`;

  let entries = slice.maps[mapSlug] || [];
  if (role !== "ALL") entries = entries.filter((e) => e.role === role);
  if (onlyPool && pool.size > 0) entries = entries.filter((e) => pool.has(e.hero));

  el("tableBody").innerHTML = sortByTier(entries).map((e) => `
    <tr>
      <td><span class="badge ${e.tier}">${e.tier}</span></td>
      <td><strong>${heroName(e.hero)}</strong>${provTag(e)}</td>
      <td><span class="role-tag ${e.role}">${e.role}</span></td>
      <td><span class="mode-badge">${mode}</span></td>
      <td>${deltaCell(e.delta_wr, e)}</td>
      <td class="muted">${e.presence}</td>
      <td>${e.archetype}</td>
      <td>${confCell(e)}</td>
    </tr>`).join("");
}

function renderHeroTab(slice) {
  const hero = el("heroSelect").value;
  const hData = slice.heroes[hero] || { role: data.hero_roles[hero] || "Damage", modes: {}, maps: [], volatility: 0, volatility_class: "no data in this view" };

  el("heroSummary").classList.remove("hidden");
  el("heroName").textContent = heroName(hero);
  el("heroRolePill").textContent = hData.role;
  el("heroRolePill").className = `role-pill ${hData.role}`;
  el("heroProv").innerHTML = hData.provisional ? provTag(hData) : "";
  el("heroVol").innerHTML = `Map sensitivity: <strong>${sigmaText(hData)}</strong> <span class="muted">(${hData.volatility_class})</span>`;

  el("modeGrid").innerHTML = MODES.map((m) => {
    const val = hData.modes[m] ?? 0;
    const cls = val >= 1 ? "pos" : val <= -1 ? "neg" : "";
    return `<div class="mode-card"><h4>${m}</h4><div class="val delta ${cls}">${val > 0 ? "+" : ""}${val.toFixed(2)}%</div></div>`;
  }).join("");

  el("tableHead").innerHTML = `
    <tr>
      <th>Tier</th><th>Map</th><th>Mode</th>
      <th>Delta WR</th><th>Presence</th><th>Archetype</th><th>Confidence</th>
    </tr>`;

  el("tableBody").innerHTML = sortByTier(hData.maps || []).map((e) => `
    <tr>
      <td><span class="badge ${e.tier}">${e.tier}</span></td>
      <td><strong>${fmt(e.map)}</strong>${provTag(e)}</td>
      <td><span class="mode-badge">${e.mode}</span></td>
      <td>${deltaCell(e.delta_wr, e)}</td>
      <td class="muted">${e.presence}</td>
      <td>${e.archetype}</td>
      <td>${confCell(e)}</td>
    </tr>`).join("");
}

function volClass(sigma) {
  if (sigma >= 3.0) return "vol-high";
  if (sigma >= 1.2) return "vol-mid";
  return "vol-low";
}

function renderPoolTab(slice) {
  const grid = el("poolGrid");
  const stats = el("poolStats");

  if (pool.size === 0) {
    grid.innerHTML = `<p class="empty-note">Select heroes in the pool editor above to build your board.</p>`;
    stats.innerHTML = "";
    return;
  }

  const statHeroes = [...pool]
    .filter((h) => poolRoleFilter === "ALL" || (data.hero_roles[h] || "Damage") === poolRoleFilter)
    .map((h) => ({ hero: h, role: data.hero_roles[h] || "Damage", ...(slice.heroes[h] || { volatility: 0, volatility_class: "" }) }))
    .sort((a, b) => b.volatility - a.volatility);

  stats.innerHTML = statHeroes.map((h) => `
    <div class="pool-stat-chip">
      <span class="role-tag ${h.role}">${heroName(h.hero)}</span>
      <span class="sigma ${volClass(h.volatility)}">${sigmaText(h)}</span>
    </div>`).join("");

  const modesToShow = poolModeFilter === "ALL" ? MODES : [poolModeFilter];

  grid.innerHTML = modesToShow.map((mode) => {
    const maps = data.map_list.filter((m) => data.map_modes[m] === mode);

    const cards = maps.map((mapSlug) => {
      const entries = (slice.maps[mapSlug] || []).filter((e) => pool.has(e.hero));
      let body = "";
      let any = false;

      ROLES.forEach((role) => {
        if (poolRoleFilter !== "ALL" && poolRoleFilter !== role) return;
        const roleEntries = entries.filter((e) => e.role === role).sort((a, b) => b.delta_wr - a.delta_wr);
        if (roleEntries.length === 0) return;
        any = true;

        body += `<p class="pick-role-label role-tag ${role}">${role}</p>`;
        body += roleEntries.map((e, idx) => {
          const isBest = idx === 0 && e.delta_wr > 0;
          return `
            <div class="pick-row">
              <span class="name">
                <span class="badge ${e.tier}" style="font-size:.65rem;padding:1px 5px;">${e.tier}</span>
                ${heroName(e.hero)}${provTag(e)}
                ${isBest ? `<span class="best-tag ${role}">#1</span>` : ""}
              </span>
              <span class="pick-stats">
                <span class="pick-arch" title="Presence: ${e.presence}">${e.archetype}</span>
                ${deltaCell(e.delta_wr, e)}
              </span>
            </div>`;
        }).join("");
      });

      if (!any) body = `<p class="empty-note">No pool heroes here.</p>`;

      return `<div class="map-card"><h4>${fmt(mapSlug)}</h4>${body}</div>`;
    }).join("");

    return `<div class="mode-section"><h3>${mode}</h3><div class="map-grid">${cards}</div></div>`;
  }).join("");
}

function openExport() {
  if (pool.size === 0) {
    alert("Add at least one hero to your pool first.");
    return;
  }

  const slice = activeSlice();
  const byRole = { Tank: [], Damage: [], Support: [] };
  pool.forEach((h) => byRole[data.hero_roles[h] || "Damage"].push(heroName(h)));

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

    data.map_list.filter((m) => data.map_modes[m] === mode).forEach((mapSlug) => {
      out += `[${fmt(mapSlug)}]\n`;
      const entries = (slice.maps[mapSlug] || []).filter((e) => pool.has(e.hero));
      let any = false;

      ROLES.forEach((role) => {
        const roleEntries = entries.filter((e) => e.role === role).sort((a, b) => b.delta_wr - a.delta_wr);
        if (roleEntries.length === 0) return;
        any = true;
        const parts = roleEntries.map((e, idx) => {
          const tag = idx === 0 && e.delta_wr > 0 ? " [best]" : "";
          return `${heroName(e.hero)}${e.provisional ? "*" : ""}${confidence(e).cls === "low" ? "?" : ""} (${e.delta_wr > 0 ? "+" : ""}${e.delta_wr.toFixed(1)}%, ${e.archetype})${tag}`;
        });
        out += `  ${role.padEnd(8)}: ${parts.join(" | ")}\n`;
      });

      if (!any) out += "  (no pool heroes with data here)\n";
      out += "\n";
    });
  });

  out += "* provisional: only current-patch data so far, still settling\n";
  out += "? low confidence: under 50% chance the tier is right\n";
  out += `Data through ${data.meta.data_through}, ${el("scopeSelect").value === "patch" ? patchLabel(data.meta) + " only" : "all seasons"}\n`;

  el("exportText").value = out;
  el("exportDialog").showModal();
}
