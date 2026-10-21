# Overwatch Map Affinity Report

Timeless per-hero, per-map win rate deltas, computed relative to each hero's baseline win rate in the same rank/region/patch slice, then averaged across every slice collected. Each average is then adjusted for noise: pulled toward the hero's mean in proportion to how much its slices disagree, so thin or inconsistent numbers don't land in extreme tiers by chance. The raw average and its 95% range are listed next to it.

## Contents
1. [Map Sensitivity (Volatility)](#1-map-sensitivity-volatility)
2. [Rank and Region](#2-rank-and-region)
3. [Map Tier Lists](#3-map-tier-lists)

## 1. Map Sensitivity (Volatility)

How much a hero's win rate really varies from map to map: the standard deviation of their map averages, minus the part explained by sampling noise. Map-Agnostic below 1.2 (most maps stay within the B band), Map-Dependent from 3.0 (a third or more of maps reach S or D).

| Hero | Sigma | Class |
|---|---|---|
| Widowmaker | 7.55% | Map-Dependent |
| Lúcio | 4.07% | Map-Dependent |
| Sigma | 3.35% | Map-Dependent |
| Winston | 3.34% | Map-Dependent |
| Junker Queen | 3.22% | Map-Dependent |
| Reinhardt | 3.05% | Map-Dependent |
| Domina | 2.53% | Flexible |
| Ana | 2.38% | Flexible |
| Pharah | 2.37% | Flexible |
| Jetpack Cat | 2.32% | Flexible |
| Zarya | 2.21% | Flexible |
| Hazard | 2.15% | Flexible |
| Wrecking Ball | 2.15% | Flexible |
| Junkrat | 2.14% | Flexible |
| Torbjörn | 2.14% | Flexible |
| Ramattra | 2.00% | Flexible |
| Symmetra | 1.96% | Flexible |
| Mizuki | 1.90% | Flexible |
| Bastion | 1.84% | Flexible |
| Mauga | 1.80% | Flexible |
| Moira | 1.78% | Flexible |
| Brigitte | 1.71% | Flexible |
| Orisa | 1.67% | Flexible |
| Echo | 1.61% | Flexible |
| D.Mon | 1.52% | Flexible |
| Soldier: 76 | 1.51% | Flexible |
| Hanzo | 1.49% | Flexible |
| Tracer | 1.49% | Flexible |
| Kiriko | 1.45% | Flexible |
| Vendetta | 1.43% | Flexible |
| Anran | 1.42% | Flexible |
| Freja | 1.35% | Flexible |
| Sojourn | 1.33% | Flexible |
| Reaper | 1.28% | Flexible |
| Cassidy | 1.23% | Flexible |
| Zenyatta | 1.21% | Flexible |
| Wuyang | 1.18% | Map-Agnostic |
| Mercy | 1.10% | Map-Agnostic |
| Baptiste | 1.08% | Map-Agnostic |
| D.Va | 1.06% | Map-Agnostic |
| Doomfist | 0.98% | Map-Agnostic |
| Mei | 0.92% | Map-Agnostic |
| Shion | 0.90% | Map-Agnostic |
| Ashe | 0.84% | Map-Agnostic |
| Illari | 0.62% | Map-Agnostic |
| Emre | 0.61% | Map-Agnostic |
| Juno | 0.59% | Map-Agnostic |
| Genji | 0.31% | Map-Agnostic |
| Doctrine | - | Too early to tell |
| Lifeweaver | 0.00% | Map-Agnostic |
| Roadhog | - | Too early to tell |
| Sierra | 0.00% | Map-Agnostic |
| Sombra | - | Too early to tell |
| Venture | 0.00% | Map-Agnostic |

---

## 2. Rank and Region

Does a hero's map affinity differ between Masters and GM+, or between regions? Each hero-map pair's slices are split into two independent halves (season first halves vs midseasons) and the gap is measured in each. A real difference would repeat between the halves; noise wouldn't. A difference counts only if the halves correlate with one-sided p < 0.05 over all pairs (region tests share it: 0.0125 each). This rule was fixed on 2026-10-21 and is rerun every season (`analysis/check_rank_region.py`).

| Comparison | Split-half correlation | Pairs | p | Detected |
|---|---|---|---|---|
| rank: GM+ vs Masters | -0.021 | 1526 | 0.7923 | no |
| region: AMER vs rest | -0.010 | 1524 | 0.6523 | no |
| region: EU vs rest | +0.069 | 1526 | 0.0034 | yes |
| region: ASIA vs rest | -0.014 | 1510 | 0.7027 | no |
| region: KOREA vs rest | +0.018 | 1351 | 0.2573 | no |

As of the 2026-10-21 analysis (the table above is recomputed on every run): the rank groups show no detectable difference. Europe shows a small consistent one (a typical hero-map gap of about 1 point), but even for European numbers the all-regions estimate predicts held-out data better than Europe alone, because a quarter of the data adds more noise than the regional difference is worth. The same holds for GM+. So the all-ranks, all-regions view is the most reliable one for everyone.

---

## 3. Map Tier Lists

### Aatlis

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| S | Junker Queen | +3.95% | +4.48% ±2.0 | Map Priority (+81%) | Meta | 51 |
| A | Lúcio | +2.68% | +2.80% ±1.3 | Map Priority (+115%) | Meta | 52 |
| A | Mauga | +2.61% | +3.73% ±2.1 | Popular (+50%) | Meta | 52 |
| A | Anran | +2.08% | +4.00% ±2.5 | Map Priority (+68%) | Meta | 52 |
| A | Junkrat | +1.91% | +2.31% ±1.9 | Standard (+17%) | Favorable | 50 |
| A | Zarya | +1.85% | +2.52% ±2.1 | Popular (+34%) | Meta | 52 |
| A | Reinhardt | +1.63% | +2.10% ±2.8 | Standard (+16%) | Favorable | 50 |
| A | D.Mon | +1.56% | +2.80% ±2.4 | Popular (+24%) | Meta | 16 |
| A | Vendetta | +1.48% | +2.77% ±2.5 | Map Priority (+65%) | Meta | 52 |
| A | Moira | +1.40% | +1.94% ±1.6 | Map Priority (+90%) | Meta | 52 |
| A | Brigitte | +1.31% | +2.17% ±2.3 | Popular (+27%) | Meta | 52 |
| B | Sombra *(provisional)* | +1.03% | +2.99% ±4.2 | Popular (+21%) | Neutral | 8 |
| B | Ramattra | +0.99% | +1.28% ±1.6 | Popular (+38%) | Neutral | 52 |
| B | Mizuki | +0.97% | +1.33% ±2.2 | Map Priority (+61%) | Neutral | 52 |
| B | Cassidy | +0.71% | +1.45% ±2.1 | Popular (+35%) | Neutral | 52 |
| B | Wrecking Ball | +0.71% | +0.82% ±1.4 | Standard (-4%) | Neutral | 51 |
| B | Jetpack Cat | +0.46% | +0.66% ±2.4 | Standard (-8%) | Neutral | 52 |
| B | Shion | +0.45% | +0.83% ±1.3 | Popular (+42%) | Neutral | 28 |
| B | Doomfist | +0.42% | +1.04% ±1.8 | Standard (+17%) | Neutral | 52 |
| B | Sierra | +0.22% | -1.67% ±1.6 | Niche (-29%) | Neutral | 27 |
| B | Hazard | +0.20% | +0.25% ±1.2 | Popular (+35%) | Neutral | 51 |
| B | Lifeweaver | +0.13% | +0.35% ±3.2 | Niche (-39%) | Neutral | 51 |
| B | Reaper | +0.08% | +0.62% ±2.7 | Map Priority (+65%) | Neutral | 52 |
| B | Venture | +0.04% | +1.06% ±2.7 | Map Priority (+57%) | Neutral | 52 |
| B | Torbjörn | +0.03% | +0.05% ±1.9 | Standard (-5%) | Neutral | 50 |
| B | Illari | -0.04% | +0.20% ±1.6 | Niche (-50%) | Neutral | 51 |
| B | Tracer | -0.11% | +0.12% ±2.4 | Popular (+29%) | Neutral | 52 |
| B | Genji | -0.13% | +0.29% ±1.9 | Standard (+5%) | Neutral | 52 |
| B | Kiriko | -0.14% | -0.14% ±0.9 | Popular (+21%) | Neutral | 51 |
| B | Emre | -0.26% | +0.08% ±2.4 | Niche (-45%) | Neutral | 52 |
| B | Mei | -0.28% | -0.47% ±2.2 | Standard (+8%) | Neutral | 52 |
| B | Symmetra | -0.36% | -0.33% ±1.8 | Standard (+8%) | Neutral | 51 |
| B | Sojourn | -0.38% | -0.36% ±2.1 | Standard (+2%) | Neutral | 52 |
| B | Soldier: 76 | -0.38% | -0.39% ±1.8 | Niche (-25%) | Neutral | 51 |
| B | Juno | -0.40% | +0.08% ±1.8 | Standard (+3%) | Neutral | 52 |
| B | Zenyatta | -0.64% | -0.72% ±1.6 | Niche (-46%) | Neutral | 51 |
| B | Mercy | -0.72% | -1.45% ±2.7 | Niche (-40%) | Neutral | 49 |
| B | Baptiste | -0.74% | -1.09% ±3.1 | Niche (-29%) | Neutral | 51 |
| B | Wuyang | -0.99% | -1.67% ±2.1 | Standard (+3%) | Neutral | 52 |
| B | Roadhog *(provisional)* | -1.05% | -2.80% ±6.8 | Standard (+3%) | Neutral | 8 |
| C | Ashe | -1.40% | -3.92% ±3.2 | Niche (-79%) | Deterrent | 37 |
| C | Doctrine *(provisional)* | -1.51% | -2.46% ±3.3 | Standard (-9%) | Unfavorable | 8 |
| C | Domina | -1.55% | -1.81% ±3.8 | Niche (-35%) | Deterrent | 46 |
| C | Bastion | -1.73% | -2.06% ±1.6 | Niche (-26%) | Deterrent | 49 |
| C | D.Va | -1.84% | -3.17% ±2.1 | Niche (-24%) | Deterrent | 52 |
| C | Hanzo | -2.07% | -3.24% ±2.5 | Niche (-50%) | Deterrent | 51 |
| C | Freja | -2.11% | -3.26% ±2.3 | Niche (-56%) | Deterrent | 46 |
| C | Orisa | -2.31% | -2.67% ±1.3 | Standard (+14%) | Unfavorable | 51 |
| C | Echo | -2.91% | -3.61% ±1.8 | Niche (-44%) | Deterrent | 51 |
| D | Ana | -3.38% | -3.98% ±2.1 | Niche (-39%) | Deterrent | 52 |
| D | Pharah | -3.65% | -4.42% ±2.5 | Niche (-21%) | Deterrent | 51 |
| D | Sigma | -4.50% | -5.00% ±2.8 | Niche (-47%) | Deterrent | 52 |
| D | Winston | -4.75% | -5.18% ±2.5 | Niche (-49%) | Deterrent | 51 |
| D | Widowmaker | -19.32% | -24.04% ±8.4 | Niche (-86%) | Deterrent | 9 |

### Antarctic Peninsula

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| S | Cassidy | +3.16% | +3.60% ±0.8 | Popular (+34%) | Meta | 40 |
| A | Junker Queen | +2.77% | +3.08% ±1.8 | Popular (+37%) | Meta | 40 |
| A | Torbjörn | +2.39% | +3.22% ±2.4 | Standard (-3%) | Favorable | 40 |
| A | Ramattra | +2.03% | +2.40% ±1.4 | Popular (+22%) | Meta | 40 |
| A | Symmetra | +1.76% | +2.19% ±1.7 | Standard (+20%) | Favorable | 40 |
| A | Mauga | +1.66% | +2.20% ±1.7 | Popular (+23%) | Meta | 40 |
| A | Zarya | +1.54% | +1.84% ±1.5 | Popular (+22%) | Meta | 40 |
| A | Bastion | +1.53% | +1.71% ±1.2 | Standard (-12%) | Favorable | 39 |
| A | Moira | +1.45% | +1.76% ±1.2 | Popular (+30%) | Meta | 40 |
| A | Reinhardt | +1.45% | +1.57% ±1.5 | Standard (+15%) | Favorable | 40 |
| A | Tracer | +1.28% | +1.46% ±0.9 | Standard (+20%) | Favorable | 40 |
| A | Domina | +1.23% | +1.73% ±2.3 | Niche (-26%) | Specialist | 39 |
| B | Kiriko | +1.17% | +1.26% ±0.8 | Standard (+11%) | Neutral | 40 |
| B | Soldier: 76 | +0.92% | +1.17% ±1.3 | Standard (-7%) | Neutral | 40 |
| B | Brigitte | +0.74% | +0.96% ±1.4 | Standard (+10%) | Neutral | 40 |
| B | Mizuki | +0.60% | +0.69% ±1.5 | Popular (+29%) | Neutral | 40 |
| B | Orisa | +0.54% | +0.72% ±1.8 | Standard (+18%) | Neutral | 40 |
| B | Wuyang | +0.53% | +0.64% ±0.9 | Standard (+7%) | Neutral | 40 |
| B | Vendetta | +0.51% | +0.76% ±1.7 | Standard (+17%) | Neutral | 37 |
| B | Baptiste | +0.41% | +0.98% ±1.6 | Standard (-14%) | Neutral | 40 |
| B | Illari | +0.30% | +1.29% ±1.8 | Niche (-29%) | Neutral | 40 |
| B | Sierra | +0.22% | -0.89% ±2.1 | Standard (-11%) | Neutral | 31 |
| B | Mei | +0.18% | +0.57% ±2.0 | Standard (+3%) | Neutral | 40 |
| B | Lifeweaver | +0.13% | +0.96% ±2.2 | Niche (-25%) | Neutral | 40 |
| B | Reaper | +0.06% | +0.25% ±1.6 | Popular (+22%) | Neutral | 40 |
| B | D.Mon | +0.04% | +0.32% ±2.4 | Popular (+24%) | Neutral | 16 |
| B | Venture | +0.04% | -1.50% ±1.8 | Standard (+8%) | Neutral | 39 |
| B | Zenyatta | +0.03% | +0.17% ±1.3 | Niche (-24%) | Neutral | 40 |
| B | Doomfist | -0.17% | -0.10% ±1.5 | Standard (+1%) | Neutral | 40 |
| B | Sojourn | -0.18% | -0.15% ±0.9 | Standard (+1%) | Neutral | 40 |
| B | Lúcio | -0.27% | -0.22% ±1.4 | Popular (+48%) | Neutral | 40 |
| B | Roadhog *(provisional)* | -0.37% | -0.23% ±7.3 | Standard (+3%) | Neutral | 8 |
| B | Anran | -0.45% | -0.59% ±2.4 | Standard (+16%) | Neutral | 39 |
| B | Genji | -0.52% | -1.77% ±1.1 | Standard (-7%) | Neutral | 40 |
| B | Emre | -0.53% | -0.77% ±1.4 | Niche (-29%) | Neutral | 40 |
| B | Hanzo | -0.61% | -0.68% ±1.9 | Niche (-42%) | Neutral | 40 |
| B | Freja | -0.66% | -0.75% ±2.2 | Niche (-30%) | Neutral | 40 |
| B | Shion | -0.69% | -0.83% ±1.0 | Popular (+36%) | Neutral | 28 |
| B | Ashe | -0.71% | -0.66% ±1.6 | Niche (-59%) | Neutral | 40 |
| B | Juno | -0.71% | -1.05% ±2.0 | Standard (+9%) | Neutral | 40 |
| B | Mercy | -0.90% | -1.62% ±2.2 | Niche (-22%) | Neutral | 39 |
| B | Echo | -0.94% | -1.00% ±1.4 | Niche (-30%) | Neutral | 40 |
| B | Wrecking Ball | -1.18% | -1.28% ±1.5 | Standard (-4%) | Neutral | 40 |
| C | D.Va | -1.22% | -1.82% ±2.0 | Standard (-18%) | Unfavorable | 40 |
| C | Sombra *(provisional)* | -1.24% | -1.72% ±4.7 | Standard (+14%) | Unfavorable | 8 |
| C | Doctrine *(provisional)* | -1.34% | -2.41% ±3.8 | Standard (-2%) | Unfavorable | 8 |
| C | Jetpack Cat | -1.41% | -1.52% ±1.3 | Standard (-6%) | Unfavorable | 40 |
| C | Sigma | -1.71% | -1.70% ±1.3 | Niche (-23%) | Deterrent | 40 |
| C | Ana | -1.78% | -1.83% ±0.9 | Standard (-19%) | Unfavorable | 40 |
| C | Junkrat | -2.12% | -2.70% ±2.2 | Standard (-5%) | Unfavorable | 40 |
| C | Hazard | -2.30% | -2.44% ±1.2 | Standard (+8%) | Unfavorable | 40 |
| C | Winston | -2.81% | -2.85% ±1.2 | Niche (-38%) | Deterrent | 40 |
| D | Pharah | -4.04% | -4.50% ±1.8 | Standard (-14%) | Unfavorable | 40 |
| D | Widowmaker | -9.23% | -9.32% ±2.0 | Niche (-77%) | Deterrent | 34 |

### Blizzard World

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| A | Doctrine *(provisional)* | +1.80% | +8.41% ±7.7 | Standard (+4%) | Favorable | 8 |
| B | Wrecking Ball | +0.96% | +1.51% ±2.7 | Popular (+20%) | Neutral | 51 |
| B | Anran | +0.60% | +2.13% ±3.7 | Standard (-15%) | Neutral | 51 |
| B | D.Va | +0.47% | +1.34% ±1.9 | Standard (+10%) | Neutral | 52 |
| B | Jetpack Cat | +0.46% | +0.86% ±3.4 | Standard (-6%) | Neutral | 52 |
| B | Winston | +0.37% | +0.48% ±1.5 | Popular (+26%) | Neutral | 52 |
| B | Sojourn | +0.32% | +0.57% ±1.5 | Standard (+7%) | Neutral | 52 |
| B | Sierra | +0.22% | -3.02% ±4.1 | Popular (+31%) | Neutral | 38 |
| B | Sombra *(provisional)* | +0.17% | +4.18% ±8.1 | Standard (-2%) | Neutral | 8 |
| B | Ana | +0.14% | +0.22% ±1.7 | Standard (+17%) | Neutral | 52 |
| B | Lifeweaver | +0.13% | +0.15% ±3.6 | Standard (+13%) | Neutral | 52 |
| B | Venture | +0.04% | +3.37% ±3.7 | Standard (-9%) | Neutral | 50 |
| B | Wuyang | +0.04% | +0.10% ±1.3 | Standard (+3%) | Neutral | 52 |
| B | D.Mon | +0.02% | +2.32% ±7.1 | Standard (-11%) | Neutral | 16 |
| B | Bastion | -0.10% | -0.16% ±2.7 | Standard (+0%) | Neutral | 51 |
| B | Illari | -0.17% | -0.16% ±1.5 | Standard (+18%) | Neutral | 52 |
| B | Roadhog *(provisional)* | -0.18% | +1.21% ±10.1 | Popular (+22%) | Neutral | 8 |
| B | Mercy | -0.21% | -0.18% ±2.9 | Standard (+14%) | Neutral | 51 |
| B | Orisa | -0.21% | -0.28% ±2.7 | Standard (-8%) | Neutral | 52 |
| B | Genji | -0.27% | -0.93% ±1.6 | Standard (-5%) | Neutral | 52 |
| B | Mei | -0.29% | -0.69% ±3.2 | Standard (-5%) | Neutral | 51 |
| B | Emre | -0.33% | -0.28% ±2.2 | Standard (+18%) | Neutral | 52 |
| B | Juno | -0.45% | +0.78% ±3.4 | Standard (-15%) | Neutral | 51 |
| B | Shion | -0.45% | -0.88% ±2.7 | Standard (-14%) | Neutral | 28 |
| B | Widowmaker | -0.48% | -0.42% ±1.7 | Map Priority (+85%) | Neutral | 52 |
| B | Ashe | -0.74% | -0.71% ±1.8 | Popular (+28%) | Neutral | 52 |
| B | Zenyatta | -0.84% | -1.05% ±1.7 | Standard (+16%) | Neutral | 51 |
| B | Reaper | -0.86% | -1.57% ±3.1 | Niche (-24%) | Neutral | 52 |
| B | Freja | -0.90% | -1.20% ±2.5 | Standard (+13%) | Neutral | 50 |
| B | Echo | -0.92% | -1.21% ±3.2 | Niche (-28%) | Neutral | 52 |
| B | Doomfist | -0.97% | -2.07% ±2.5 | Standard (+0%) | Neutral | 52 |
| B | Hanzo | -1.13% | -1.52% ±2.2 | Popular (+20%) | Neutral | 52 |
| B | Kiriko | -1.16% | -1.49% ±1.6 | Standard (-5%) | Neutral | 52 |
| C | Sigma | -1.22% | -1.19% ±1.6 | Popular (+23%) | Trap Pick | 52 |
| C | Soldier: 76 | -1.25% | -1.74% ±2.2 | Standard (+3%) | Unfavorable | 52 |
| C | Symmetra | -1.27% | -1.83% ±3.3 | Standard (-11%) | Unfavorable | 51 |
| C | Baptiste | -1.37% | -2.77% ±2.8 | Standard (-5%) | Unfavorable | 52 |
| C | Tracer | -1.57% | -1.95% ±1.7 | Standard (+2%) | Unfavorable | 52 |
| C | Cassidy | -1.66% | -1.99% ±1.2 | Standard (-20%) | Unfavorable | 52 |
| C | Domina | -1.90% | -2.14% ±2.8 | Standard (+11%) | Unfavorable | 51 |
| C | Vendetta | -2.21% | -4.59% ±3.0 | Standard (-15%) | Unfavorable | 44 |
| C | Pharah | -2.58% | -3.60% ±3.7 | Niche (-38%) | Deterrent | 52 |
| C | Zarya | -2.62% | -3.49% ±3.1 | Standard (-18%) | Unfavorable | 51 |
| C | Junkrat | -2.82% | -5.35% ±4.0 | Niche (-22%) | Deterrent | 52 |
| D | Hazard | -3.07% | -4.47% ±3.1 | Niche (-27%) | Deterrent | 51 |
| D | Mauga | -3.21% | -5.25% ±3.1 | Niche (-20%) | Deterrent | 50 |
| D | Moira | -3.42% | -5.26% ±3.1 | Niche (-25%) | Deterrent | 52 |
| D | Mizuki | -3.52% | -4.79% ±2.2 | Standard (-19%) | Unfavorable | 52 |
| D | Ramattra | -3.72% | -5.78% ±3.3 | Niche (-22%) | Deterrent | 49 |
| D | Brigitte | -4.08% | -6.24% ±2.6 | Standard (-7%) | Unfavorable | 52 |
| D | Junker Queen | -4.13% | -5.14% ±3.6 | Niche (-26%) | Deterrent | 43 |
| D | Reinhardt | -4.21% | -5.81% ±4.0 | Standard (-16%) | Unfavorable | 52 |
| D | Torbjörn | -4.42% | -6.95% ±3.2 | Standard (+14%) | Unfavorable | 50 |
| D | Lúcio | -6.65% | -7.09% ±2.5 | Niche (-41%) | Deterrent | 51 |

### Busan

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| A | Soldier: 76 | +1.81% | +3.33% ±2.5 | Popular (+35%) | Meta | 16 |
| B | Junker Queen | +1.09% | +2.10% ±4.3 | Standard (+19%) | Neutral | 16 |
| B | Mauga | +1.06% | +1.90% ±2.5 | Standard (+15%) | Neutral | 16 |
| B | Widowmaker | +0.95% | +1.17% ±2.9 | Standard (-2%) | Neutral | 16 |
| B | Roadhog *(provisional)* | +0.94% | +4.98% ±7.1 | Standard (+0%) | Neutral | 8 |
| B | Cassidy | +0.93% | +1.57% ±1.7 | Standard (+11%) | Neutral | 16 |
| B | Moira | +0.88% | +2.29% ±3.0 | Popular (+20%) | Neutral | 16 |
| B | Freja | +0.80% | +2.81% ±3.2 | Niche (-31%) | Neutral | 16 |
| B | Zenyatta | +0.68% | +1.78% ±2.3 | Standard (-12%) | Neutral | 16 |
| B | Anran | +0.66% | +2.07% ±3.4 | Standard (+9%) | Neutral | 15 |
| B | Echo | +0.53% | +2.23% ±3.8 | Niche (-49%) | Neutral | 16 |
| B | Zarya | +0.38% | +0.87% ±2.7 | Standard (-10%) | Neutral | 16 |
| B | Kiriko | +0.36% | +0.51% ±1.6 | Standard (+7%) | Neutral | 16 |
| B | Emre | +0.25% | +3.02% ±2.6 | Standard (-5%) | Neutral | 16 |
| B | Sierra | +0.22% | -2.90% ±4.3 | Standard (-11%) | Neutral | 10 |
| B | Reinhardt | +0.17% | +0.48% ±4.0 | Standard (-1%) | Neutral | 16 |
| B | Lifeweaver | +0.13% | +4.67% ±4.9 | Standard (-20%) | Neutral | 16 |
| B | D.Va | +0.11% | +1.31% ±2.8 | Standard (+8%) | Neutral | 16 |
| B | Illari | +0.11% | +1.02% ±2.1 | Niche (-33%) | Neutral | 16 |
| B | Mizuki | +0.08% | +0.12% ±2.2 | Standard (+18%) | Neutral | 16 |
| B | Venture | +0.04% | +1.93% ±3.6 | Standard (-9%) | Neutral | 16 |
| B | Vendetta | +0.00% | +0.24% ±3.1 | Standard (+12%) | Neutral | 16 |
| B | Wrecking Ball | -0.02% | +0.14% ±2.8 | Popular (+37%) | Neutral | 16 |
| B | Tracer | -0.05% | +0.08% ±1.6 | Popular (+26%) | Neutral | 16 |
| B | Reaper | -0.08% | +0.29% ±2.8 | Standard (+4%) | Neutral | 16 |
| B | Orisa | -0.12% | -0.13% ±2.5 | Standard (+2%) | Neutral | 16 |
| B | Winston | -0.14% | +0.08% ±2.4 | Standard (-6%) | Neutral | 16 |
| B | Mercy | -0.15% | +0.20% ±4.5 | Niche (-23%) | Neutral | 13 |
| B | Sojourn | -0.16% | -0.02% ±1.9 | Standard (-6%) | Neutral | 16 |
| B | Genji | -0.25% | -1.85% ±2.8 | Standard (-9%) | Neutral | 16 |
| B | D.Mon | -0.28% | -0.23% ±2.1 | Popular (+22%) | Neutral | 16 |
| B | Wuyang | -0.28% | -0.33% ±1.8 | Standard (-0%) | Neutral | 16 |
| B | Pharah | -0.31% | -0.05% ±2.8 | Niche (-52%) | Neutral | 16 |
| B | Ana | -0.39% | -0.38% ±1.6 | Standard (-6%) | Neutral | 16 |
| B | Mei | -0.47% | -1.72% ±3.6 | Standard (-20%) | Neutral | 16 |
| B | Sombra *(provisional)* | -0.47% | +0.00% ±4.5 | Standard (+15%) | Neutral | 8 |
| B | Symmetra | -0.48% | -0.47% ±3.9 | Standard (+13%) | Neutral | 16 |
| B | Shion | -0.49% | -0.73% ±1.8 | Popular (+27%) | Neutral | 16 |
| B | Juno | -0.55% | -0.26% ±2.8 | Standard (-7%) | Neutral | 16 |
| B | Torbjörn | -0.62% | -1.16% ±4.2 | Standard (-8%) | Neutral | 16 |
| B | Doomfist | -0.66% | -1.39% ±2.7 | Standard (+4%) | Neutral | 16 |
| B | Hazard | -0.71% | -0.77% ±2.5 | Standard (-1%) | Neutral | 16 |
| B | Ashe | -0.73% | -0.62% ±3.1 | Niche (-35%) | Neutral | 16 |
| B | Baptiste | -0.73% | -1.03% ±3.1 | Niche (-28%) | Neutral | 16 |
| B | Bastion | -0.73% | -1.52% ±3.7 | Standard (-17%) | Neutral | 16 |
| B | Domina | -1.10% | -1.09% ±4.3 | Niche (-29%) | Neutral | 15 |
| C | Hanzo | -1.24% | -2.83% ±4.1 | Niche (-46%) | Deterrent | 16 |
| C | Jetpack Cat | -1.25% | -1.70% ±3.0 | Standard (+8%) | Unfavorable | 16 |
| C | Ramattra | -1.28% | -1.64% ±3.5 | Standard (-19%) | Unfavorable | 16 |
| C | Brigitte | -1.50% | -2.23% ±2.9 | Standard (+15%) | Unfavorable | 16 |
| C | Sigma | -1.65% | -1.64% ±2.5 | Niche (-34%) | Deterrent | 16 |
| C | Doctrine *(provisional)* | -1.76% | -2.71% ±3.1 | Standard (-1%) | Unfavorable | 8 |
| C | Lúcio | -1.87% | -1.85% ±2.9 | Popular (+26%) | Trap Pick | 16 |
| D | Junkrat | -3.19% | -7.87% ±5.1 | Niche (-31%) | Deterrent | 16 |

### Circuit Royal

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| S | Sigma | +7.45% | +8.02% ±1.6 | Map Priority (+150%) | Meta | 52 |
| S | Domina | +5.64% | +6.60% ±1.9 | Map Priority (+153%) | Meta | 52 |
| S | Widowmaker | +5.63% | +5.92% ±2.5 | Map Priority (+125%) | Meta | 52 |
| S | Doctrine *(provisional)* | +3.09% | +6.31% ±4.1 | Standard (+6%) | Favorable | 8 |
| A | Bastion | +2.61% | +4.27% ±2.9 | Map Priority (+60%) | Meta | 52 |
| A | Sojourn | +1.88% | +2.47% ±1.3 | Map Priority (+70%) | Meta | 52 |
| A | Symmetra | +1.68% | +2.48% ±2.3 | Standard (+9%) | Favorable | 51 |
| B | Mizuki | +1.20% | +1.91% ±2.8 | Niche (-49%) | Neutral | 51 |
| B | Mei | +1.19% | +3.29% ±2.3 | Map Priority (+82%) | Neutral | 51 |
| B | Reinhardt | +1.16% | +1.43% ±2.4 | Popular (+22%) | Neutral | 51 |
| B | Juno | +1.11% | +4.14% ±1.5 | Map Priority (+86%) | Neutral | 52 |
| B | Roadhog *(provisional)* | +1.01% | +7.51% ±8.8 | Niche (-34%) | Neutral | 8 |
| B | Zenyatta | +0.96% | +1.65% ±1.6 | Map Priority (+110%) | Neutral | 52 |
| B | Ramattra | +0.91% | +1.12% ±1.4 | Map Priority (+129%) | Neutral | 51 |
| B | Orisa | +0.78% | +1.26% ±2.4 | Standard (+15%) | Neutral | 51 |
| B | Illari | +0.75% | +1.85% ±1.3 | Map Priority (+69%) | Neutral | 52 |
| B | Baptiste | +0.62% | +2.30% ±2.5 | Map Priority (+114%) | Neutral | 52 |
| B | Hanzo | +0.34% | +0.71% ±2.0 | Map Priority (+128%) | Neutral | 52 |
| B | Sierra | +0.22% | +2.45% ±1.8 | Map Priority (+58%) | Neutral | 39 |
| B | Lifeweaver | +0.13% | -0.27% ±2.5 | Popular (+25%) | Neutral | 51 |
| B | Wuyang | +0.07% | +0.33% ±2.3 | Standard (+1%) | Neutral | 52 |
| B | Venture | +0.04% | -1.00% ±3.1 | Standard (-20%) | Neutral | 52 |
| B | Reaper | -0.10% | +0.58% ±3.8 | Niche (-57%) | Neutral | 52 |
| B | Mercy | -0.13% | +0.02% ±2.6 | Popular (+23%) | Neutral | 51 |
| B | Genji | -0.15% | +0.05% ±2.0 | Standard (-6%) | Neutral | 52 |
| B | Emre | -0.19% | +0.28% ±2.1 | Map Priority (+63%) | Neutral | 52 |
| B | Ana | -0.41% | -0.41% ±1.4 | Standard (+20%) | Neutral | 52 |
| B | Freja | -0.50% | -0.47% ±2.4 | Map Priority (+113%) | Neutral | 52 |
| B | Ashe | -0.55% | -0.02% ±2.6 | Map Priority (+83%) | Neutral | 52 |
| B | Cassidy | -0.67% | -0.87% ±1.8 | Niche (-59%) | Neutral | 51 |
| B | Vendetta | -0.78% | -1.67% ±3.5 | Niche (-39%) | Neutral | 35 |
| B | Wrecking Ball | -1.07% | -1.41% ±3.0 | Niche (-42%) | Neutral | 50 |
| C | Zarya | -1.22% | -1.29% ±1.9 | Standard (+9%) | Unfavorable | 52 |
| C | Doomfist | -1.35% | -4.16% ±3.1 | Niche (-23%) | Deterrent | 52 |
| C | Junkrat | -1.40% | -1.72% ±2.1 | Standard (+4%) | Unfavorable | 52 |
| C | D.Va | -1.57% | -3.46% ±2.8 | Niche (-43%) | Deterrent | 52 |
| C | D.Mon | -1.65% | -4.38% ±4.4 | Niche (-34%) | Deterrent | 16 |
| C | Moira | -1.65% | -2.31% ±3.6 | Niche (-39%) | Deterrent | 51 |
| C | Soldier: 76 | -1.77% | -2.50% ±2.1 | Niche (-27%) | Deterrent | 51 |
| C | Anran | -1.78% | -3.09% ±2.6 | Niche (-48%) | Deterrent | 41 |
| C | Jetpack Cat | -1.86% | -2.54% ±2.9 | Niche (-25%) | Deterrent | 52 |
| C | Torbjörn | -1.93% | -3.15% ±3.4 | Standard (-18%) | Unfavorable | 50 |
| C | Shion | -2.07% | -4.18% ±1.9 | Niche (-67%) | Deterrent | 28 |
| C | Echo | -2.40% | -3.11% ±2.0 | Standard (-15%) | Unfavorable | 51 |
| C | Pharah | -2.55% | -3.09% ±2.7 | Popular (+43%) | Trap Pick | 51 |
| C | Kiriko | -2.78% | -3.63% ±1.6 | Niche (-39%) | Deterrent | 52 |
| C | Sombra *(provisional)* | -2.99% | -14.20% ±9.4 | Niche (-51%) | Deterrent | 8 |
| D | Mauga | -3.54% | -4.78% ±2.3 | Niche (-39%) | Deterrent | 47 |
| D | Brigitte | -4.19% | -6.47% ±2.6 | Niche (-71%) | Deterrent | 48 |
| D | Tracer | -4.55% | -6.33% ±1.9 | Niche (-79%) | Deterrent | 51 |
| D | Hazard | -5.45% | -8.40% ±3.3 | Niche (-67%) | Deterrent | 43 |
| D | Junker Queen | -6.53% | -8.44% ±3.7 | Niche (-51%) | Deterrent | 35 |
| D | Winston | -8.81% | -9.57% ±2.2 | Niche (-61%) | Deterrent | 51 |
| D | Lúcio | -9.30% | -9.93% ±2.4 | Niche (-73%) | Deterrent | 43 |

### Colosseo

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| S | Reinhardt | +3.95% | +4.49% ±2.1 | Standard (+5%) | Favorable | 51 |
| A | Lúcio | +2.60% | +2.89% ±2.0 | Standard (+17%) | Favorable | 52 |
| A | Torbjörn | +2.09% | +2.83% ±2.5 | Standard (-6%) | Favorable | 51 |
| A | Jetpack Cat | +2.08% | +2.57% ±2.1 | Standard (+3%) | Favorable | 52 |
| A | Junkrat | +2.07% | +2.76% ±2.4 | Standard (-17%) | Favorable | 51 |
| A | Doomfist | +1.74% | +3.12% ±1.6 | Standard (+10%) | Favorable | 52 |
| A | Tracer | +1.61% | +1.85% ±1.0 | Popular (+24%) | Meta | 52 |
| A | Anran | +1.42% | +2.48% ±2.2 | Standard (+5%) | Favorable | 49 |
| A | Sombra *(provisional)* | +1.25% | +4.38% ±5.0 | Standard (+11%) | Favorable | 8 |
| B | Junker Queen | +1.19% | +1.37% ±1.8 | Popular (+22%) | Neutral | 50 |
| B | Vendetta | +1.08% | +3.20% ±3.6 | Standard (+1%) | Neutral | 47 |
| B | Winston | +0.97% | +1.17% ±1.8 | Standard (+0%) | Neutral | 52 |
| B | Sojourn | +0.90% | +1.61% ±1.9 | Standard (+17%) | Neutral | 52 |
| B | Hazard | +0.77% | +0.90% ±1.3 | Standard (+2%) | Neutral | 51 |
| B | Shion | +0.67% | +1.08% ±1.2 | Popular (+25%) | Neutral | 28 |
| B | Freja | +0.61% | +1.25% ±1.9 | Niche (-22%) | Neutral | 51 |
| B | Kiriko | +0.61% | +0.84% ±1.6 | Standard (+5%) | Neutral | 52 |
| B | Wuyang | +0.57% | +1.24% ±2.2 | Standard (+5%) | Neutral | 52 |
| B | Illari | +0.53% | +1.15% ±1.1 | Standard (-8%) | Neutral | 52 |
| B | Wrecking Ball | +0.52% | +0.81% ±2.4 | Standard (+18%) | Neutral | 52 |
| B | Mercy | +0.42% | +1.59% ±2.9 | Standard (-11%) | Neutral | 51 |
| B | Mei | +0.37% | +1.17% ±2.2 | Niche (-31%) | Neutral | 51 |
| B | Echo | +0.22% | +0.48% ±1.7 | Standard (-14%) | Neutral | 52 |
| B | Sierra | +0.22% | +1.05% ±3.6 | Standard (-6%) | Neutral | 36 |
| B | Soldier: 76 | +0.18% | +0.58% ±2.6 | Standard (+11%) | Neutral | 52 |
| B | D.Mon | +0.15% | +0.60% ±2.7 | Standard (+17%) | Neutral | 16 |
| B | Hanzo | +0.13% | +0.37% ±1.9 | Niche (-38%) | Neutral | 51 |
| B | Lifeweaver | +0.13% | +0.93% ±3.2 | Standard (-2%) | Neutral | 51 |
| B | Mizuki | +0.06% | +0.07% ±1.0 | Standard (+9%) | Neutral | 52 |
| B | Venture | +0.04% | -0.47% ±3.6 | Standard (-8%) | Neutral | 52 |
| B | Juno | -0.15% | +0.67% ±1.6 | Standard (+4%) | Neutral | 51 |
| B | Genji | -0.16% | -0.06% ±2.2 | Standard (-8%) | Neutral | 52 |
| B | Zenyatta | -0.16% | +0.18% ±2.5 | Standard (-17%) | Neutral | 52 |
| B | Brigitte | -0.49% | -0.48% ±2.2 | Standard (-1%) | Neutral | 52 |
| B | Emre | -0.55% | -1.11% ±2.0 | Standard (+4%) | Neutral | 52 |
| B | Zarya | -0.67% | -0.60% ±2.5 | Standard (-3%) | Neutral | 52 |
| B | Mauga | -0.84% | -0.90% ±1.8 | Standard (+10%) | Neutral | 51 |
| B | Ashe | -0.89% | -0.99% ±1.5 | Niche (-30%) | Neutral | 51 |
| B | Roadhog *(provisional)* | -0.89% | -2.19% ±6.8 | Standard (-5%) | Neutral | 8 |
| B | Reaper | -0.92% | -1.63% ±2.9 | Standard (-8%) | Neutral | 52 |
| B | Pharah | -0.95% | -0.93% ±3.1 | Standard (-5%) | Neutral | 52 |
| B | Doctrine *(provisional)* | -1.15% | -2.41% ±4.5 | Standard (+3%) | Neutral | 8 |
| C | D.Va | -1.31% | -3.05% ±3.1 | Standard (-8%) | Unfavorable | 52 |
| C | Moira | -1.39% | -1.56% ±2.4 | Standard (+3%) | Unfavorable | 51 |
| C | Bastion | -1.45% | -1.88% ±1.9 | Standard (-18%) | Unfavorable | 49 |
| C | Baptiste | -1.48% | -2.19% ±1.9 | Niche (-26%) | Deterrent | 52 |
| C | Cassidy | -1.51% | -1.92% ±1.4 | Standard (+2%) | Unfavorable | 52 |
| C | Ramattra | -1.91% | -2.34% ±2.5 | Standard (-20%) | Unfavorable | 50 |
| C | Symmetra | -2.35% | -3.63% ±3.2 | Niche (-32%) | Deterrent | 43 |
| C | Orisa | -2.49% | -2.83% ±1.2 | Standard (-2%) | Unfavorable | 51 |
| C | Ana | -2.80% | -2.88% ±0.9 | Standard (-6%) | Unfavorable | 52 |
| D | Sigma | -3.50% | -3.71% ±2.2 | Niche (-25%) | Deterrent | 52 |
| D | Domina | -3.68% | -4.56% ±2.9 | Standard (-16%) | Unfavorable | 48 |
| D | Widowmaker | -4.57% | -4.56% ±2.7 | Niche (-22%) | Deterrent | 52 |

### Dorado

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| S | Ana | +4.05% | +4.87% ±2.0 | Standard (+19%) | Favorable | 52 |
| S | Winston | +3.88% | +4.29% ±1.8 | Map Priority (+111%) | Meta | 52 |
| S | Wrecking Ball | +3.74% | +5.02% ±2.3 | Standard (+15%) | Favorable | 51 |
| A | Echo | +2.05% | +4.33% ±2.9 | Map Priority (+76%) | Meta | 52 |
| A | Doctrine *(provisional)* | +1.81% | +3.82% ±4.2 | Standard (-6%) | Favorable | 8 |
| A | Wuyang | +1.32% | +2.46% ±2.0 | Standard (-18%) | Favorable | 52 |
| A | Pharah | +1.29% | +2.03% ±2.6 | Standard (+1%) | Favorable | 50 |
| B | Ashe | +0.96% | +3.66% ±2.1 | Map Priority (+72%) | Neutral | 52 |
| B | D.Mon | +0.70% | +3.42% ±4.7 | Niche (-33%) | Neutral | 16 |
| B | Doomfist | +0.64% | +1.92% ±2.2 | Standard (+5%) | Neutral | 51 |
| B | D.Va | +0.34% | +1.65% ±2.5 | Popular (+50%) | Neutral | 52 |
| B | Mauga | +0.29% | +1.31% ±3.8 | Standard (-19%) | Neutral | 49 |
| B | Sierra | +0.22% | -2.62% ±3.0 | Standard (+9%) | Neutral | 36 |
| B | Hanzo | +0.21% | +0.59% ±2.2 | Standard (-11%) | Neutral | 52 |
| B | Lifeweaver | +0.13% | +2.13% ±2.9 | Popular (+30%) | Neutral | 49 |
| B | Venture | +0.04% | +0.67% ±3.7 | Standard (-2%) | Neutral | 50 |
| B | Brigitte | -0.02% | +0.24% ±2.5 | Popular (+46%) | Neutral | 52 |
| B | Freja | -0.03% | +0.54% ±2.8 | Popular (+39%) | Neutral | 51 |
| B | Mercy | -0.07% | +0.23% ±2.9 | Popular (+34%) | Neutral | 52 |
| B | Jetpack Cat | -0.08% | +0.00% ±3.5 | Popular (+21%) | Neutral | 52 |
| B | Genji | -0.09% | +0.77% ±1.9 | Standard (+18%) | Neutral | 51 |
| B | Roadhog *(provisional)* | -0.09% | +5.02% ±16.2 | Standard (-7%) | Neutral | 8 |
| B | Reaper | -0.11% | +0.28% ±3.0 | Popular (+24%) | Neutral | 52 |
| B | Soldier: 76 | -0.17% | -0.05% ±2.3 | Standard (+5%) | Neutral | 52 |
| B | Shion | -0.24% | -0.20% ±2.4 | Niche (-29%) | Neutral | 28 |
| B | Illari | -0.38% | -1.26% ±2.5 | Popular (+22%) | Neutral | 52 |
| B | Sombra *(provisional)* | -0.43% | +0.59% ±6.2 | Standard (+2%) | Neutral | 8 |
| B | Mei | -0.59% | -2.36% ±3.6 | Niche (-21%) | Neutral | 51 |
| B | Anran | -0.61% | -1.17% ±3.5 | Standard (-13%) | Neutral | 49 |
| B | Cassidy | -0.62% | -0.67% ±0.9 | Standard (-6%) | Neutral | 52 |
| B | Emre | -0.65% | -2.07% ±2.6 | Standard (+5%) | Neutral | 52 |
| B | Juno | -0.68% | -1.03% ±2.4 | Standard (-19%) | Neutral | 48 |
| B | Mizuki | -0.69% | -1.26% ±3.5 | Standard (-19%) | Neutral | 52 |
| B | Tracer | -0.85% | -0.98% ±1.7 | Standard (-8%) | Neutral | 52 |
| B | Vendetta | -0.98% | -2.74% ±4.2 | Standard (-4%) | Neutral | 48 |
| B | Zenyatta | -1.03% | -1.91% ±3.0 | Niche (-22%) | Neutral | 52 |
| C | Junkrat | -1.30% | -2.04% ±3.3 | Standard (+19%) | Unfavorable | 50 |
| C | Bastion | -1.53% | -2.36% ±2.6 | Standard (+6%) | Unfavorable | 49 |
| C | Baptiste | -1.78% | -3.80% ±2.8 | Standard (-7%) | Unfavorable | 51 |
| C | Kiriko | -1.93% | -2.68% ±1.9 | Standard (-5%) | Unfavorable | 52 |
| C | Hazard | -1.95% | -2.64% ±2.9 | Popular (+29%) | Trap Pick | 51 |
| C | Moira | -1.97% | -2.57% ±2.8 | Niche (-28%) | Deterrent | 50 |
| C | Symmetra | -1.99% | -3.09% ±3.3 | Niche (-21%) | Deterrent | 48 |
| C | Sojourn | -2.26% | -3.20% ±1.9 | Niche (-47%) | Deterrent | 52 |
| C | Reinhardt | -2.56% | -3.05% ±3.0 | Niche (-40%) | Deterrent | 49 |
| C | Torbjörn | -2.64% | -3.69% ±2.7 | Standard (-4%) | Unfavorable | 49 |
| C | Orisa | -2.65% | -5.19% ±3.3 | Niche (-47%) | Deterrent | 51 |
| D | Ramattra | -3.74% | -6.85% ±4.1 | Niche (-62%) | Deterrent | 28 |
| D | Widowmaker | -3.97% | -3.95% ±2.4 | Standard (-4%) | Unfavorable | 52 |
| D | Junker Queen | -4.38% | -5.62% ±3.9 | Niche (-38%) | Deterrent | 40 |
| D | Lúcio | -4.39% | -4.83% ±3.4 | Niche (-52%) | Deterrent | 49 |
| D | Domina | -5.38% | -7.15% ±3.2 | Niche (-34%) | Deterrent | 44 |
| D | Zarya | -6.21% | -7.73% ±2.3 | Niche (-49%) | Deterrent | 49 |
| D | Sigma | -6.99% | -8.15% ±3.1 | Niche (-35%) | Deterrent | 52 |

### Eichenwalde

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| A | Ana | +2.55% | +3.71% ±2.9 | Standard (+7%) | Favorable | 16 |
| A | Jetpack Cat | +1.93% | +5.41% ±5.8 | Standard (+6%) | Favorable | 16 |
| A | Junkrat | +1.59% | +5.35% ±6.3 | Map Priority (+88%) | Meta | 16 |
| A | D.Mon | +1.41% | +5.87% ±4.7 | Standard (+16%) | Favorable | 16 |
| B | Roadhog *(provisional)* | +1.01% | +7.10% ±8.5 | Standard (-3%) | Neutral | 8 |
| B | Echo | +0.93% | +2.96% ±3.6 | Map Priority (+85%) | Neutral | 16 |
| B | Orisa | +0.72% | +1.65% ±3.5 | Popular (+23%) | Neutral | 16 |
| B | Junker Queen | +0.62% | +2.90% ±7.3 | Standard (+4%) | Neutral | 16 |
| B | Wuyang | +0.54% | +2.50% ±3.8 | Standard (+0%) | Neutral | 16 |
| B | Pharah | +0.39% | +2.09% ±5.1 | Map Priority (+66%) | Neutral | 16 |
| B | Sierra | +0.22% | +1.26% ±6.5 | Standard (+9%) | Neutral | 10 |
| B | Tracer | +0.15% | +0.95% ±3.3 | Standard (-15%) | Neutral | 16 |
| B | Lifeweaver | +0.13% | -0.23% ±12.7 | Standard (-4%) | Neutral | 16 |
| B | Mercy | +0.08% | +1.65% ±4.9 | Standard (+7%) | Neutral | 14 |
| B | Venture | +0.04% | +2.71% ±9.3 | Standard (+12%) | Neutral | 16 |
| B | Bastion | +0.01% | -0.01% ±5.2 | Popular (+32%) | Neutral | 16 |
| B | Vendetta | +0.00% | +0.64% ±5.1 | Standard (-2%) | Neutral | 15 |
| B | Mei | -0.02% | +1.95% ±6.8 | Popular (+24%) | Neutral | 16 |
| B | Illari | -0.10% | +0.71% ±4.0 | Standard (+2%) | Neutral | 16 |
| B | Doomfist | -0.12% | +1.31% ±5.5 | Standard (-2%) | Neutral | 16 |
| B | Doctrine *(provisional)* | -0.19% | -0.44% ±5.9 | Standard (-1%) | Neutral | 8 |
| B | Genji | -0.19% | -0.69% ±3.3 | Standard (+5%) | Neutral | 16 |
| B | Soldier: 76 | -0.25% | +0.53% ±8.1 | Niche (-26%) | Neutral | 16 |
| B | Mauga | -0.41% | +0.18% ±6.2 | Standard (-6%) | Neutral | 15 |
| B | Mizuki | -0.41% | -0.86% ±4.2 | Standard (-5%) | Neutral | 16 |
| B | Sojourn | -0.44% | -0.49% ±4.2 | Niche (-24%) | Neutral | 16 |
| B | Domina | -0.46% | +0.28% ±5.2 | Standard (+8%) | Neutral | 16 |
| B | Emre | -0.55% | -4.47% ±5.2 | Standard (-15%) | Neutral | 16 |
| B | Freja | -0.55% | -0.61% ±8.4 | Standard (+9%) | Neutral | 16 |
| B | Hazard | -0.55% | -0.55% ±4.1 | Niche (-21%) | Neutral | 16 |
| B | D.Va | -0.59% | -0.92% ±6.5 | Standard (-9%) | Neutral | 16 |
| B | Juno | -0.62% | -1.01% ±4.7 | Standard (-8%) | Neutral | 16 |
| B | Ramattra | -0.65% | -0.11% ±6.8 | Standard (+14%) | Neutral | 15 |
| B | Zenyatta | -0.65% | -1.93% ±6.1 | Standard (+16%) | Neutral | 16 |
| B | Cassidy | -0.66% | -1.01% ±2.4 | Standard (+16%) | Neutral | 16 |
| B | Ashe | -0.82% | -1.47% ±5.3 | Standard (-19%) | Neutral | 16 |
| B | Shion | -0.82% | -2.63% ±3.2 | Niche (-22%) | Neutral | 16 |
| B | Wrecking Ball | -0.87% | -1.94% ±6.3 | Standard (-10%) | Neutral | 16 |
| B | Kiriko | -0.89% | -2.14% ±3.7 | Standard (-5%) | Neutral | 16 |
| B | Torbjörn | -0.94% | -1.63% ±3.8 | Popular (+40%) | Neutral | 15 |
| B | Brigitte | -0.98% | -2.84% ±6.7 | Standard (-11%) | Neutral | 15 |
| B | Sombra *(provisional)* | -0.98% | -1.36% ±7.4 | Standard (-7%) | Neutral | 8 |
| B | Anran | -1.07% | -6.24% ±7.0 | Standard (-5%) | Neutral | 15 |
| B | Baptiste | -1.13% | -3.02% ±3.9 | Popular (+20%) | Neutral | 16 |
| C | Reaper | -1.46% | -4.23% ±4.0 | Standard (+1%) | Unfavorable | 16 |
| C | Symmetra | -1.49% | -5.84% ±8.0 | Standard (-6%) | Unfavorable | 13 |
| C | Sigma | -1.74% | -1.75% ±4.3 | Standard (-2%) | Unfavorable | 16 |
| C | Widowmaker | -2.14% | -1.86% ±4.8 | Niche (-35%) | Deterrent | 16 |
| C | Zarya | -2.18% | -5.65% ±7.1 | Popular (+23%) | Trap Pick | 16 |
| C | Moira | -2.56% | -8.47% ±6.8 | Standard (-10%) | Unfavorable | 16 |
| C | Reinhardt | -2.73% | -4.59% ±5.5 | Popular (+29%) | Trap Pick | 16 |
| C | Hanzo | -2.75% | -7.25% ±4.1 | Standard (+14%) | Unfavorable | 16 |
| D | Winston | -3.31% | -3.95% ±4.3 | Niche (-24%) | Deterrent | 16 |
| D | Lúcio | -3.84% | -4.44% ±4.6 | Niche (-23%) | Deterrent | 16 |

### Esperanca

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| A | Lúcio | +2.97% | +3.34% ±2.2 | Popular (+36%) | Meta | 52 |
| A | Winston | +2.22% | +2.50% ±1.7 | Popular (+31%) | Meta | 52 |
| A | Junker Queen | +1.61% | +1.93% ±2.2 | Popular (+26%) | Meta | 49 |
| A | Soldier: 76 | +1.53% | +2.22% ±1.8 | Popular (+31%) | Meta | 51 |
| A | Kiriko | +1.50% | +1.69% ±1.0 | Standard (+16%) | Favorable | 52 |
| B | Reinhardt | +1.19% | +1.44% ±2.3 | Standard (-15%) | Neutral | 51 |
| B | Junkrat | +1.13% | +1.71% ±2.9 | Niche (-24%) | Neutral | 50 |
| B | Torbjörn | +0.99% | +1.48% ±2.9 | Standard (-13%) | Neutral | 50 |
| B | D.Mon | +0.96% | +2.30% ±3.0 | Standard (+8%) | Neutral | 16 |
| B | Echo | +0.77% | +1.14% ±1.6 | Standard (+1%) | Neutral | 52 |
| B | Hanzo | +0.69% | +1.45% ±2.4 | Niche (-56%) | Neutral | 49 |
| B | Jetpack Cat | +0.57% | +0.86% ±2.8 | Standard (+17%) | Neutral | 52 |
| B | Mauga | +0.56% | +0.93% ±2.0 | Popular (+24%) | Neutral | 51 |
| B | Shion | +0.51% | +0.69% ±0.8 | Popular (+35%) | Neutral | 28 |
| B | Vendetta | +0.50% | +1.41% ±3.2 | Standard (+7%) | Neutral | 47 |
| B | Moira | +0.45% | +1.37% ±2.8 | Standard (+12%) | Neutral | 52 |
| B | Doctrine *(provisional)* | +0.43% | +0.74% ±3.2 | Standard (+1%) | Neutral | 8 |
| B | Mei | +0.35% | +2.32% ±3.6 | Niche (-34%) | Neutral | 51 |
| B | Brigitte | +0.34% | +0.48% ±1.3 | Standard (+16%) | Neutral | 51 |
| B | Wrecking Ball | +0.33% | +0.54% ±2.2 | Popular (+26%) | Neutral | 52 |
| B | Bastion | +0.24% | +0.44% ±3.4 | Niche (-22%) | Neutral | 50 |
| B | Sierra | +0.22% | +0.88% ±2.5 | Standard (-8%) | Neutral | 33 |
| B | Mizuki | +0.15% | +0.18% ±1.4 | Standard (+10%) | Neutral | 52 |
| B | Lifeweaver | +0.13% | +1.05% ±2.7 | Standard (-12%) | Neutral | 50 |
| B | Wuyang | +0.09% | +0.39% ±2.5 | Standard (-1%) | Neutral | 52 |
| B | Venture | +0.04% | +0.61% ±2.2 | Standard (-12%) | Neutral | 48 |
| B | Sombra *(provisional)* | -0.00% | +0.95% ±4.3 | Popular (+23%) | Neutral | 8 |
| B | Mercy | -0.05% | +0.06% ±1.6 | Standard (-13%) | Neutral | 49 |
| B | Tracer | -0.07% | -0.00% ±1.2 | Popular (+38%) | Neutral | 52 |
| B | Symmetra | -0.08% | +0.31% ±3.7 | Niche (-29%) | Neutral | 45 |
| B | Doomfist | -0.10% | +0.10% ±2.0 | Standard (+2%) | Neutral | 52 |
| B | Emre | -0.10% | +0.77% ±2.3 | Standard (-2%) | Neutral | 52 |
| B | Pharah | -0.10% | +0.18% ±2.6 | Standard (-18%) | Neutral | 50 |
| B | Sojourn | -0.10% | -0.06% ±0.9 | Standard (-1%) | Neutral | 52 |
| B | Genji | -0.11% | +0.53% ±1.9 | Standard (-6%) | Neutral | 52 |
| B | Reaper | -0.12% | +0.11% ±2.3 | Standard (-2%) | Neutral | 51 |
| B | Hazard | -0.14% | -0.07% ±1.7 | Popular (+22%) | Neutral | 51 |
| B | Illari | -0.41% | -0.73% ±1.4 | Standard (-14%) | Neutral | 52 |
| B | Cassidy | -0.52% | -0.58% ±1.4 | Standard (+12%) | Neutral | 52 |
| B | Orisa | -0.57% | -0.96% ±3.0 | Standard (-16%) | Neutral | 52 |
| B | Ashe | -0.61% | -0.53% ±1.3 | Niche (-43%) | Neutral | 51 |
| B | Freja | -0.65% | -0.77% ±2.8 | Niche (-25%) | Neutral | 49 |
| B | Juno | -0.69% | -1.33% ±3.2 | Standard (+12%) | Neutral | 51 |
| B | Roadhog *(provisional)* | -0.97% | -2.40% ±6.6 | Standard (-6%) | Neutral | 8 |
| B | Baptiste | -1.00% | -1.61% ±2.6 | Niche (-37%) | Neutral | 51 |
| C | Anran | -1.23% | -2.14% ±2.7 | Standard (+2%) | Unfavorable | 49 |
| C | D.Va | -1.47% | -2.25% ±1.9 | Popular (+23%) | Trap Pick | 51 |
| C | Zarya | -1.63% | -1.98% ±3.0 | Niche (-21%) | Deterrent | 52 |
| C | Zenyatta | -1.67% | -2.36% ±1.8 | Niche (-39%) | Deterrent | 51 |
| C | Ana | -1.97% | -2.29% ±2.1 | Standard (-20%) | Unfavorable | 52 |
| C | Domina | -2.32% | -2.91% ±3.5 | Niche (-35%) | Deterrent | 47 |
| C | Ramattra | -2.35% | -3.19% ±2.9 | Niche (-41%) | Deterrent | 47 |
| D | Sigma | -4.99% | -5.81% ±3.3 | Niche (-48%) | Deterrent | 52 |
| D | Widowmaker | -15.34% | -15.60% ±2.3 | Niche (-65%) | Deterrent | 49 |

### Grimsvotn

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| S | Junkrat *(provisional)* | +3.76% | +8.38% ±4.6 | Popular (+29%) | Meta | 8 |
| A | Mizuki *(provisional)* | +2.04% | +7.19% ±5.8 | Standard (-19%) | Favorable | 8 |
| A | Jetpack Cat *(provisional)* | +1.53% | +4.67% ±6.1 | Niche (-36%) | Specialist | 8 |
| A | Lúcio *(provisional)* | +1.47% | +5.54% ±8.6 | Niche (-31%) | Specialist | 6 |
| A | Ana *(provisional)* | +1.28% | +1.89% ±2.8 | Standard (+9%) | Favorable | 8 |
| A | Hanzo *(provisional)* | +1.26% | +5.07% ±4.3 | Map Priority (+61%) | Meta | 8 |
| B | Ramattra *(provisional)* | +0.67% | +3.35% ±5.2 | Map Priority (+117%) | Neutral | 8 |
| B | Orisa *(provisional)* | +0.61% | +1.93% ±4.5 | Map Priority (+54%) | Neutral | 8 |
| B | Vendetta *(provisional)* | +0.59% | +4.66% ±6.4 | Standard (-11%) | Neutral | 8 |
| B | Anran *(provisional)* | +0.42% | +5.68% ±7.7 | Standard (-8%) | Neutral | 7 |
| B | Hazard *(provisional)* | +0.33% | +1.68% ±5.2 | Niche (-52%) | Neutral | 8 |
| B | Brigitte *(provisional)* | +0.26% | +2.32% ±5.4 | Niche (-35%) | Neutral | 8 |
| B | Sierra *(provisional)* | +0.22% | +2.00% ±5.4 | Standard (+15%) | Neutral | 8 |
| B | Kiriko *(provisional)* | +0.18% | +0.56% ±3.1 | Standard (-12%) | Neutral | 8 |
| B | Bastion *(provisional)* | +0.14% | +0.37% ±4.8 | Popular (+41%) | Neutral | 8 |
| B | Lifeweaver *(provisional)* | +0.13% | -2.05% ±5.2 | Standard (+6%) | Neutral | 8 |
| B | Torbjörn *(provisional)* | +0.13% | +0.40% ±4.8 | Standard (+7%) | Neutral | 8 |
| B | Symmetra *(provisional)* | +0.09% | +2.24% ±7.3 | Standard (-4%) | Neutral | 8 |
| B | Roadhog *(provisional)* | +0.05% | +1.68% ±7.7 | Standard (+12%) | Neutral | 8 |
| B | Venture *(provisional)* | +0.04% | +1.89% ±5.7 | Standard (-0%) | Neutral | 8 |
| B | Reinhardt *(provisional)* | +0.03% | +0.37% ±4.5 | Popular (+41%) | Neutral | 8 |
| B | Sigma *(provisional)* | +0.03% | +0.66% ±3.9 | Map Priority (+75%) | Neutral | 8 |
| B | Sombra *(provisional)* | -0.10% | +1.79% ±6.4 | Standard (-17%) | Neutral | 8 |
| B | Echo *(provisional)* | -0.12% | +2.61% ±7.3 | Niche (-22%) | Neutral | 8 |
| B | Genji *(provisional)* | -0.15% | +0.72% ±3.6 | Standard (-4%) | Neutral | 8 |
| B | Cassidy *(provisional)* | -0.16% | +0.07% ±3.0 | Standard (-4%) | Neutral | 8 |
| B | Mei *(provisional)* | -0.16% | -0.19% ±8.7 | Map Priority (+52%) | Neutral | 8 |
| B | Illari *(provisional)* | -0.21% | -3.47% ±11.2 | Standard (-2%) | Neutral | 8 |
| B | Reaper *(provisional)* | -0.21% | +0.93% ±6.4 | Standard (-12%) | Neutral | 8 |
| B | Sojourn *(provisional)* | -0.30% | -0.17% ±2.8 | Popular (+39%) | Neutral | 8 |
| B | Wuyang *(provisional)* | -0.30% | -0.75% ±4.5 | Popular (+35%) | Neutral | 8 |
| B | Doomfist *(provisional)* | -0.31% | -0.46% ±6.0 | Standard (-8%) | Neutral | 8 |
| B | Wrecking Ball *(provisional)* | -0.31% | +0.03% ±8.0 | Niche (-44%) | Neutral | 8 |
| B | Zarya *(provisional)* | -0.31% | +0.52% ±5.2 | Map Priority (+59%) | Neutral | 8 |
| B | Soldier: 76 *(provisional)* | -0.36% | -0.41% ±6.7 | Niche (-25%) | Neutral | 8 |
| B | Tracer *(provisional)* | -0.39% | -0.25% ±3.7 | Niche (-34%) | Neutral | 8 |
| B | Emre *(provisional)* | -0.41% | -1.37% ±4.4 | Standard (+13%) | Neutral | 8 |
| B | D.Va *(provisional)* | -0.55% | -0.53% ±5.4 | Niche (-54%) | Neutral | 8 |
| B | Junker Queen *(provisional)* | -0.58% | -0.10% ±6.0 | Standard (+8%) | Neutral | 7 |
| B | D.Mon *(provisional)* | -0.59% | -1.02% ±4.4 | Standard (+0%) | Neutral | 8 |
| B | Juno *(provisional)* | -0.59% | -0.32% ±5.8 | Standard (+10%) | Neutral | 7 |
| B | Doctrine *(provisional)* | -0.62% | -1.39% ±4.9 | Standard (+7%) | Neutral | 8 |
| B | Shion *(provisional)* | -0.67% | -1.61% ±2.7 | Standard (-6%) | Neutral | 8 |
| B | Zenyatta *(provisional)* | -0.67% | -1.71% ±5.3 | Popular (+49%) | Neutral | 8 |
| B | Mercy *(provisional)* | -0.68% | -2.86% ±4.8 | Standard (-7%) | Neutral | 7 |
| B | Mauga *(provisional)* | -0.75% | -1.28% ±6.7 | Standard (-11%) | Neutral | 6 |
| B | Baptiste *(provisional)* | -0.82% | -3.11% ±6.5 | Popular (+37%) | Neutral | 8 |
| B | Freja *(provisional)* | -1.01% | -4.47% ±7.2 | Standard (-0%) | Neutral | 8 |
| C | Domina *(provisional)* | -1.21% | -1.33% ±5.6 | Map Priority (+80%) | Trap Pick | 8 |
| C | Ashe *(provisional)* | -1.27% | -4.27% ±4.0 | Standard (+11%) | Unfavorable | 8 |
| C | Moira *(provisional)* | -2.04% | -5.31% ±6.3 | Standard (-14%) | Unfavorable | 8 |
| C | Pharah *(provisional)* | -2.38% | -3.90% ±4.8 | Standard (+1%) | Unfavorable | 8 |
| C | Winston *(provisional)* | -2.88% | -3.39% ±4.5 | Niche (-53%) | Deterrent | 8 |
| D | Widowmaker *(provisional)* | -3.17% | -3.03% ±4.3 | Standard (+18%) | Unfavorable | 8 |

### Havana

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| S | Widowmaker | +5.88% | +6.19% ±2.5 | Map Priority (+176%) | Meta | 52 |
| S | Sigma | +5.72% | +6.19% ±1.6 | Map Priority (+136%) | Meta | 51 |
| S | Zenyatta | +3.33% | +4.93% ±1.5 | Map Priority (+114%) | Meta | 51 |
| A | Ana | +1.81% | +2.00% ±1.3 | Popular (+33%) | Meta | 51 |
| A | Doctrine *(provisional)* | +1.56% | +3.52% ±4.5 | Standard (+1%) | Favorable | 8 |
| A | Domina | +1.38% | +2.08% ±2.6 | Map Priority (+147%) | Meta | 50 |
| A | Orisa | +1.24% | +2.49% ±3.2 | Standard (+5%) | Favorable | 51 |
| B | Bastion | +1.15% | +1.58% ±2.2 | Standard (+18%) | Neutral | 49 |
| B | Hanzo | +0.51% | +1.00% ±2.1 | Map Priority (+158%) | Neutral | 52 |
| B | Soldier: 76 | +0.48% | +1.35% ±3.0 | Standard (-9%) | Neutral | 51 |
| B | Baptiste | +0.31% | +1.29% ±2.2 | Map Priority (+52%) | Neutral | 51 |
| B | Sierra | +0.22% | +1.77% ±3.4 | Map Priority (+51%) | Neutral | 37 |
| B | Illari | +0.21% | +1.39% ±2.1 | Map Priority (+59%) | Neutral | 52 |
| B | Emre | +0.15% | +0.89% ±1.5 | Popular (+49%) | Neutral | 52 |
| B | Lifeweaver | +0.13% | +1.28% ±2.6 | Popular (+21%) | Neutral | 50 |
| B | Ashe | +0.07% | +1.03% ±1.8 | Map Priority (+83%) | Neutral | 51 |
| B | Venture | +0.04% | -0.77% ±4.0 | Niche (-23%) | Neutral | 47 |
| B | Torbjörn | +0.02% | +0.06% ±2.9 | Standard (+3%) | Neutral | 50 |
| B | Tracer | -0.08% | +0.28% ±2.8 | Niche (-48%) | Neutral | 52 |
| B | Sojourn | -0.14% | +0.09% ±2.3 | Popular (+37%) | Neutral | 52 |
| B | Freja | -0.15% | +0.30% ±2.9 | Popular (+42%) | Neutral | 51 |
| B | Genji | -0.15% | +0.32% ±3.2 | Standard (+9%) | Neutral | 52 |
| B | Sombra *(provisional)* | -0.17% | +1.93% ±7.1 | Niche (-22%) | Neutral | 8 |
| B | Roadhog *(provisional)* | -0.25% | +1.60% ±14.0 | Standard (-9%) | Neutral | 8 |
| B | D.Va | -0.30% | +0.06% ±2.5 | Niche (-28%) | Neutral | 51 |
| B | Juno | -0.48% | +0.21% ±2.8 | Standard (-16%) | Neutral | 49 |
| B | Mercy | -0.58% | -1.40% ±3.3 | Popular (+24%) | Neutral | 50 |
| B | Shion | -0.71% | -2.05% ±3.0 | Niche (-53%) | Neutral | 28 |
| B | Mei | -0.72% | -2.51% ±3.2 | Popular (+24%) | Neutral | 51 |
| B | D.Mon | -0.83% | -3.47% ±7.3 | Niche (-24%) | Neutral | 15 |
| B | Anran | -0.90% | -2.06% ±3.8 | Niche (-26%) | Neutral | 46 |
| B | Reaper | -1.07% | -2.45% ±3.5 | Niche (-49%) | Neutral | 51 |
| B | Junkrat | -1.10% | -2.04% ±4.0 | Niche (-28%) | Neutral | 49 |
| B | Wuyang | -1.15% | -2.78% ±3.0 | Standard (-3%) | Neutral | 52 |
| C | Cassidy | -1.32% | -2.21% ±2.3 | Niche (-50%) | Deterrent | 51 |
| C | Hazard | -1.33% | -1.94% ±3.7 | Niche (-62%) | Deterrent | 46 |
| C | Symmetra | -1.34% | -2.12% ±3.7 | Standard (-1%) | Unfavorable | 48 |
| C | Mauga | -1.35% | -1.88% ±3.0 | Niche (-35%) | Deterrent | 47 |
| C | Doomfist | -1.43% | -3.19% ±2.4 | Standard (-15%) | Unfavorable | 51 |
| C | Vendetta | -1.47% | -4.03% ±4.0 | Niche (-29%) | Deterrent | 37 |
| C | Moira | -1.55% | -2.23% ±4.0 | Niche (-39%) | Deterrent | 50 |
| C | Mizuki | -1.64% | -2.57% ±2.9 | Niche (-48%) | Deterrent | 50 |
| C | Ramattra | -1.83% | -2.28% ±2.6 | Popular (+44%) | Trap Pick | 50 |
| C | Brigitte | -2.00% | -3.02% ±2.8 | Niche (-52%) | Deterrent | 48 |
| C | Zarya | -2.01% | -2.50% ±2.9 | Standard (-11%) | Unfavorable | 50 |
| C | Echo | -2.10% | -3.04% ±2.5 | Niche (-55%) | Deterrent | 47 |
| C | Kiriko | -2.18% | -3.48% ±2.3 | Niche (-27%) | Deterrent | 52 |
| C | Wrecking Ball | -2.29% | -4.10% ±4.1 | Niche (-41%) | Deterrent | 50 |
| C | Pharah | -2.85% | -4.03% ±3.7 | Niche (-45%) | Deterrent | 49 |
| D | Reinhardt | -3.20% | -3.87% ±3.0 | Standard (+10%) | Unfavorable | 51 |
| D | Jetpack Cat | -3.39% | -6.18% ±4.3 | Niche (-34%) | Deterrent | 51 |
| D | Junker Queen | -4.87% | -6.24% ±3.8 | Niche (-44%) | Deterrent | 38 |
| D | Winston | -6.74% | -7.42% ±2.4 | Niche (-39%) | Deterrent | 51 |
| D | Lúcio | -8.62% | -9.40% ±2.7 | Niche (-68%) | Deterrent | 46 |

### Hollywood

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| A | Zarya | +1.43% | +2.30% ±2.6 | Standard (+15%) | Favorable | 51 |
| B | Ana | +0.99% | +1.11% ±1.3 | Standard (+19%) | Neutral | 52 |
| B | Sierra | +0.22% | -0.56% ±2.9 | Standard (+5%) | Neutral | 34 |
| B | Lifeweaver | +0.13% | -1.88% ±2.5 | Standard (+19%) | Neutral | 50 |
| B | Venture | +0.04% | -4.47% ±3.9 | Standard (-9%) | Neutral | 50 |
| B | Hanzo | +0.01% | +0.64% ±3.5 | Popular (+28%) | Neutral | 52 |
| B | D.Va | -0.09% | +0.44% ±2.2 | Standard (+5%) | Neutral | 51 |
| B | Doctrine *(provisional)* | -0.10% | -0.12% ±4.1 | Standard (+0%) | Neutral | 6 |
| B | Roadhog *(provisional)* | -0.13% | +4.40% ±16.4 | Standard (+5%) | Neutral | 6 |
| B | Genji | -0.15% | +0.13% ±2.2 | Standard (+11%) | Neutral | 51 |
| B | Shion | -0.20% | +0.02% ±3.1 | Niche (-22%) | Neutral | 28 |
| B | Winston | -0.22% | -0.12% ±1.7 | Popular (+22%) | Neutral | 52 |
| B | Wuyang | -0.25% | -0.35% ±2.8 | Standard (-3%) | Neutral | 52 |
| B | Ashe | -0.31% | +0.58% ±2.3 | Popular (+47%) | Neutral | 52 |
| B | Doomfist | -0.37% | -0.64% ±3.5 | Standard (-5%) | Neutral | 51 |
| B | Emre | -0.37% | -0.54% ±3.2 | Standard (+2%) | Neutral | 52 |
| B | Kiriko | -0.37% | -0.49% ±2.0 | Standard (-10%) | Neutral | 52 |
| B | Mei | -0.39% | -0.99% ±2.9 | Standard (+15%) | Neutral | 51 |
| B | Illari | -0.40% | -1.72% ±2.9 | Standard (+10%) | Neutral | 52 |
| B | Tracer | -0.40% | -0.37% ±2.1 | Standard (-16%) | Neutral | 52 |
| B | Mercy | -0.45% | -0.87% ±3.0 | Standard (+19%) | Neutral | 51 |
| B | Bastion | -0.52% | -0.84% ±2.8 | Standard (+11%) | Neutral | 51 |
| B | Freja | -0.55% | -0.55% ±2.9 | Standard (+6%) | Neutral | 51 |
| B | Domina | -0.61% | -0.41% ±3.2 | Standard (+8%) | Neutral | 52 |
| B | Zenyatta | -0.66% | -0.98% ±2.9 | Standard (+16%) | Neutral | 52 |
| B | Ramattra | -0.69% | -0.53% ±4.3 | Standard (-12%) | Neutral | 51 |
| B | Juno | -0.85% | -2.51% ±3.0 | Standard (-8%) | Neutral | 52 |
| B | Baptiste | -0.87% | -1.32% ±2.7 | Standard (+10%) | Neutral | 52 |
| B | Hazard | -0.87% | -1.04% ±3.0 | Standard (-9%) | Neutral | 50 |
| B | D.Mon | -0.94% | -2.83% ±5.5 | Standard (-8%) | Neutral | 16 |
| B | Anran | -1.01% | -2.27% ±3.6 | Standard (-5%) | Neutral | 52 |
| B | Sombra *(provisional)* | -1.10% | -1.82% ±7.2 | Standard (-16%) | Neutral | 6 |
| B | Echo | -1.11% | -1.37% ±2.3 | Standard (+4%) | Neutral | 52 |
| C | Reaper | -1.25% | -2.67% ±3.2 | Standard (-3%) | Unfavorable | 52 |
| C | Mizuki | -1.29% | -1.55% ±1.7 | Standard (-11%) | Unfavorable | 52 |
| C | Wrecking Ball | -1.29% | -1.53% ±2.2 | Standard (-16%) | Unfavorable | 50 |
| C | Cassidy | -1.30% | -1.71% ±1.6 | Standard (-6%) | Unfavorable | 52 |
| C | Orisa | -1.31% | -2.12% ±2.7 | Standard (-5%) | Unfavorable | 52 |
| C | Moira | -1.35% | -1.53% ±2.5 | Standard (-13%) | Unfavorable | 51 |
| C | Pharah | -1.45% | -1.55% ±2.1 | Standard (-5%) | Unfavorable | 50 |
| C | Torbjörn | -1.58% | -2.19% ±2.6 | Popular (+27%) | Trap Pick | 51 |
| C | Brigitte | -1.62% | -2.07% ±2.1 | Standard (-8%) | Unfavorable | 51 |
| C | Vendetta | -1.85% | -2.97% ±2.3 | Standard (-6%) | Unfavorable | 46 |
| C | Soldier: 76 | -2.09% | -3.56% ±2.7 | Niche (-20%) | Deterrent | 50 |
| C | Junkrat | -2.18% | -2.79% ±2.3 | Standard (+20%) | Unfavorable | 50 |
| C | Widowmaker | -2.18% | -2.15% ±1.5 | Popular (+35%) | Trap Pick | 52 |
| C | Symmetra | -2.50% | -4.86% ±4.2 | Standard (-2%) | Unfavorable | 51 |
| C | Sojourn | -2.60% | -3.84% ±2.0 | Standard (-14%) | Unfavorable | 52 |
| C | Sigma | -2.77% | -2.93% ±2.6 | Standard (+13%) | Unfavorable | 52 |
| C | Jetpack Cat | -2.80% | -4.29% ±3.5 | Standard (-13%) | Unfavorable | 52 |
| D | Mauga | -3.73% | -4.91% ±2.2 | Standard (-18%) | Unfavorable | 47 |
| D | Junker Queen | -3.96% | -5.01% ±3.8 | Niche (-22%) | Deterrent | 45 |
| D | Lúcio | -5.21% | -5.38% ±1.8 | Niche (-47%) | Deterrent | 47 |
| D | Reinhardt | -7.77% | -9.47% ±2.9 | Standard (-13%) | Unfavorable | 51 |

### Ilios

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| S | Lúcio | +4.31% | +4.71% ±2.0 | Map Priority (+84%) | Meta | 52 |
| S | Hazard | +3.18% | +3.42% ±1.1 | Popular (+50%) | Meta | 51 |
| A | Jetpack Cat | +2.90% | +4.20% ±2.9 | Popular (+46%) | Meta | 52 |
| A | Torbjörn | +2.29% | +2.77% ±1.9 | Standard (-12%) | Favorable | 51 |
| A | Pharah | +1.86% | +2.05% ±1.2 | Popular (+37%) | Meta | 51 |
| A | Echo | +1.75% | +2.04% ±1.1 | Map Priority (+83%) | Meta | 52 |
| A | Junkrat | +1.58% | +2.22% ±2.6 | Niche (-21%) | Specialist | 51 |
| A | Junker Queen | +1.31% | +1.78% ±2.8 | Standard (+4%) | Favorable | 47 |
| A | Winston | +1.30% | +1.46% ±1.5 | Popular (+43%) | Meta | 52 |
| B | Vendetta | +1.17% | +1.65% ±1.7 | Standard (+8%) | Neutral | 47 |
| B | Kiriko | +0.80% | +1.01% ±1.3 | Standard (+12%) | Neutral | 52 |
| B | Mercy | +0.71% | +1.12% ±1.4 | Standard (-6%) | Neutral | 50 |
| B | Anran | +0.64% | +0.93% ±1.6 | Standard (+11%) | Neutral | 49 |
| B | Freja | +0.56% | +1.12% ±1.9 | Popular (+46%) | Neutral | 52 |
| B | Reaper | +0.41% | +0.65% ±1.4 | Popular (+30%) | Neutral | 52 |
| B | Widowmaker | +0.41% | +0.49% ±1.9 | Standard (-11%) | Neutral | 52 |
| B | Wrecking Ball | +0.41% | +0.67% ±2.4 | Popular (+42%) | Neutral | 52 |
| B | Sombra *(provisional)* | +0.32% | +1.73% ±4.5 | Popular (+20%) | Neutral | 8 |
| B | Bastion | +0.29% | +0.37% ±1.9 | Niche (-26%) | Neutral | 48 |
| B | Zenyatta | +0.27% | +0.41% ±1.0 | Niche (-40%) | Neutral | 50 |
| B | Sierra | +0.22% | -0.01% ±2.0 | Standard (-19%) | Neutral | 32 |
| B | Symmetra | +0.17% | +0.33% ±1.9 | Standard (+0%) | Neutral | 52 |
| B | Lifeweaver | +0.13% | -1.64% ±1.6 | Standard (-12%) | Neutral | 50 |
| B | Venture | +0.04% | -0.60% ±2.3 | Standard (+8%) | Neutral | 52 |
| B | D.Va | -0.06% | +0.57% ±2.4 | Popular (+43%) | Neutral | 52 |
| B | Juno | -0.08% | +0.30% ±1.0 | Standard (+1%) | Neutral | 51 |
| B | Genji | -0.09% | +0.80% ±1.9 | Standard (+1%) | Neutral | 52 |
| B | Moira | -0.18% | -0.09% ±1.1 | Standard (+11%) | Neutral | 51 |
| B | Doomfist | -0.24% | -0.20% ±1.7 | Standard (+9%) | Neutral | 52 |
| B | Emre | -0.29% | -0.13% ±2.1 | Niche (-29%) | Neutral | 52 |
| B | Cassidy | -0.30% | -0.30% ±1.0 | Popular (+21%) | Neutral | 52 |
| B | Shion | -0.48% | -0.53% ±0.9 | Standard (+9%) | Neutral | 28 |
| B | Ashe | -0.67% | -0.58% ±1.5 | Niche (-44%) | Neutral | 51 |
| B | Brigitte | -0.67% | -0.74% ±2.2 | Popular (+43%) | Neutral | 52 |
| B | Roadhog *(provisional)* | -0.67% | -1.19% ±5.9 | Standard (+19%) | Neutral | 8 |
| B | Baptiste | -0.71% | -0.80% ±1.7 | Niche (-27%) | Neutral | 51 |
| B | Illari | -0.79% | -2.34% ±1.9 | Niche (-28%) | Neutral | 52 |
| B | D.Mon | -0.81% | -1.11% ±2.5 | Standard (-11%) | Neutral | 16 |
| B | Hanzo | -0.82% | -0.96% ±1.8 | Niche (-49%) | Neutral | 52 |
| B | Orisa | -0.99% | -1.10% ±1.1 | Standard (-14%) | Neutral | 50 |
| B | Mizuki | -1.02% | -1.22% ±1.7 | Standard (+17%) | Neutral | 52 |
| B | Sojourn | -1.11% | -1.44% ±1.8 | Niche (-40%) | Neutral | 52 |
| C | Tracer | -1.26% | -1.73% ±2.2 | Popular (+29%) | Trap Pick | 52 |
| C | Reinhardt | -1.33% | -1.38% ±1.6 | Niche (-35%) | Deterrent | 50 |
| C | Wuyang | -1.45% | -1.83% ±1.3 | Niche (-26%) | Deterrent | 52 |
| C | Ana | -1.59% | -1.61% ±0.7 | Standard (-19%) | Unfavorable | 52 |
| C | Mei | -1.75% | -3.82% ±2.1 | Niche (-40%) | Deterrent | 50 |
| C | Soldier: 76 | -2.04% | -2.80% ±2.0 | Niche (-33%) | Deterrent | 51 |
| C | Ramattra | -2.06% | -2.57% ±2.5 | Niche (-60%) | Deterrent | 36 |
| C | Mauga | -2.13% | -2.48% ±1.7 | Standard (-3%) | Unfavorable | 49 |
| C | Zarya | -2.51% | -2.71% ±1.5 | Niche (-41%) | Deterrent | 50 |
| D | Doctrine *(provisional)* | -3.75% | -6.06% ±3.3 | Standard (-9%) | Unfavorable | 8 |
| D | Domina | -4.57% | -6.23% ±3.4 | Niche (-48%) | Deterrent | 43 |
| D | Sigma | -4.59% | -4.73% ±1.5 | Niche (-62%) | Deterrent | 51 |

### Junkertown

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| S | Widowmaker | +5.82% | +6.00% ±1.9 | Map Priority (+119%) | Meta | 52 |
| A | Sigma | +2.61% | +3.13% ±2.3 | Map Priority (+81%) | Meta | 52 |
| A | Ana | +2.29% | +2.90% ±2.2 | Popular (+28%) | Meta | 52 |
| A | Wrecking Ball | +1.79% | +3.07% ±3.2 | Standard (+11%) | Favorable | 51 |
| A | Hanzo | +1.47% | +2.02% ±1.6 | Map Priority (+76%) | Meta | 51 |
| A | Junkrat | +1.41% | +2.19% ±3.0 | Standard (-19%) | Favorable | 48 |
| B | Zenyatta | +1.02% | +3.65% ±3.1 | Map Priority (+51%) | Neutral | 52 |
| B | Freja | +0.90% | +3.76% ±3.7 | Popular (+29%) | Neutral | 51 |
| B | Sojourn | +0.50% | +0.95% ±1.8 | Standard (+2%) | Neutral | 52 |
| B | Brigitte | +0.38% | +1.16% ±3.1 | Standard (-19%) | Neutral | 51 |
| B | Kiriko | +0.35% | +0.79% ±2.7 | Standard (-17%) | Neutral | 52 |
| B | Torbjörn | +0.35% | +0.64% ±3.4 | Standard (+9%) | Neutral | 49 |
| B | Hazard | +0.29% | +0.67% ±2.9 | Niche (-30%) | Neutral | 51 |
| B | Illari | +0.26% | +1.92% ±2.4 | Map Priority (+50%) | Neutral | 52 |
| B | Sierra | +0.22% | +1.57% ±3.9 | Popular (+40%) | Neutral | 35 |
| B | Orisa | +0.21% | +0.50% ±3.2 | Standard (-20%) | Neutral | 50 |
| B | Lifeweaver | +0.13% | -2.26% ±3.6 | Popular (+30%) | Neutral | 50 |
| B | Venture | +0.04% | +0.43% ±4.1 | Standard (-12%) | Neutral | 50 |
| B | Shion | +0.01% | +0.80% ±3.0 | Niche (-32%) | Neutral | 28 |
| B | Reinhardt | -0.06% | +0.07% ±3.0 | Standard (-17%) | Neutral | 49 |
| B | Genji | -0.13% | +1.00% ±3.1 | Standard (+14%) | Neutral | 52 |
| B | Mercy | -0.13% | +0.01% ±2.6 | Popular (+23%) | Neutral | 51 |
| B | Tracer | -0.13% | +0.03% ±2.0 | Niche (-29%) | Neutral | 52 |
| B | Anran | -0.15% | +0.10% ±4.1 | Standard (-19%) | Neutral | 50 |
| B | Doctrine *(provisional)* | -0.24% | -0.50% ±5.1 | Standard (+1%) | Neutral | 8 |
| B | Baptiste | -0.27% | +0.30% ±2.9 | Standard (+14%) | Neutral | 51 |
| B | Emre | -0.36% | -0.48% ±3.1 | Popular (+30%) | Neutral | 52 |
| B | Mei | -0.37% | -1.24% ±3.6 | Standard (-10%) | Neutral | 50 |
| B | Bastion | -0.44% | -0.88% ±3.5 | Standard (+8%) | Neutral | 50 |
| B | Roadhog *(provisional)* | -0.56% | -1.95% ±12.6 | Standard (+17%) | Neutral | 8 |
| B | Winston | -0.59% | -0.49% ±1.9 | Standard (+10%) | Neutral | 52 |
| B | D.Va | -0.62% | -0.81% ±3.3 | Standard (+7%) | Neutral | 52 |
| B | Mauga | -0.63% | -0.65% ±4.0 | Standard (-17%) | Neutral | 51 |
| B | Reaper | -0.73% | -1.24% ±3.1 | Niche (-25%) | Neutral | 51 |
| B | Jetpack Cat | -0.75% | -1.09% ±3.7 | Niche (-21%) | Neutral | 51 |
| B | Echo | -0.76% | -0.93% ±3.6 | Niche (-36%) | Neutral | 50 |
| B | Juno | -0.82% | -2.62% ±3.3 | Standard (-18%) | Neutral | 50 |
| B | Cassidy | -0.85% | -1.31% ±2.2 | Niche (-26%) | Neutral | 52 |
| B | Doomfist | -0.89% | -2.42% ±3.0 | Standard (-12%) | Neutral | 51 |
| B | Sombra *(provisional)* | -0.91% | -1.05% ±8.2 | Standard (-18%) | Neutral | 8 |
| B | D.Mon | -0.96% | -4.50% ±7.4 | Niche (-21%) | Neutral | 16 |
| B | Symmetra | -1.03% | -1.64% ±4.1 | Niche (-34%) | Neutral | 45 |
| B | Ashe | -1.09% | -1.46% ±1.7 | Map Priority (+66%) | Neutral | 51 |
| B | Wuyang | -1.11% | -2.02% ±2.3 | Standard (-2%) | Neutral | 52 |
| B | Vendetta | -1.13% | -3.28% ±4.2 | Standard (-8%) | Neutral | 44 |
| C | Mizuki | -1.64% | -2.84% ±3.2 | Niche (-30%) | Deterrent | 51 |
| C | Moira | -1.75% | -2.42% ±3.3 | Niche (-29%) | Deterrent | 51 |
| C | Soldier: 76 | -1.89% | -3.49% ±3.0 | Popular (+25%) | Trap Pick | 52 |
| C | Domina | -1.93% | -2.30% ±3.3 | Popular (+40%) | Trap Pick | 50 |
| C | Zarya | -2.43% | -3.43% ±3.5 | Niche (-35%) | Deterrent | 51 |
| C | Ramattra | -2.45% | -3.20% ±2.7 | Niche (-36%) | Deterrent | 46 |
| D | Pharah | -3.92% | -5.70% ±3.6 | Niche (-54%) | Deterrent | 49 |
| D | Junker Queen | -4.00% | -5.26% ±4.2 | Niche (-27%) | Deterrent | 40 |
| D | Lúcio | -5.01% | -5.56% ±3.4 | Niche (-65%) | Deterrent | 47 |

### Kings Row

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| A | Junkrat | +2.19% | +2.40% ±1.3 | Popular (+40%) | Meta | 51 |
| A | Orisa | +2.10% | +4.17% ±3.2 | Popular (+22%) | Meta | 52 |
| A | Ana | +1.50% | +1.62% ±1.2 | Standard (+11%) | Favorable | 52 |
| A | Hanzo | +1.48% | +2.12% ±1.7 | Map Priority (+58%) | Meta | 52 |
| B | Reaper | +1.06% | +1.78% ±1.8 | Standard (-4%) | Neutral | 52 |
| B | Widowmaker | +0.99% | +1.13% ±2.3 | Map Priority (+53%) | Neutral | 52 |
| B | Pharah | +0.98% | +1.33% ±1.9 | Map Priority (+52%) | Neutral | 52 |
| B | Zarya | +0.82% | +1.27% ±2.2 | Map Priority (+53%) | Neutral | 52 |
| B | D.Mon | +0.75% | +1.72% ±2.7 | Standard (+1%) | Neutral | 16 |
| B | Sierra | +0.22% | +0.87% ±1.6 | Standard (+4%) | Neutral | 35 |
| B | Lifeweaver | +0.13% | -1.44% ±2.3 | Standard (+2%) | Neutral | 51 |
| B | Domina | +0.11% | +0.19% ±1.3 | Popular (+22%) | Neutral | 51 |
| B | Mizuki | +0.09% | +0.12% ±1.8 | Standard (-6%) | Neutral | 52 |
| B | Venture | +0.04% | +2.12% ±2.9 | Standard (+9%) | Neutral | 51 |
| B | Cassidy | +0.01% | +0.13% ±1.5 | Standard (-8%) | Neutral | 52 |
| B | Reinhardt | -0.03% | +0.03% ±2.1 | Popular (+39%) | Neutral | 52 |
| B | Genji | -0.11% | +0.02% ±0.9 | Standard (+5%) | Neutral | 52 |
| B | Anran | -0.19% | -0.11% ±3.0 | Standard (-5%) | Neutral | 52 |
| B | Roadhog *(provisional)* | -0.22% | +0.32% ±6.9 | Standard (-11%) | Neutral | 8 |
| B | Kiriko | -0.24% | -0.25% ±0.9 | Standard (-11%) | Neutral | 52 |
| B | Baptiste | -0.39% | -0.35% ±1.1 | Popular (+41%) | Neutral | 52 |
| B | Mei | -0.42% | -0.68% ±1.8 | Map Priority (+69%) | Neutral | 52 |
| B | Bastion | -0.52% | -0.62% ±1.6 | Popular (+44%) | Neutral | 51 |
| B | Juno | -0.58% | -0.56% ±1.5 | Standard (+1%) | Neutral | 51 |
| B | Shion | -0.58% | -0.72% ±1.2 | Niche (-23%) | Neutral | 28 |
| B | Doomfist | -0.67% | -0.95% ±1.7 | Standard (-5%) | Neutral | 52 |
| B | Ramattra | -0.67% | -0.65% ±1.5 | Map Priority (+65%) | Neutral | 51 |
| B | D.Va | -0.72% | -0.93% ±2.3 | Niche (-21%) | Neutral | 52 |
| B | Sojourn | -0.75% | -0.82% ±1.2 | Standard (+7%) | Neutral | 52 |
| B | Sigma | -0.78% | -0.64% ±2.5 | Standard (+18%) | Neutral | 52 |
| B | Hazard | -0.79% | -0.86% ±2.3 | Niche (-28%) | Neutral | 51 |
| B | Illari | -0.86% | -1.47% ±1.1 | Standard (-8%) | Neutral | 52 |
| B | Zenyatta | -0.86% | -1.07% ±1.7 | Popular (+37%) | Neutral | 52 |
| B | Freja | -0.90% | -1.05% ±1.7 | Standard (+10%) | Neutral | 52 |
| B | Sombra *(provisional)* | -0.90% | -0.96% ±5.3 | Standard (-18%) | Neutral | 8 |
| B | Symmetra | -0.91% | -1.03% ±2.1 | Standard (+12%) | Neutral | 51 |
| B | Echo | -0.92% | -1.01% ±1.7 | Standard (+4%) | Neutral | 52 |
| B | Emre | -0.95% | -2.77% ±2.1 | Standard (-9%) | Neutral | 52 |
| B | Mauga | -1.08% | -1.17% ±1.5 | Standard (-18%) | Neutral | 51 |
| B | Soldier: 76 | -1.16% | -1.85% ±2.7 | Niche (-39%) | Neutral | 51 |
| C | Lúcio | -1.22% | -1.11% ±3.0 | Niche (-34%) | Deterrent | 52 |
| C | Moira | -1.24% | -1.27% ±1.3 | Standard (-8%) | Unfavorable | 51 |
| C | Brigitte | -1.26% | -1.65% ±2.5 | Niche (-35%) | Deterrent | 52 |
| C | Wuyang | -1.27% | -1.56% ±1.2 | Standard (+11%) | Unfavorable | 52 |
| C | Vendetta | -1.39% | -2.27% ±2.4 | Standard (-7%) | Unfavorable | 49 |
| C | Mercy | -1.41% | -2.26% ±1.8 | Standard (-2%) | Unfavorable | 52 |
| C | Ashe | -1.47% | -1.81% ±1.1 | Standard (-5%) | Unfavorable | 52 |
| C | Torbjörn | -1.74% | -2.06% ±1.8 | Standard (+5%) | Unfavorable | 50 |
| C | Doctrine *(provisional)* | -1.93% | -5.38% ±5.6 | Standard (-0%) | Unfavorable | 8 |
| C | Jetpack Cat | -2.41% | -3.18% ±2.7 | Standard (-17%) | Unfavorable | 52 |
| C | Tracer | -2.67% | -3.00% ±1.1 | Niche (-35%) | Deterrent | 52 |
| D | Junker Queen | -3.06% | -3.22% ±1.8 | Standard (-1%) | Unfavorable | 48 |
| D | Winston | -3.94% | -4.02% ±1.2 | Niche (-38%) | Deterrent | 52 |
| D | Wrecking Ball | -4.01% | -5.70% ±2.9 | Niche (-42%) | Deterrent | 52 |

### Lijiang Tower

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| S | Pharah | +4.54% | +4.84% ±1.1 | Map Priority (+106%) | Meta | 52 |
| S | Torbjörn | +3.26% | +3.61% ±1.4 | Niche (-20%) | Specialist | 47 |
| S | Reinhardt | +3.13% | +3.34% ±1.4 | Popular (+35%) | Meta | 52 |
| A | Lúcio | +2.70% | +2.78% ±1.1 | Map Priority (+90%) | Meta | 51 |
| A | Symmetra | +2.58% | +3.11% ±1.6 | Map Priority (+100%) | Meta | 52 |
| A | Zarya | +1.97% | +2.62% ±2.1 | Popular (+32%) | Meta | 52 |
| A | Reaper | +1.79% | +2.57% ±1.5 | Standard (+16%) | Favorable | 52 |
| A | Domina | +1.65% | +2.23% ±2.3 | Niche (-29%) | Specialist | 51 |
| A | Orisa | +1.40% | +2.59% ±2.9 | Popular (+34%) | Meta | 52 |
| A | Mizuki | +1.20% | +1.35% ±1.3 | Popular (+23%) | Meta | 52 |
| B | Jetpack Cat | +1.00% | +1.25% ±2.0 | Standard (+13%) | Neutral | 52 |
| B | Hazard | +0.92% | +0.99% ±0.9 | Standard (+2%) | Neutral | 51 |
| B | Kiriko | +0.90% | +1.03% ±1.0 | Standard (+10%) | Neutral | 52 |
| B | Mei | +0.81% | +3.52% ±3.0 | Standard (+7%) | Neutral | 52 |
| B | Moira | +0.78% | +1.25% ±1.8 | Popular (+25%) | Neutral | 51 |
| B | Ramattra | +0.72% | +1.00% ±1.7 | Popular (+36%) | Neutral | 52 |
| B | Sojourn | +0.62% | +0.95% ±1.4 | Standard (+5%) | Neutral | 52 |
| B | Cassidy | +0.45% | +0.54% ±0.8 | Popular (+23%) | Neutral | 52 |
| B | Junkrat | +0.35% | +0.42% ±1.7 | Popular (+26%) | Neutral | 51 |
| B | Doomfist | +0.24% | +0.64% ±1.7 | Standard (+13%) | Neutral | 52 |
| B | Sierra | +0.22% | -0.58% ±1.4 | Standard (-19%) | Neutral | 33 |
| B | Lifeweaver | +0.13% | -1.49% ±2.4 | Standard (-20%) | Neutral | 49 |
| B | Venture | +0.04% | -1.30% ±2.4 | Standard (+6%) | Neutral | 51 |
| B | Zenyatta | -0.04% | +0.39% ±2.4 | Niche (-23%) | Neutral | 52 |
| B | Brigitte | -0.07% | +0.28% ±3.0 | Standard (-4%) | Neutral | 52 |
| B | Genji | -0.13% | -0.02% ±0.9 | Standard (-9%) | Neutral | 51 |
| B | Hanzo | -0.13% | +0.27% ±3.2 | Niche (-39%) | Neutral | 52 |
| B | Bastion | -0.16% | -0.26% ±2.6 | Standard (-7%) | Neutral | 52 |
| B | Junker Queen | -0.28% | -0.21% ±1.8 | Popular (+30%) | Neutral | 51 |
| B | Illari | -0.29% | -0.46% ±1.4 | Niche (-36%) | Neutral | 52 |
| B | Roadhog *(provisional)* | -0.33% | -0.13% ±6.2 | Standard (+1%) | Neutral | 8 |
| B | Wuyang | -0.42% | -0.47% ±1.0 | Standard (-4%) | Neutral | 52 |
| B | Shion | -0.45% | -0.52% ±1.1 | Standard (+16%) | Neutral | 28 |
| B | Baptiste | -0.52% | -0.49% ±1.6 | Standard (-19%) | Neutral | 51 |
| B | Vendetta | -0.52% | -0.85% ±2.8 | Standard (+12%) | Neutral | 49 |
| B | Emre | -0.61% | -1.16% ±1.7 | Niche (-27%) | Neutral | 52 |
| B | D.Mon | -0.63% | -0.75% ±2.1 | Standard (+16%) | Neutral | 16 |
| B | Sombra *(provisional)* | -0.80% | -0.73% ±4.2 | Standard (+15%) | Neutral | 8 |
| B | Juno | -0.95% | -1.75% ±1.7 | Standard (+8%) | Neutral | 51 |
| B | D.Va | -1.09% | -1.95% ±2.6 | Niche (-23%) | Neutral | 52 |
| B | Mercy | -1.12% | -1.59% ±1.6 | Standard (-13%) | Neutral | 51 |
| B | Mauga | -1.17% | -1.44% ±2.4 | Popular (+25%) | Neutral | 52 |
| C | Freja | -1.38% | -1.70% ±1.7 | Niche (-25%) | Deterrent | 50 |
| C | Soldier: 76 | -1.39% | -1.57% ±1.2 | Niche (-21%) | Deterrent | 51 |
| C | Tracer | -1.46% | -1.57% ±1.0 | Standard (+10%) | Unfavorable | 52 |
| C | Anran | -1.47% | -2.35% ±2.4 | Standard (+11%) | Unfavorable | 51 |
| C | Wrecking Ball | -1.50% | -1.67% ±1.7 | Standard (+16%) | Unfavorable | 52 |
| C | Ana | -1.66% | -1.82% ±1.7 | Standard (-20%) | Unfavorable | 52 |
| C | Ashe | -1.66% | -3.47% ±2.3 | Niche (-66%) | Deterrent | 50 |
| C | Winston | -1.68% | -1.67% ±1.7 | Niche (-42%) | Deterrent | 52 |
| C | Sigma | -1.81% | -1.81% ±1.8 | Niche (-43%) | Deterrent | 52 |
| C | Echo | -2.16% | -3.21% ±2.6 | Standard (+3%) | Unfavorable | 52 |
| C | Doctrine *(provisional)* | -2.81% | -4.74% ±3.5 | Standard (-3%) | Unfavorable | 8 |
| D | Widowmaker | -7.37% | -7.42% ±1.9 | Niche (-65%) | Deterrent | 49 |

### Midtown

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| B | Orisa | +1.04% | +1.84% ±2.7 | Standard (+11%) | Neutral | 52 |
| B | Widowmaker | +0.67% | +0.99% ±3.6 | Map Priority (+52%) | Neutral | 52 |
| B | Doctrine *(provisional)* | +0.55% | +1.25% ±4.4 | Standard (+5%) | Neutral | 8 |
| B | Brigitte | +0.48% | +1.66% ±3.6 | Niche (-36%) | Neutral | 52 |
| B | Sierra | +0.22% | -0.15% ±3.9 | Standard (+13%) | Neutral | 35 |
| B | Lifeweaver | +0.13% | -0.59% ±3.6 | Standard (+18%) | Neutral | 51 |
| B | Venture | +0.04% | +1.88% ±4.1 | Standard (+11%) | Neutral | 51 |
| B | Illari | +0.02% | +0.79% ±2.4 | Standard (+19%) | Neutral | 52 |
| B | Baptiste | +0.00% | +0.66% ±2.3 | Popular (+39%) | Neutral | 52 |
| B | Genji | -0.03% | +3.06% ±2.9 | Standard (-10%) | Neutral | 52 |
| B | Wuyang | -0.07% | +0.07% ±2.6 | Popular (+20%) | Neutral | 52 |
| B | Vendetta | -0.14% | -0.06% ±3.6 | Standard (-17%) | Neutral | 42 |
| B | Reaper | -0.15% | +0.25% ±3.3 | Niche (-24%) | Neutral | 52 |
| B | Zarya | -0.15% | +0.25% ±3.2 | Popular (+43%) | Neutral | 52 |
| B | Sigma | -0.17% | +0.05% ±2.5 | Map Priority (+77%) | Neutral | 52 |
| B | Emre | -0.18% | +0.65% ±2.7 | Standard (+19%) | Neutral | 52 |
| B | Mizuki | -0.27% | -0.39% ±2.6 | Standard (-16%) | Neutral | 52 |
| B | Sojourn | -0.28% | -0.21% ±1.8 | Popular (+24%) | Neutral | 52 |
| B | Domina | -0.32% | -0.04% ±2.9 | Map Priority (+72%) | Neutral | 52 |
| B | Doomfist | -0.32% | -0.42% ±3.7 | Niche (-21%) | Neutral | 52 |
| B | Juno | -0.35% | +1.96% ±3.5 | Standard (+1%) | Neutral | 51 |
| B | Anran | -0.39% | -0.72% ±4.6 | Standard (-2%) | Neutral | 49 |
| B | Junkrat | -0.39% | -0.71% ±4.2 | Standard (+9%) | Neutral | 52 |
| B | Freja | -0.44% | -0.26% ±3.6 | Standard (-14%) | Neutral | 50 |
| B | Hanzo | -0.45% | -0.45% ±1.4 | Popular (+46%) | Neutral | 50 |
| B | D.Va | -0.47% | -0.32% ±2.9 | Niche (-32%) | Neutral | 50 |
| B | Shion | -0.55% | -0.96% ±2.1 | Standard (-18%) | Neutral | 28 |
| B | Mei | -0.70% | -2.83% ±3.6 | Popular (+34%) | Neutral | 52 |
| B | Ana | -0.77% | -0.83% ±2.0 | Standard (+10%) | Neutral | 52 |
| B | D.Mon | -0.80% | -1.92% ±4.9 | Standard (-8%) | Neutral | 16 |
| B | Moira | -0.80% | -0.56% ±3.6 | Standard (-18%) | Neutral | 51 |
| B | Mercy | -0.89% | -2.04% ±2.9 | Standard (+3%) | Neutral | 50 |
| B | Ashe | -0.99% | -1.50% ±2.5 | Popular (+37%) | Neutral | 52 |
| B | Tracer | -1.00% | -1.25% ±2.0 | Niche (-26%) | Neutral | 52 |
| B | Cassidy | -1.06% | -1.26% ±1.2 | Standard (-17%) | Neutral | 52 |
| B | Zenyatta | -1.13% | -1.85% ±2.4 | Popular (+37%) | Neutral | 52 |
| B | Soldier: 76 | -1.15% | -1.60% ±2.2 | Standard (-12%) | Neutral | 51 |
| C | Torbjörn | -1.22% | -2.21% ±3.9 | Standard (+16%) | Unfavorable | 50 |
| C | Symmetra | -1.23% | -1.70% ±3.1 | Popular (+42%) | Trap Pick | 52 |
| C | Roadhog *(provisional)* | -1.30% | -7.98% ±11.3 | Standard (-7%) | Unfavorable | 8 |
| C | Ramattra | -1.46% | -1.99% ±3.6 | Map Priority (+54%) | Trap Pick | 52 |
| C | Kiriko | -1.60% | -1.94% ±1.4 | Standard (-10%) | Unfavorable | 52 |
| C | Sombra *(provisional)* | -1.64% | -3.41% ±6.2 | Standard (-19%) | Unfavorable | 8 |
| C | Echo | -1.87% | -3.16% ±3.2 | Niche (-27%) | Deterrent | 52 |
| C | Mauga | -2.08% | -3.30% ±3.2 | Niche (-25%) | Deterrent | 48 |
| C | Pharah | -2.21% | -2.97% ±3.7 | Standard (-7%) | Unfavorable | 51 |
| C | Hazard | -2.44% | -3.93% ±3.7 | Niche (-46%) | Deterrent | 49 |
| C | Junker Queen | -2.63% | -3.10% ±3.5 | Standard (-18%) | Unfavorable | 45 |
| C | Bastion | -2.66% | -5.60% ±3.8 | Standard (+16%) | Unfavorable | 52 |
| C | Reinhardt | -2.89% | -3.69% ±3.5 | Standard (+11%) | Unfavorable | 52 |
| D | Wrecking Ball | -3.35% | -5.47% ±3.6 | Niche (-40%) | Deterrent | 50 |
| D | Jetpack Cat | -4.24% | -6.55% ±3.5 | Niche (-35%) | Deterrent | 52 |
| D | Winston | -5.16% | -5.97% ±3.2 | Niche (-41%) | Deterrent | 52 |
| D | Lúcio | -6.08% | -6.85% ±3.5 | Niche (-49%) | Deterrent | 45 |

### Neon Junction

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| A | Mizuki | +2.77% | +3.51% ±1.9 | Standard (-3%) | Favorable | 28 |
| A | Reinhardt | +1.74% | +2.14% ±2.5 | Popular (+40%) | Meta | 28 |
| A | Vendetta | +1.55% | +3.10% ±2.6 | Standard (-15%) | Favorable | 28 |
| B | Orisa | +1.09% | +1.49% ±1.9 | Popular (+27%) | Neutral | 28 |
| B | Shion | +1.06% | +1.64% ±1.2 | Standard (+13%) | Neutral | 28 |
| B | Zarya | +0.92% | +1.44% ±2.3 | Popular (+45%) | Neutral | 28 |
| B | Sigma | +0.78% | +0.94% ±1.6 | Map Priority (+61%) | Neutral | 28 |
| B | Reaper | +0.66% | +2.10% ±2.9 | Standard (-19%) | Neutral | 28 |
| B | Bastion | +0.63% | +1.03% ±2.9 | Popular (+45%) | Neutral | 28 |
| B | Ramattra | +0.59% | +1.16% ±2.5 | Map Priority (+91%) | Neutral | 28 |
| B | Widowmaker | +0.40% | +0.47% ±1.7 | Popular (+40%) | Neutral | 28 |
| B | Sierra | +0.22% | +1.35% ±3.3 | Standard (+15%) | Neutral | 24 |
| B | Lifeweaver | +0.13% | -1.09% ±2.4 | Standard (+12%) | Neutral | 28 |
| B | Zenyatta | +0.08% | +0.35% ±1.7 | Popular (+36%) | Neutral | 28 |
| B | Soldier: 76 | +0.07% | +0.34% ±2.4 | Niche (-24%) | Neutral | 28 |
| B | Junker Queen | +0.06% | +0.36% ±3.2 | Standard (-5%) | Neutral | 26 |
| B | Symmetra | +0.06% | +0.34% ±2.8 | Standard (+17%) | Neutral | 28 |
| B | Venture | +0.04% | +2.16% ±3.5 | Standard (-0%) | Neutral | 28 |
| B | Moira | +0.00% | +0.70% ±2.9 | Standard (-9%) | Neutral | 28 |
| B | Torbjörn | -0.03% | +0.02% ±4.0 | Standard (+8%) | Neutral | 27 |
| B | Genji | -0.22% | -0.48% ±1.5 | Standard (-11%) | Neutral | 28 |
| B | Kiriko | -0.22% | -0.26% ±2.0 | Standard (-7%) | Neutral | 28 |
| B | Illari | -0.26% | -0.63% ±2.5 | Standard (-7%) | Neutral | 28 |
| B | Sojourn | -0.36% | -0.34% ±1.5 | Popular (+27%) | Neutral | 28 |
| B | Emre | -0.42% | -0.60% ±1.9 | Standard (+16%) | Neutral | 28 |
| B | Cassidy | -0.50% | -0.57% ±1.5 | Standard (-10%) | Neutral | 28 |
| B | Mei | -0.55% | -1.28% ±2.5 | Map Priority (+65%) | Neutral | 28 |
| B | Roadhog *(provisional)* | -0.56% | -1.09% ±7.7 | Standard (-5%) | Neutral | 8 |
| B | Doctrine *(provisional)* | -0.60% | -1.75% ±6.1 | Standard (+3%) | Neutral | 8 |
| B | Anran | -0.68% | -1.77% ±4.5 | Standard (-3%) | Neutral | 28 |
| B | D.Mon | -0.71% | -1.00% ±2.8 | Standard (+6%) | Neutral | 16 |
| B | Juno | -0.77% | -1.69% ±2.7 | Standard (+11%) | Neutral | 28 |
| B | Sombra *(provisional)* | -0.80% | -0.66% ±5.6 | Niche (-25%) | Neutral | 8 |
| B | Baptiste | -0.89% | -1.55% ±3.1 | Popular (+25%) | Neutral | 28 |
| B | Domina | -0.89% | -0.82% ±2.6 | Map Priority (+57%) | Neutral | 28 |
| B | Pharah | -0.96% | -0.94% ±2.7 | Standard (+4%) | Neutral | 28 |
| B | Doomfist | -1.01% | -2.05% ±2.3 | Standard (-15%) | Neutral | 28 |
| B | Wuyang | -1.06% | -1.69% ±2.0 | Popular (+24%) | Neutral | 28 |
| B | Ashe | -1.12% | -1.48% ±1.6 | Standard (+8%) | Neutral | 28 |
| C | Ana | -1.23% | -1.33% ±1.6 | Standard (+7%) | Unfavorable | 28 |
| C | Wrecking Ball | -1.36% | -2.47% ±4.5 | Niche (-50%) | Deterrent | 28 |
| C | Hanzo | -1.37% | -1.90% ±2.2 | Popular (+30%) | Trap Pick | 28 |
| C | Mercy | -1.54% | -2.62% ±2.0 | Standard (-3%) | Unfavorable | 26 |
| C | Mauga | -1.70% | -2.26% ±2.5 | Standard (-17%) | Unfavorable | 27 |
| C | Jetpack Cat | -1.81% | -2.72% ±3.5 | Niche (-36%) | Deterrent | 28 |
| C | D.Va | -1.95% | -3.05% ±1.9 | Niche (-50%) | Deterrent | 28 |
| C | Lúcio | -2.29% | -2.33% ±3.3 | Niche (-40%) | Deterrent | 26 |
| C | Freja | -2.34% | -3.77% ±2.4 | Standard (+0%) | Unfavorable | 28 |
| C | Junkrat | -2.40% | -4.47% ±4.0 | Standard (+11%) | Unfavorable | 28 |
| C | Brigitte | -2.74% | -4.42% ±2.9 | Niche (-42%) | Deterrent | 28 |
| C | Tracer | -2.89% | -4.04% ±2.0 | Niche (-39%) | Deterrent | 28 |
| D | Echo | -3.47% | -4.90% ±2.2 | Niche (-41%) | Deterrent | 28 |
| D | Hazard | -4.53% | -5.78% ±2.4 | Niche (-48%) | Deterrent | 28 |
| D | Winston | -5.87% | -6.31% ±2.2 | Niche (-55%) | Deterrent | 28 |

### Nepal

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| A | Symmetra | +3.00% | +3.61% ±1.6 | Map Priority (+84%) | Meta | 52 |
| A | Torbjörn | +2.42% | +2.74% ±1.5 | Standard (-14%) | Favorable | 51 |
| A | Pharah | +2.19% | +2.45% ±1.3 | Map Priority (+52%) | Meta | 52 |
| A | Bastion | +2.13% | +2.56% ±1.6 | Standard (-14%) | Favorable | 52 |
| A | Reinhardt | +2.06% | +2.16% ±1.2 | Popular (+25%) | Meta | 52 |
| A | Mauga | +2.04% | +2.55% ±1.6 | Standard (+16%) | Favorable | 51 |
| A | Lúcio | +1.78% | +1.87% ±1.2 | Popular (+50%) | Meta | 52 |
| A | Ramattra | +1.78% | +2.21% ±1.6 | Standard (+18%) | Favorable | 52 |
| A | Jetpack Cat | +1.69% | +1.85% ±1.3 | Standard (+5%) | Favorable | 52 |
| A | Hazard | +1.67% | +1.98% ±1.6 | Standard (+6%) | Favorable | 52 |
| A | Orisa | +1.49% | +1.84% ±1.5 | Standard (+12%) | Favorable | 52 |
| A | Roadhog *(provisional)* | +1.24% | +4.96% ±6.2 | Standard (+4%) | Favorable | 8 |
| B | Sojourn | +1.13% | +1.35% ±1.0 | Standard (+8%) | Neutral | 52 |
| B | Junkrat | +1.11% | +1.37% ±2.0 | Standard (+8%) | Neutral | 52 |
| B | Mizuki | +1.06% | +1.12% ±0.9 | Standard (+15%) | Neutral | 52 |
| B | Kiriko | +0.82% | +0.87% ±0.7 | Standard (+8%) | Neutral | 52 |
| B | Brigitte | +0.79% | +1.15% ±1.8 | Standard (+1%) | Neutral | 52 |
| B | Reaper | +0.69% | +0.97% ±1.3 | Standard (+9%) | Neutral | 52 |
| B | Doomfist | +0.58% | +0.97% ±1.3 | Standard (+11%) | Neutral | 52 |
| B | Mei | +0.43% | +0.85% ±1.5 | Standard (-9%) | Neutral | 52 |
| B | Cassidy | +0.40% | +0.45% ±0.6 | Standard (+13%) | Neutral | 52 |
| B | Vendetta | +0.35% | +0.57% ±1.8 | Standard (+8%) | Neutral | 49 |
| B | Zarya | +0.29% | +0.35% ±0.9 | Standard (+17%) | Neutral | 52 |
| B | Sierra | +0.22% | +1.93% ±2.6 | Standard (-13%) | Neutral | 32 |
| B | Hanzo | +0.21% | +0.56% ±2.2 | Niche (-37%) | Neutral | 52 |
| B | Baptiste | +0.17% | +0.43% ±1.3 | Standard (-11%) | Neutral | 52 |
| B | Lifeweaver | +0.13% | +0.75% ±2.1 | Niche (-24%) | Neutral | 50 |
| B | Wuyang | +0.12% | +0.15% ±0.8 | Standard (+5%) | Neutral | 52 |
| B | Zenyatta | +0.09% | +0.20% ±1.1 | Niche (-21%) | Neutral | 52 |
| B | Venture | +0.04% | +0.91% ±2.3 | Standard (+5%) | Neutral | 52 |
| B | Emre | +0.03% | +0.35% ±1.1 | Standard (-15%) | Neutral | 52 |
| B | Moira | -0.10% | +0.36% ±2.5 | Standard (+20%) | Neutral | 52 |
| B | Domina | -0.13% | +0.03% ±2.0 | Standard (-17%) | Neutral | 50 |
| B | Freja | -0.31% | -0.24% ±1.5 | Niche (-23%) | Neutral | 52 |
| B | Illari | -0.32% | -0.42% ±1.0 | Niche (-27%) | Neutral | 51 |
| B | Sigma | -0.35% | -0.32% ±1.0 | Standard (-16%) | Neutral | 52 |
| B | Anran | -0.38% | -0.42% ±1.6 | Standard (+13%) | Neutral | 51 |
| B | Genji | -0.39% | -1.18% ±1.1 | Standard (-5%) | Neutral | 52 |
| B | Mercy | -0.56% | -0.69% ±1.4 | Standard (-13%) | Neutral | 51 |
| B | D.Mon | -0.60% | -0.78% ±2.7 | Standard (+11%) | Neutral | 16 |
| B | Sombra *(provisional)* | -0.60% | -0.26% ±4.6 | Standard (+8%) | Neutral | 8 |
| B | Junker Queen | -0.73% | -0.67% ±2.5 | Standard (+11%) | Neutral | 48 |
| B | Ashe | -0.87% | -0.94% ±1.4 | Niche (-44%) | Neutral | 52 |
| B | Tracer | -0.88% | -0.91% ±0.8 | Standard (+11%) | Neutral | 52 |
| B | Shion | -1.01% | -1.25% ±1.0 | Standard (+19%) | Neutral | 28 |
| B | Juno | -1.02% | -1.72% ±1.5 | Standard (+10%) | Neutral | 52 |
| B | Soldier: 76 | -1.17% | -1.34% ±1.4 | Standard (-10%) | Neutral | 52 |
| B | D.Va | -1.20% | -1.49% ±1.4 | Standard (-17%) | Neutral | 52 |
| C | Echo | -1.64% | -1.80% ±1.3 | Standard (+1%) | Unfavorable | 52 |
| C | Doctrine *(provisional)* | -2.21% | -3.40% ±3.1 | Standard (-2%) | Unfavorable | 8 |
| C | Ana | -2.51% | -2.56% ±0.7 | Standard (-16%) | Unfavorable | 52 |
| D | Wrecking Ball | -3.16% | -3.39% ±1.2 | Standard (-0%) | Unfavorable | 52 |
| D | Winston | -3.80% | -3.87% ±1.2 | Niche (-36%) | Deterrent | 52 |
| D | Widowmaker | -9.85% | -9.98% ±2.3 | Niche (-71%) | Deterrent | 51 |

### New Junk City

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| S | Junker Queen | +3.68% | +4.60% ±2.8 | Map Priority (+107%) | Meta | 50 |
| A | Lúcio | +2.96% | +3.15% ±1.6 | Map Priority (+99%) | Meta | 52 |
| A | Hazard | +2.40% | +2.93% ±1.8 | Standard (+11%) | Favorable | 51 |
| A | Symmetra | +2.07% | +3.53% ±2.9 | Standard (+15%) | Favorable | 50 |
| A | Mizuki | +1.99% | +3.21% ±2.9 | Popular (+48%) | Meta | 52 |
| A | Vendetta | +1.89% | +2.35% ±1.3 | Map Priority (+51%) | Meta | 48 |
| A | Moira | +1.57% | +2.60% ±2.2 | Map Priority (+67%) | Meta | 51 |
| A | D.Mon | +1.35% | +2.34% ±2.2 | Popular (+27%) | Meta | 16 |
| A | Torbjörn | +1.33% | +1.85% ±2.5 | Standard (-3%) | Favorable | 50 |
| A | Reinhardt | +1.23% | +1.56% ±2.6 | Popular (+26%) | Meta | 52 |
| B | Sombra *(provisional)* | +1.10% | +3.72% ±4.8 | Standard (+15%) | Neutral | 8 |
| B | Mauga | +1.02% | +1.42% ±1.8 | Popular (+47%) | Neutral | 50 |
| B | Reaper | +0.81% | +1.79% ±2.3 | Popular (+46%) | Neutral | 52 |
| B | Cassidy | +0.80% | +1.35% ±1.7 | Popular (+32%) | Neutral | 52 |
| B | Shion | +0.72% | +1.23% ±1.3 | Popular (+45%) | Neutral | 28 |
| B | Zarya | +0.71% | +1.35% ±2.7 | Popular (+44%) | Neutral | 52 |
| B | Domina | +0.69% | +1.69% ±3.7 | Niche (-29%) | Neutral | 46 |
| B | Tracer | +0.68% | +1.06% ±1.7 | Popular (+25%) | Neutral | 52 |
| B | Wrecking Ball | +0.49% | +0.93% ±2.9 | Standard (-19%) | Neutral | 52 |
| B | Sojourn | +0.39% | +0.56% ±1.2 | Standard (+17%) | Neutral | 52 |
| B | Brigitte | +0.37% | +0.77% ±2.3 | Standard (+9%) | Neutral | 51 |
| B | Anran | +0.35% | +0.87% ±2.6 | Popular (+49%) | Neutral | 51 |
| B | Orisa | +0.22% | +0.45% ±2.8 | Popular (+35%) | Neutral | 51 |
| B | Sierra | +0.22% | -1.36% ±1.6 | Niche (-22%) | Neutral | 26 |
| B | Doomfist | +0.21% | +1.11% ±2.6 | Standard (+2%) | Neutral | 51 |
| B | Mei | +0.20% | +0.94% ±2.6 | Standard (+19%) | Neutral | 51 |
| B | Lifeweaver | +0.13% | +0.23% ±2.2 | Niche (-35%) | Neutral | 49 |
| B | Baptiste | +0.11% | +1.92% ±3.5 | Niche (-25%) | Neutral | 52 |
| B | Ramattra | +0.09% | +0.54% ±2.8 | Map Priority (+56%) | Neutral | 52 |
| B | Venture | +0.04% | +1.43% ±2.2 | Popular (+38%) | Neutral | 50 |
| B | Doctrine *(provisional)* | -0.03% | +0.02% ±4.1 | Standard (-5%) | Neutral | 8 |
| B | Wuyang | -0.05% | -0.01% ±1.3 | Standard (+12%) | Neutral | 52 |
| B | Kiriko | -0.09% | -0.06% ±2.1 | Popular (+23%) | Neutral | 52 |
| B | Emre | -0.11% | +0.28% ±1.6 | Niche (-41%) | Neutral | 51 |
| B | Roadhog *(provisional)* | -0.16% | +0.61% ±7.2 | Standard (+2%) | Neutral | 8 |
| B | Genji | -0.23% | -1.19% ±2.4 | Standard (+2%) | Neutral | 52 |
| B | Mercy | -0.29% | -0.37% ±2.6 | Niche (-32%) | Neutral | 49 |
| B | Juno | -0.30% | +0.24% ±1.6 | Standard (+2%) | Neutral | 50 |
| B | Illari | -0.32% | -1.22% ±3.0 | Niche (-49%) | Neutral | 52 |
| B | Soldier: 76 | -0.68% | -0.84% ±2.1 | Standard (-8%) | Neutral | 51 |
| B | Junkrat | -0.70% | -0.87% ±2.2 | Standard (+9%) | Neutral | 49 |
| B | Bastion | -0.77% | -1.07% ±2.2 | Niche (-29%) | Neutral | 48 |
| B | Jetpack Cat | -0.96% | -1.17% ±2.4 | Standard (-14%) | Neutral | 51 |
| B | D.Va | -1.12% | -2.42% ±3.2 | Niche (-28%) | Neutral | 52 |
| C | Hanzo | -1.21% | -1.94% ±2.9 | Niche (-39%) | Deterrent | 51 |
| C | Ashe | -1.23% | -3.06% ±3.2 | Niche (-74%) | Deterrent | 46 |
| C | Zenyatta | -1.39% | -1.98% ±1.9 | Niche (-35%) | Deterrent | 50 |
| C | Echo | -1.47% | -1.81% ±2.0 | Niche (-52%) | Deterrent | 51 |
| C | Freja | -2.63% | -5.83% ±3.3 | Niche (-58%) | Deterrent | 47 |
| C | Sigma | -2.98% | -3.10% ±2.0 | Niche (-44%) | Deterrent | 51 |
| D | Ana | -4.14% | -5.24% ±2.6 | Niche (-36%) | Deterrent | 52 |
| D | Pharah | -4.83% | -6.66% ±3.2 | Niche (-36%) | Deterrent | 51 |
| D | Winston | -6.98% | -8.10% ±3.0 | Niche (-56%) | Deterrent | 52 |
| D | Widowmaker | -18.09% | -19.36% ±4.6 | Niche (-83%) | Deterrent | 29 |

### New Queen Street

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| S | Soldier: 76 | +4.10% | +5.27% ±1.5 | Map Priority (+134%) | Meta | 52 |
| A | Torbjörn | +2.98% | +3.37% ±1.5 | Standard (-12%) | Favorable | 51 |
| A | Junker Queen | +1.73% | +2.00% ±2.0 | Standard (+19%) | Favorable | 49 |
| A | Kiriko | +1.61% | +2.38% ±1.9 | Standard (+13%) | Favorable | 52 |
| A | Wrecking Ball | +1.36% | +1.80% ±2.1 | Popular (+42%) | Meta | 52 |
| A | Mizuki | +1.25% | +1.47% ±1.5 | Standard (+8%) | Favorable | 52 |
| A | Ramattra | +1.25% | +2.30% ±2.8 | Niche (-35%) | Specialist | 46 |
| B | Symmetra | +1.13% | +2.95% ±4.1 | Niche (-38%) | Neutral | 41 |
| B | Wuyang | +1.13% | +1.62% ±1.4 | Standard (+14%) | Neutral | 52 |
| B | Junkrat | +1.08% | +2.01% ±3.8 | Niche (-41%) | Neutral | 49 |
| B | Tracer | +1.00% | +1.24% ±1.2 | Popular (+34%) | Neutral | 52 |
| B | D.Mon | +0.92% | +2.52% ±3.3 | Standard (+9%) | Neutral | 16 |
| B | Doomfist | +0.89% | +2.62% ±2.3 | Standard (+11%) | Neutral | 52 |
| B | Zarya | +0.79% | +0.99% ±1.5 | Niche (-21%) | Neutral | 51 |
| B | Reinhardt | +0.78% | +0.95% ±2.2 | Standard (-3%) | Neutral | 52 |
| B | Freja | +0.67% | +2.31% ±3.1 | Niche (-33%) | Neutral | 51 |
| B | Mauga | +0.65% | +1.23% ±2.4 | Popular (+21%) | Neutral | 51 |
| B | Reaper | +0.61% | +1.26% ±2.0 | Standard (-12%) | Neutral | 52 |
| B | Hazard | +0.48% | +1.06% ±3.2 | Standard (+10%) | Neutral | 52 |
| B | Zenyatta | +0.41% | +1.27% ±2.4 | Niche (-30%) | Neutral | 52 |
| B | Mercy | +0.28% | +0.89% ±2.4 | Standard (-15%) | Neutral | 49 |
| B | Sierra | +0.22% | -1.07% ±2.0 | Standard (-7%) | Neutral | 34 |
| B | Hanzo | +0.18% | +0.45% ±1.9 | Niche (-54%) | Neutral | 50 |
| B | Lúcio | +0.15% | +0.19% ±1.1 | Standard (+16%) | Neutral | 52 |
| B | Lifeweaver | +0.13% | +1.90% ±3.0 | Standard (-14%) | Neutral | 51 |
| B | Shion | +0.07% | +0.22% ±1.2 | Popular (+28%) | Neutral | 28 |
| B | Venture | +0.04% | +0.06% ±3.5 | Standard (-17%) | Neutral | 51 |
| B | Winston | -0.19% | -0.07% ±1.8 | Standard (+4%) | Neutral | 52 |
| B | Genji | -0.24% | -0.75% ±1.6 | Standard (-10%) | Neutral | 52 |
| B | Illari | -0.27% | -0.46% ±1.6 | Standard (-14%) | Neutral | 52 |
| B | Mei | -0.37% | -1.12% ±3.4 | Niche (-37%) | Neutral | 52 |
| B | Brigitte | -0.41% | -0.38% ±1.5 | Standard (+9%) | Neutral | 52 |
| B | Emre | -0.52% | -0.87% ±1.7 | Standard (-5%) | Neutral | 52 |
| B | Moira | -0.52% | -0.16% ±2.9 | Standard (+5%) | Neutral | 52 |
| B | D.Va | -0.53% | -0.50% ±2.6 | Standard (+13%) | Neutral | 52 |
| B | Juno | -0.68% | -0.91% ±2.0 | Standard (+5%) | Neutral | 52 |
| B | Vendetta | -0.73% | -1.28% ±2.8 | Standard (-5%) | Neutral | 48 |
| B | Baptiste | -0.80% | -1.11% ±2.5 | Niche (-35%) | Neutral | 52 |
| B | Echo | -0.80% | -0.92% ±2.8 | Niche (-39%) | Neutral | 52 |
| B | Ashe | -0.86% | -1.03% ±2.1 | Niche (-47%) | Neutral | 51 |
| B | Sojourn | -0.88% | -0.98% ±1.2 | Standard (+10%) | Neutral | 52 |
| B | Pharah | -1.05% | -1.07% ±2.3 | Niche (-39%) | Neutral | 52 |
| B | Sombra *(provisional)* | -1.17% | -1.62% ±5.0 | Standard (+13%) | Neutral | 8 |
| C | Bastion | -1.26% | -2.13% ±3.0 | Niche (-26%) | Deterrent | 48 |
| C | Cassidy | -1.28% | -1.69% ±1.6 | Standard (-1%) | Unfavorable | 52 |
| C | Orisa | -1.35% | -2.23% ±2.7 | Standard (-3%) | Unfavorable | 52 |
| C | Doctrine *(provisional)* | -1.45% | -2.39% ±3.4 | Standard (+1%) | Unfavorable | 8 |
| C | Anran | -1.77% | -2.94% ±2.4 | Standard (-1%) | Unfavorable | 50 |
| C | Roadhog *(provisional)* | -1.95% | -5.68% ±6.4 | Standard (-0%) | Unfavorable | 8 |
| C | Domina | -1.99% | -2.46% ±3.6 | Niche (-26%) | Deterrent | 49 |
| C | Jetpack Cat | -2.51% | -2.86% ±1.8 | Standard (+6%) | Unfavorable | 52 |
| D | Ana | -3.39% | -3.60% ±1.3 | Standard (-12%) | Unfavorable | 52 |
| D | Sigma | -5.19% | -5.60% ±2.2 | Niche (-37%) | Deterrent | 52 |
| D | Widowmaker | -7.58% | -7.64% ±2.2 | Niche (-54%) | Deterrent | 51 |

### Numbani

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| A | Wrecking Ball | +1.86% | +2.76% ±2.7 | Standard (+6%) | Favorable | 51 |
| A | Doctrine *(provisional)* | +1.74% | +5.20% ±5.7 | Standard (+4%) | Favorable | 8 |
| A | Winston | +1.47% | +1.83% ±2.2 | Map Priority (+78%) | Meta | 52 |
| B | Bastion | +0.90% | +1.69% ±3.4 | Standard (+19%) | Neutral | 51 |
| B | Ana | +0.59% | +0.82% ±2.2 | Standard (+18%) | Neutral | 52 |
| B | Mercy | +0.44% | +1.57% ±2.8 | Popular (+38%) | Neutral | 51 |
| B | Tracer | +0.31% | +0.65% ±1.9 | Standard (-1%) | Neutral | 52 |
| B | Sierra | +0.22% | +2.14% ±3.9 | Standard (+7%) | Neutral | 32 |
| B | Kiriko | +0.19% | +0.30% ±1.6 | Standard (+1%) | Neutral | 52 |
| B | Lifeweaver | +0.13% | +1.04% ±4.0 | Standard (+19%) | Neutral | 51 |
| B | Junkrat | +0.12% | +0.28% ±3.7 | Standard (-1%) | Neutral | 50 |
| B | Venture | +0.04% | -3.68% ±4.0 | Standard (-5%) | Neutral | 51 |
| B | D.Va | -0.07% | +1.33% ±3.6 | Popular (+33%) | Neutral | 51 |
| B | Freja | -0.23% | +0.51% ±4.0 | Popular (+24%) | Neutral | 52 |
| B | Ashe | -0.28% | +0.63% ±2.3 | Map Priority (+63%) | Neutral | 52 |
| B | Hazard | -0.31% | -0.26% ±2.1 | Popular (+34%) | Neutral | 50 |
| B | Genji | -0.34% | -2.40% ±2.2 | Standard (+9%) | Neutral | 52 |
| B | Emre | -0.41% | -0.90% ±3.1 | Standard (+12%) | Neutral | 52 |
| B | Cassidy | -0.55% | -0.70% ±1.9 | Standard (-11%) | Neutral | 52 |
| B | Anran | -0.63% | -1.29% ±3.8 | Standard (-4%) | Neutral | 50 |
| B | Mei | -0.63% | -3.39% ±4.4 | Niche (-21%) | Neutral | 50 |
| B | Doomfist | -0.64% | -1.68% ±3.3 | Standard (+6%) | Neutral | 52 |
| B | Soldier: 76 | -0.70% | -0.88% ±2.1 | Standard (+5%) | Neutral | 52 |
| B | Hanzo | -0.71% | -1.01% ±3.1 | Standard (+1%) | Neutral | 52 |
| B | Illari | -0.72% | -2.33% ±2.1 | Standard (+8%) | Neutral | 52 |
| B | Sombra *(provisional)* | -0.72% | -0.20% ±7.6 | Standard (-9%) | Neutral | 8 |
| B | Shion | -0.75% | -1.33% ±1.9 | Standard (-19%) | Neutral | 28 |
| B | Juno | -0.84% | -2.61% ±3.1 | Standard (-8%) | Neutral | 51 |
| B | Vendetta | -0.86% | -1.94% ±3.6 | Standard (-1%) | Neutral | 43 |
| B | Echo | -1.05% | -1.32% ±2.6 | Map Priority (+74%) | Neutral | 52 |
| B | Torbjörn | -1.16% | -1.75% ±3.1 | Standard (+16%) | Neutral | 50 |
| B | Jetpack Cat | -1.17% | -1.61% ±3.1 | Standard (+16%) | Neutral | 52 |
| C | Wuyang | -1.24% | -2.04% ±2.0 | Niche (-20%) | Deterrent | 51 |
| C | Zenyatta | -1.24% | -2.32% ±2.8 | Niche (-21%) | Deterrent | 52 |
| C | Roadhog *(provisional)* | -1.25% | -10.23% ±13.4 | Standard (-6%) | Unfavorable | 7 |
| C | Sigma | -1.34% | -1.28% ±2.5 | Niche (-22%) | Deterrent | 51 |
| C | Orisa | -1.54% | -3.03% ±3.3 | Niche (-28%) | Deterrent | 51 |
| C | D.Mon | -1.68% | -6.15% ±5.5 | Niche (-24%) | Deterrent | 16 |
| C | Baptiste | -1.69% | -4.27% ±3.2 | Standard (-0%) | Unfavorable | 52 |
| C | Mauga | -1.83% | -2.66% ±2.9 | Standard (-13%) | Unfavorable | 48 |
| C | Brigitte | -1.90% | -2.72% ±2.6 | Standard (+15%) | Unfavorable | 51 |
| C | Reaper | -1.96% | -4.50% ±3.2 | Standard (-5%) | Unfavorable | 52 |
| C | Zarya | -2.16% | -2.88% ±3.3 | Niche (-33%) | Deterrent | 52 |
| C | Sojourn | -2.41% | -4.63% ±2.8 | Niche (-34%) | Deterrent | 52 |
| C | Moira | -2.44% | -4.00% ±3.7 | Niche (-27%) | Deterrent | 51 |
| C | Symmetra | -2.46% | -4.90% ±4.3 | Standard (-18%) | Unfavorable | 46 |
| C | Reinhardt | -2.94% | -4.23% ±4.4 | Niche (-36%) | Deterrent | 51 |
| D | Ramattra | -3.22% | -4.89% ±3.3 | Niche (-49%) | Deterrent | 41 |
| D | Pharah | -3.29% | -4.42% ±3.2 | Standard (-1%) | Unfavorable | 51 |
| D | Mizuki | -3.36% | -4.46% ±2.1 | Niche (-27%) | Deterrent | 51 |
| D | Lúcio | -3.84% | -4.28% ±4.0 | Niche (-35%) | Deterrent | 52 |
| D | Domina | -4.26% | -5.48% ±3.1 | Niche (-25%) | Deterrent | 45 |
| D | Junker Queen | -6.89% | -10.10% ±4.7 | Niche (-38%) | Deterrent | 39 |
| D | Widowmaker | -9.36% | -9.48% ±2.4 | Niche (-36%) | Deterrent | 51 |

### Oasis

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| S | Torbjörn | +3.42% | +3.84% ±1.4 | Standard (-10%) | Favorable | 51 |
| A | Cassidy | +2.09% | +2.36% ±0.8 | Popular (+45%) | Meta | 52 |
| A | Orisa | +1.77% | +2.32% ±1.8 | Standard (+6%) | Favorable | 52 |
| A | Doomfist | +1.48% | +2.37% ±1.4 | Standard (+12%) | Favorable | 52 |
| B | Jetpack Cat | +1.11% | +1.20% ±1.2 | Standard (+13%) | Neutral | 52 |
| B | Hazard | +1.00% | +1.10% ±1.1 | Popular (+28%) | Neutral | 52 |
| B | Mizuki | +0.96% | +1.04% ±1.1 | Popular (+31%) | Neutral | 52 |
| B | Vendetta | +0.92% | +1.41% ±1.9 | Standard (+18%) | Neutral | 48 |
| B | Freja | +0.81% | +2.31% ±2.8 | Niche (-31%) | Neutral | 52 |
| B | Kiriko | +0.81% | +0.89% ±0.8 | Standard (+15%) | Neutral | 52 |
| B | Brigitte | +0.77% | +0.87% ±0.9 | Popular (+26%) | Neutral | 52 |
| B | Zarya | +0.57% | +0.70% ±1.3 | Standard (+2%) | Neutral | 52 |
| B | Mauga | +0.55% | +1.26% ±2.8 | Popular (+20%) | Neutral | 51 |
| B | Moira | +0.54% | +0.85% ±1.5 | Popular (+24%) | Neutral | 52 |
| B | Shion | +0.54% | +0.82% ±1.0 | Popular (+28%) | Neutral | 28 |
| B | Reaper | +0.44% | +0.72% ±1.5 | Popular (+21%) | Neutral | 52 |
| B | Illari | +0.43% | +1.67% ±1.7 | Niche (-29%) | Neutral | 52 |
| B | Ramattra | +0.43% | +0.80% ±2.1 | Niche (-25%) | Neutral | 50 |
| B | Roadhog *(provisional)* | +0.42% | +2.21% ±6.0 | Standard (+2%) | Neutral | 8 |
| B | Hanzo | +0.39% | +1.00% ±2.5 | Niche (-42%) | Neutral | 52 |
| B | Soldier: 76 | +0.28% | +0.36% ±1.0 | Standard (-11%) | Neutral | 52 |
| B | Domina | +0.25% | +0.60% ±2.5 | Niche (-30%) | Neutral | 47 |
| B | Sierra | +0.22% | +0.52% ±1.8 | Standard (-16%) | Neutral | 32 |
| B | Tracer | +0.16% | +0.20% ±0.7 | Popular (+29%) | Neutral | 52 |
| B | Lifeweaver | +0.13% | +0.37% ±2.0 | Niche (-23%) | Neutral | 49 |
| B | Wuyang | +0.07% | +0.10% ±0.8 | Standard (-8%) | Neutral | 52 |
| B | Venture | +0.04% | -0.62% ±1.9 | Standard (+1%) | Neutral | 52 |
| B | Sojourn | -0.02% | +0.02% ±0.8 | Standard (-13%) | Neutral | 52 |
| B | Mei | -0.05% | +0.03% ±1.5 | Standard (-17%) | Neutral | 52 |
| B | Anran | -0.06% | +0.14% ±2.7 | Standard (+10%) | Neutral | 52 |
| B | Junkrat | -0.06% | -0.06% ±1.7 | Standard (-12%) | Neutral | 51 |
| B | D.Va | -0.21% | +0.23% ±2.4 | Standard (+12%) | Neutral | 52 |
| B | Symmetra | -0.30% | -0.27% ±1.5 | Standard (+11%) | Neutral | 52 |
| B | Baptiste | -0.34% | -0.13% ±2.0 | Standard (-18%) | Neutral | 52 |
| B | Bastion | -0.34% | -0.43% ±1.9 | Standard (-19%) | Neutral | 51 |
| B | Genji | -0.36% | -1.24% ±1.3 | Standard (-4%) | Neutral | 52 |
| B | Zenyatta | -0.49% | -0.50% ±1.2 | Niche (-31%) | Neutral | 52 |
| B | Junker Queen | -0.56% | -0.51% ±2.0 | Popular (+24%) | Neutral | 52 |
| B | Juno | -0.62% | -0.69% ±1.9 | Standard (-3%) | Neutral | 52 |
| B | Echo | -0.65% | -0.66% ±1.5 | Standard (-4%) | Neutral | 52 |
| B | Sombra *(provisional)* | -0.65% | -0.35% ±4.8 | Standard (+16%) | Neutral | 8 |
| B | Lúcio | -0.72% | -0.70% ±1.0 | Map Priority (+54%) | Neutral | 52 |
| B | Winston | -0.73% | -0.69% ±1.2 | Standard (-5%) | Neutral | 52 |
| B | Emre | -0.90% | -1.46% ±1.2 | Niche (-33%) | Neutral | 52 |
| B | Mercy | -0.95% | -1.31% ±1.5 | Standard (-16%) | Neutral | 51 |
| B | D.Mon | -0.97% | -1.28% ±2.2 | Standard (+6%) | Neutral | 16 |
| B | Ashe | -1.03% | -1.51% ±2.2 | Niche (-67%) | Neutral | 52 |
| B | Pharah | -1.06% | -1.08% ±2.4 | Standard (+18%) | Neutral | 52 |
| B | Reinhardt | -1.17% | -1.21% ±1.6 | Standard (-9%) | Neutral | 51 |
| C | Ana | -1.96% | -2.00% ±0.8 | Niche (-23%) | Deterrent | 52 |
| C | Wrecking Ball | -2.24% | -2.48% ±1.5 | Standard (+14%) | Unfavorable | 52 |
| C | Doctrine *(provisional)* | -2.81% | -4.89% ±3.6 | Standard (-5%) | Unfavorable | 8 |
| D | Sigma | -4.12% | -4.34% ±2.0 | Niche (-49%) | Deterrent | 52 |
| D | Widowmaker | -15.52% | -15.93% ±2.9 | Niche (-78%) | Deterrent | 46 |

### Paraiso

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| A | Jetpack Cat | +2.08% | +4.69% ±4.8 | Standard (+17%) | Favorable | 16 |
| A | Doctrine *(provisional)* | +1.91% | +11.86% ±9.2 | Standard (+6%) | Favorable | 8 |
| A | Bastion | +1.47% | +6.42% ±6.7 | Standard (+8%) | Favorable | 15 |
| A | Winston | +1.46% | +1.97% ±2.6 | Popular (+40%) | Meta | 16 |
| A | Ana | +1.25% | +1.68% ±2.3 | Standard (+16%) | Favorable | 16 |
| B | Pharah | +1.02% | +2.55% ±4.0 | Standard (+3%) | Neutral | 16 |
| B | Mercy | +0.96% | +5.29% ±4.1 | Map Priority (+56%) | Neutral | 16 |
| B | Orisa | +0.26% | +1.31% ±5.7 | Niche (-32%) | Neutral | 16 |
| B | Sierra | +0.22% | +0.25% ±7.5 | Standard (+15%) | Neutral | 11 |
| B | Vendetta | +0.17% | +1.30% ±5.0 | Standard (-5%) | Neutral | 16 |
| B | Lifeweaver | +0.13% | +1.03% ±7.2 | Standard (+17%) | Neutral | 16 |
| B | Venture | +0.04% | -3.40% ±8.6 | Standard (-9%) | Neutral | 15 |
| B | Echo | -0.00% | +0.68% ±3.3 | Map Priority (+85%) | Neutral | 16 |
| B | Mei | -0.02% | +2.33% ±7.5 | Niche (-28%) | Neutral | 16 |
| B | Symmetra | -0.09% | +1.84% ±8.4 | Niche (-21%) | Neutral | 15 |
| B | Genji | -0.21% | -0.90% ±2.7 | Standard (+10%) | Neutral | 16 |
| B | Emre | -0.35% | -0.42% ±3.2 | Standard (+19%) | Neutral | 16 |
| B | Brigitte | -0.38% | -0.08% ±4.9 | Standard (+8%) | Neutral | 16 |
| B | D.Va | -0.39% | +0.24% ±4.2 | Map Priority (+65%) | Neutral | 16 |
| B | Illari | -0.40% | -3.31% ±4.3 | Popular (+22%) | Neutral | 16 |
| B | Mauga | -0.40% | +0.51% ±7.4 | Standard (-11%) | Neutral | 15 |
| B | Soldier: 76 | -0.41% | -0.59% ±5.1 | Standard (-2%) | Neutral | 16 |
| B | Zenyatta | -0.48% | -0.53% ±3.0 | Standard (-6%) | Neutral | 16 |
| B | Doomfist | -0.50% | -2.10% ±5.3 | Standard (-10%) | Neutral | 16 |
| B | Shion | -0.50% | -1.42% ±3.5 | Niche (-24%) | Neutral | 16 |
| B | Reinhardt | -0.56% | -0.57% ±7.0 | Standard (-19%) | Neutral | 16 |
| B | Kiriko | -0.57% | -0.97% ±2.7 | Standard (-6%) | Neutral | 16 |
| B | D.Mon | -0.60% | -1.11% ±4.7 | Standard (-7%) | Neutral | 16 |
| B | Junkrat | -0.63% | -2.48% ±7.6 | Standard (+13%) | Neutral | 16 |
| B | Ashe | -0.66% | -0.14% ±3.6 | Map Priority (+70%) | Neutral | 16 |
| B | Roadhog *(provisional)* | -0.68% | -3.75% ±13.9 | Standard (-1%) | Neutral | 8 |
| B | Juno | -0.70% | -3.29% ±6.0 | Standard (-12%) | Neutral | 16 |
| B | Freja | -0.75% | -2.13% ±6.8 | Standard (+15%) | Neutral | 16 |
| B | Baptiste | -0.79% | -1.69% ±4.3 | Standard (-2%) | Neutral | 16 |
| B | Tracer | -0.94% | -1.43% ±3.0 | Standard (-15%) | Neutral | 16 |
| B | Anran | -1.01% | -6.13% ±7.3 | Standard (-7%) | Neutral | 15 |
| B | Torbjörn | -1.16% | -2.54% ±4.7 | Standard (+16%) | Neutral | 15 |
| C | Moira | -1.25% | -1.47% ±3.6 | Standard (-15%) | Unfavorable | 15 |
| C | Wrecking Ball | -1.29% | -3.49% ±6.6 | Standard (-15%) | Unfavorable | 16 |
| C | Wuyang | -1.35% | -4.55% ±3.8 | Standard (-11%) | Unfavorable | 16 |
| C | Cassidy | -1.36% | -2.20% ±2.2 | Standard (-10%) | Unfavorable | 16 |
| C | Sojourn | -1.36% | -4.47% ±4.7 | Niche (-25%) | Deterrent | 16 |
| C | Hazard | -1.38% | -2.02% ±3.7 | Popular (+29%) | Trap Pick | 16 |
| C | Widowmaker | -1.38% | -1.16% ±3.7 | Popular (+25%) | Trap Pick | 16 |
| C | Mizuki | -1.42% | -5.08% ±6.1 | Niche (-28%) | Deterrent | 16 |
| C | Sombra *(provisional)* | -1.46% | -7.81% ±13.4 | Standard (+0%) | Unfavorable | 8 |
| C | Reaper | -1.47% | -3.83% ±3.7 | Standard (-6%) | Unfavorable | 16 |
| C | Ramattra | -1.56% | -5.55% ±9.2 | Niche (-46%) | Deterrent | 13 |
| C | Hanzo | -2.01% | -4.18% ±3.5 | Standard (+1%) | Unfavorable | 16 |
| C | Junker Queen | -2.15% | -4.84% ±10.1 | Niche (-34%) | Deterrent | 14 |
| C | Domina | -2.66% | -7.36% ±8.6 | Standard (-6%) | Unfavorable | 13 |
| D | Zarya | -3.08% | -5.69% ±4.7 | Niche (-29%) | Deterrent | 16 |
| D | Sigma | -3.18% | -3.73% ±4.0 | Standard (-6%) | Unfavorable | 16 |
| D | Lúcio | -5.64% | -8.70% ±7.3 | Niche (-48%) | Deterrent | 16 |

### Rialto

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| A | Widowmaker | +2.15% | +2.40% ±2.8 | Map Priority (+110%) | Meta | 52 |
| A | Ana | +1.42% | +1.87% ±2.3 | Popular (+27%) | Meta | 52 |
| B | Pharah | +1.16% | +1.84% ±2.6 | Popular (+37%) | Neutral | 52 |
| B | Sigma | +1.11% | +1.47% ±2.3 | Standard (+13%) | Neutral | 52 |
| B | Winston | +0.94% | +1.08% ±1.5 | Standard (+7%) | Neutral | 51 |
| B | Brigitte | +0.91% | +2.06% ±3.0 | Niche (-20%) | Neutral | 52 |
| B | Bastion | +0.86% | +1.63% ±3.4 | Standard (+14%) | Neutral | 50 |
| B | Wuyang | +0.48% | +1.05% ±2.1 | Standard (-4%) | Neutral | 52 |
| B | Hazard | +0.35% | +0.50% ±1.7 | Standard (+1%) | Neutral | 51 |
| B | Echo | +0.34% | +0.67% ±1.8 | Popular (+48%) | Neutral | 52 |
| B | Illari | +0.33% | +0.97% ±1.4 | Popular (+27%) | Neutral | 52 |
| B | Sierra | +0.22% | +0.20% ±2.1 | Standard (+10%) | Neutral | 37 |
| B | Anran | +0.14% | +0.98% ±4.0 | Standard (-18%) | Neutral | 51 |
| B | Emre | +0.13% | +2.13% ±2.5 | Popular (+21%) | Neutral | 52 |
| B | Lifeweaver | +0.13% | -0.85% ±2.6 | Standard (+17%) | Neutral | 50 |
| B | Freja | +0.11% | +0.92% ±2.9 | Standard (+14%) | Neutral | 52 |
| B | Venture | +0.04% | -0.96% ±2.9 | Standard (-10%) | Neutral | 51 |
| B | Zarya | +0.03% | +0.37% ±2.6 | Standard (-10%) | Neutral | 51 |
| B | D.Va | -0.00% | +0.50% ±2.0 | Popular (+24%) | Neutral | 51 |
| B | Hanzo | +0.00% | +0.30% ±2.4 | Popular (+26%) | Neutral | 52 |
| B | Reaper | -0.03% | +0.41% ±2.8 | Niche (-23%) | Neutral | 52 |
| B | Shion | -0.08% | +0.03% ±1.4 | Niche (-30%) | Neutral | 28 |
| B | Genji | -0.11% | +0.85% ±2.4 | Standard (-3%) | Neutral | 52 |
| B | Mei | -0.11% | -0.00% ±2.7 | Standard (+7%) | Neutral | 51 |
| B | Baptiste | -0.19% | +0.40% ±2.6 | Standard (+5%) | Neutral | 52 |
| B | Orisa | -0.21% | -0.27% ±2.2 | Standard (+5%) | Neutral | 52 |
| B | Doomfist | -0.27% | -0.22% ±3.0 | Standard (-1%) | Neutral | 52 |
| B | Ashe | -0.40% | -0.02% ±1.7 | Popular (+50%) | Neutral | 52 |
| B | Vendetta | -0.40% | -0.71% ±3.4 | Standard (-20%) | Neutral | 46 |
| B | D.Mon | -0.45% | -0.52% ±3.1 | Standard (-10%) | Neutral | 16 |
| B | Mercy | -0.45% | -0.72% ±2.4 | Standard (+20%) | Neutral | 51 |
| B | Kiriko | -0.48% | -0.54% ±1.2 | Standard (-13%) | Neutral | 52 |
| B | Junkrat | -0.56% | -0.75% ±2.6 | Standard (+1%) | Neutral | 51 |
| B | Zenyatta | -0.64% | -0.81% ±2.3 | Popular (+34%) | Neutral | 52 |
| B | Sojourn | -0.66% | -0.86% ±2.4 | Standard (-9%) | Neutral | 52 |
| B | Jetpack Cat | -0.71% | -0.82% ±2.1 | Standard (+9%) | Neutral | 51 |
| B | Mizuki | -0.71% | -0.83% ±1.6 | Niche (-26%) | Neutral | 51 |
| B | Ramattra | -0.75% | -0.69% ±3.4 | Standard (-15%) | Neutral | 49 |
| B | Domina | -0.80% | -0.69% ±2.9 | Standard (+9%) | Neutral | 50 |
| B | Junker Queen | -0.87% | -0.73% ±4.9 | Niche (-28%) | Neutral | 45 |
| B | Tracer | -0.89% | -1.19% ±2.5 | Niche (-22%) | Neutral | 52 |
| B | Juno | -0.95% | -2.82% ±2.7 | Niche (-20%) | Neutral | 51 |
| B | Moira | -1.01% | -1.00% ±2.5 | Niche (-28%) | Neutral | 51 |
| C | Doctrine *(provisional)* | -1.32% | -3.39% ±5.3 | Standard (+1%) | Unfavorable | 8 |
| C | Roadhog *(provisional)* | -1.38% | -9.40% ±11.8 | Standard (+11%) | Unfavorable | 8 |
| C | Reinhardt | -1.43% | -1.56% ±2.3 | Standard (+4%) | Unfavorable | 51 |
| C | Cassidy | -1.45% | -2.17% ±1.9 | Niche (-28%) | Deterrent | 52 |
| C | Soldier: 76 | -1.46% | -2.13% ±2.3 | Standard (-15%) | Unfavorable | 51 |
| C | Mauga | -1.66% | -2.30% ±2.7 | Niche (-22%) | Deterrent | 49 |
| C | Sombra *(provisional)* | -1.88% | -9.20% ±11.1 | Standard (-16%) | Unfavorable | 8 |
| C | Torbjörn | -1.94% | -2.53% ±2.3 | Standard (+7%) | Unfavorable | 50 |
| C | Symmetra | -2.02% | -2.53% ±2.2 | Standard (-18%) | Unfavorable | 49 |
| C | Wrecking Ball | -2.62% | -3.07% ±1.9 | Standard (-16%) | Unfavorable | 51 |
| D | Lúcio | -6.33% | -6.82% ±2.7 | Niche (-51%) | Deterrent | 50 |

### Route 66

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| A | Ana | +2.44% | +2.63% ±1.2 | Standard (+17%) | Favorable | 52 |
| A | Sombra *(provisional)* | +1.62% | +7.68% ±6.4 | Standard (+13%) | Favorable | 8 |
| B | Torbjörn | +0.95% | +1.46% ±3.0 | Standard (+15%) | Neutral | 51 |
| B | Tracer | +0.84% | +1.58% ±2.2 | Standard (-16%) | Neutral | 52 |
| B | Shion | +0.83% | +2.92% ±2.4 | Niche (-21%) | Neutral | 28 |
| B | Wrecking Ball | +0.65% | +1.06% ±2.6 | Standard (+2%) | Neutral | 52 |
| B | Hazard | +0.62% | +1.26% ±3.1 | Standard (+6%) | Neutral | 51 |
| B | Mercy | +0.62% | +3.03% ±3.6 | Popular (+35%) | Neutral | 51 |
| B | Cassidy | +0.54% | +1.01% ±1.8 | Standard (-10%) | Neutral | 52 |
| B | Baptiste | +0.45% | +2.16% ±2.7 | Standard (+15%) | Neutral | 52 |
| B | Hanzo | +0.34% | +0.84% ±2.3 | Popular (+25%) | Neutral | 51 |
| B | Sojourn | +0.26% | +0.74% ±2.2 | Standard (-12%) | Neutral | 52 |
| B | Sierra | +0.22% | +1.77% ±4.4 | Popular (+37%) | Neutral | 36 |
| B | Doctrine *(provisional)* | +0.20% | +0.50% ±4.4 | Standard (+2%) | Neutral | 8 |
| B | D.Va | +0.18% | +2.82% ±4.0 | Standard (+18%) | Neutral | 52 |
| B | Ashe | +0.13% | +1.62% ±2.1 | Map Priority (+58%) | Neutral | 52 |
| B | Lifeweaver | +0.13% | +1.17% ±2.6 | Popular (+24%) | Neutral | 49 |
| B | Brigitte | +0.05% | +0.29% ±2.2 | Standard (+3%) | Neutral | 50 |
| B | Venture | +0.04% | -1.57% ±3.7 | Standard (+0%) | Neutral | 50 |
| B | Doomfist | -0.00% | +0.87% ±3.3 | Standard (-10%) | Neutral | 51 |
| B | Mauga | -0.02% | +0.74% ±4.0 | Niche (-24%) | Neutral | 50 |
| B | Junkrat | -0.03% | -0.01% ±2.7 | Standard (-1%) | Neutral | 48 |
| B | Illari | -0.10% | +0.22% ±2.4 | Popular (+34%) | Neutral | 52 |
| B | Freja | -0.15% | +0.28% ±2.8 | Popular (+28%) | Neutral | 52 |
| B | Wuyang | -0.20% | -0.22% ±2.2 | Standard (-1%) | Neutral | 52 |
| B | Genji | -0.22% | -0.59% ±1.8 | Standard (+12%) | Neutral | 52 |
| B | Vendetta | -0.28% | -0.43% ±3.5 | Standard (-8%) | Neutral | 46 |
| B | Widowmaker | -0.31% | -0.16% ±2.7 | Popular (+39%) | Neutral | 52 |
| B | Roadhog *(provisional)* | -0.40% | -0.33% ±12.3 | Popular (+29%) | Neutral | 8 |
| B | Juno | -0.41% | +0.39% ±2.4 | Standard (-8%) | Neutral | 50 |
| B | Emre | -0.44% | -0.64% ±1.7 | Standard (+19%) | Neutral | 52 |
| B | Jetpack Cat | -0.44% | -0.58% ±3.6 | Standard (-14%) | Neutral | 52 |
| B | Anran | -0.51% | -1.03% ±4.0 | Standard (-11%) | Neutral | 49 |
| B | Mei | -0.62% | -2.02% ±3.1 | Standard (+2%) | Neutral | 52 |
| B | Zarya | -0.98% | -1.05% ±4.1 | Standard (-17%) | Neutral | 52 |
| B | Pharah | -1.00% | -1.01% ±3.0 | Niche (-28%) | Neutral | 50 |
| B | Soldier: 76 | -1.04% | -1.38% ±2.0 | Standard (-15%) | Neutral | 52 |
| B | Echo | -1.11% | -1.81% ±3.9 | Standard (-2%) | Neutral | 52 |
| B | Sigma | -1.13% | -1.07% ±2.0 | Popular (+22%) | Neutral | 52 |
| B | D.Mon | -1.16% | -2.75% ±4.3 | Niche (-21%) | Neutral | 16 |
| B | Zenyatta | -1.19% | -1.90% ±2.3 | Standard (+5%) | Neutral | 51 |
| C | Reaper | -1.53% | -3.71% ±3.5 | Standard (-14%) | Unfavorable | 52 |
| C | Orisa | -1.60% | -2.95% ±3.1 | Niche (-25%) | Deterrent | 51 |
| C | Junker Queen | -1.62% | -1.86% ±4.3 | Niche (-27%) | Deterrent | 44 |
| C | Symmetra | -1.74% | -2.87% ±3.6 | Niche (-22%) | Deterrent | 50 |
| C | Ramattra | -1.81% | -2.61% ±3.6 | Niche (-37%) | Deterrent | 47 |
| C | Domina | -1.91% | -2.32% ±3.6 | Standard (+1%) | Unfavorable | 51 |
| C | Moira | -1.99% | -3.25% ±4.0 | Niche (-27%) | Deterrent | 52 |
| C | Winston | -2.22% | -2.33% ±3.4 | Popular (+35%) | Trap Pick | 52 |
| C | Kiriko | -2.51% | -3.31% ±1.7 | Standard (-12%) | Unfavorable | 52 |
| C | Mizuki | -2.52% | -3.30% ±2.1 | Standard (-18%) | Unfavorable | 52 |
| C | Bastion | -2.94% | -5.61% ±3.4 | Standard (+16%) | Unfavorable | 52 |
| D | Reinhardt | -3.10% | -3.89% ±3.3 | Niche (-25%) | Deterrent | 50 |
| D | Lúcio | -4.80% | -5.30% ±3.4 | Niche (-53%) | Deterrent | 48 |

### Runasapi

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| S | Reinhardt | +3.58% | +3.92% ±1.7 | Standard (+7%) | Favorable | 51 |
| A | Soldier: 76 | +2.10% | +3.96% ±2.6 | Map Priority (+66%) | Meta | 52 |
| A | Kiriko | +1.97% | +3.12% ±2.1 | Standard (+17%) | Favorable | 52 |
| A | Junker Queen | +1.80% | +2.06% ±1.9 | Popular (+28%) | Meta | 50 |
| A | Mauga | +1.48% | +2.44% ±2.4 | Popular (+41%) | Meta | 50 |
| A | Mizuki | +1.38% | +2.02% ±2.5 | Standard (+18%) | Favorable | 52 |
| B | Lúcio | +0.99% | +1.13% ±1.7 | Popular (+48%) | Neutral | 51 |
| B | Wrecking Ball | +0.90% | +1.31% ±2.4 | Popular (+22%) | Neutral | 51 |
| B | Domina | +0.89% | +1.84% ±3.4 | Niche (-21%) | Neutral | 49 |
| B | Anran | +0.86% | +1.31% ±1.8 | Standard (+8%) | Neutral | 49 |
| B | Torbjörn | +0.74% | +1.17% ±3.0 | Standard (-15%) | Neutral | 49 |
| B | Vendetta | +0.74% | +1.78% ±3.0 | Standard (+12%) | Neutral | 48 |
| B | Doctrine *(provisional)* | +0.64% | +1.04% ±3.1 | Standard (+1%) | Neutral | 8 |
| B | Mei | +0.61% | +2.32% ±2.7 | Niche (-29%) | Neutral | 50 |
| B | Bastion | +0.55% | +0.82% ±2.6 | Standard (-16%) | Neutral | 48 |
| B | D.Mon | +0.55% | +1.42% ±2.9 | Standard (+17%) | Neutral | 16 |
| B | Wuyang | +0.44% | +1.27% ±2.7 | Standard (+9%) | Neutral | 52 |
| B | Tracer | +0.29% | +0.51% ±1.6 | Popular (+33%) | Neutral | 52 |
| B | Zarya | +0.29% | +0.45% ±1.6 | Standard (+2%) | Neutral | 50 |
| B | Sierra | +0.22% | +1.17% ±2.8 | Standard (-8%) | Neutral | 33 |
| B | Jetpack Cat | +0.15% | +0.37% ±3.4 | Standard (+6%) | Neutral | 52 |
| B | Lifeweaver | +0.13% | +2.69% ±2.6 | Standard (-16%) | Neutral | 50 |
| B | Juno | +0.09% | +1.82% ±1.8 | Popular (+26%) | Neutral | 51 |
| B | Venture | +0.04% | +1.76% ±3.5 | Standard (-6%) | Neutral | 51 |
| B | Cassidy | -0.03% | +0.39% ±3.0 | Standard (+12%) | Neutral | 52 |
| B | Genji | -0.05% | +0.74% ±1.6 | Standard (-11%) | Neutral | 51 |
| B | Illari | -0.11% | +0.21% ±2.7 | Standard (-17%) | Neutral | 51 |
| B | Emre | -0.24% | +0.15% ±2.3 | Standard (-5%) | Neutral | 52 |
| B | D.Va | -0.28% | +0.30% ±3.0 | Standard (+0%) | Neutral | 52 |
| B | Sojourn | -0.28% | -0.26% ±1.0 | Standard (+15%) | Neutral | 52 |
| B | Winston | -0.31% | -0.12% ±2.3 | Standard (-14%) | Neutral | 52 |
| B | Brigitte | -0.34% | -0.20% ±2.9 | Standard (+11%) | Neutral | 52 |
| B | Reaper | -0.42% | -0.47% ±3.0 | Standard (-9%) | Neutral | 51 |
| B | Roadhog *(provisional)* | -0.52% | -0.78% ±6.5 | Standard (-1%) | Neutral | 8 |
| B | Orisa | -0.53% | -0.81% ±2.6 | Standard (+3%) | Neutral | 51 |
| B | Doomfist | -0.55% | -0.95% ±2.4 | Standard (+2%) | Neutral | 51 |
| B | Symmetra | -0.58% | -0.63% ±3.0 | Niche (-27%) | Neutral | 44 |
| B | Baptiste | -0.64% | -0.73% ±2.6 | Niche (-33%) | Neutral | 50 |
| B | Hazard | -0.64% | -0.66% ±2.2 | Standard (+9%) | Neutral | 50 |
| B | Shion | -0.75% | -1.01% ±1.3 | Popular (+40%) | Neutral | 28 |
| B | Ashe | -0.76% | -0.74% ±2.8 | Niche (-55%) | Neutral | 51 |
| B | Junkrat | -0.77% | -0.99% ±2.4 | Niche (-32%) | Neutral | 47 |
| B | Mercy | -0.94% | -2.08% ±2.7 | Niche (-21%) | Neutral | 49 |
| B | Zenyatta | -0.97% | -1.72% ±2.9 | Niche (-35%) | Neutral | 52 |
| C | Moira | -1.24% | -1.41% ±3.0 | Standard (+11%) | Unfavorable | 51 |
| C | Sombra *(provisional)* | -1.32% | -1.91% ±4.7 | Standard (+19%) | Unfavorable | 8 |
| C | Pharah | -1.33% | -1.43% ±2.5 | Niche (-30%) | Deterrent | 48 |
| C | Echo | -1.60% | -2.34% ±2.8 | Niche (-37%) | Deterrent | 51 |
| C | Hanzo | -1.74% | -3.27% ±3.2 | Niche (-58%) | Deterrent | 50 |
| C | Ramattra | -1.90% | -2.53% ±3.0 | Standard (-11%) | Unfavorable | 51 |
| C | Freja | -2.38% | -4.45% ±2.8 | Niche (-33%) | Deterrent | 50 |
| D | Ana | -3.79% | -4.60% ±2.3 | Niche (-24%) | Deterrent | 52 |
| D | Sigma | -4.13% | -4.46% ±2.4 | Niche (-32%) | Deterrent | 52 |
| D | Widowmaker | -16.67% | -17.19% ±3.1 | Niche (-62%) | Deterrent | 52 |

### Samoa

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| A | Symmetra | +1.93% | +2.20% ±1.3 | Popular (+31%) | Meta | 51 |
| A | Torbjörn | +1.77% | +2.31% ±2.3 | Standard (-1%) | Favorable | 52 |
| A | Mizuki | +1.55% | +1.69% ±1.1 | Popular (+23%) | Meta | 52 |
| A | Cassidy | +1.51% | +1.74% ±0.9 | Popular (+27%) | Meta | 52 |
| A | Moira | +1.43% | +2.19% ±1.9 | Popular (+22%) | Meta | 52 |
| B | Tracer | +1.12% | +1.25% ±0.8 | Popular (+26%) | Neutral | 52 |
| B | Anran | +1.05% | +2.23% ±2.6 | Standard (+18%) | Neutral | 51 |
| B | Wuyang | +0.97% | +1.41% ±1.4 | Standard (+6%) | Neutral | 52 |
| B | Junker Queen | +0.77% | +0.94% ±1.9 | Popular (+30%) | Neutral | 51 |
| B | Zarya | +0.65% | +0.83% ±1.5 | Popular (+21%) | Neutral | 52 |
| B | Ramattra | +0.60% | +1.05% ±2.2 | Standard (+8%) | Neutral | 50 |
| B | Kiriko | +0.51% | +0.57% ±0.9 | Standard (+9%) | Neutral | 52 |
| B | Hazard | +0.49% | +0.79% ±2.3 | Standard (+5%) | Neutral | 52 |
| B | Mauga | +0.49% | +0.96% ±2.3 | Popular (+22%) | Neutral | 50 |
| B | Shion | +0.49% | +0.80% ±1.1 | Popular (+28%) | Neutral | 28 |
| B | Bastion | +0.47% | +0.57% ±1.7 | Standard (-9%) | Neutral | 50 |
| B | Reinhardt | +0.39% | +0.45% ±1.4 | Standard (+12%) | Neutral | 52 |
| B | Sojourn | +0.39% | +0.68% ±1.6 | Standard (+8%) | Neutral | 52 |
| B | Doomfist | +0.32% | +0.52% ±1.1 | Standard (+6%) | Neutral | 52 |
| B | Orisa | +0.29% | +0.43% ±1.9 | Standard (+16%) | Neutral | 52 |
| B | Sierra | +0.22% | -0.60% ±1.8 | Standard (-15%) | Neutral | 32 |
| B | Emre | +0.21% | +0.80% ±1.2 | Standard (-17%) | Neutral | 52 |
| B | Baptiste | +0.15% | +1.03% ±2.4 | Standard (-16%) | Neutral | 51 |
| B | Lifeweaver | +0.13% | +2.17% ±1.7 | Standard (-15%) | Neutral | 51 |
| B | Lúcio | +0.13% | +0.25% ±1.9 | Popular (+33%) | Neutral | 52 |
| B | Illari | +0.08% | +0.38% ±1.3 | Niche (-22%) | Neutral | 52 |
| B | Domina | +0.07% | +0.51% ±3.0 | Standard (-16%) | Neutral | 51 |
| B | Venture | +0.04% | -0.23% ±2.5 | Standard (+9%) | Neutral | 51 |
| B | Roadhog *(provisional)* | -0.16% | +0.42% ±6.2 | Standard (+0%) | Neutral | 8 |
| B | Hanzo | -0.19% | -0.10% ±1.7 | Niche (-41%) | Neutral | 51 |
| B | Brigitte | -0.30% | -0.24% ±1.7 | Standard (+13%) | Neutral | 52 |
| B | Genji | -0.30% | -2.11% ±2.3 | Standard (-12%) | Neutral | 52 |
| B | Mei | -0.39% | -0.84% ±2.5 | Standard (-9%) | Neutral | 51 |
| B | Ashe | -0.41% | -0.21% ±1.2 | Niche (-44%) | Neutral | 52 |
| B | Zenyatta | -0.46% | -0.46% ±1.3 | Standard (-20%) | Neutral | 52 |
| B | D.Mon | -0.61% | -0.79% ±2.6 | Popular (+20%) | Neutral | 16 |
| B | Mercy | -0.65% | -0.90% ±1.7 | Niche (-21%) | Neutral | 50 |
| B | Reaper | -0.69% | -0.98% ±2.5 | Popular (+22%) | Neutral | 52 |
| B | Vendetta | -0.69% | -1.23% ±2.9 | Standard (+6%) | Neutral | 48 |
| B | Juno | -0.75% | -1.50% ±2.6 | Standard (+2%) | Neutral | 52 |
| B | Freja | -1.05% | -1.49% ±2.5 | Niche (-33%) | Neutral | 52 |
| B | Soldier: 76 | -1.08% | -1.23% ±1.4 | Standard (-13%) | Neutral | 52 |
| C | Sigma | -1.28% | -1.26% ±1.5 | Niche (-25%) | Deterrent | 52 |
| C | Echo | -1.33% | -1.58% ±1.9 | Niche (-32%) | Deterrent | 52 |
| C | D.Va | -1.50% | -1.94% ±1.4 | Standard (-16%) | Unfavorable | 52 |
| C | Wrecking Ball | -1.55% | -1.64% ±1.2 | Standard (+5%) | Unfavorable | 51 |
| C | Pharah | -1.66% | -1.82% ±2.3 | Standard (-14%) | Unfavorable | 51 |
| C | Junkrat | -1.76% | -2.16% ±2.0 | Standard (-8%) | Unfavorable | 51 |
| C | Jetpack Cat | -1.81% | -2.38% ±2.7 | Standard (-6%) | Unfavorable | 52 |
| C | Ana | -2.00% | -2.07% ±1.0 | Standard (-14%) | Unfavorable | 52 |
| C | Sombra *(provisional)* | -2.05% | -3.45% ±4.5 | Standard (+9%) | Unfavorable | 8 |
| C | Doctrine *(provisional)* | -2.21% | -3.34% ±3.0 | Standard (-2%) | Unfavorable | 8 |
| C | Winston | -2.90% | -2.96% ±1.6 | Niche (-30%) | Deterrent | 52 |
| D | Widowmaker | -6.71% | -6.74% ±1.9 | Niche (-71%) | Deterrent | 44 |

### Shambali Monastery

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| S | Reinhardt | +3.89% | +5.15% ±3.2 | Popular (+37%) | Meta | 51 |
| A | Mizuki | +2.45% | +3.25% ±2.1 | Standard (-12%) | Favorable | 51 |
| A | Ramattra | +2.31% | +3.72% ±2.6 | Map Priority (+88%) | Meta | 51 |
| A | Sigma | +1.71% | +2.22% ±2.5 | Map Priority (+53%) | Meta | 52 |
| A | Doctrine *(provisional)* | +1.55% | +3.04% ±3.9 | Standard (+5%) | Favorable | 8 |
| A | Bastion | +1.48% | +2.11% ±2.4 | Popular (+28%) | Meta | 50 |
| A | Junkrat | +1.36% | +1.80% ±2.3 | Popular (+44%) | Meta | 49 |
| A | Wuyang | +1.33% | +2.64% ±2.2 | Standard (+16%) | Favorable | 52 |
| B | Orisa | +1.07% | +1.50% ±2.0 | Popular (+21%) | Neutral | 52 |
| B | Pharah | +0.72% | +1.49% ±3.1 | Popular (+34%) | Neutral | 52 |
| B | Jetpack Cat | +0.65% | +1.06% ±3.1 | Standard (-1%) | Neutral | 52 |
| B | Mei | +0.65% | +2.41% ±2.7 | Popular (+39%) | Neutral | 51 |
| B | Echo | +0.31% | +0.92% ±2.5 | Map Priority (+51%) | Neutral | 52 |
| B | Sierra | +0.22% | -0.75% ±2.0 | Standard (+13%) | Neutral | 36 |
| B | Hanzo | +0.21% | +0.42% ±1.7 | Popular (+26%) | Neutral | 51 |
| B | Lifeweaver | +0.13% | -2.92% ±2.9 | Standard (+19%) | Neutral | 50 |
| B | Baptiste | +0.12% | +1.32% ±2.8 | Popular (+32%) | Neutral | 52 |
| B | Reaper | +0.12% | +0.74% ±2.8 | Standard (-15%) | Neutral | 51 |
| B | Vendetta | +0.09% | +0.60% ±3.8 | Standard (-3%) | Neutral | 42 |
| B | Sojourn | +0.05% | +0.51% ±2.6 | Standard (+4%) | Neutral | 52 |
| B | Venture | +0.04% | +2.01% ±3.1 | Standard (+18%) | Neutral | 48 |
| B | D.Va | -0.02% | +1.09% ±3.0 | Niche (-31%) | Neutral | 51 |
| B | Freja | -0.07% | +0.78% ±3.5 | Standard (+16%) | Neutral | 51 |
| B | Illari | -0.08% | +0.47% ±2.9 | Popular (+28%) | Neutral | 52 |
| B | Anran | -0.11% | +0.12% ±3.3 | Standard (+1%) | Neutral | 49 |
| B | Genji | -0.15% | +0.15% ±2.5 | Standard (-6%) | Neutral | 52 |
| B | Wrecking Ball | -0.21% | -0.07% ±3.6 | Niche (-25%) | Neutral | 51 |
| B | Shion | -0.23% | -0.15% ±2.6 | Standard (-15%) | Neutral | 28 |
| B | Emre | -0.26% | +0.08% ±2.4 | Standard (+17%) | Neutral | 52 |
| B | Kiriko | -0.42% | -0.62% ±2.4 | Standard (-13%) | Neutral | 52 |
| B | Brigitte | -0.50% | -0.47% ±3.6 | Niche (-29%) | Neutral | 51 |
| B | Juno | -0.57% | -0.38% ±3.1 | Standard (+4%) | Neutral | 52 |
| B | D.Mon | -0.66% | -1.03% ±3.5 | Standard (+15%) | Neutral | 16 |
| B | Ashe | -0.70% | -0.55% ±2.5 | Standard (+19%) | Neutral | 52 |
| B | Doomfist | -0.70% | -2.10% ±3.6 | Standard (-13%) | Neutral | 52 |
| B | Moira | -0.77% | -0.52% ±3.5 | Standard (-10%) | Neutral | 50 |
| B | Mercy | -0.81% | -2.00% ±3.1 | Standard (+10%) | Neutral | 49 |
| B | Hazard | -0.82% | -1.00% ±3.4 | Niche (-35%) | Neutral | 51 |
| B | Zarya | -1.09% | -1.19% ±3.0 | Standard (+15%) | Neutral | 52 |
| B | Torbjörn | -1.13% | -1.73% ±3.1 | Standard (+5%) | Neutral | 50 |
| B | Zenyatta | -1.18% | -1.80% ±2.2 | Popular (+22%) | Neutral | 52 |
| C | Ana | -1.22% | -1.50% ±2.8 | Standard (+7%) | Unfavorable | 52 |
| C | Domina | -1.25% | -1.33% ±3.9 | Popular (+30%) | Trap Pick | 52 |
| C | Roadhog *(provisional)* | -1.25% | -9.33% ±12.8 | Standard (-20%) | Unfavorable | 8 |
| C | Cassidy | -1.27% | -2.48% ±2.7 | Standard (-14%) | Unfavorable | 52 |
| C | Symmetra | -1.28% | -2.10% ±4.0 | Standard (-1%) | Unfavorable | 49 |
| C | Junker Queen | -1.45% | -1.60% ±4.2 | Standard (-9%) | Unfavorable | 46 |
| C | Soldier: 76 | -1.50% | -2.26% ±2.4 | Standard (-19%) | Unfavorable | 52 |
| C | Tracer | -1.53% | -1.96% ±1.9 | Niche (-32%) | Deterrent | 52 |
| C | Sombra *(provisional)* | -1.59% | -3.88% ±7.3 | Standard (-15%) | Unfavorable | 8 |
| C | Widowmaker | -1.60% | -1.53% ±2.2 | Standard (+8%) | Unfavorable | 50 |
| C | Mauga | -1.70% | -2.42% ±2.9 | Standard (-11%) | Unfavorable | 49 |
| D | Lúcio | -3.98% | -4.37% ±3.6 | Niche (-41%) | Deterrent | 49 |
| D | Winston | -5.17% | -5.41% ±1.8 | Niche (-46%) | Deterrent | 51 |

### Suravasa

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| S | Lúcio | +3.70% | +3.93% ±1.6 | Map Priority (+74%) | Meta | 51 |
| A | Symmetra | +2.48% | +3.24% ±1.9 | Standard (-4%) | Favorable | 49 |
| A | Junker Queen | +2.33% | +2.93% ±2.6 | Popular (+47%) | Meta | 50 |
| A | Wrecking Ball | +2.19% | +2.94% ±2.3 | Popular (+24%) | Meta | 52 |
| A | Jetpack Cat | +2.09% | +2.49% ±1.9 | Standard (+3%) | Favorable | 51 |
| A | Domina | +1.97% | +2.63% ±2.3 | Niche (-25%) | Specialist | 51 |
| A | Pharah | +1.71% | +2.16% ±1.9 | Standard (-19%) | Favorable | 51 |
| A | Ramattra | +1.66% | +2.47% ±2.2 | Standard (-10%) | Favorable | 50 |
| A | Kiriko | +1.61% | +2.69% ±2.2 | Standard (+17%) | Favorable | 52 |
| B | Brigitte | +1.17% | +1.94% ±2.3 | Standard (+16%) | Neutral | 52 |
| B | Anran | +0.88% | +2.01% ±2.8 | Standard (+19%) | Neutral | 52 |
| B | Mauga | +0.82% | +1.05% ±1.4 | Popular (+29%) | Neutral | 51 |
| B | Sojourn | +0.76% | +0.86% ±0.8 | Standard (+20%) | Neutral | 52 |
| B | Soldier: 76 | +0.67% | +0.82% ±1.1 | Popular (+20%) | Neutral | 51 |
| B | Reinhardt | +0.66% | +0.93% ±2.9 | Standard (+2%) | Neutral | 52 |
| B | Shion | +0.58% | +0.80% ±0.9 | Popular (+38%) | Neutral | 28 |
| B | Winston | +0.55% | +0.80% ±2.2 | Standard (-16%) | Neutral | 52 |
| B | Hazard | +0.35% | +0.51% ±1.8 | Standard (+15%) | Neutral | 51 |
| B | Reaper | +0.35% | +0.69% ±1.7 | Popular (+21%) | Neutral | 52 |
| B | Tracer | +0.27% | +0.37% ±1.0 | Popular (+31%) | Neutral | 52 |
| B | Sierra | +0.22% | +2.03% ±2.0 | Standard (-14%) | Neutral | 33 |
| B | Echo | +0.20% | +0.53% ±2.0 | Niche (-36%) | Neutral | 52 |
| B | Lifeweaver | +0.13% | -1.57% ±1.6 | Niche (-22%) | Neutral | 51 |
| B | Vendetta | +0.05% | +0.25% ±2.5 | Standard (+17%) | Neutral | 48 |
| B | D.Mon | +0.04% | +0.32% ±2.4 | Standard (+11%) | Neutral | 16 |
| B | Venture | +0.04% | -1.12% ±2.7 | Standard (+7%) | Neutral | 51 |
| B | Torbjörn | +0.03% | +0.06% ±2.5 | Standard (-4%) | Neutral | 52 |
| B | Doomfist | -0.01% | +0.47% ±2.5 | Standard (+9%) | Neutral | 52 |
| B | Genji | -0.03% | +1.04% ±1.7 | Standard (-2%) | Neutral | 51 |
| B | Sombra *(provisional)* | -0.05% | +0.95% ±4.5 | Standard (+17%) | Neutral | 8 |
| B | Mei | -0.10% | -0.04% ±1.9 | Niche (-21%) | Neutral | 52 |
| B | Illari | -0.15% | -0.09% ±2.0 | Niche (-30%) | Neutral | 52 |
| B | Bastion | -0.21% | -0.27% ±1.8 | Niche (-24%) | Neutral | 49 |
| B | Orisa | -0.32% | -0.57% ±3.4 | Standard (+7%) | Neutral | 52 |
| B | Wuyang | -0.33% | -0.45% ±2.1 | Standard (+3%) | Neutral | 52 |
| B | Doctrine *(provisional)* | -0.36% | -0.51% ±3.0 | Standard (-3%) | Neutral | 8 |
| B | Emre | -0.42% | -0.61% ±1.8 | Niche (-27%) | Neutral | 52 |
| B | Roadhog *(provisional)* | -0.43% | -0.48% ±6.1 | Standard (+6%) | Neutral | 8 |
| B | Zenyatta | -0.47% | -0.49% ±2.6 | Niche (-33%) | Neutral | 52 |
| B | Moira | -0.55% | -0.44% ±1.6 | Popular (+38%) | Neutral | 51 |
| B | Juno | -0.60% | -0.58% ±3.1 | Standard (+4%) | Neutral | 52 |
| B | Mercy | -0.63% | -1.14% ±2.4 | Niche (-25%) | Neutral | 51 |
| B | Cassidy | -0.67% | -0.70% ±0.7 | Standard (+20%) | Neutral | 52 |
| B | Ashe | -0.81% | -0.87% ±1.9 | Niche (-64%) | Neutral | 51 |
| B | Zarya | -0.90% | -0.91% ±2.3 | Standard (+7%) | Neutral | 52 |
| B | Hanzo | -0.96% | -1.61% ±3.3 | Niche (-49%) | Neutral | 52 |
| B | Junkrat | -0.98% | -1.15% ±1.8 | Standard (-19%) | Neutral | 50 |
| B | Mizuki | -1.11% | -1.34% ±1.7 | Popular (+33%) | Neutral | 52 |
| B | Baptiste | -1.18% | -1.79% ±2.1 | Niche (-30%) | Neutral | 52 |
| C | Freja | -1.87% | -3.08% ±2.5 | Niche (-38%) | Deterrent | 52 |
| C | D.Va | -2.38% | -3.38% ±1.6 | Standard (-6%) | Unfavorable | 52 |
| C | Ana | -2.91% | -3.18% ±1.5 | Niche (-28%) | Deterrent | 52 |
| D | Sigma | -4.30% | -4.56% ±2.1 | Niche (-44%) | Deterrent | 52 |
| D | Widowmaker | -11.90% | -12.04% ±2.1 | Niche (-79%) | Deterrent | 44 |

### Watchpoint Gibraltar

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|
| A | Winston | +2.74% | +3.11% ±1.9 | Map Priority (+135%) | Meta | 52 |
| A | Wrecking Ball | +2.38% | +3.74% ±3.0 | Standard (+8%) | Favorable | 51 |
| A | Ana | +2.11% | +2.38% ±1.5 | Popular (+24%) | Meta | 52 |
| A | Junkrat | +1.74% | +2.61% ±2.9 | Standard (+9%) | Favorable | 50 |
| A | Hazard | +1.50% | +1.97% ±2.0 | Map Priority (+53%) | Meta | 52 |
| A | Mercy | +1.39% | +3.22% ±2.3 | Popular (+21%) | Meta | 51 |
| A | D.Va | +1.32% | +3.08% ±2.0 | Popular (+47%) | Meta | 51 |
| B | Brigitte | +1.13% | +1.79% ±2.1 | Map Priority (+61%) | Neutral | 52 |
| B | Baptiste | +0.90% | +2.10% ±1.9 | Standard (+1%) | Neutral | 52 |
| B | Freja | +0.80% | +2.33% ±2.8 | Popular (+31%) | Neutral | 52 |
| B | Roadhog *(provisional)* | +0.71% | +5.12% ±8.2 | Standard (+9%) | Neutral | 7 |
| B | Bastion | +0.46% | +0.61% ±2.1 | Standard (-1%) | Neutral | 50 |
| B | Tracer | +0.44% | +0.68% ±1.5 | Standard (+10%) | Neutral | 52 |
| B | Ashe | +0.34% | +1.39% ±1.6 | Map Priority (+83%) | Neutral | 52 |
| B | Sierra | +0.22% | -0.26% ±2.3 | Standard (+9%) | Neutral | 36 |
| B | Anran | +0.15% | +1.05% ±4.1 | Standard (-15%) | Neutral | 49 |
| B | Lifeweaver | +0.13% | -0.60% ±3.6 | Popular (+31%) | Neutral | 52 |
| B | Echo | +0.11% | +0.45% ±2.1 | Popular (+21%) | Neutral | 52 |
| B | Doctrine *(provisional)* | +0.10% | +0.39% ±5.3 | Standard (-3%) | Neutral | 8 |
| B | Venture | +0.04% | -2.05% ±3.5 | Standard (-3%) | Neutral | 50 |
| B | Illari | +0.03% | +0.42% ±1.7 | Standard (+16%) | Neutral | 52 |
| B | Cassidy | +0.02% | +0.15% ±1.5 | Standard (-14%) | Neutral | 52 |
| B | Shion | -0.02% | +0.96% ±3.5 | Niche (-40%) | Neutral | 28 |
| B | Genji | -0.07% | +0.38% ±1.3 | Popular (+21%) | Neutral | 52 |
| B | Emre | -0.09% | +0.54% ±1.9 | Standard (+11%) | Neutral | 52 |
| B | Jetpack Cat | -0.13% | -0.08% ±3.0 | Standard (+20%) | Neutral | 52 |
| B | Mei | -0.23% | -0.41% ±2.9 | Niche (-37%) | Neutral | 47 |
| B | Soldier: 76 | -0.32% | -0.26% ±3.8 | Standard (-5%) | Neutral | 52 |
| B | Doomfist | -0.53% | -1.03% ±2.8 | Standard (+0%) | Neutral | 52 |
| B | Juno | -0.60% | -0.55% ±3.6 | Standard (-18%) | Neutral | 49 |
| B | Widowmaker | -0.62% | -0.58% ±1.4 | Map Priority (+52%) | Neutral | 51 |
| B | Wuyang | -0.64% | -0.86% ±1.6 | Niche (-29%) | Neutral | 52 |
| B | Kiriko | -0.65% | -0.83% ±1.7 | Standard (-4%) | Neutral | 52 |
| B | Hanzo | -0.66% | -0.86% ±2.8 | Standard (+13%) | Neutral | 52 |
| B | Pharah | -0.75% | -0.62% ±3.4 | Niche (-37%) | Neutral | 51 |
| B | Mizuki | -0.87% | -1.17% ±2.2 | Niche (-25%) | Neutral | 52 |
| B | D.Mon | -0.88% | -2.30% ±5.1 | Niche (-40%) | Neutral | 16 |
| B | Reaper | -1.05% | -1.70% ±2.5 | Standard (+17%) | Neutral | 52 |
| B | Moira | -1.13% | -1.27% ±4.1 | Niche (-37%) | Neutral | 52 |
| C | Ramattra | -1.33% | -1.70% ±3.4 | Niche (-69%) | Deterrent | 18 |
| C | Sojourn | -1.33% | -2.00% ±2.2 | Niche (-52%) | Deterrent | 52 |
| C | Zenyatta | -1.45% | -2.97% ±2.9 | Niche (-23%) | Deterrent | 52 |
| C | Sombra *(provisional)* | -1.50% | -3.33% ±7.0 | Standard (-1%) | Unfavorable | 8 |
| C | Torbjörn | -1.59% | -2.47% ±3.2 | Standard (+5%) | Unfavorable | 52 |
| C | Vendetta | -1.69% | -4.45% ±3.8 | Standard (-1%) | Unfavorable | 46 |
| C | Junker Queen | -1.73% | -2.10% ±4.9 | Niche (-49%) | Deterrent | 38 |
| C | Orisa | -2.10% | -4.26% ±3.4 | Niche (-50%) | Deterrent | 52 |
| C | Mauga | -2.11% | -3.49% ±3.4 | Niche (-26%) | Deterrent | 49 |
| C | Symmetra | -2.32% | -3.86% ±3.5 | Niche (-31%) | Deterrent | 47 |
| D | Domina | -3.36% | -4.66% ±3.8 | Niche (-44%) | Deterrent | 42 |
| D | Zarya | -3.91% | -5.36% ±3.0 | Niche (-59%) | Deterrent | 52 |
| D | Reinhardt | -5.22% | -6.58% ±3.2 | Niche (-52%) | Deterrent | 48 |
| D | Lúcio | -6.19% | -6.78% ±3.0 | Niche (-54%) | Deterrent | 47 |
| D | Sigma | -6.74% | -7.53% ±2.6 | Niche (-44%) | Deterrent | 52 |

