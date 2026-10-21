import json
import os
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from config import hero_name

BASE = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE, "..", "data")
CSV_DIR = os.path.join(DATA_DIR, "csv")
CHART_DIR = os.path.join(BASE, "..", "charts")

sns.set_theme(style="whitegrid", font="sans-serif")


def load_web_data():
    """web_data.json with the all-seasons scope expanded into
    database[combo]["heroes"][hero] = {role, modes, maps: [entries]}."""
    with open(os.path.join(DATA_DIR, "web_data.json"), encoding="utf-8") as f:
        data = json.load(f)
    data["database"] = data["scopes"]["all"]
    for combo in data["database"].values():
        for hero, hd in combo["heroes"].items():
            hd["role"] = data["hero_roles"][hero]
            hd["maps"] = [e for e in combo["entries"] if e["hero"] == hero]
    return data


def heatmap():
    df = pd.read_csv(os.path.join(CSV_DIR, "map_tierlists.csv"))
    pivot = df.pivot(index="hero", columns="map", values="delta_wr")
    pivot.index = pivot.index.map(hero_name)
    pivot.columns = pivot.columns.str.replace("-", " ").str.title()

    plt.figure(figsize=(22, 16))
    cmap = sns.diverging_palette(10, 133, s=85, l=55, as_cmap=True)
    sns.heatmap(pivot, cmap=cmap, center=0, cbar_kws={"label": "Delta WR (%)", "shrink": 0.8}, linewidths=0.5, linecolor="#f0f0f0")
    plt.title("Hero-Map Affinity Matrix", fontsize=18, fontweight="bold", pad=20)
    plt.xlabel("Map", fontsize=14, fontweight="bold")
    plt.ylabel("Hero", fontsize=14, fontweight="bold")
    plt.xticks(rotation=45, ha="right", fontsize=10)
    plt.yticks(fontsize=9)
    plt.tight_layout()
    plt.savefig(os.path.join(CHART_DIR, "hero_map_heatmap.png"), dpi=300)
    plt.close()
    print("wrote hero_map_heatmap.png")


def volatility_bar():
    df = pd.read_csv(os.path.join(CSV_DIR, "hero_volatility.csv"))
    df = df[~df["classification"].str.startswith("Too early")].sort_values("volatility_sigma")

    plt.figure(figsize=(10, 14))
    colors = ["#2ecc71" if s < 1.2 else "#f39c12" if s < 3.0 else "#e74c3c" for s in df["volatility_sigma"]]
    plt.barh(df["hero"].map(hero_name), df["volatility_sigma"], color=colors, height=0.7)
    plt.axvline(1.2, color="#7f8c8d", linestyle="--", linewidth=1, alpha=0.7)
    plt.axvline(3.0, color="#7f8c8d", linestyle="--", linewidth=1, alpha=0.7)
    plt.title("Hero Map-Sensitivity Index (noise-corrected sigma of Delta WR)", fontsize=14, fontweight="bold", pad=15)
    plt.xlabel("Standard deviation of real map effects (%)")
    plt.ylabel("Hero")
    plt.tight_layout()
    plt.savefig(os.path.join(CHART_DIR, "hero_volatility_bar.png"), dpi=300)
    plt.close()
    print("wrote hero_volatility_bar.png")


def rank_agreement_scatter(data):
    """Masters vs GM+ raw averages per established hero-map pair. The spread
    around the diagonal is what noise alone produces; the split-half test in
    check_rank_region.py found no real rank difference on top of it."""
    master = {(e["hero"], e["map"]): e for e in data["database"]["MASTER_ALL"]["entries"] if not e["provisional"]}
    gm = {(e["hero"], e["map"]): e for e in data["database"]["GRANDMASTER_AND_CHAMPION_ALL"]["entries"] if not e["provisional"]}

    rows = [
        {"role": data["hero_roles"][hero], "masters": master[(hero, m)]["raw_delta_wr"], "gm": gm[(hero, m)]["raw_delta_wr"]}
        for hero, m in master.keys() & gm.keys()
    ]
    df = pd.DataFrame(rows)
    r = df["masters"].corr(df["gm"])
    role_colors = {"Tank": "#3498db", "Damage": "#e74c3c", "Support": "#2ecc71"}

    plt.figure(figsize=(11, 11))
    for role, group in df.groupby("role"):
        plt.scatter(group["masters"], group["gm"], s=14, alpha=0.5, label=role, color=role_colors.get(role, "#999"))

    lim = max(df["masters"].abs().max(), df["gm"].abs().max()) * 1.1
    plt.plot([-lim, lim], [-lim, lim], color="#7f8c8d", linestyle="--", linewidth=1)
    plt.xlim(-lim, lim)
    plt.ylim(-lim, lim)

    plt.xlabel("Raw delta WR in Masters (%)")
    plt.ylabel("Raw delta WR in GM+ (%)")
    plt.title(f"Masters and GM+ agree (r = {r:.2f}, {len(df)} hero-map pairs)", fontsize=14, fontweight="bold", pad=15)
    plt.figtext(0.5, 0.005, "Scatter around the diagonal is sampling noise: a split-half test finds no real rank difference (see report section 2).",
                ha="center", fontsize=8.5, color="#7f8c8d")
    plt.legend(title="Role")
    plt.tight_layout()
    plt.savefig(os.path.join(CHART_DIR, "rank_agreement_scatter.png"), dpi=300)
    plt.close()
    print("wrote rank_agreement_scatter.png")


def archetype_by_role():
    df = pd.read_csv(os.path.join(CSV_DIR, "map_tierlists.csv"))
    web_data = load_web_data()
    df["role"] = df["hero"].map(web_data["hero_roles"])

    counts = df.groupby(["role", "archetype"]).size().unstack(fill_value=0)
    order = ["Meta", "Favorable", "Neutral", "Specialist", "Trap Pick", "Unfavorable", "Deterrent"]
    counts = counts[[c for c in order if c in counts.columns]]

    plt.figure(figsize=(11, 6))
    counts.plot(kind="bar", stacked=True, ax=plt.gca(), colormap="RdYlGn_r", edgecolor="none")
    plt.title("Archetype Distribution by Role", fontsize=14, fontweight="bold", pad=15)
    plt.xlabel("Role")
    plt.ylabel("Hero-Map Entries")
    plt.xticks(rotation=0)
    plt.legend(title="Archetype", bbox_to_anchor=(1.02, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig(os.path.join(CHART_DIR, "archetype_by_role.png"), dpi=300)
    plt.close()
    print("wrote archetype_by_role.png")


def mode_role_matrix(data):
    heroes = data["database"]["ALL_ALL"]["heroes"]
    modes = ["Escort", "Hybrid", "Control", "Push", "Flashpoint"]
    roles = ["Tank", "Damage", "Support"]

    sums = defaultdict(lambda: defaultdict(list))
    for hero, hd in heroes.items():
        for mode, val in hd["modes"].items():
            sums[hd["role"]][mode].append(val)

    matrix = pd.DataFrame(index=roles, columns=modes, dtype=float)
    for role in roles:
        for mode in modes:
            vals = sums[role].get(mode, [])
            matrix.loc[role, mode] = sum(vals) / len(vals) if vals else 0.0

    plt.figure(figsize=(10, 5))
    cmap = sns.diverging_palette(10, 133, s=85, l=55, as_cmap=True)
    sns.heatmap(matrix, cmap=cmap, center=0, annot=True, fmt=".2f", cbar_kws={"label": "Avg Delta WR (%)"}, linewidths=1, linecolor="#f0f0f0")
    plt.title("Average Win Rate Delta by Role and Game Mode", fontsize=14, fontweight="bold", pad=15)
    plt.xlabel("Game Mode")
    plt.ylabel("Role")
    plt.tight_layout()
    plt.savefig(os.path.join(CHART_DIR, "mode_role_matrix.png"), dpi=300)
    plt.close()
    print("wrote mode_role_matrix.png")


def main():
    os.makedirs(CHART_DIR, exist_ok=True)
    data = load_web_data()
    heatmap()
    volatility_bar()
    rank_agreement_scatter(data)
    archetype_by_role()
    mode_role_matrix(data)


if __name__ == "__main__":
    main()
