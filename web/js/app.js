const MODES = ["Escort", "Hybrid", "Control", "Push", "Flashpoint"];
const ROLES = ["Tank", "Damage", "Support"];
const TIER_ORDER = { S: 0, A: 1, B: 2, C: 3, D: 4 };

let data = null;
let activeTab = "map";
let poolRoleFilter = "ALL";
let pool = new Set(JSON.parse(localStorage.getItem("owPool") || '["winston","tracer","ana"]'));

const el = (id) => document.getElementById(id);
const fmt = (slug) => slug.replace(/-/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());

fetch("../data/web_data.json")
  .then((r) => r.json())
  .then((json) => {
    data = json;
    init();
  });

function init() {
  el("mapSelect").innerHTML = data.map_list.map((m) => `<option value="${m}">${fmt(m)}</option>`).join("");
  el("heroSelect").innerHTML = data.hero_list.map((h) => `<option value="${h}">${fmt(h)}</option>`).join("");

  const buckets = { Tank: el("chipsTank"), Damage: el("chipsDamage"), Support: el("chipsSupport") };
  data.hero_list.forEach((h) => {
    const role = data.hero_roles[h] || "Damage";
    const chip = document.createElement("div");
    chip.className = "chip" + (pool.has(h) ? " selected" : "");
    chip.textContent = fmt(h);
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

  ["rankSelect", "regionSelect", "mapSelect", "heroSelect", "onlyPoolCheck"].forEach((id) => {
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
  el("tableView").classList.toggle("hidden", tab === "pool");
  el("poolView").classList.toggle("hidden", tab !== "pool");
  if (tab !== "hero") el("heroSummary").classList.add("hidden");
  render();
}

function activeSlice() {
  const key = `${el("rankSelect").value}_${el("regionSelect").value}`;
  return data.database[key] || { maps: {}, heroes: {} };
}

function rankFlag(skew) {
  if (skew === "Better in GM+") return '<span class="rank-flag gm">Better in GM+</span>';
  if (skew === "Better in Masters") return '<span class="rank-flag master">Better in Masters</span>';
  return '<span class="rank-flag">-</span>';
}

function deltaCell(v) {
  const cls = v >= 0 ? "pos" : "neg";
  const sign = v > 0 ? "+" : "";
  return `<span class="delta ${cls}">${sign}${v.toFixed(2)}%</span>`;
}

function sortByTier(entries) {
  return [...entries].sort((a, b) => TIER_ORDER[a.tier] - TIER_ORDER[b.tier] || b.delta_wr - a.delta_wr);
}

function render() {
  if (!data) return;
  const slice = activeSlice();

  if (activeTab === "map") renderMapTab(slice);
  else if (activeTab === "hero") renderHeroTab(slice);
  else renderPoolTab(slice);
}

function renderMapTab(slice) {
  el("heroSummary").classList.add("hidden");

  const mapSlug = el("mapSelect").value;
  const mode = data.map_modes[mapSlug];
  const onlyPool = el("onlyPoolCheck").checked;

  el("tableHead").innerHTML = `
    <tr>
      <th>Tier</th><th>Hero</th><th>Role</th><th>Mode</th>
      <th>Delta WR</th><th>Presence</th><th>Archetype</th><th>Rank</th><th>n</th>
    </tr>`;

  let entries = slice.maps[mapSlug] || [];
  if (onlyPool && pool.size > 0) entries = entries.filter((e) => pool.has(e.hero));

  el("tableBody").innerHTML = sortByTier(entries).map((e) => `
    <tr>
      <td><span class="badge ${e.tier}">${e.tier}</span></td>
      <td><strong>${fmt(e.hero)}</strong></td>
      <td><span class="role-tag ${e.role}">${e.role}</span></td>
      <td><span class="mode-badge">${mode}</span></td>
      <td>${deltaCell(e.delta_wr)}</td>
      <td class="muted">${e.presence}</td>
      <td>${e.archetype}</td>
      <td>${rankFlag(e.rank_skew)}</td>
      <td class="muted">n=${e.sample_size}</td>
    </tr>`).join("");
}

function renderHeroTab(slice) {
  const hero = el("heroSelect").value;
  const hData = slice.heroes[hero] || { role: "Damage", modes: {}, maps: [], volatility: 0, volatility_class: "" };

  el("heroSummary").classList.remove("hidden");
  el("heroName").textContent = fmt(hero);
  el("heroRolePill").textContent = hData.role;
  el("heroRolePill").className = `role-pill ${hData.role}`;
  el("heroVol").innerHTML = `Map sensitivity: <strong>&sigma; ${hData.volatility.toFixed(2)}%</strong> <span class="muted">(${hData.volatility_class})</span>`;

  el("modeGrid").innerHTML = MODES.map((m) => {
    const val = hData.modes[m] ?? 0;
    const cls = val >= 1 ? "pos" : val <= -1 ? "neg" : "";
    return `<div class="mode-card"><h4>${m}</h4><div class="val delta ${cls}">${val > 0 ? "+" : ""}${val.toFixed(2)}%</div></div>`;
  }).join("");

  el("tableHead").innerHTML = `
    <tr>
      <th>Tier</th><th>Map</th><th>Mode</th>
      <th>Delta WR</th><th>Presence</th><th>Archetype</th><th>Rank</th><th>n</th>
    </tr>`;

  el("tableBody").innerHTML = sortByTier(hData.maps || []).map((e) => `
    <tr>
      <td><span class="badge ${e.tier}">${e.tier}</span></td>
      <td><strong>${fmt(e.map)}</strong></td>
      <td><span class="mode-badge">${e.mode}</span></td>
      <td>${deltaCell(e.delta_wr)}</td>
      <td class="muted">${e.presence}</td>
      <td>${e.archetype}</td>
      <td>${rankFlag(e.rank_skew)}</td>
      <td class="muted">n=${e.sample_size}</td>
    </tr>`).join("");
}

function renderPoolTab(slice) {
  const grid = el("poolGrid");

  if (pool.size === 0) {
    grid.innerHTML = `<p class="empty-note">Select heroes in the pool editor above to build your board.</p>`;
    return;
  }

  grid.innerHTML = MODES.map((mode) => {
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
                ${fmt(e.hero)}
                ${isBest ? `<span class="best-tag ${role}">#1</span>` : ""}
              </span>
              ${deltaCell(e.delta_wr)}
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
  pool.forEach((h) => byRole[data.hero_roles[h] || "Damage"].push(fmt(h)));

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
          return `${fmt(e.hero)} (${e.delta_wr > 0 ? "+" : ""}${e.delta_wr.toFixed(1)}%)${tag}`;
        });
        out += `  ${role.padEnd(8)}: ${parts.join(" | ")}\n`;
      });

      if (!any) out += "  (no pool heroes with data here)\n";
      out += "\n";
    });
  });

  el("exportText").value = out;
  el("exportDialog").showModal();
}
