import json
import os
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BASE = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE, "..", "data")
CSV_DIR = os.path.join(DATA_DIR, "csv")
CHART_DIR = os.path.join(BASE, "..", "charts")

sns.set_theme(style="whitegrid", font="sans-serif")


def fmt(slug):
    return slug.replace("-", " ").title()


def load_web_data():
    with open(os.path.join(DATA_DIR, "web_data.json"), encoding="utf-8") as f:
        return json.load(f)


def heatmap():
    df = pd.read_csv(os.path.join(CSV_DIR, "map_tierlists.csv"))
    pivot = df.pivot(index="hero", columns="map", values="delta_wr")
    pivot.index = pivot.index.str.title()
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
    df = pd.read_csv(os.path.join(CSV_DIR, "hero_volatility.csv")).sort_values("volatility_sigma")

    plt.figure(figsize=(10, 14))
    colors = ["#2ecc71" if s < 1.8 else "#f39c12" if s < 3.0 else "#e74c3c" for s in df["volatility_sigma"]]
    plt.barh(df["hero"].str.title(), df["volatility_sigma"], color=colors, height=0.7)
    plt.axvline(1.8, color="#7f8c8d", linestyle="--", linewidth=1, alpha=0.7)
    plt.axvline(3.0, color="#7f8c8d", linestyle="--", linewidth=1, alpha=0.7)
    plt.title("Hero Map-Sensitivity Index (sigma of Delta WR)", fontsize=14, fontweight="bold", pad=15)
    plt.xlabel("Standard deviation (%)")
    plt.ylabel("Hero")
    plt.tight_layout()
    plt.savefig(os.path.join(CHART_DIR, "hero_volatility_bar.png"), dpi=300)
    plt.close()
    print("wrote hero_volatility_bar.png")


def rank_divergence_scatter(data):
    master = data["database"].get("MASTER_ALL", {}).get("heroes", {})
    gm = data["database"].get("GRANDMASTER_AND_CHAMPION_ALL", {}).get("heroes", {})

    rows = []
    for hero, hd in master.items():
        if hero not in gm:
            continue
        m_by_map = {e["map"]: e["delta_wr"] for e in hd["maps"]}
        gm_by_map = {e["map"]: e["delta_wr"] for e in gm[hero]["maps"]}
        for map_slug, m_val in m_by_map.items():
            if map_slug in gm_by_map:
                rows.append({"hero": hero, "map": map_slug, "role": hd["role"], "masters": m_val, "gm": gm_by_map[map_slug]})

    df = pd.DataFrame(rows)
    df["diff"] = (df["gm"] - df["masters"]).abs()
    role_colors = {"Tank": "#3498db", "Damage": "#e74c3c", "Support": "#2ecc71"}

    plt.figure(figsize=(11, 11))
    for role, group in df.groupby("role"):
        plt.scatter(group["masters"], group["gm"], s=14, alpha=0.5, label=role, color=role_colors.get(role, "#999"))

    lim = max(df["masters"].abs().max(), df["gm"].abs().max()) * 1.1
    plt.plot([-lim, lim], [-lim, lim], color="#7f8c8d", linestyle="--", linewidth=1)
    plt.xlim(-lim, lim)
    plt.ylim(-lim, lim)

    for _, row in df.nlargest(20, "diff").iterrows():
        plt.annotate(
            fmt(row["hero"]),
            (row["masters"], row["gm"]),
            textcoords="offset points", xytext=(5, 4),
            fontsize=7.5, color="#333333",
            bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.65),
        )

    plt.xlabel("Delta WR in Masters (%)")
    plt.ylabel("Delta WR in GM+ (%)")
    plt.title("Rank Divergence: Masters vs GM+ per hero-map pair", fontsize=14, fontweight="bold", pad=15)
    plt.figtext(0.5, 0.005, "Labeled: the 20 hero-map pairs with the biggest Masters/GM+ split", ha="center", fontsize=8.5, color="#7f8c8d")
    plt.legend(title="Role")
    plt.tight_layout()
    plt.savefig(os.path.join(CHART_DIR, "rank_divergence_scatter.png"), dpi=300)
    plt.close()
    print("wrote rank_divergence_scatter.png")


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
    rank_divergence_scatter(data)
    archetype_by_role()
    mode_role_matrix(data)


if __name__ == "__main__":
    main()
