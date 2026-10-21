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

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| S | 83% | Junker Queen | +3.95% | +4.48% ±2.0 | Map Priority (+81%) | Meta | 51 |
| A | 68% | Lúcio | +2.68% | +2.80% ±1.3 | Map Priority (+115%) | Meta | 52 |
| A | 60% | Mauga | +2.61% | +3.73% ±2.1 | Popular (+50%) | Meta | 52 |
| A | 66% | Anran | +2.08% | +4.00% ±2.5 | Map Priority (+68%) | Meta | 52 |
| A | 69% | Junkrat | +1.91% | +2.31% ±1.9 | Standard (+17%) | Favorable | 50 |
| A | 63% | Zarya | +1.85% | +2.52% ±2.1 | Popular (+34%) | Meta | 52 |
| A | 49% | Reinhardt | +1.63% | +2.10% ±2.8 | Standard (+16%) | Favorable | 50 |
| A | 58% | D.Mon | +1.56% | +2.80% ±2.4 | Popular (+24%) | Meta | 16 |
| A | 56% | Vendetta | +1.48% | +2.77% ±2.5 | Map Priority (+65%) | Meta | 52 |
| A | 59% | Moira | +1.40% | +1.94% ±1.6 | Map Priority (+90%) | Meta | 52 |
| A | 51% | Brigitte | +1.31% | +2.17% ±2.3 | Popular (+27%) | Meta | 52 |
| B | 48% | Sombra *(provisional)* | +1.03% | +2.99% ±4.2 | Popular (+21%) | Neutral | 8 |
| B | 61% | Ramattra | +0.99% | +1.28% ±1.6 | Popular (+38%) | Neutral | 52 |
| B | 58% | Mizuki | +0.97% | +1.33% ±2.2 | Map Priority (+61%) | Neutral | 52 |
| B | 71% | Cassidy | +0.71% | +1.45% ±2.1 | Popular (+35%) | Neutral | 52 |
| B | 77% | Wrecking Ball | +0.71% | +0.82% ±1.4 | Standard (-4%) | Neutral | 51 |
| B | 69% | Jetpack Cat | +0.46% | +0.66% ±2.4 | Standard (-8%) | Neutral | 52 |
| B | 89% | Shion | +0.45% | +0.83% ±1.3 | Popular (+42%) | Neutral | 28 |
| B | 83% | Doomfist | +0.42% | +1.04% ±1.8 | Standard (+17%) | Neutral | 52 |
| B | 90% | Sierra | +0.22% | -1.67% ±1.6 | Niche (-29%) | Neutral | 27 |
| B | 95% | Hazard | +0.20% | +0.25% ±1.2 | Popular (+35%) | Neutral | 51 |
| B | 74% | Lifeweaver | +0.13% | +0.35% ±3.2 | Niche (-39%) | Neutral | 51 |
| B | 78% | Reaper | +0.08% | +0.62% ±2.7 | Map Priority (+65%) | Neutral | 52 |
| B | 77% | Venture | +0.04% | +1.06% ±2.7 | Map Priority (+57%) | Neutral | 52 |
| B | 83% | Torbjörn | +0.03% | +0.05% ±1.9 | Standard (-5%) | Neutral | 50 |
| B | 91% | Illari | -0.04% | +0.20% ±1.6 | Niche (-50%) | Neutral | 51 |
| B | 80% | Tracer | -0.11% | +0.12% ±2.4 | Popular (+29%) | Neutral | 52 |
| B | 87% | Genji | -0.13% | +0.29% ±1.9 | Standard (+5%) | Neutral | 52 |
| B | 99% | Kiriko | -0.14% | -0.14% ±0.9 | Popular (+21%) | Neutral | 51 |
| B | 78% | Emre | -0.26% | +0.08% ±2.4 | Niche (-45%) | Neutral | 52 |
| B | 80% | Mei | -0.28% | -0.47% ±2.2 | Standard (+8%) | Neutral | 52 |
| B | 82% | Symmetra | -0.36% | -0.33% ±1.8 | Standard (+8%) | Neutral | 51 |
| B | 80% | Sojourn | -0.38% | -0.36% ±2.1 | Standard (+2%) | Neutral | 52 |
| B | 83% | Soldier: 76 | -0.38% | -0.39% ±1.8 | Niche (-25%) | Neutral | 51 |
| B | 83% | Juno | -0.40% | +0.08% ±1.8 | Standard (+3%) | Neutral | 52 |
| B | 78% | Zenyatta | -0.64% | -0.72% ±1.6 | Niche (-46%) | Neutral | 51 |
| B | 66% | Mercy | -0.72% | -1.45% ±2.7 | Niche (-40%) | Neutral | 49 |
| B | 63% | Baptiste | -0.74% | -1.09% ±3.1 | Niche (-29%) | Neutral | 51 |
| B | 59% | Wuyang | -0.99% | -1.67% ±2.1 | Standard (+3%) | Neutral | 52 |
| B | 43% | Roadhog *(provisional)* | -1.05% | -2.80% ±6.8 | Standard (+3%) | Neutral | 8 |
| C | 51% | Ashe | -1.40% | -3.92% ±3.2 | Niche (-79%) | Deterrent | 37 |
| C | 46% | Doctrine *(provisional)* | -1.51% | -2.46% ±3.3 | Standard (-9%) | Unfavorable | 8 |
| C | 42% | Domina | -1.55% | -1.81% ±3.8 | Niche (-35%) | Deterrent | 46 |
| C | 72% | Bastion | -1.73% | -2.06% ±1.6 | Niche (-26%) | Deterrent | 49 |
| C | 68% | D.Va | -1.84% | -3.17% ±2.1 | Niche (-24%) | Deterrent | 52 |
| C | 65% | Hanzo | -2.07% | -3.24% ±2.5 | Niche (-50%) | Deterrent | 51 |
| C | 69% | Freja | -2.11% | -3.26% ±2.3 | Niche (-56%) | Deterrent | 46 |
| C | 83% | Orisa | -2.31% | -2.67% ±1.3 | Standard (+14%) | Unfavorable | 51 |
| C | 53% | Echo | -2.91% | -3.61% ±1.8 | Niche (-44%) | Deterrent | 51 |
| D | 65% | Ana | -3.38% | -3.98% ±2.1 | Niche (-39%) | Deterrent | 52 |
| D | 72% | Pharah | -3.65% | -4.42% ±2.5 | Niche (-21%) | Deterrent | 51 |
| D | 87% | Sigma | -4.50% | -5.00% ±2.8 | Niche (-47%) | Deterrent | 52 |
| D | 93% | Winston | -4.75% | -5.18% ±2.5 | Niche (-49%) | Deterrent | 51 |
| D | 100% | Widowmaker | -19.32% | -24.04% ±8.4 | Niche (-86%) | Deterrent | 9 |

### Antarctic Peninsula

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| S | 65% | Cassidy | +3.16% | +3.60% ±0.8 | Popular (+34%) | Meta | 40 |
| A | 57% | Junker Queen | +2.77% | +3.08% ±1.8 | Popular (+37%) | Meta | 40 |
| A | 58% | Torbjörn | +2.39% | +3.22% ±2.4 | Standard (-3%) | Favorable | 40 |
| A | 82% | Ramattra | +2.03% | +2.40% ±1.4 | Popular (+22%) | Meta | 40 |
| A | 70% | Symmetra | +1.76% | +2.19% ±1.7 | Standard (+20%) | Favorable | 40 |
| A | 67% | Mauga | +1.66% | +2.20% ±1.7 | Popular (+23%) | Meta | 40 |
| A | 66% | Zarya | +1.54% | +1.84% ±1.5 | Popular (+22%) | Meta | 40 |
| A | 70% | Bastion | +1.53% | +1.71% ±1.2 | Standard (-12%) | Favorable | 39 |
| A | 66% | Moira | +1.45% | +1.76% ±1.2 | Popular (+30%) | Meta | 40 |
| A | 62% | Reinhardt | +1.45% | +1.57% ±1.5 | Standard (+15%) | Favorable | 40 |
| A | 57% | Tracer | +1.28% | +1.46% ±0.9 | Standard (+20%) | Favorable | 40 |
| A | 46% | Domina | +1.23% | +1.73% ±2.3 | Niche (-26%) | Specialist | 39 |
| B | 54% | Kiriko | +1.17% | +1.26% ±0.8 | Standard (+11%) | Neutral | 40 |
| B | 68% | Soldier: 76 | +0.92% | +1.17% ±1.3 | Standard (-7%) | Neutral | 40 |
| B | 76% | Brigitte | +0.74% | +0.96% ±1.4 | Standard (+10%) | Neutral | 40 |
| B | 80% | Mizuki | +0.60% | +0.69% ±1.5 | Popular (+29%) | Neutral | 40 |
| B | 79% | Orisa | +0.54% | +0.72% ±1.8 | Standard (+18%) | Neutral | 40 |
| B | 93% | Wuyang | +0.53% | +0.64% ±0.9 | Standard (+7%) | Neutral | 40 |
| B | 81% | Vendetta | +0.51% | +0.76% ±1.7 | Standard (+17%) | Neutral | 37 |
| B | 85% | Baptiste | +0.41% | +0.98% ±1.6 | Standard (-14%) | Neutral | 40 |
| B | 86% | Illari | +0.30% | +1.29% ±1.8 | Niche (-29%) | Neutral | 40 |
| B | 83% | Sierra | +0.22% | -0.89% ±2.1 | Standard (-11%) | Neutral | 31 |
| B | 85% | Mei | +0.18% | +0.57% ±2.0 | Standard (+3%) | Neutral | 40 |
| B | 82% | Lifeweaver | +0.13% | +0.96% ±2.2 | Niche (-25%) | Neutral | 40 |
| B | 91% | Reaper | +0.06% | +0.25% ±1.6 | Popular (+22%) | Neutral | 40 |
| B | 79% | D.Mon | +0.04% | +0.32% ±2.4 | Popular (+24%) | Neutral | 16 |
| B | 88% | Venture | +0.04% | -1.50% ±1.8 | Standard (+8%) | Neutral | 39 |
| B | 96% | Zenyatta | +0.03% | +0.17% ±1.3 | Niche (-24%) | Neutral | 40 |
| B | 92% | Doomfist | -0.17% | -0.10% ±1.5 | Standard (+1%) | Neutral | 40 |
| B | 99% | Sojourn | -0.18% | -0.15% ±0.9 | Standard (+1%) | Neutral | 40 |
| B | 90% | Lúcio | -0.27% | -0.22% ±1.4 | Popular (+48%) | Neutral | 40 |
| B | 48% | Roadhog *(provisional)* | -0.37% | -0.23% ±7.3 | Standard (+3%) | Neutral | 8 |
| B | 76% | Anran | -0.45% | -0.59% ±2.4 | Standard (+16%) | Neutral | 39 |
| B | 89% | Genji | -0.52% | -1.77% ±1.1 | Standard (-7%) | Neutral | 40 |
| B | 86% | Emre | -0.53% | -0.77% ±1.4 | Niche (-29%) | Neutral | 40 |
| B | 75% | Hanzo | -0.61% | -0.68% ±1.9 | Niche (-42%) | Neutral | 40 |
| B | 71% | Freja | -0.66% | -0.75% ±2.2 | Niche (-30%) | Neutral | 40 |
| B | 85% | Shion | -0.69% | -0.83% ±1.0 | Popular (+36%) | Neutral | 28 |
| B | 75% | Ashe | -0.71% | -0.66% ±1.6 | Niche (-59%) | Neutral | 40 |
| B | 71% | Juno | -0.71% | -1.05% ±2.0 | Standard (+9%) | Neutral | 40 |
| B | 62% | Mercy | -0.90% | -1.62% ±2.2 | Niche (-22%) | Neutral | 39 |
| B | 65% | Echo | -0.94% | -1.00% ±1.4 | Niche (-30%) | Neutral | 40 |
| B | 51% | Wrecking Ball | -1.18% | -1.28% ±1.5 | Standard (-4%) | Neutral | 40 |
| C | 49% | D.Va | -1.22% | -1.82% ±2.0 | Standard (-18%) | Unfavorable | 40 |
| C | 38% | Sombra *(provisional)* | -1.24% | -1.72% ±4.7 | Standard (+14%) | Unfavorable | 8 |
| C | 42% | Doctrine *(provisional)* | -1.34% | -2.41% ±3.8 | Standard (-2%) | Unfavorable | 8 |
| C | 62% | Jetpack Cat | -1.41% | -1.52% ±1.3 | Standard (-6%) | Unfavorable | 40 |
| C | 77% | Sigma | -1.71% | -1.70% ±1.3 | Niche (-23%) | Deterrent | 40 |
| C | 90% | Ana | -1.78% | -1.83% ±0.9 | Standard (-19%) | Unfavorable | 40 |
| C | 63% | Junkrat | -2.12% | -2.70% ±2.2 | Standard (-5%) | Unfavorable | 40 |
| C | 86% | Hazard | -2.30% | -2.44% ±1.2 | Standard (+8%) | Unfavorable | 40 |
| C | 62% | Winston | -2.81% | -2.85% ±1.2 | Niche (-38%) | Deterrent | 40 |
| D | 89% | Pharah | -4.04% | -4.50% ±1.8 | Standard (-14%) | Unfavorable | 40 |
| D | 100% | Widowmaker | -9.23% | -9.32% ±2.0 | Niche (-77%) | Deterrent | 34 |

### Blizzard World

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| A | 37% | Doctrine *(provisional)* | +1.80% | +8.41% ±7.7 | Standard (+4%) | Favorable | 8 |
| B | 55% | Wrecking Ball | +0.96% | +1.51% ±2.7 | Popular (+20%) | Neutral | 51 |
| B | 65% | Anran | +0.60% | +2.13% ±3.7 | Standard (-15%) | Neutral | 51 |
| B | 80% | D.Va | +0.47% | +1.34% ±1.9 | Standard (+10%) | Neutral | 52 |
| B | 59% | Jetpack Cat | +0.46% | +0.86% ±3.4 | Standard (-6%) | Neutral | 52 |
| B | 85% | Winston | +0.37% | +0.48% ±1.5 | Popular (+26%) | Neutral | 52 |
| B | 89% | Sojourn | +0.32% | +0.57% ±1.5 | Standard (+7%) | Neutral | 52 |
| B | 69% | Sierra | +0.22% | -3.02% ±4.1 | Popular (+31%) | Neutral | 38 |
| B | 48% | Sombra *(provisional)* | +0.17% | +4.18% ±8.1 | Standard (-2%) | Neutral | 8 |
| B | 85% | Ana | +0.14% | +0.22% ±1.7 | Standard (+17%) | Neutral | 52 |
| B | 71% | Lifeweaver | +0.13% | +0.15% ±3.6 | Standard (+13%) | Neutral | 52 |
| B | 71% | Venture | +0.04% | +3.37% ±3.7 | Standard (-9%) | Neutral | 50 |
| B | 96% | Wuyang | +0.04% | +0.10% ±1.3 | Standard (+3%) | Neutral | 52 |
| B | 61% | D.Mon | +0.02% | +2.32% ±7.1 | Standard (-11%) | Neutral | 16 |
| B | 72% | Bastion | -0.10% | -0.16% ±2.7 | Standard (+0%) | Neutral | 51 |
| B | 92% | Illari | -0.17% | -0.16% ±1.5 | Standard (+18%) | Neutral | 52 |
| B | 46% | Roadhog *(provisional)* | -0.18% | +1.21% ±10.1 | Popular (+22%) | Neutral | 8 |
| B | 75% | Mercy | -0.21% | -0.18% ±2.9 | Standard (+14%) | Neutral | 51 |
| B | 74% | Orisa | -0.21% | -0.28% ±2.7 | Standard (-8%) | Neutral | 52 |
| B | 89% | Genji | -0.27% | -0.93% ±1.6 | Standard (-5%) | Neutral | 52 |
| B | 72% | Mei | -0.29% | -0.69% ±3.2 | Standard (-5%) | Neutral | 51 |
| B | 80% | Emre | -0.33% | -0.28% ±2.2 | Standard (+18%) | Neutral | 52 |
| B | 69% | Juno | -0.45% | +0.78% ±3.4 | Standard (-15%) | Neutral | 51 |
| B | 73% | Shion | -0.45% | -0.88% ±2.7 | Standard (-14%) | Neutral | 28 |
| B | 77% | Widowmaker | -0.48% | -0.42% ±1.7 | Map Priority (+85%) | Neutral | 52 |
| B | 72% | Ashe | -0.74% | -0.71% ±1.8 | Popular (+28%) | Neutral | 52 |
| B | 68% | Zenyatta | -0.84% | -1.05% ±1.7 | Standard (+16%) | Neutral | 51 |
| B | 60% | Reaper | -0.86% | -1.57% ±3.1 | Niche (-24%) | Neutral | 52 |
| B | 61% | Freja | -0.90% | -1.20% ±2.5 | Standard (+13%) | Neutral | 50 |
| B | 56% | Echo | -0.92% | -1.21% ±3.2 | Niche (-28%) | Neutral | 52 |
| B | 59% | Doomfist | -0.97% | -2.07% ±2.5 | Standard (+0%) | Neutral | 52 |
| B | 53% | Hanzo | -1.13% | -1.52% ±2.2 | Popular (+20%) | Neutral | 52 |
| B | 52% | Kiriko | -1.16% | -1.49% ±1.6 | Standard (-5%) | Neutral | 52 |
| C | 50% | Sigma | -1.22% | -1.19% ±1.6 | Popular (+23%) | Trap Pick | 52 |
| C | 49% | Soldier: 76 | -1.25% | -1.74% ±2.2 | Standard (+3%) | Unfavorable | 52 |
| C | 44% | Symmetra | -1.27% | -1.83% ±3.3 | Standard (-11%) | Unfavorable | 51 |
| C | 51% | Baptiste | -1.37% | -2.77% ±2.8 | Standard (-5%) | Unfavorable | 52 |
| C | 66% | Tracer | -1.57% | -1.95% ±1.7 | Standard (+2%) | Unfavorable | 52 |
| C | 79% | Cassidy | -1.66% | -1.99% ±1.2 | Standard (-20%) | Unfavorable | 52 |
| C | 53% | Domina | -1.90% | -2.14% ±2.8 | Standard (+11%) | Unfavorable | 51 |
| C | 60% | Vendetta | -2.21% | -4.59% ±3.0 | Standard (-15%) | Unfavorable | 44 |
| C | 44% | Pharah | -2.58% | -3.60% ±3.7 | Niche (-38%) | Deterrent | 52 |
| C | 48% | Zarya | -2.62% | -3.49% ±3.1 | Standard (-18%) | Unfavorable | 51 |
| C | 41% | Junkrat | -2.82% | -5.35% ±4.0 | Niche (-22%) | Deterrent | 52 |
| D | 52% | Hazard | -3.07% | -4.47% ±3.1 | Niche (-27%) | Deterrent | 51 |
| D | 57% | Mauga | -3.21% | -5.25% ±3.1 | Niche (-20%) | Deterrent | 50 |
| D | 64% | Moira | -3.42% | -5.26% ±3.1 | Niche (-25%) | Deterrent | 52 |
| D | 70% | Mizuki | -3.52% | -4.79% ±2.2 | Standard (-19%) | Unfavorable | 52 |
| D | 71% | Ramattra | -3.72% | -5.78% ±3.3 | Niche (-22%) | Deterrent | 49 |
| D | 85% | Brigitte | -4.08% | -6.24% ±2.6 | Standard (-7%) | Unfavorable | 52 |
| D | 76% | Junker Queen | -4.13% | -5.14% ±3.6 | Niche (-26%) | Deterrent | 43 |
| D | 76% | Reinhardt | -4.21% | -5.81% ±4.0 | Standard (-16%) | Unfavorable | 52 |
| D | 86% | Torbjörn | -4.42% | -6.95% ±3.2 | Standard (+14%) | Unfavorable | 50 |
| D | 100% | Lúcio | -6.65% | -7.09% ±2.5 | Niche (-41%) | Deterrent | 51 |

### Busan

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| A | 63% | Soldier: 76 | +1.81% | +3.33% ±2.5 | Popular (+35%) | Meta | 16 |
| B | 42% | Junker Queen | +1.09% | +2.10% ±4.3 | Standard (+19%) | Neutral | 16 |
| B | 54% | Mauga | +1.06% | +1.90% ±2.5 | Standard (+15%) | Neutral | 16 |
| B | 50% | Widowmaker | +0.95% | +1.17% ±2.9 | Standard (-2%) | Neutral | 16 |
| B | 44% | Roadhog *(provisional)* | +0.94% | +4.98% ±7.1 | Standard (+0%) | Neutral | 8 |
| B | 64% | Cassidy | +0.93% | +1.57% ±1.7 | Standard (+11%) | Neutral | 16 |
| B | 57% | Moira | +0.88% | +2.29% ±3.0 | Popular (+20%) | Neutral | 16 |
| B | 62% | Freja | +0.80% | +2.81% ±3.2 | Niche (-31%) | Neutral | 16 |
| B | 70% | Zenyatta | +0.68% | +1.78% ±2.3 | Standard (-12%) | Neutral | 16 |
| B | 64% | Anran | +0.66% | +2.07% ±3.4 | Standard (+9%) | Neutral | 15 |
| B | 62% | Echo | +0.53% | +2.23% ±3.8 | Niche (-49%) | Neutral | 16 |
| B | 67% | Zarya | +0.38% | +0.87% ±2.7 | Standard (-10%) | Neutral | 16 |
| B | 87% | Kiriko | +0.36% | +0.51% ±1.6 | Standard (+7%) | Neutral | 16 |
| B | 77% | Emre | +0.25% | +3.02% ±2.6 | Standard (-5%) | Neutral | 16 |
| B | 68% | Sierra | +0.22% | -2.90% ±4.3 | Standard (-11%) | Neutral | 10 |
| B | 52% | Reinhardt | +0.17% | +0.48% ±4.0 | Standard (-1%) | Neutral | 16 |
| B | 67% | Lifeweaver | +0.13% | +4.67% ±4.9 | Standard (-20%) | Neutral | 16 |
| B | 76% | D.Va | +0.11% | +1.31% ±2.8 | Standard (+8%) | Neutral | 16 |
| B | 83% | Illari | +0.11% | +1.02% ±2.1 | Niche (-33%) | Neutral | 16 |
| B | 78% | Mizuki | +0.08% | +0.12% ±2.2 | Standard (+18%) | Neutral | 16 |
| B | 72% | Venture | +0.04% | +1.93% ±3.6 | Standard (-9%) | Neutral | 16 |
| B | 74% | Vendetta | +0.00% | +0.24% ±3.1 | Standard (+12%) | Neutral | 16 |
| B | 69% | Wrecking Ball | -0.02% | +0.14% ±2.8 | Popular (+37%) | Neutral | 16 |
| B | 90% | Tracer | -0.05% | +0.08% ±1.6 | Popular (+26%) | Neutral | 16 |
| B | 77% | Reaper | -0.08% | +0.29% ±2.8 | Standard (+4%) | Neutral | 16 |
| B | 76% | Orisa | -0.12% | -0.13% ±2.5 | Standard (+2%) | Neutral | 16 |
| B | 69% | Winston | -0.14% | +0.08% ±2.4 | Standard (-6%) | Neutral | 16 |
| B | 68% | Mercy | -0.15% | +0.20% ±4.5 | Niche (-23%) | Neutral | 13 |
| B | 85% | Sojourn | -0.16% | -0.02% ±1.9 | Standard (-6%) | Neutral | 16 |
| B | 75% | Genji | -0.25% | -1.85% ±2.8 | Standard (-9%) | Neutral | 16 |
| B | 81% | D.Mon | -0.28% | -0.23% ±2.1 | Popular (+22%) | Neutral | 16 |
| B | 85% | Wuyang | -0.28% | -0.33% ±1.8 | Standard (-0%) | Neutral | 16 |
| B | 65% | Pharah | -0.31% | -0.05% ±2.8 | Niche (-52%) | Neutral | 16 |
| B | 83% | Ana | -0.39% | -0.38% ±1.6 | Standard (-6%) | Neutral | 16 |
| B | 67% | Mei | -0.47% | -1.72% ±3.6 | Standard (-20%) | Neutral | 16 |
| B | 54% | Sombra *(provisional)* | -0.47% | +0.00% ±4.5 | Standard (+15%) | Neutral | 8 |
| B | 58% | Symmetra | -0.48% | -0.47% ±3.9 | Standard (+13%) | Neutral | 16 |
| B | 81% | Shion | -0.49% | -0.73% ±1.8 | Popular (+27%) | Neutral | 16 |
| B | 70% | Juno | -0.55% | -0.26% ±2.8 | Standard (-7%) | Neutral | 16 |
| B | 54% | Torbjörn | -0.62% | -1.16% ±4.2 | Standard (-8%) | Neutral | 16 |
| B | 68% | Doomfist | -0.66% | -1.39% ±2.7 | Standard (+4%) | Neutral | 16 |
| B | 63% | Hazard | -0.71% | -0.77% ±2.5 | Standard (-1%) | Neutral | 16 |
| B | 64% | Ashe | -0.73% | -0.62% ±3.1 | Niche (-35%) | Neutral | 16 |
| B | 64% | Baptiste | -0.73% | -1.03% ±3.1 | Niche (-28%) | Neutral | 16 |
| B | 57% | Bastion | -0.73% | -1.52% ±3.7 | Standard (-17%) | Neutral | 16 |
| B | 44% | Domina | -1.10% | -1.09% ±4.3 | Niche (-29%) | Neutral | 15 |
| C | 44% | Hanzo | -1.24% | -2.83% ±4.1 | Niche (-46%) | Deterrent | 16 |
| C | 43% | Jetpack Cat | -1.25% | -1.70% ±3.0 | Standard (+8%) | Unfavorable | 16 |
| C | 43% | Ramattra | -1.28% | -1.64% ±3.5 | Standard (-19%) | Unfavorable | 16 |
| C | 52% | Brigitte | -1.50% | -2.23% ±2.9 | Standard (+15%) | Unfavorable | 16 |
| C | 52% | Sigma | -1.65% | -1.64% ±2.5 | Niche (-34%) | Deterrent | 16 |
| C | 51% | Doctrine *(provisional)* | -1.76% | -2.71% ±3.1 | Standard (-1%) | Unfavorable | 8 |
| C | 48% | Lúcio | -1.87% | -1.85% ±2.9 | Popular (+26%) | Trap Pick | 16 |
| D | 55% | Junkrat | -3.19% | -7.87% ±5.1 | Niche (-31%) | Deterrent | 16 |

### Circuit Royal

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| S | 100% | Sigma | +7.45% | +8.02% ±1.6 | Map Priority (+150%) | Meta | 52 |
| S | 100% | Domina | +5.64% | +6.60% ±1.9 | Map Priority (+153%) | Meta | 52 |
| S | 98% | Widowmaker | +5.63% | +5.92% ±2.5 | Map Priority (+125%) | Meta | 52 |
| S | 52% | Doctrine *(provisional)* | +3.09% | +6.31% ±4.1 | Standard (+6%) | Favorable | 8 |
| A | 52% | Bastion | +2.61% | +4.27% ±2.9 | Map Priority (+60%) | Meta | 52 |
| A | 84% | Sojourn | +1.88% | +2.47% ±1.3 | Map Priority (+70%) | Meta | 52 |
| A | 59% | Symmetra | +1.68% | +2.48% ±2.3 | Standard (+9%) | Favorable | 51 |
| B | 48% | Mizuki | +1.20% | +1.91% ±2.8 | Niche (-49%) | Neutral | 51 |
| B | 50% | Mei | +1.19% | +3.29% ±2.3 | Map Priority (+82%) | Neutral | 51 |
| B | 50% | Reinhardt | +1.16% | +1.43% ±2.4 | Popular (+22%) | Neutral | 51 |
| B | 55% | Juno | +1.11% | +4.14% ±1.5 | Map Priority (+86%) | Neutral | 52 |
| B | 42% | Roadhog *(provisional)* | +1.01% | +7.51% ±8.8 | Niche (-34%) | Neutral | 8 |
| B | 63% | Zenyatta | +0.96% | +1.65% ±1.6 | Map Priority (+110%) | Neutral | 52 |
| B | 67% | Ramattra | +0.91% | +1.12% ±1.4 | Map Priority (+129%) | Neutral | 51 |
| B | 64% | Orisa | +0.78% | +1.26% ±2.4 | Standard (+15%) | Neutral | 51 |
| B | 77% | Illari | +0.75% | +1.85% ±1.3 | Map Priority (+69%) | Neutral | 52 |
| B | 70% | Baptiste | +0.62% | +2.30% ±2.5 | Map Priority (+114%) | Neutral | 52 |
| B | 82% | Hanzo | +0.34% | +0.71% ±2.0 | Map Priority (+128%) | Neutral | 52 |
| B | 86% | Sierra | +0.22% | +2.45% ±1.8 | Map Priority (+58%) | Neutral | 39 |
| B | 79% | Lifeweaver | +0.13% | -0.27% ±2.5 | Popular (+25%) | Neutral | 51 |
| B | 81% | Wuyang | +0.07% | +0.33% ±2.3 | Standard (+1%) | Neutral | 52 |
| B | 75% | Venture | +0.04% | -1.00% ±3.1 | Standard (-20%) | Neutral | 52 |
| B | 70% | Reaper | -0.10% | +0.58% ±3.8 | Niche (-57%) | Neutral | 52 |
| B | 78% | Mercy | -0.13% | +0.02% ±2.6 | Popular (+23%) | Neutral | 51 |
| B | 84% | Genji | -0.15% | +0.05% ±2.0 | Standard (-6%) | Neutral | 52 |
| B | 82% | Emre | -0.19% | +0.28% ±2.1 | Map Priority (+63%) | Neutral | 52 |
| B | 86% | Ana | -0.41% | -0.41% ±1.4 | Standard (+20%) | Neutral | 52 |
| B | 75% | Freja | -0.50% | -0.47% ±2.4 | Map Priority (+113%) | Neutral | 52 |
| B | 72% | Ashe | -0.55% | -0.02% ±2.6 | Map Priority (+83%) | Neutral | 52 |
| B | 75% | Cassidy | -0.67% | -0.87% ±1.8 | Niche (-59%) | Neutral | 51 |
| B | 61% | Vendetta | -0.78% | -1.67% ±3.5 | Niche (-39%) | Neutral | 35 |
| B | 51% | Wrecking Ball | -1.07% | -1.41% ±3.0 | Niche (-42%) | Neutral | 50 |
| C | 49% | Zarya | -1.22% | -1.29% ±1.9 | Standard (+9%) | Unfavorable | 52 |
| C | 50% | Doomfist | -1.35% | -4.16% ±3.1 | Niche (-23%) | Deterrent | 52 |
| C | 53% | Junkrat | -1.40% | -1.72% ±2.1 | Standard (+4%) | Unfavorable | 52 |
| C | 56% | D.Va | -1.57% | -3.46% ±2.8 | Niche (-43%) | Deterrent | 52 |
| C | 50% | D.Mon | -1.65% | -4.38% ±4.4 | Niche (-34%) | Deterrent | 16 |
| C | 49% | Moira | -1.65% | -2.31% ±3.6 | Niche (-39%) | Deterrent | 51 |
| C | 66% | Soldier: 76 | -1.77% | -2.50% ±2.1 | Niche (-27%) | Deterrent | 51 |
| C | 62% | Anran | -1.78% | -3.09% ±2.6 | Niche (-48%) | Deterrent | 41 |
| C | 52% | Jetpack Cat | -1.86% | -2.54% ±2.9 | Niche (-25%) | Deterrent | 52 |
| C | 49% | Torbjörn | -1.93% | -3.15% ±3.4 | Standard (-18%) | Unfavorable | 50 |
| C | 74% | Shion | -2.07% | -4.18% ±1.9 | Niche (-67%) | Deterrent | 28 |
| C | 67% | Echo | -2.40% | -3.11% ±2.0 | Standard (-15%) | Unfavorable | 51 |
| C | 51% | Pharah | -2.55% | -3.09% ±2.7 | Popular (+43%) | Trap Pick | 51 |
| C | 61% | Kiriko | -2.78% | -3.63% ±1.6 | Niche (-39%) | Deterrent | 52 |
| C | 33% | Sombra *(provisional)* | -2.99% | -14.20% ±9.4 | Niche (-51%) | Deterrent | 8 |
| D | 71% | Mauga | -3.54% | -4.78% ±2.3 | Niche (-39%) | Deterrent | 47 |
| D | 87% | Brigitte | -4.19% | -6.47% ±2.6 | Niche (-71%) | Deterrent | 48 |
| D | 97% | Tracer | -4.55% | -6.33% ±1.9 | Niche (-79%) | Deterrent | 51 |
| D | 97% | Hazard | -5.45% | -8.40% ±3.3 | Niche (-67%) | Deterrent | 43 |
| D | 98% | Junker Queen | -6.53% | -8.44% ±3.7 | Niche (-51%) | Deterrent | 35 |
| D | 100% | Winston | -8.81% | -9.57% ±2.2 | Niche (-61%) | Deterrent | 51 |
| D | 100% | Lúcio | -9.30% | -9.93% ±2.4 | Niche (-73%) | Deterrent | 43 |

### Colosseo

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| S | 83% | Reinhardt | +3.95% | +4.49% ±2.1 | Standard (+5%) | Favorable | 51 |
| A | 58% | Lúcio | +2.60% | +2.89% ±2.0 | Standard (+17%) | Favorable | 52 |
| A | 59% | Torbjörn | +2.09% | +2.83% ±2.5 | Standard (-6%) | Favorable | 51 |
| A | 65% | Jetpack Cat | +2.08% | +2.57% ±2.1 | Standard (+3%) | Favorable | 52 |
| A | 61% | Junkrat | +2.07% | +2.76% ±2.4 | Standard (-17%) | Favorable | 51 |
| A | 74% | Doomfist | +1.74% | +3.12% ±1.6 | Standard (+10%) | Favorable | 52 |
| A | 80% | Tracer | +1.61% | +1.85% ±1.0 | Popular (+24%) | Meta | 52 |
| A | 56% | Anran | +1.42% | +2.48% ±2.2 | Standard (+5%) | Favorable | 49 |
| A | 37% | Sombra *(provisional)* | +1.25% | +4.38% ±5.0 | Standard (+11%) | Favorable | 8 |
| B | 50% | Junker Queen | +1.19% | +1.37% ±1.8 | Popular (+22%) | Neutral | 50 |
| B | 52% | Vendetta | +1.08% | +3.20% ±3.6 | Standard (+1%) | Neutral | 47 |
| B | 60% | Winston | +0.97% | +1.17% ±1.8 | Standard (+0%) | Neutral | 52 |
| B | 64% | Sojourn | +0.90% | +1.61% ±1.9 | Standard (+17%) | Neutral | 52 |
| B | 75% | Hazard | +0.77% | +0.90% ±1.3 | Standard (+2%) | Neutral | 51 |
| B | 83% | Shion | +0.67% | +1.08% ±1.2 | Popular (+25%) | Neutral | 28 |
| B | 75% | Freja | +0.61% | +1.25% ±1.9 | Niche (-22%) | Neutral | 51 |
| B | 80% | Kiriko | +0.61% | +0.84% ±1.6 | Standard (+5%) | Neutral | 52 |
| B | 74% | Wuyang | +0.57% | +1.24% ±2.2 | Standard (+5%) | Neutral | 52 |
| B | 89% | Illari | +0.53% | +1.15% ±1.1 | Standard (-8%) | Neutral | 52 |
| B | 69% | Wrecking Ball | +0.52% | +0.81% ±2.4 | Standard (+18%) | Neutral | 52 |
| B | 72% | Mercy | +0.42% | +1.59% ±2.9 | Standard (-11%) | Neutral | 51 |
| B | 79% | Mei | +0.37% | +1.17% ±2.2 | Niche (-31%) | Neutral | 51 |
| B | 87% | Echo | +0.22% | +0.48% ±1.7 | Standard (-14%) | Neutral | 52 |
| B | 70% | Sierra | +0.22% | +1.05% ±3.6 | Standard (-6%) | Neutral | 36 |
| B | 77% | Soldier: 76 | +0.18% | +0.58% ±2.6 | Standard (+11%) | Neutral | 52 |
| B | 75% | D.Mon | +0.15% | +0.60% ±2.7 | Standard (+17%) | Neutral | 16 |
| B | 86% | Hanzo | +0.13% | +0.37% ±1.9 | Niche (-38%) | Neutral | 51 |
| B | 73% | Lifeweaver | +0.13% | +0.93% ±3.2 | Standard (-2%) | Neutral | 51 |
| B | 98% | Mizuki | +0.06% | +0.07% ±1.0 | Standard (+9%) | Neutral | 52 |
| B | 72% | Venture | +0.04% | -0.47% ±3.6 | Standard (-8%) | Neutral | 52 |
| B | 91% | Juno | -0.15% | +0.67% ±1.6 | Standard (+4%) | Neutral | 51 |
| B | 82% | Genji | -0.16% | -0.06% ±2.2 | Standard (-8%) | Neutral | 52 |
| B | 79% | Zenyatta | -0.16% | +0.18% ±2.5 | Standard (-17%) | Neutral | 52 |
| B | 74% | Brigitte | -0.49% | -0.48% ±2.2 | Standard (-1%) | Neutral | 52 |
| B | 77% | Emre | -0.55% | -1.11% ±2.0 | Standard (+4%) | Neutral | 52 |
| B | 64% | Zarya | -0.67% | -0.60% ±2.5 | Standard (-3%) | Neutral | 52 |
| B | 66% | Mauga | -0.84% | -0.90% ±1.8 | Standard (+10%) | Neutral | 51 |
| B | 68% | Ashe | -0.89% | -0.99% ±1.5 | Niche (-30%) | Neutral | 51 |
| B | 45% | Roadhog *(provisional)* | -0.89% | -2.19% ±6.8 | Standard (-5%) | Neutral | 8 |
| B | 59% | Reaper | -0.92% | -1.63% ±2.9 | Standard (-8%) | Neutral | 52 |
| B | 52% | Pharah | -0.95% | -0.93% ±3.1 | Standard (-5%) | Neutral | 52 |
| B | 45% | Doctrine *(provisional)* | -1.15% | -2.41% ±4.5 | Standard (+3%) | Neutral | 8 |
| C | 49% | D.Va | -1.31% | -3.05% ±3.1 | Standard (-8%) | Unfavorable | 52 |
| C | 52% | Moira | -1.39% | -1.56% ±2.4 | Standard (+3%) | Unfavorable | 51 |
| C | 57% | Bastion | -1.45% | -1.88% ±1.9 | Standard (-18%) | Unfavorable | 49 |
| C | 61% | Baptiste | -1.48% | -2.19% ±1.9 | Niche (-26%) | Deterrent | 52 |
| C | 67% | Cassidy | -1.51% | -1.92% ±1.4 | Standard (+2%) | Unfavorable | 52 |
| C | 59% | Ramattra | -1.91% | -2.34% ±2.5 | Standard (-20%) | Unfavorable | 50 |
| C | 52% | Symmetra | -2.35% | -3.63% ±3.2 | Niche (-32%) | Deterrent | 43 |
| C | 79% | Orisa | -2.49% | -2.83% ±1.2 | Standard (-2%) | Unfavorable | 51 |
| C | 68% | Ana | -2.80% | -2.88% ±0.9 | Standard (-6%) | Unfavorable | 52 |
| D | 68% | Sigma | -3.50% | -3.71% ±2.2 | Niche (-25%) | Deterrent | 52 |
| D | 70% | Domina | -3.68% | -4.56% ±2.9 | Standard (-16%) | Unfavorable | 48 |
| D | 88% | Widowmaker | -4.57% | -4.56% ±2.7 | Niche (-22%) | Deterrent | 52 |

### Dorado

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| S | 87% | Ana | +4.05% | +4.87% ±2.0 | Standard (+19%) | Favorable | 52 |
| S | 84% | Winston | +3.88% | +4.29% ±1.8 | Map Priority (+111%) | Meta | 52 |
| S | 76% | Wrecking Ball | +3.74% | +5.02% ±2.3 | Standard (+15%) | Favorable | 51 |
| A | 59% | Echo | +2.05% | +4.33% ±2.9 | Map Priority (+76%) | Meta | 52 |
| A | 44% | Doctrine *(provisional)* | +1.81% | +3.82% ±4.2 | Standard (-6%) | Favorable | 8 |
| A | 53% | Wuyang | +1.32% | +2.46% ±2.0 | Standard (-18%) | Favorable | 52 |
| A | 46% | Pharah | +1.29% | +2.03% ±2.6 | Standard (+1%) | Favorable | 50 |
| B | 61% | Ashe | +0.96% | +3.66% ±2.1 | Map Priority (+72%) | Neutral | 52 |
| B | 58% | D.Mon | +0.70% | +3.42% ±4.7 | Niche (-33%) | Neutral | 16 |
| B | 72% | Doomfist | +0.64% | +1.92% ±2.2 | Standard (+5%) | Neutral | 51 |
| B | 76% | D.Va | +0.34% | +1.65% ±2.5 | Popular (+50%) | Neutral | 52 |
| B | 63% | Mauga | +0.29% | +1.31% ±3.8 | Standard (-19%) | Neutral | 49 |
| B | 74% | Sierra | +0.22% | -2.62% ±3.0 | Standard (+9%) | Neutral | 36 |
| B | 80% | Hanzo | +0.21% | +0.59% ±2.2 | Standard (-11%) | Neutral | 52 |
| B | 76% | Lifeweaver | +0.13% | +2.13% ±2.9 | Popular (+30%) | Neutral | 49 |
| B | 71% | Venture | +0.04% | +0.67% ±3.7 | Standard (-2%) | Neutral | 50 |
| B | 77% | Brigitte | -0.02% | +0.24% ±2.5 | Popular (+46%) | Neutral | 52 |
| B | 77% | Freja | -0.03% | +0.54% ±2.8 | Popular (+39%) | Neutral | 51 |
| B | 76% | Mercy | -0.07% | +0.23% ±2.9 | Popular (+34%) | Neutral | 52 |
| B | 60% | Jetpack Cat | -0.08% | +0.00% ±3.5 | Popular (+21%) | Neutral | 52 |
| B | 86% | Genji | -0.09% | +0.77% ±1.9 | Standard (+18%) | Neutral | 51 |
| B | 44% | Roadhog *(provisional)* | -0.09% | +5.02% ±16.2 | Standard (-7%) | Neutral | 8 |
| B | 75% | Reaper | -0.11% | +0.28% ±3.0 | Popular (+24%) | Neutral | 52 |
| B | 79% | Soldier: 76 | -0.17% | -0.05% ±2.3 | Standard (+5%) | Neutral | 52 |
| B | 79% | Shion | -0.24% | -0.20% ±2.4 | Niche (-29%) | Neutral | 28 |
| B | 76% | Illari | -0.38% | -1.26% ±2.5 | Popular (+22%) | Neutral | 52 |
| B | 49% | Sombra *(provisional)* | -0.43% | +0.59% ±6.2 | Standard (+2%) | Neutral | 8 |
| B | 65% | Mei | -0.59% | -2.36% ±3.6 | Niche (-21%) | Neutral | 51 |
| B | 65% | Anran | -0.61% | -1.17% ±3.5 | Standard (-13%) | Neutral | 49 |
| B | 90% | Cassidy | -0.62% | -0.67% ±0.9 | Standard (-6%) | Neutral | 52 |
| B | 69% | Emre | -0.65% | -2.07% ±2.6 | Standard (+5%) | Neutral | 52 |
| B | 69% | Juno | -0.68% | -1.03% ±2.4 | Standard (-19%) | Neutral | 48 |
| B | 58% | Mizuki | -0.69% | -1.26% ±3.5 | Standard (-19%) | Neutral | 52 |
| B | 67% | Tracer | -0.85% | -0.98% ±1.7 | Standard (-8%) | Neutral | 52 |
| B | 54% | Vendetta | -0.98% | -2.74% ±4.2 | Standard (-4%) | Neutral | 48 |
| B | 55% | Zenyatta | -1.03% | -1.91% ±3.0 | Niche (-22%) | Neutral | 52 |
| C | 43% | Junkrat | -1.30% | -2.04% ±3.3 | Standard (+19%) | Unfavorable | 50 |
| C | 53% | Bastion | -1.53% | -2.36% ±2.6 | Standard (+6%) | Unfavorable | 49 |
| C | 61% | Baptiste | -1.78% | -3.80% ±2.8 | Standard (-7%) | Unfavorable | 51 |
| C | 73% | Kiriko | -1.93% | -2.68% ±1.9 | Standard (-5%) | Unfavorable | 52 |
| C | 53% | Hazard | -1.95% | -2.64% ±2.9 | Popular (+29%) | Trap Pick | 51 |
| C | 58% | Moira | -1.97% | -2.57% ±2.8 | Niche (-28%) | Deterrent | 50 |
| C | 52% | Symmetra | -1.99% | -3.09% ±3.3 | Niche (-21%) | Deterrent | 48 |
| C | 74% | Sojourn | -2.26% | -3.20% ±1.9 | Niche (-47%) | Deterrent | 52 |
| C | 47% | Reinhardt | -2.56% | -3.05% ±3.0 | Niche (-40%) | Deterrent | 49 |
| C | 52% | Torbjörn | -2.64% | -3.69% ±2.7 | Standard (-4%) | Unfavorable | 49 |
| C | 51% | Orisa | -2.65% | -5.19% ±3.3 | Niche (-47%) | Deterrent | 51 |
| D | 70% | Ramattra | -3.74% | -6.85% ±4.1 | Niche (-62%) | Deterrent | 28 |
| D | 79% | Widowmaker | -3.97% | -3.95% ±2.4 | Standard (-4%) | Unfavorable | 52 |
| D | 79% | Junker Queen | -4.38% | -5.62% ±3.9 | Niche (-38%) | Deterrent | 40 |
| D | 81% | Lúcio | -4.39% | -4.83% ±3.4 | Niche (-52%) | Deterrent | 49 |
| D | 96% | Domina | -5.38% | -7.15% ±3.2 | Niche (-34%) | Deterrent | 44 |
| D | 100% | Zarya | -6.21% | -7.73% ±2.3 | Niche (-49%) | Deterrent | 49 |
| D | 100% | Sigma | -6.99% | -8.15% ±3.1 | Niche (-35%) | Deterrent | 52 |

### Eichenwalde

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| A | 50% | Ana | +2.55% | +3.71% ±2.9 | Standard (+7%) | Favorable | 16 |
| A | 38% | Jetpack Cat | +1.93% | +5.41% ±5.8 | Standard (+6%) | Favorable | 16 |
| A | 37% | Junkrat | +1.59% | +5.35% ±6.3 | Map Priority (+88%) | Meta | 16 |
| A | 46% | D.Mon | +1.41% | +5.87% ±4.7 | Standard (+16%) | Favorable | 16 |
| B | 42% | Roadhog *(provisional)* | +1.01% | +7.10% ±8.5 | Standard (-3%) | Neutral | 8 |
| B | 55% | Echo | +0.93% | +2.96% ±3.6 | Map Priority (+85%) | Neutral | 16 |
| B | 60% | Orisa | +0.72% | +1.65% ±3.5 | Popular (+23%) | Neutral | 16 |
| B | 37% | Junker Queen | +0.62% | +2.90% ±7.3 | Standard (+4%) | Neutral | 16 |
| B | 65% | Wuyang | +0.54% | +2.50% ±3.8 | Standard (+0%) | Neutral | 16 |
| B | 49% | Pharah | +0.39% | +2.09% ±5.1 | Map Priority (+66%) | Neutral | 16 |
| B | 64% | Sierra | +0.22% | +1.26% ±6.5 | Standard (+9%) | Neutral | 10 |
| B | 71% | Tracer | +0.15% | +0.95% ±3.3 | Standard (-15%) | Neutral | 16 |
| B | 61% | Lifeweaver | +0.13% | -0.23% ±12.7 | Standard (-4%) | Neutral | 16 |
| B | 67% | Mercy | +0.08% | +1.65% ±4.9 | Standard (+7%) | Neutral | 14 |
| B | 62% | Venture | +0.04% | +2.71% ±9.3 | Standard (+12%) | Neutral | 16 |
| B | 57% | Bastion | +0.01% | -0.01% ±5.2 | Popular (+32%) | Neutral | 16 |
| B | 66% | Vendetta | +0.00% | +0.64% ±5.1 | Standard (-2%) | Neutral | 15 |
| B | 64% | Mei | -0.02% | +1.95% ±6.8 | Popular (+24%) | Neutral | 16 |
| B | 70% | Illari | -0.10% | +0.71% ±4.0 | Standard (+2%) | Neutral | 16 |
| B | 66% | Doomfist | -0.12% | +1.31% ±5.5 | Standard (-2%) | Neutral | 16 |
| B | 51% | Doctrine *(provisional)* | -0.19% | -0.44% ±5.9 | Standard (-1%) | Neutral | 8 |
| B | 72% | Genji | -0.19% | -0.69% ±3.3 | Standard (+5%) | Neutral | 16 |
| B | 60% | Soldier: 76 | -0.25% | +0.53% ±8.1 | Niche (-26%) | Neutral | 16 |
| B | 54% | Mauga | -0.41% | +0.18% ±6.2 | Standard (-6%) | Neutral | 15 |
| B | 58% | Mizuki | -0.41% | -0.86% ±4.2 | Standard (-5%) | Neutral | 16 |
| B | 66% | Sojourn | -0.44% | -0.49% ±4.2 | Niche (-24%) | Neutral | 16 |
| B | 47% | Domina | -0.46% | +0.28% ±5.2 | Standard (+8%) | Neutral | 16 |
| B | 62% | Emre | -0.55% | -4.47% ±5.2 | Standard (-15%) | Neutral | 16 |
| B | 59% | Freja | -0.55% | -0.61% ±8.4 | Standard (+9%) | Neutral | 16 |
| B | 55% | Hazard | -0.55% | -0.55% ±4.1 | Niche (-21%) | Neutral | 16 |
| B | 60% | D.Va | -0.59% | -0.92% ±6.5 | Standard (-9%) | Neutral | 16 |
| B | 61% | Juno | -0.62% | -1.01% ±4.7 | Standard (-8%) | Neutral | 16 |
| B | 48% | Ramattra | -0.65% | -0.11% ±6.8 | Standard (+14%) | Neutral | 15 |
| B | 59% | Zenyatta | -0.65% | -1.93% ±6.1 | Standard (+16%) | Neutral | 16 |
| B | 70% | Cassidy | -0.66% | -1.01% ±2.4 | Standard (+16%) | Neutral | 16 |
| B | 56% | Ashe | -0.82% | -1.47% ±5.3 | Standard (-19%) | Neutral | 16 |
| B | 61% | Shion | -0.82% | -2.63% ±3.2 | Niche (-22%) | Neutral | 16 |
| B | 45% | Wrecking Ball | -0.87% | -1.94% ±6.3 | Standard (-10%) | Neutral | 16 |
| B | 57% | Kiriko | -0.89% | -2.14% ±3.7 | Standard (-5%) | Neutral | 16 |
| B | 51% | Torbjörn | -0.94% | -1.63% ±3.8 | Popular (+40%) | Neutral | 15 |
| B | 48% | Brigitte | -0.98% | -2.84% ±6.7 | Standard (-11%) | Neutral | 15 |
| B | 43% | Sombra *(provisional)* | -0.98% | -1.36% ±7.4 | Standard (-7%) | Neutral | 8 |
| B | 50% | Anran | -1.07% | -6.24% ±7.0 | Standard (-5%) | Neutral | 15 |
| B | 50% | Baptiste | -1.13% | -3.02% ±3.9 | Popular (+20%) | Neutral | 16 |
| C | 50% | Reaper | -1.46% | -4.23% ±4.0 | Standard (+1%) | Unfavorable | 16 |
| C | 37% | Symmetra | -1.49% | -5.84% ±8.0 | Standard (-6%) | Unfavorable | 13 |
| C | 37% | Sigma | -1.74% | -1.75% ±4.3 | Standard (-2%) | Unfavorable | 16 |
| C | 30% | Widowmaker | -2.14% | -1.86% ±4.8 | Niche (-35%) | Deterrent | 16 |
| C | 37% | Zarya | -2.18% | -5.65% ±7.1 | Popular (+23%) | Trap Pick | 16 |
| C | 41% | Moira | -2.56% | -8.47% ±6.8 | Standard (-10%) | Unfavorable | 16 |
| C | 32% | Reinhardt | -2.73% | -4.59% ±5.5 | Popular (+29%) | Trap Pick | 16 |
| C | 48% | Hanzo | -2.75% | -7.25% ±4.1 | Standard (+14%) | Unfavorable | 16 |
| D | 57% | Winston | -3.31% | -3.95% ±4.3 | Niche (-24%) | Deterrent | 16 |
| D | 66% | Lúcio | -3.84% | -4.44% ±4.6 | Niche (-23%) | Deterrent | 16 |

### Esperanca

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| A | 46% | Lúcio | +2.97% | +3.34% ±2.2 | Popular (+36%) | Meta | 52 |
| A | 70% | Winston | +2.22% | +2.50% ±1.7 | Popular (+31%) | Meta | 52 |
| A | 56% | Junker Queen | +1.61% | +1.93% ±2.2 | Popular (+26%) | Meta | 49 |
| A | 64% | Soldier: 76 | +1.53% | +2.22% ±1.8 | Popular (+31%) | Meta | 51 |
| A | 74% | Kiriko | +1.50% | +1.69% ±1.0 | Standard (+16%) | Favorable | 52 |
| B | 49% | Reinhardt | +1.19% | +1.44% ±2.3 | Standard (-15%) | Neutral | 51 |
| B | 49% | Junkrat | +1.13% | +1.71% ±2.9 | Niche (-24%) | Neutral | 50 |
| B | 54% | Torbjörn | +0.99% | +1.48% ±2.9 | Standard (-13%) | Neutral | 50 |
| B | 57% | D.Mon | +0.96% | +2.30% ±3.0 | Standard (+8%) | Neutral | 16 |
| B | 72% | Echo | +0.77% | +1.14% ±1.6 | Standard (+1%) | Neutral | 52 |
| B | 68% | Hanzo | +0.69% | +1.45% ±2.4 | Niche (-56%) | Neutral | 49 |
| B | 63% | Jetpack Cat | +0.57% | +0.86% ±2.8 | Standard (+17%) | Neutral | 52 |
| B | 74% | Mauga | +0.56% | +0.93% ±2.0 | Popular (+24%) | Neutral | 51 |
| B | 95% | Shion | +0.51% | +0.69% ±0.8 | Popular (+35%) | Neutral | 28 |
| B | 68% | Vendetta | +0.50% | +1.41% ±3.2 | Standard (+7%) | Neutral | 47 |
| B | 68% | Moira | +0.45% | +1.37% ±2.8 | Standard (+12%) | Neutral | 52 |
| B | 62% | Doctrine *(provisional)* | +0.43% | +0.74% ±3.2 | Standard (+1%) | Neutral | 8 |
| B | 69% | Mei | +0.35% | +2.32% ±3.6 | Niche (-34%) | Neutral | 51 |
| B | 91% | Brigitte | +0.34% | +0.48% ±1.3 | Standard (+16%) | Neutral | 51 |
| B | 74% | Wrecking Ball | +0.33% | +0.54% ±2.2 | Popular (+26%) | Neutral | 52 |
| B | 65% | Bastion | +0.24% | +0.44% ±3.4 | Niche (-22%) | Neutral | 50 |
| B | 78% | Sierra | +0.22% | +0.88% ±2.5 | Standard (-8%) | Neutral | 33 |
| B | 91% | Mizuki | +0.15% | +0.18% ±1.4 | Standard (+10%) | Neutral | 52 |
| B | 77% | Lifeweaver | +0.13% | +1.05% ±2.7 | Standard (-12%) | Neutral | 50 |
| B | 80% | Wuyang | +0.09% | +0.39% ±2.5 | Standard (-1%) | Neutral | 52 |
| B | 83% | Venture | +0.04% | +0.61% ±2.2 | Standard (-12%) | Neutral | 48 |
| B | 57% | Sombra *(provisional)* | -0.00% | +0.95% ±4.3 | Popular (+23%) | Neutral | 8 |
| B | 90% | Mercy | -0.05% | +0.06% ±1.6 | Standard (-13%) | Neutral | 49 |
| B | 96% | Tracer | -0.07% | -0.00% ±1.2 | Popular (+38%) | Neutral | 52 |
| B | 62% | Symmetra | -0.08% | +0.31% ±3.7 | Niche (-29%) | Neutral | 45 |
| B | 85% | Doomfist | -0.10% | +0.10% ±2.0 | Standard (+2%) | Neutral | 52 |
| B | 81% | Emre | -0.10% | +0.77% ±2.3 | Standard (-2%) | Neutral | 52 |
| B | 70% | Pharah | -0.10% | +0.18% ±2.6 | Standard (-18%) | Neutral | 50 |
| B | 99% | Sojourn | -0.10% | -0.06% ±0.9 | Standard (-1%) | Neutral | 52 |
| B | 86% | Genji | -0.11% | +0.53% ±1.9 | Standard (-6%) | Neutral | 52 |
| B | 81% | Reaper | -0.12% | +0.11% ±2.3 | Standard (-2%) | Neutral | 51 |
| B | 85% | Hazard | -0.14% | -0.07% ±1.7 | Popular (+22%) | Neutral | 51 |
| B | 88% | Illari | -0.41% | -0.73% ±1.4 | Standard (-14%) | Neutral | 52 |
| B | 86% | Cassidy | -0.52% | -0.58% ±1.4 | Standard (+12%) | Neutral | 52 |
| B | 66% | Orisa | -0.57% | -0.96% ±3.0 | Standard (-16%) | Neutral | 52 |
| B | 84% | Ashe | -0.61% | -0.53% ±1.3 | Niche (-43%) | Neutral | 51 |
| B | 67% | Freja | -0.65% | -0.77% ±2.8 | Niche (-25%) | Neutral | 49 |
| B | 65% | Juno | -0.69% | -1.33% ±3.2 | Standard (+12%) | Neutral | 51 |
| B | 44% | Roadhog *(provisional)* | -0.97% | -2.40% ±6.6 | Standard (-6%) | Neutral | 8 |
| B | 57% | Baptiste | -1.00% | -1.61% ±2.6 | Niche (-37%) | Neutral | 51 |
| C | 48% | Anran | -1.23% | -2.14% ±2.7 | Standard (+2%) | Unfavorable | 49 |
| C | 60% | D.Va | -1.47% | -2.25% ±1.9 | Popular (+23%) | Trap Pick | 51 |
| C | 49% | Zarya | -1.63% | -1.98% ±3.0 | Niche (-21%) | Deterrent | 52 |
| C | 69% | Zenyatta | -1.67% | -2.36% ±1.8 | Niche (-39%) | Deterrent | 51 |
| C | 63% | Ana | -1.97% | -2.29% ±2.1 | Standard (-20%) | Unfavorable | 52 |
| C | 46% | Domina | -2.32% | -2.91% ±3.5 | Niche (-35%) | Deterrent | 47 |
| C | 54% | Ramattra | -2.35% | -3.19% ±2.9 | Niche (-41%) | Deterrent | 47 |
| D | 91% | Sigma | -4.99% | -5.81% ±3.3 | Niche (-48%) | Deterrent | 52 |
| D | 100% | Widowmaker | -15.34% | -15.60% ±2.3 | Niche (-65%) | Deterrent | 49 |

### Grimsvotn

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| S | 68% | Junkrat *(provisional)* | +3.76% | +8.38% ±4.6 | Popular (+29%) | Meta | 8 |
| A | 43% | Mizuki *(provisional)* | +2.04% | +7.19% ±5.8 | Standard (-19%) | Favorable | 8 |
| A | 36% | Jetpack Cat *(provisional)* | +1.53% | +4.67% ±6.1 | Niche (-36%) | Specialist | 8 |
| A | 23% | Lúcio *(provisional)* | +1.47% | +5.54% ±8.6 | Niche (-31%) | Specialist | 6 |
| A | 45% | Ana *(provisional)* | +1.28% | +1.89% ±2.8 | Standard (+9%) | Favorable | 8 |
| A | 44% | Hanzo *(provisional)* | +1.26% | +5.07% ±4.3 | Map Priority (+61%) | Meta | 8 |
| B | 51% | Ramattra *(provisional)* | +0.67% | +3.35% ±5.2 | Map Priority (+117%) | Neutral | 8 |
| B | 58% | Orisa *(provisional)* | +0.61% | +1.93% ±4.5 | Map Priority (+54%) | Neutral | 8 |
| B | 59% | Vendetta *(provisional)* | +0.59% | +4.66% ±6.4 | Standard (-11%) | Neutral | 8 |
| B | 61% | Anran *(provisional)* | +0.42% | +5.68% ±7.7 | Standard (-8%) | Neutral | 7 |
| B | 52% | Hazard *(provisional)* | +0.33% | +1.68% ±5.2 | Niche (-52%) | Neutral | 8 |
| B | 58% | Brigitte *(provisional)* | +0.26% | +2.32% ±5.4 | Niche (-35%) | Neutral | 8 |
| B | 65% | Sierra *(provisional)* | +0.22% | +2.00% ±5.4 | Standard (+15%) | Neutral | 8 |
| B | 73% | Kiriko *(provisional)* | +0.18% | +0.56% ±3.1 | Standard (-12%) | Neutral | 8 |
| B | 58% | Bastion *(provisional)* | +0.14% | +0.37% ±4.8 | Popular (+41%) | Neutral | 8 |
| B | 66% | Lifeweaver *(provisional)* | +0.13% | -2.05% ±5.2 | Standard (+6%) | Neutral | 8 |
| B | 54% | Torbjörn *(provisional)* | +0.13% | +0.40% ±4.8 | Standard (+7%) | Neutral | 8 |
| B | 51% | Symmetra *(provisional)* | +0.09% | +2.24% ±7.3 | Standard (-4%) | Neutral | 8 |
| B | 48% | Roadhog *(provisional)* | +0.05% | +1.68% ±7.7 | Standard (+12%) | Neutral | 8 |
| B | 65% | Venture *(provisional)* | +0.04% | +1.89% ±5.7 | Standard (-0%) | Neutral | 8 |
| B | 49% | Reinhardt *(provisional)* | +0.03% | +0.37% ±4.5 | Popular (+41%) | Neutral | 8 |
| B | 51% | Sigma *(provisional)* | +0.03% | +0.66% ±3.9 | Map Priority (+75%) | Neutral | 8 |
| B | 50% | Sombra *(provisional)* | -0.10% | +1.79% ±6.4 | Standard (-17%) | Neutral | 8 |
| B | 58% | Echo *(provisional)* | -0.12% | +2.61% ±7.3 | Niche (-22%) | Neutral | 8 |
| B | 71% | Genji *(provisional)* | -0.15% | +0.72% ±3.6 | Standard (-4%) | Neutral | 8 |
| B | 75% | Cassidy *(provisional)* | -0.16% | +0.07% ±3.0 | Standard (-4%) | Neutral | 8 |
| B | 62% | Mei *(provisional)* | -0.16% | -0.19% ±8.7 | Map Priority (+52%) | Neutral | 8 |
| B | 61% | Illari *(provisional)* | -0.21% | -3.47% ±11.2 | Standard (-2%) | Neutral | 8 |
| B | 64% | Reaper *(provisional)* | -0.21% | +0.93% ±6.4 | Standard (-12%) | Neutral | 8 |
| B | 75% | Sojourn *(provisional)* | -0.30% | -0.17% ±2.8 | Popular (+39%) | Neutral | 8 |
| B | 67% | Wuyang *(provisional)* | -0.30% | -0.75% ±4.5 | Popular (+35%) | Neutral | 8 |
| B | 64% | Doomfist *(provisional)* | -0.31% | -0.46% ±6.0 | Standard (-8%) | Neutral | 8 |
| B | 47% | Wrecking Ball *(provisional)* | -0.31% | +0.03% ±8.0 | Niche (-44%) | Neutral | 8 |
| B | 51% | Zarya *(provisional)* | -0.31% | +0.52% ±5.2 | Map Priority (+59%) | Neutral | 8 |
| B | 60% | Soldier: 76 *(provisional)* | -0.36% | -0.41% ±6.7 | Niche (-25%) | Neutral | 8 |
| B | 67% | Tracer *(provisional)* | -0.39% | -0.25% ±3.7 | Niche (-34%) | Neutral | 8 |
| B | 66% | Emre *(provisional)* | -0.41% | -1.37% ±4.4 | Standard (+13%) | Neutral | 8 |
| B | 62% | D.Va *(provisional)* | -0.55% | -0.53% ±5.4 | Niche (-54%) | Neutral | 8 |
| B | 40% | Junker Queen *(provisional)* | -0.58% | -0.10% ±6.0 | Standard (+8%) | Neutral | 7 |
| B | 61% | D.Mon *(provisional)* | -0.59% | -1.02% ±4.4 | Standard (+0%) | Neutral | 8 |
| B | 60% | Juno *(provisional)* | -0.59% | -0.32% ±5.8 | Standard (+10%) | Neutral | 7 |
| B | 51% | Doctrine *(provisional)* | -0.62% | -1.39% ±4.9 | Standard (+7%) | Neutral | 8 |
| B | 68% | Shion *(provisional)* | -0.67% | -1.61% ±2.7 | Standard (-6%) | Neutral | 8 |
| B | 60% | Zenyatta *(provisional)* | -0.67% | -1.71% ±5.3 | Popular (+49%) | Neutral | 8 |
| B | 60% | Mercy *(provisional)* | -0.68% | -2.86% ±4.8 | Standard (-7%) | Neutral | 7 |
| B | 50% | Mauga *(provisional)* | -0.75% | -1.28% ±6.7 | Standard (-11%) | Neutral | 6 |
| B | 55% | Baptiste *(provisional)* | -0.82% | -3.11% ±6.5 | Popular (+37%) | Neutral | 8 |
| B | 51% | Freja *(provisional)* | -1.01% | -4.47% ±7.2 | Standard (-0%) | Neutral | 8 |
| C | 33% | Domina *(provisional)* | -1.21% | -1.33% ±5.6 | Map Priority (+80%) | Trap Pick | 8 |
| C | 46% | Ashe *(provisional)* | -1.27% | -4.27% ±4.0 | Standard (+11%) | Unfavorable | 8 |
| C | 44% | Moira *(provisional)* | -2.04% | -5.31% ±6.3 | Standard (-14%) | Unfavorable | 8 |
| C | 40% | Pharah *(provisional)* | -2.38% | -3.90% ±4.8 | Standard (+1%) | Unfavorable | 8 |
| C | 34% | Winston *(provisional)* | -2.88% | -3.39% ±4.5 | Niche (-53%) | Deterrent | 8 |
| D | 53% | Widowmaker *(provisional)* | -3.17% | -3.03% ±4.3 | Standard (+18%) | Unfavorable | 8 |

### Havana

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| S | 99% | Widowmaker | +5.88% | +6.19% ±2.5 | Map Priority (+176%) | Meta | 52 |
| S | 100% | Sigma | +5.72% | +6.19% ±1.6 | Map Priority (+136%) | Meta | 51 |
| S | 69% | Zenyatta | +3.33% | +4.93% ±1.5 | Map Priority (+114%) | Meta | 51 |
| A | 79% | Ana | +1.81% | +2.00% ±1.3 | Popular (+33%) | Meta | 51 |
| A | 42% | Doctrine *(provisional)* | +1.56% | +3.52% ±4.5 | Standard (+1%) | Favorable | 8 |
| A | 47% | Domina | +1.38% | +2.08% ±2.6 | Map Priority (+147%) | Meta | 50 |
| A | 45% | Orisa | +1.24% | +2.49% ±3.2 | Standard (+5%) | Favorable | 51 |
| B | 51% | Bastion | +1.15% | +1.58% ±2.2 | Standard (+18%) | Neutral | 49 |
| B | 76% | Hanzo | +0.51% | +1.00% ±2.1 | Map Priority (+158%) | Neutral | 52 |
| B | 69% | Soldier: 76 | +0.48% | +1.35% ±3.0 | Standard (-9%) | Neutral | 51 |
| B | 80% | Baptiste | +0.31% | +1.29% ±2.2 | Map Priority (+52%) | Neutral | 51 |
| B | 72% | Sierra | +0.22% | +1.77% ±3.4 | Map Priority (+51%) | Neutral | 37 |
| B | 82% | Illari | +0.21% | +1.39% ±2.1 | Map Priority (+59%) | Neutral | 52 |
| B | 92% | Emre | +0.15% | +0.89% ±1.5 | Popular (+49%) | Neutral | 52 |
| B | 78% | Lifeweaver | +0.13% | +1.28% ±2.6 | Popular (+21%) | Neutral | 50 |
| B | 88% | Ashe | +0.07% | +1.03% ±1.8 | Map Priority (+83%) | Neutral | 51 |
| B | 70% | Venture | +0.04% | -0.77% ±4.0 | Niche (-23%) | Neutral | 47 |
| B | 67% | Torbjörn | +0.02% | +0.06% ±2.9 | Standard (+3%) | Neutral | 50 |
| B | 75% | Tracer | -0.08% | +0.28% ±2.8 | Niche (-48%) | Neutral | 52 |
| B | 81% | Sojourn | -0.14% | +0.09% ±2.3 | Popular (+37%) | Neutral | 52 |
| B | 76% | Freja | -0.15% | +0.30% ±2.9 | Popular (+42%) | Neutral | 51 |
| B | 73% | Genji | -0.15% | +0.32% ±3.2 | Standard (+9%) | Neutral | 52 |
| B | 49% | Sombra *(provisional)* | -0.17% | +1.93% ±7.1 | Niche (-22%) | Neutral | 8 |
| B | 45% | Roadhog *(provisional)* | -0.25% | +1.60% ±14.0 | Standard (-9%) | Neutral | 8 |
| B | 77% | D.Va | -0.30% | +0.06% ±2.5 | Niche (-28%) | Neutral | 51 |
| B | 72% | Juno | -0.48% | +0.21% ±2.8 | Standard (-16%) | Neutral | 49 |
| B | 67% | Mercy | -0.58% | -1.40% ±3.3 | Popular (+24%) | Neutral | 50 |
| B | 65% | Shion | -0.71% | -2.05% ±3.0 | Niche (-53%) | Neutral | 28 |
| B | 64% | Mei | -0.72% | -2.51% ±3.2 | Popular (+24%) | Neutral | 51 |
| B | 53% | D.Mon | -0.83% | -3.47% ±7.3 | Niche (-24%) | Neutral | 15 |
| B | 57% | Anran | -0.90% | -2.06% ±3.8 | Niche (-26%) | Neutral | 46 |
| B | 52% | Reaper | -1.07% | -2.45% ±3.5 | Niche (-49%) | Neutral | 51 |
| B | 47% | Junkrat | -1.10% | -2.04% ±4.0 | Niche (-28%) | Neutral | 49 |
| B | 51% | Wuyang | -1.15% | -2.78% ±3.0 | Standard (-3%) | Neutral | 52 |
| C | 52% | Cassidy | -1.32% | -2.21% ±2.3 | Niche (-50%) | Deterrent | 51 |
| C | 42% | Hazard | -1.33% | -1.94% ±3.7 | Niche (-62%) | Deterrent | 46 |
| C | 43% | Symmetra | -1.34% | -2.12% ±3.7 | Standard (-1%) | Unfavorable | 48 |
| C | 47% | Mauga | -1.35% | -1.88% ±3.0 | Niche (-35%) | Deterrent | 47 |
| C | 55% | Doomfist | -1.43% | -3.19% ±2.4 | Standard (-15%) | Unfavorable | 51 |
| C | 50% | Vendetta | -1.47% | -4.03% ±4.0 | Niche (-29%) | Deterrent | 37 |
| C | 47% | Moira | -1.55% | -2.23% ±4.0 | Niche (-39%) | Deterrent | 50 |
| C | 53% | Mizuki | -1.64% | -2.57% ±2.9 | Niche (-48%) | Deterrent | 50 |
| C | 57% | Ramattra | -1.83% | -2.28% ±2.6 | Popular (+44%) | Trap Pick | 50 |
| C | 59% | Brigitte | -2.00% | -3.02% ±2.8 | Niche (-52%) | Deterrent | 48 |
| C | 54% | Zarya | -2.01% | -2.50% ±2.9 | Standard (-11%) | Unfavorable | 50 |
| C | 63% | Echo | -2.10% | -3.04% ±2.5 | Niche (-55%) | Deterrent | 47 |
| C | 68% | Kiriko | -2.18% | -3.48% ±2.3 | Niche (-27%) | Deterrent | 52 |
| C | 45% | Wrecking Ball | -2.29% | -4.10% ±4.1 | Niche (-41%) | Deterrent | 50 |
| C | 41% | Pharah | -2.85% | -4.03% ±3.7 | Niche (-45%) | Deterrent | 49 |
| D | 56% | Reinhardt | -3.20% | -3.87% ±3.0 | Standard (+10%) | Unfavorable | 51 |
| D | 60% | Jetpack Cat | -3.39% | -6.18% ±4.3 | Niche (-34%) | Deterrent | 51 |
| D | 87% | Junker Queen | -4.87% | -6.24% ±3.8 | Niche (-44%) | Deterrent | 38 |
| D | 100% | Winston | -6.74% | -7.42% ±2.4 | Niche (-39%) | Deterrent | 51 |
| D | 100% | Lúcio | -8.62% | -9.40% ±2.7 | Niche (-68%) | Deterrent | 46 |

### Hollywood

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| A | 49% | Zarya | +1.43% | +2.30% ±2.6 | Standard (+15%) | Favorable | 51 |
| B | 63% | Ana | +0.99% | +1.11% ±1.3 | Standard (+19%) | Neutral | 52 |
| B | 75% | Sierra | +0.22% | -0.56% ±2.9 | Standard (+5%) | Neutral | 34 |
| B | 79% | Lifeweaver | +0.13% | -1.88% ±2.5 | Standard (+19%) | Neutral | 50 |
| B | 70% | Venture | +0.04% | -4.47% ±3.9 | Standard (-9%) | Neutral | 50 |
| B | 71% | Hanzo | +0.01% | +0.64% ±3.5 | Popular (+28%) | Neutral | 52 |
| B | 82% | D.Va | -0.09% | +0.44% ±2.2 | Standard (+5%) | Neutral | 51 |
| B | 58% | Doctrine *(provisional)* | -0.10% | -0.12% ±4.1 | Standard (+0%) | Neutral | 6 |
| B | 44% | Roadhog *(provisional)* | -0.13% | +4.40% ±16.4 | Standard (+5%) | Neutral | 6 |
| B | 82% | Genji | -0.15% | +0.13% ±2.2 | Standard (+11%) | Neutral | 51 |
| B | 73% | Shion | -0.20% | +0.02% ±3.1 | Niche (-22%) | Neutral | 28 |
| B | 84% | Winston | -0.22% | -0.12% ±1.7 | Popular (+22%) | Neutral | 52 |
| B | 75% | Wuyang | -0.25% | -0.35% ±2.8 | Standard (-3%) | Neutral | 52 |
| B | 79% | Ashe | -0.31% | +0.58% ±2.3 | Popular (+47%) | Neutral | 52 |
| B | 70% | Doomfist | -0.37% | -0.64% ±3.5 | Standard (-5%) | Neutral | 51 |
| B | 71% | Emre | -0.37% | -0.54% ±3.2 | Standard (+2%) | Neutral | 52 |
| B | 80% | Kiriko | -0.37% | -0.49% ±2.0 | Standard (-10%) | Neutral | 52 |
| B | 73% | Mei | -0.39% | -0.99% ±2.9 | Standard (+15%) | Neutral | 51 |
| B | 72% | Illari | -0.40% | -1.72% ±2.9 | Standard (+10%) | Neutral | 52 |
| B | 78% | Tracer | -0.40% | -0.37% ±2.1 | Standard (-16%) | Neutral | 52 |
| B | 71% | Mercy | -0.45% | -0.87% ±3.0 | Standard (+19%) | Neutral | 51 |
| B | 66% | Bastion | -0.52% | -0.84% ±2.8 | Standard (+11%) | Neutral | 51 |
| B | 69% | Freja | -0.55% | -0.55% ±2.9 | Standard (+6%) | Neutral | 51 |
| B | 57% | Domina | -0.61% | -0.41% ±3.2 | Standard (+8%) | Neutral | 52 |
| B | 66% | Zenyatta | -0.66% | -0.98% ±2.9 | Standard (+16%) | Neutral | 52 |
| B | 53% | Ramattra | -0.69% | -0.53% ±4.3 | Standard (-12%) | Neutral | 51 |
| B | 61% | Juno | -0.85% | -2.51% ±3.0 | Standard (-8%) | Neutral | 52 |
| B | 61% | Baptiste | -0.87% | -1.32% ±2.7 | Standard (+10%) | Neutral | 52 |
| B | 56% | Hazard | -0.87% | -1.04% ±3.0 | Standard (-9%) | Neutral | 50 |
| B | 52% | D.Mon | -0.94% | -2.83% ±5.5 | Standard (-8%) | Neutral | 16 |
| B | 54% | Anran | -1.01% | -2.27% ±3.6 | Standard (-5%) | Neutral | 52 |
| B | 42% | Sombra *(provisional)* | -1.10% | -1.82% ±7.2 | Standard (-16%) | Neutral | 6 |
| B | 53% | Echo | -1.11% | -1.37% ±2.3 | Standard (+4%) | Neutral | 52 |
| C | 47% | Reaper | -1.25% | -2.67% ±3.2 | Standard (-3%) | Unfavorable | 52 |
| C | 53% | Mizuki | -1.29% | -1.55% ±1.7 | Standard (-11%) | Unfavorable | 52 |
| C | 50% | Wrecking Ball | -1.29% | -1.53% ±2.2 | Standard (-16%) | Unfavorable | 50 |
| C | 55% | Cassidy | -1.30% | -1.71% ±1.6 | Standard (-6%) | Unfavorable | 52 |
| C | 49% | Orisa | -1.31% | -2.12% ±2.7 | Standard (-5%) | Unfavorable | 52 |
| C | 50% | Moira | -1.35% | -1.53% ±2.5 | Standard (-13%) | Unfavorable | 51 |
| C | 54% | Pharah | -1.45% | -1.55% ±2.1 | Standard (-5%) | Unfavorable | 50 |
| C | 52% | Torbjörn | -1.58% | -2.19% ±2.6 | Popular (+27%) | Trap Pick | 51 |
| C | 61% | Brigitte | -1.62% | -2.07% ±2.1 | Standard (-8%) | Unfavorable | 51 |
| C | 66% | Vendetta | -1.85% | -2.97% ±2.3 | Standard (-6%) | Unfavorable | 46 |
| C | 62% | Soldier: 76 | -2.09% | -3.56% ±2.7 | Niche (-20%) | Deterrent | 50 |
| C | 62% | Junkrat | -2.18% | -2.79% ±2.3 | Standard (+20%) | Unfavorable | 50 |
| C | 75% | Widowmaker | -2.18% | -2.15% ±1.5 | Popular (+35%) | Trap Pick | 52 |
| C | 45% | Symmetra | -2.50% | -4.86% ±4.2 | Standard (-2%) | Unfavorable | 51 |
| C | 64% | Sojourn | -2.60% | -3.84% ±2.0 | Standard (-14%) | Unfavorable | 52 |
| C | 47% | Sigma | -2.77% | -2.93% ±2.6 | Standard (+13%) | Unfavorable | 52 |
| C | 43% | Jetpack Cat | -2.80% | -4.29% ±3.5 | Standard (-13%) | Unfavorable | 52 |
| D | 78% | Mauga | -3.73% | -4.91% ±2.2 | Standard (-18%) | Unfavorable | 47 |
| D | 72% | Junker Queen | -3.96% | -5.01% ±3.8 | Niche (-22%) | Deterrent | 45 |
| D | 99% | Lúcio | -5.21% | -5.38% ±1.8 | Niche (-47%) | Deterrent | 47 |
| D | 100% | Reinhardt | -7.77% | -9.47% ±2.9 | Standard (-13%) | Unfavorable | 51 |

### Ilios

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| S | 91% | Lúcio | +4.31% | +4.71% ±2.0 | Map Priority (+84%) | Meta | 52 |
| S | 63% | Hazard | +3.18% | +3.42% ±1.1 | Popular (+50%) | Meta | 51 |
| A | 44% | Jetpack Cat | +2.90% | +4.20% ±2.9 | Popular (+46%) | Meta | 52 |
| A | 69% | Torbjörn | +2.29% | +2.77% ±1.9 | Standard (-12%) | Favorable | 51 |
| A | 84% | Pharah | +1.86% | +2.05% ±1.2 | Popular (+37%) | Meta | 51 |
| A | 84% | Echo | +1.75% | +2.04% ±1.1 | Map Priority (+83%) | Meta | 52 |
| A | 53% | Junkrat | +1.58% | +2.22% ±2.6 | Niche (-21%) | Specialist | 51 |
| A | 43% | Junker Queen | +1.31% | +1.78% ±2.8 | Standard (+4%) | Favorable | 47 |
| A | 54% | Winston | +1.30% | +1.46% ±1.5 | Popular (+43%) | Meta | 52 |
| B | 52% | Vendetta | +1.17% | +1.65% ±1.7 | Standard (+8%) | Neutral | 47 |
| B | 74% | Kiriko | +0.80% | +1.01% ±1.3 | Standard (+12%) | Neutral | 52 |
| B | 77% | Mercy | +0.71% | +1.12% ±1.4 | Standard (-6%) | Neutral | 50 |
| B | 78% | Anran | +0.64% | +0.93% ±1.6 | Standard (+11%) | Neutral | 49 |
| B | 78% | Freja | +0.56% | +1.12% ±1.9 | Popular (+46%) | Neutral | 52 |
| B | 89% | Reaper | +0.41% | +0.65% ±1.4 | Popular (+30%) | Neutral | 52 |
| B | 75% | Widowmaker | +0.41% | +0.49% ±1.9 | Standard (-11%) | Neutral | 52 |
| B | 71% | Wrecking Ball | +0.41% | +0.67% ±2.4 | Popular (+42%) | Neutral | 52 |
| B | 55% | Sombra *(provisional)* | +0.32% | +1.73% ±4.5 | Popular (+20%) | Neutral | 8 |
| B | 81% | Bastion | +0.29% | +0.37% ±1.9 | Niche (-26%) | Neutral | 48 |
| B | 97% | Zenyatta | +0.27% | +0.41% ±1.0 | Niche (-40%) | Neutral | 50 |
| B | 83% | Sierra | +0.22% | -0.01% ±2.0 | Standard (-19%) | Neutral | 32 |
| B | 82% | Symmetra | +0.17% | +0.33% ±1.9 | Standard (+0%) | Neutral | 52 |
| B | 91% | Lifeweaver | +0.13% | -1.64% ±1.6 | Standard (-12%) | Neutral | 50 |
| B | 82% | Venture | +0.04% | -0.60% ±2.3 | Standard (+8%) | Neutral | 52 |
| B | 81% | D.Va | -0.06% | +0.57% ±2.4 | Popular (+43%) | Neutral | 52 |
| B | 99% | Juno | -0.08% | +0.30% ±1.0 | Standard (+1%) | Neutral | 51 |
| B | 86% | Genji | -0.09% | +0.80% ±1.9 | Standard (+1%) | Neutral | 52 |
| B | 96% | Moira | -0.18% | -0.09% ±1.1 | Standard (+11%) | Neutral | 51 |
| B | 88% | Doomfist | -0.24% | -0.20% ±1.7 | Standard (+9%) | Neutral | 52 |
| B | 82% | Emre | -0.29% | -0.13% ±2.1 | Niche (-29%) | Neutral | 52 |
| B | 96% | Cassidy | -0.30% | -0.30% ±1.0 | Popular (+21%) | Neutral | 52 |
| B | 96% | Shion | -0.48% | -0.53% ±0.9 | Standard (+9%) | Neutral | 28 |
| B | 78% | Ashe | -0.67% | -0.58% ±1.5 | Niche (-44%) | Neutral | 51 |
| B | 69% | Brigitte | -0.67% | -0.74% ±2.2 | Popular (+43%) | Neutral | 52 |
| B | 48% | Roadhog *(provisional)* | -0.67% | -1.19% ±5.9 | Standard (+19%) | Neutral | 8 |
| B | 74% | Baptiste | -0.71% | -0.80% ±1.7 | Niche (-27%) | Neutral | 51 |
| B | 69% | Illari | -0.79% | -2.34% ±1.9 | Niche (-28%) | Neutral | 52 |
| B | 64% | D.Mon | -0.81% | -1.11% ±2.5 | Standard (-11%) | Neutral | 16 |
| B | 68% | Hanzo | -0.82% | -0.96% ±1.8 | Niche (-49%) | Neutral | 52 |
| B | 65% | Orisa | -0.99% | -1.10% ±1.1 | Standard (-14%) | Neutral | 50 |
| B | 59% | Mizuki | -1.02% | -1.22% ±1.7 | Standard (+17%) | Neutral | 52 |
| B | 54% | Sojourn | -1.11% | -1.44% ±1.8 | Niche (-40%) | Neutral | 52 |
| C | 50% | Tracer | -1.26% | -1.73% ±2.2 | Popular (+29%) | Trap Pick | 52 |
| C | 55% | Reinhardt | -1.33% | -1.38% ±1.6 | Niche (-35%) | Deterrent | 50 |
| C | 66% | Wuyang | -1.45% | -1.83% ±1.3 | Niche (-26%) | Deterrent | 52 |
| C | 87% | Ana | -1.59% | -1.61% ±0.7 | Standard (-19%) | Unfavorable | 52 |
| C | 68% | Mei | -1.75% | -3.82% ±2.1 | Niche (-40%) | Deterrent | 50 |
| C | 72% | Soldier: 76 | -2.04% | -2.80% ±2.0 | Niche (-33%) | Deterrent | 51 |
| C | 59% | Ramattra | -2.06% | -2.57% ±2.5 | Niche (-60%) | Deterrent | 36 |
| C | 76% | Mauga | -2.13% | -2.48% ±1.7 | Standard (-3%) | Unfavorable | 49 |
| C | 71% | Zarya | -2.51% | -2.71% ±1.5 | Niche (-41%) | Deterrent | 50 |
| D | 72% | Doctrine *(provisional)* | -3.75% | -6.06% ±3.3 | Standard (-9%) | Unfavorable | 8 |
| D | 86% | Domina | -4.57% | -6.23% ±3.4 | Niche (-48%) | Deterrent | 43 |
| D | 98% | Sigma | -4.59% | -4.73% ±1.5 | Niche (-62%) | Deterrent | 51 |

### Junkertown

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| S | 100% | Widowmaker | +5.82% | +6.00% ±1.9 | Map Priority (+119%) | Meta | 52 |
| A | 54% | Sigma | +2.61% | +3.13% ±2.3 | Map Priority (+81%) | Meta | 52 |
| A | 62% | Ana | +2.29% | +2.90% ±2.2 | Popular (+28%) | Meta | 52 |
| A | 50% | Wrecking Ball | +1.79% | +3.07% ±3.2 | Standard (+11%) | Favorable | 51 |
| A | 63% | Hanzo | +1.47% | +2.02% ±1.6 | Map Priority (+76%) | Meta | 51 |
| A | 46% | Junkrat | +1.41% | +2.19% ±3.0 | Standard (-19%) | Favorable | 48 |
| B | 55% | Zenyatta | +1.02% | +3.65% ±3.1 | Map Priority (+51%) | Neutral | 52 |
| B | 57% | Freja | +0.90% | +3.76% ±3.7 | Popular (+29%) | Neutral | 51 |
| B | 80% | Sojourn | +0.50% | +0.95% ±1.8 | Standard (+2%) | Neutral | 52 |
| B | 67% | Brigitte | +0.38% | +1.16% ±3.1 | Standard (-19%) | Neutral | 51 |
| B | 74% | Kiriko | +0.35% | +0.79% ±2.7 | Standard (-17%) | Neutral | 52 |
| B | 61% | Torbjörn | +0.35% | +0.64% ±3.4 | Standard (+9%) | Neutral | 49 |
| B | 66% | Hazard | +0.29% | +0.67% ±2.9 | Niche (-30%) | Neutral | 51 |
| B | 79% | Illari | +0.26% | +1.92% ±2.4 | Map Priority (+50%) | Neutral | 52 |
| B | 69% | Sierra | +0.22% | +1.57% ±3.9 | Popular (+40%) | Neutral | 35 |
| B | 69% | Orisa | +0.21% | +0.50% ±3.2 | Standard (-20%) | Neutral | 50 |
| B | 71% | Lifeweaver | +0.13% | -2.26% ±3.6 | Popular (+30%) | Neutral | 50 |
| B | 69% | Venture | +0.04% | +0.43% ±4.1 | Standard (-12%) | Neutral | 50 |
| B | 75% | Shion | +0.01% | +0.80% ±3.0 | Niche (-32%) | Neutral | 28 |
| B | 62% | Reinhardt | -0.06% | +0.07% ±3.0 | Standard (-17%) | Neutral | 49 |
| B | 74% | Genji | -0.13% | +1.00% ±3.1 | Standard (+14%) | Neutral | 52 |
| B | 78% | Mercy | -0.13% | +0.01% ±2.6 | Popular (+23%) | Neutral | 51 |
| B | 84% | Tracer | -0.13% | +0.03% ±2.0 | Niche (-29%) | Neutral | 52 |
| B | 69% | Anran | -0.15% | +0.10% ±4.1 | Standard (-19%) | Neutral | 50 |
| B | 53% | Doctrine *(provisional)* | -0.24% | -0.50% ±5.1 | Standard (+1%) | Neutral | 8 |
| B | 74% | Baptiste | -0.27% | +0.30% ±2.9 | Standard (+14%) | Neutral | 51 |
| B | 72% | Emre | -0.36% | -0.48% ±3.1 | Popular (+30%) | Neutral | 52 |
| B | 69% | Mei | -0.37% | -1.24% ±3.6 | Standard (-10%) | Neutral | 50 |
| B | 62% | Bastion | -0.44% | -0.88% ±3.5 | Standard (+8%) | Neutral | 50 |
| B | 44% | Roadhog *(provisional)* | -0.56% | -1.95% ±12.6 | Standard (+17%) | Neutral | 8 |
| B | 71% | Winston | -0.59% | -0.49% ±1.9 | Standard (+10%) | Neutral | 52 |
| B | 66% | D.Va | -0.62% | -0.81% ±3.3 | Standard (+7%) | Neutral | 52 |
| B | 58% | Mauga | -0.63% | -0.65% ±4.0 | Standard (-17%) | Neutral | 51 |
| B | 64% | Reaper | -0.73% | -1.24% ±3.1 | Niche (-25%) | Neutral | 51 |
| B | 53% | Jetpack Cat | -0.75% | -1.09% ±3.7 | Niche (-21%) | Neutral | 51 |
| B | 59% | Echo | -0.76% | -0.93% ±3.6 | Niche (-36%) | Neutral | 50 |
| B | 61% | Juno | -0.82% | -2.62% ±3.3 | Standard (-18%) | Neutral | 50 |
| B | 64% | Cassidy | -0.85% | -1.31% ±2.2 | Niche (-26%) | Neutral | 52 |
| B | 59% | Doomfist | -0.89% | -2.42% ±3.0 | Standard (-12%) | Neutral | 51 |
| B | 43% | Sombra *(provisional)* | -0.91% | -1.05% ±8.2 | Standard (-18%) | Neutral | 8 |
| B | 50% | D.Mon | -0.96% | -4.50% ±7.4 | Niche (-21%) | Neutral | 16 |
| B | 49% | Symmetra | -1.03% | -1.64% ±4.1 | Niche (-34%) | Neutral | 45 |
| B | 56% | Ashe | -1.09% | -1.46% ±1.7 | Map Priority (+66%) | Neutral | 51 |
| B | 54% | Wuyang | -1.11% | -2.02% ±2.3 | Standard (-2%) | Neutral | 52 |
| B | 50% | Vendetta | -1.13% | -3.28% ±4.2 | Standard (-8%) | Neutral | 44 |
| C | 50% | Mizuki | -1.64% | -2.84% ±3.2 | Niche (-30%) | Deterrent | 51 |
| C | 52% | Moira | -1.75% | -2.42% ±3.3 | Niche (-29%) | Deterrent | 51 |
| C | 59% | Soldier: 76 | -1.89% | -3.49% ±3.0 | Popular (+25%) | Trap Pick | 52 |
| C | 48% | Domina | -1.93% | -2.30% ±3.3 | Popular (+40%) | Trap Pick | 50 |
| C | 47% | Zarya | -2.43% | -3.43% ±3.5 | Niche (-35%) | Deterrent | 51 |
| C | 55% | Ramattra | -2.45% | -3.20% ±2.7 | Niche (-36%) | Deterrent | 46 |
| D | 74% | Pharah | -3.92% | -5.70% ±3.6 | Niche (-54%) | Deterrent | 49 |
| D | 71% | Junker Queen | -4.00% | -5.26% ±4.2 | Niche (-27%) | Deterrent | 40 |
| D | 90% | Lúcio | -5.01% | -5.56% ±3.4 | Niche (-65%) | Deterrent | 47 |

### Kings Row

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| A | 85% | Junkrat | +2.19% | +2.40% ±1.3 | Popular (+40%) | Meta | 51 |
| A | 56% | Orisa | +2.10% | +4.17% ±3.2 | Popular (+22%) | Meta | 52 |
| A | 69% | Ana | +1.50% | +1.62% ±1.2 | Standard (+11%) | Favorable | 52 |
| A | 63% | Hanzo | +1.48% | +2.12% ±1.7 | Map Priority (+58%) | Meta | 52 |
| B | 57% | Reaper | +1.06% | +1.78% ±1.8 | Standard (-4%) | Neutral | 52 |
| B | 54% | Widowmaker | +0.99% | +1.13% ±2.3 | Map Priority (+53%) | Neutral | 52 |
| B | 59% | Pharah | +0.98% | +1.33% ±1.9 | Map Priority (+52%) | Neutral | 52 |
| B | 63% | Zarya | +0.82% | +1.27% ±2.2 | Map Priority (+53%) | Neutral | 52 |
| B | 64% | D.Mon | +0.75% | +1.72% ±2.7 | Standard (+1%) | Neutral | 16 |
| B | 89% | Sierra | +0.22% | +0.87% ±1.6 | Standard (+4%) | Neutral | 35 |
| B | 81% | Lifeweaver | +0.13% | -1.44% ±2.3 | Standard (+2%) | Neutral | 51 |
| B | 93% | Domina | +0.11% | +0.19% ±1.3 | Popular (+22%) | Neutral | 51 |
| B | 85% | Mizuki | +0.09% | +0.12% ±1.8 | Standard (-6%) | Neutral | 52 |
| B | 76% | Venture | +0.04% | +2.12% ±2.9 | Standard (+9%) | Neutral | 51 |
| B | 92% | Cassidy | +0.01% | +0.13% ±1.5 | Standard (-8%) | Neutral | 52 |
| B | 77% | Reinhardt | -0.03% | +0.03% ±2.1 | Popular (+39%) | Neutral | 52 |
| B | 99% | Genji | -0.11% | +0.02% ±0.9 | Standard (+5%) | Neutral | 52 |
| B | 74% | Anran | -0.19% | -0.11% ±3.0 | Standard (-5%) | Neutral | 52 |
| B | 49% | Roadhog *(provisional)* | -0.22% | +0.32% ±6.9 | Standard (-11%) | Neutral | 8 |
| B | 99% | Kiriko | -0.24% | -0.25% ±0.9 | Standard (-11%) | Neutral | 52 |
| B | 94% | Baptiste | -0.39% | -0.35% ±1.1 | Popular (+41%) | Neutral | 52 |
| B | 83% | Mei | -0.42% | -0.68% ±1.8 | Map Priority (+69%) | Neutral | 52 |
| B | 81% | Bastion | -0.52% | -0.62% ±1.6 | Popular (+44%) | Neutral | 51 |
| B | 82% | Juno | -0.58% | -0.56% ±1.5 | Standard (+1%) | Neutral | 51 |
| B | 87% | Shion | -0.58% | -0.72% ±1.2 | Niche (-23%) | Neutral | 28 |
| B | 76% | Doomfist | -0.67% | -0.95% ±1.7 | Standard (-5%) | Neutral | 52 |
| B | 76% | Ramattra | -0.67% | -0.65% ±1.5 | Map Priority (+65%) | Neutral | 51 |
| B | 69% | D.Va | -0.72% | -0.93% ±2.3 | Niche (-21%) | Neutral | 52 |
| B | 79% | Sojourn | -0.75% | -0.82% ±1.2 | Standard (+7%) | Neutral | 52 |
| B | 59% | Sigma | -0.78% | -0.64% ±2.5 | Standard (+18%) | Neutral | 52 |
| B | 63% | Hazard | -0.79% | -0.86% ±2.3 | Niche (-28%) | Neutral | 51 |
| B | 74% | Illari | -0.86% | -1.47% ±1.1 | Standard (-8%) | Neutral | 52 |
| B | 67% | Zenyatta | -0.86% | -1.07% ±1.7 | Popular (+37%) | Neutral | 52 |
| B | 65% | Freja | -0.90% | -1.05% ±1.7 | Standard (+10%) | Neutral | 52 |
| B | 47% | Sombra *(provisional)* | -0.90% | -0.96% ±5.3 | Standard (-18%) | Neutral | 8 |
| B | 61% | Symmetra | -0.91% | -1.03% ±2.1 | Standard (+12%) | Neutral | 51 |
| B | 64% | Echo | -0.92% | -1.01% ±1.7 | Standard (+4%) | Neutral | 52 |
| B | 61% | Emre | -0.95% | -2.77% ±2.1 | Standard (-9%) | Neutral | 52 |
| B | 57% | Mauga | -1.08% | -1.17% ±1.5 | Standard (-18%) | Neutral | 51 |
| B | 50% | Soldier: 76 | -1.16% | -1.85% ±2.7 | Niche (-39%) | Neutral | 51 |
| C | 40% | Lúcio | -1.22% | -1.11% ±3.0 | Niche (-34%) | Deterrent | 52 |
| C | 52% | Moira | -1.24% | -1.27% ±1.3 | Standard (-8%) | Unfavorable | 51 |
| C | 48% | Brigitte | -1.26% | -1.65% ±2.5 | Niche (-35%) | Deterrent | 52 |
| C | 55% | Wuyang | -1.27% | -1.56% ±1.2 | Standard (+11%) | Unfavorable | 52 |
| C | 54% | Vendetta | -1.39% | -2.27% ±2.4 | Standard (-7%) | Unfavorable | 49 |
| C | 59% | Mercy | -1.41% | -2.26% ±1.8 | Standard (-2%) | Unfavorable | 52 |
| C | 69% | Ashe | -1.47% | -1.81% ±1.1 | Standard (-5%) | Unfavorable | 52 |
| C | 67% | Torbjörn | -1.74% | -2.06% ±1.8 | Standard (+5%) | Unfavorable | 50 |
| C | 40% | Doctrine *(provisional)* | -1.93% | -5.38% ±5.6 | Standard (-0%) | Unfavorable | 8 |
| C | 54% | Jetpack Cat | -2.41% | -3.18% ±2.7 | Standard (-17%) | Unfavorable | 52 |
| C | 73% | Tracer | -2.67% | -3.00% ±1.1 | Niche (-35%) | Deterrent | 52 |
| D | 53% | Junker Queen | -3.06% | -3.22% ±1.8 | Standard (-1%) | Unfavorable | 48 |
| D | 94% | Winston | -3.94% | -4.02% ±1.2 | Niche (-38%) | Deterrent | 52 |
| D | 80% | Wrecking Ball | -4.01% | -5.70% ±2.9 | Niche (-42%) | Deterrent | 52 |

### Lijiang Tower

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| S | 100% | Pharah | +4.54% | +4.84% ±1.1 | Map Priority (+106%) | Meta | 52 |
| S | 65% | Torbjörn | +3.26% | +3.61% ±1.4 | Niche (-20%) | Specialist | 47 |
| S | 57% | Reinhardt | +3.13% | +3.34% ±1.4 | Popular (+35%) | Meta | 52 |
| A | 71% | Lúcio | +2.70% | +2.78% ±1.1 | Map Priority (+90%) | Meta | 51 |
| A | 68% | Symmetra | +2.58% | +3.11% ±1.6 | Map Priority (+100%) | Meta | 52 |
| A | 65% | Zarya | +1.97% | +2.62% ±2.1 | Popular (+32%) | Meta | 52 |
| A | 77% | Reaper | +1.79% | +2.57% ±1.5 | Standard (+16%) | Favorable | 52 |
| A | 57% | Domina | +1.65% | +2.23% ±2.3 | Niche (-29%) | Specialist | 51 |
| A | 50% | Orisa | +1.40% | +2.59% ±2.9 | Popular (+34%) | Meta | 52 |
| A | 50% | Mizuki | +1.20% | +1.35% ±1.3 | Popular (+23%) | Meta | 52 |
| B | 57% | Jetpack Cat | +1.00% | +1.25% ±2.0 | Standard (+13%) | Neutral | 52 |
| B | 74% | Hazard | +0.92% | +0.99% ±0.9 | Standard (+2%) | Neutral | 51 |
| B | 73% | Kiriko | +0.90% | +1.03% ±1.0 | Standard (+10%) | Neutral | 52 |
| B | 62% | Mei | +0.81% | +3.52% ±3.0 | Standard (+7%) | Neutral | 52 |
| B | 69% | Moira | +0.78% | +1.25% ±1.8 | Popular (+25%) | Neutral | 51 |
| B | 72% | Ramattra | +0.72% | +1.00% ±1.7 | Popular (+36%) | Neutral | 52 |
| B | 81% | Sojourn | +0.62% | +0.95% ±1.4 | Standard (+5%) | Neutral | 52 |
| B | 97% | Cassidy | +0.45% | +0.54% ±0.8 | Popular (+23%) | Neutral | 52 |
| B | 83% | Junkrat | +0.35% | +0.42% ±1.7 | Popular (+26%) | Neutral | 51 |
| B | 88% | Doomfist | +0.24% | +0.64% ±1.7 | Standard (+13%) | Neutral | 52 |
| B | 93% | Sierra | +0.22% | -0.58% ±1.4 | Standard (-19%) | Neutral | 33 |
| B | 80% | Lifeweaver | +0.13% | -1.49% ±2.4 | Standard (-20%) | Neutral | 49 |
| B | 80% | Venture | +0.04% | -1.30% ±2.4 | Standard (+6%) | Neutral | 51 |
| B | 80% | Zenyatta | -0.04% | +0.39% ±2.4 | Niche (-23%) | Neutral | 52 |
| B | 71% | Brigitte | -0.07% | +0.28% ±3.0 | Standard (-4%) | Neutral | 52 |
| B | 99% | Genji | -0.13% | -0.02% ±0.9 | Standard (-9%) | Neutral | 51 |
| B | 72% | Hanzo | -0.13% | +0.27% ±3.2 | Niche (-39%) | Neutral | 52 |
| B | 72% | Bastion | -0.16% | -0.26% ±2.6 | Standard (-7%) | Neutral | 52 |
| B | 79% | Junker Queen | -0.28% | -0.21% ±1.8 | Popular (+30%) | Neutral | 51 |
| B | 91% | Illari | -0.29% | -0.46% ±1.4 | Niche (-36%) | Neutral | 52 |
| B | 50% | Roadhog *(provisional)* | -0.33% | -0.13% ±6.2 | Standard (+1%) | Neutral | 8 |
| B | 94% | Wuyang | -0.42% | -0.47% ±1.0 | Standard (-4%) | Neutral | 52 |
| B | 93% | Shion | -0.45% | -0.52% ±1.1 | Standard (+16%) | Neutral | 28 |
| B | 83% | Baptiste | -0.52% | -0.49% ±1.6 | Standard (-19%) | Neutral | 51 |
| B | 70% | Vendetta | -0.52% | -0.85% ±2.8 | Standard (+12%) | Neutral | 49 |
| B | 78% | Emre | -0.61% | -1.16% ±1.7 | Niche (-27%) | Neutral | 52 |
| B | 73% | D.Mon | -0.63% | -0.75% ±2.1 | Standard (+16%) | Neutral | 16 |
| B | 51% | Sombra *(provisional)* | -0.80% | -0.73% ±4.2 | Standard (+15%) | Neutral | 8 |
| B | 63% | Juno | -0.95% | -1.75% ±1.7 | Standard (+8%) | Neutral | 51 |
| B | 54% | D.Va | -1.09% | -1.95% ±2.6 | Niche (-23%) | Neutral | 52 |
| B | 55% | Mercy | -1.12% | -1.59% ±1.6 | Standard (-13%) | Neutral | 51 |
| B | 50% | Mauga | -1.17% | -1.44% ±2.4 | Popular (+25%) | Neutral | 52 |
| C | 58% | Freja | -1.38% | -1.70% ±1.7 | Niche (-25%) | Deterrent | 50 |
| C | 63% | Soldier: 76 | -1.39% | -1.57% ±1.2 | Niche (-21%) | Deterrent | 51 |
| C | 70% | Tracer | -1.46% | -1.57% ±1.0 | Standard (+10%) | Unfavorable | 52 |
| C | 57% | Anran | -1.47% | -2.35% ±2.4 | Standard (+11%) | Unfavorable | 51 |
| C | 62% | Wrecking Ball | -1.50% | -1.67% ±1.7 | Standard (+16%) | Unfavorable | 52 |
| C | 67% | Ana | -1.66% | -1.82% ±1.7 | Standard (-20%) | Unfavorable | 52 |
| C | 62% | Ashe | -1.66% | -3.47% ±2.3 | Niche (-66%) | Deterrent | 50 |
| C | 65% | Winston | -1.68% | -1.67% ±1.7 | Niche (-42%) | Deterrent | 52 |
| C | 66% | Sigma | -1.81% | -1.81% ±1.8 | Niche (-43%) | Deterrent | 52 |
| C | 62% | Echo | -2.16% | -3.21% ±2.6 | Standard (+3%) | Unfavorable | 52 |
| C | 44% | Doctrine *(provisional)* | -2.81% | -4.74% ±3.5 | Standard (-3%) | Unfavorable | 8 |
| D | 100% | Widowmaker | -7.37% | -7.42% ±1.9 | Niche (-65%) | Deterrent | 49 |

### Midtown

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| B | 54% | Orisa | +1.04% | +1.84% ±2.7 | Standard (+11%) | Neutral | 52 |
| B | 47% | Widowmaker | +0.67% | +0.99% ±3.6 | Map Priority (+52%) | Neutral | 52 |
| B | 54% | Doctrine *(provisional)* | +0.55% | +1.25% ±4.4 | Standard (+5%) | Neutral | 8 |
| B | 62% | Brigitte | +0.48% | +1.66% ±3.6 | Niche (-36%) | Neutral | 52 |
| B | 69% | Sierra | +0.22% | -0.15% ±3.9 | Standard (+13%) | Neutral | 35 |
| B | 71% | Lifeweaver | +0.13% | -0.59% ±3.6 | Standard (+18%) | Neutral | 51 |
| B | 70% | Venture | +0.04% | +1.88% ±4.1 | Standard (+11%) | Neutral | 51 |
| B | 80% | Illari | +0.02% | +0.79% ±2.4 | Standard (+19%) | Neutral | 52 |
| B | 82% | Baptiste | +0.00% | +0.66% ±2.3 | Popular (+39%) | Neutral | 52 |
| B | 76% | Genji | -0.03% | +3.06% ±2.9 | Standard (-10%) | Neutral | 52 |
| B | 79% | Wuyang | -0.07% | +0.07% ±2.6 | Popular (+20%) | Neutral | 52 |
| B | 71% | Vendetta | -0.14% | -0.06% ±3.6 | Standard (-17%) | Neutral | 42 |
| B | 73% | Reaper | -0.15% | +0.25% ±3.3 | Niche (-24%) | Neutral | 52 |
| B | 64% | Zarya | -0.15% | +0.25% ±3.2 | Popular (+43%) | Neutral | 52 |
| B | 69% | Sigma | -0.17% | +0.05% ±2.5 | Map Priority (+77%) | Neutral | 52 |
| B | 77% | Emre | -0.18% | +0.65% ±2.7 | Standard (+19%) | Neutral | 52 |
| B | 71% | Mizuki | -0.27% | -0.39% ±2.6 | Standard (-16%) | Neutral | 52 |
| B | 86% | Sojourn | -0.28% | -0.21% ±1.8 | Popular (+24%) | Neutral | 52 |
| B | 64% | Domina | -0.32% | -0.04% ±2.9 | Map Priority (+72%) | Neutral | 52 |
| B | 69% | Doomfist | -0.32% | -0.42% ±3.7 | Niche (-21%) | Neutral | 52 |
| B | 70% | Juno | -0.35% | +1.96% ±3.5 | Standard (+1%) | Neutral | 51 |
| B | 65% | Anran | -0.39% | -0.72% ±4.6 | Standard (-2%) | Neutral | 49 |
| B | 56% | Junkrat | -0.39% | -0.71% ±4.2 | Standard (+9%) | Neutral | 52 |
| B | 68% | Freja | -0.44% | -0.26% ±3.6 | Standard (-14%) | Neutral | 50 |
| B | 87% | Hanzo | -0.45% | -0.45% ±1.4 | Popular (+46%) | Neutral | 50 |
| B | 71% | D.Va | -0.47% | -0.32% ±2.9 | Niche (-32%) | Neutral | 50 |
| B | 76% | Shion | -0.55% | -0.96% ±2.1 | Standard (-18%) | Neutral | 28 |
| B | 63% | Mei | -0.70% | -2.83% ±3.6 | Popular (+34%) | Neutral | 52 |
| B | 65% | Ana | -0.77% | -0.83% ±2.0 | Standard (+10%) | Neutral | 52 |
| B | 56% | D.Mon | -0.80% | -1.92% ±4.9 | Standard (-8%) | Neutral | 16 |
| B | 56% | Moira | -0.80% | -0.56% ±3.6 | Standard (-18%) | Neutral | 51 |
| B | 60% | Mercy | -0.89% | -2.04% ±2.9 | Standard (+3%) | Neutral | 50 |
| B | 58% | Ashe | -0.99% | -1.50% ±2.5 | Popular (+37%) | Neutral | 52 |
| B | 59% | Tracer | -1.00% | -1.25% ±2.0 | Niche (-26%) | Neutral | 52 |
| B | 59% | Cassidy | -1.06% | -1.26% ±1.2 | Standard (-17%) | Neutral | 52 |
| B | 52% | Zenyatta | -1.13% | -1.85% ±2.4 | Popular (+37%) | Neutral | 52 |
| B | 52% | Soldier: 76 | -1.15% | -1.60% ±2.2 | Standard (-12%) | Neutral | 51 |
| C | 39% | Torbjörn | -1.22% | -2.21% ±3.9 | Standard (+16%) | Unfavorable | 50 |
| C | 44% | Symmetra | -1.23% | -1.70% ±3.1 | Popular (+42%) | Trap Pick | 52 |
| C | 33% | Roadhog *(provisional)* | -1.30% | -7.98% ±11.3 | Standard (-7%) | Unfavorable | 8 |
| C | 45% | Ramattra | -1.46% | -1.99% ±3.6 | Map Priority (+54%) | Trap Pick | 52 |
| C | 72% | Kiriko | -1.60% | -1.94% ±1.4 | Standard (-10%) | Unfavorable | 52 |
| C | 38% | Sombra *(provisional)* | -1.64% | -3.41% ±6.2 | Standard (-19%) | Unfavorable | 8 |
| C | 56% | Echo | -1.87% | -3.16% ±3.2 | Niche (-27%) | Deterrent | 52 |
| C | 54% | Mauga | -2.08% | -3.30% ±3.2 | Niche (-25%) | Deterrent | 48 |
| C | 46% | Pharah | -2.21% | -2.97% ±3.7 | Standard (-7%) | Unfavorable | 51 |
| C | 46% | Hazard | -2.44% | -3.93% ±3.7 | Niche (-46%) | Deterrent | 49 |
| C | 41% | Junker Queen | -2.63% | -3.10% ±3.5 | Standard (-18%) | Unfavorable | 45 |
| C | 47% | Bastion | -2.66% | -5.60% ±3.8 | Standard (+16%) | Unfavorable | 52 |
| C | 39% | Reinhardt | -2.89% | -3.69% ±3.5 | Standard (+11%) | Unfavorable | 52 |
| D | 60% | Wrecking Ball | -3.35% | -5.47% ±3.6 | Niche (-40%) | Deterrent | 50 |
| D | 81% | Jetpack Cat | -4.24% | -6.55% ±3.5 | Niche (-35%) | Deterrent | 52 |
| D | 93% | Winston | -5.16% | -5.97% ±3.2 | Niche (-41%) | Deterrent | 52 |
| D | 97% | Lúcio | -6.08% | -6.85% ±3.5 | Niche (-49%) | Deterrent | 45 |

### Neon Junction

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| A | 57% | Mizuki | +2.77% | +3.51% ±1.9 | Standard (-3%) | Favorable | 28 |
| A | 54% | Reinhardt | +1.74% | +2.14% ±2.5 | Popular (+40%) | Meta | 28 |
| A | 57% | Vendetta | +1.55% | +3.10% ±2.6 | Standard (-15%) | Favorable | 28 |
| B | 55% | Orisa | +1.09% | +1.49% ±1.9 | Popular (+27%) | Neutral | 28 |
| B | 60% | Shion | +1.06% | +1.64% ±1.2 | Standard (+13%) | Neutral | 28 |
| B | 58% | Zarya | +0.92% | +1.44% ±2.3 | Popular (+45%) | Neutral | 28 |
| B | 69% | Sigma | +0.78% | +0.94% ±1.6 | Map Priority (+61%) | Neutral | 28 |
| B | 67% | Reaper | +0.66% | +2.10% ±2.9 | Standard (-19%) | Neutral | 28 |
| B | 63% | Bastion | +0.63% | +1.03% ±2.9 | Popular (+45%) | Neutral | 28 |
| B | 67% | Ramattra | +0.59% | +1.16% ±2.5 | Map Priority (+91%) | Neutral | 28 |
| B | 79% | Widowmaker | +0.40% | +0.47% ±1.7 | Popular (+40%) | Neutral | 28 |
| B | 72% | Sierra | +0.22% | +1.35% ±3.3 | Standard (+15%) | Neutral | 24 |
| B | 80% | Lifeweaver | +0.13% | -1.09% ±2.4 | Standard (+12%) | Neutral | 28 |
| B | 90% | Zenyatta | +0.08% | +0.35% ±1.7 | Popular (+36%) | Neutral | 28 |
| B | 80% | Soldier: 76 | +0.07% | +0.34% ±2.4 | Niche (-24%) | Neutral | 28 |
| B | 59% | Junker Queen | +0.06% | +0.36% ±3.2 | Standard (-5%) | Neutral | 26 |
| B | 70% | Symmetra | +0.06% | +0.34% ±2.8 | Standard (+17%) | Neutral | 28 |
| B | 72% | Venture | +0.04% | +2.16% ±3.5 | Standard (-0%) | Neutral | 28 |
| B | 71% | Moira | +0.00% | +0.70% ±2.9 | Standard (-9%) | Neutral | 28 |
| B | 58% | Torbjörn | -0.03% | +0.02% ±4.0 | Standard (+8%) | Neutral | 27 |
| B | 91% | Genji | -0.22% | -0.48% ±1.5 | Standard (-11%) | Neutral | 28 |
| B | 83% | Kiriko | -0.22% | -0.26% ±2.0 | Standard (-7%) | Neutral | 28 |
| B | 78% | Illari | -0.26% | -0.63% ±2.5 | Standard (-7%) | Neutral | 28 |
| B | 89% | Sojourn | -0.36% | -0.34% ±1.5 | Popular (+27%) | Neutral | 28 |
| B | 82% | Emre | -0.42% | -0.60% ±1.9 | Standard (+16%) | Neutral | 28 |
| B | 84% | Cassidy | -0.50% | -0.57% ±1.5 | Standard (-10%) | Neutral | 28 |
| B | 72% | Mei | -0.55% | -1.28% ±2.5 | Map Priority (+65%) | Neutral | 28 |
| B | 46% | Roadhog *(provisional)* | -0.56% | -1.09% ±7.7 | Standard (-5%) | Neutral | 8 |
| B | 49% | Doctrine *(provisional)* | -0.60% | -1.75% ±6.1 | Standard (+3%) | Neutral | 8 |
| B | 61% | Anran | -0.68% | -1.77% ±4.5 | Standard (-3%) | Neutral | 28 |
| B | 65% | D.Mon | -0.71% | -1.00% ±2.8 | Standard (+6%) | Neutral | 16 |
| B | 65% | Juno | -0.77% | -1.69% ±2.7 | Standard (+11%) | Neutral | 28 |
| B | 47% | Sombra *(provisional)* | -0.80% | -0.66% ±5.6 | Niche (-25%) | Neutral | 8 |
| B | 59% | Baptiste | -0.89% | -1.55% ±3.1 | Popular (+25%) | Neutral | 28 |
| B | 57% | Domina | -0.89% | -0.82% ±2.6 | Map Priority (+57%) | Neutral | 28 |
| B | 55% | Pharah | -0.96% | -0.94% ±2.7 | Standard (+4%) | Neutral | 28 |
| B | 58% | Doomfist | -1.01% | -2.05% ±2.3 | Standard (-15%) | Neutral | 28 |
| B | 57% | Wuyang | -1.06% | -1.69% ±2.0 | Popular (+24%) | Neutral | 28 |
| B | 54% | Ashe | -1.12% | -1.48% ±1.6 | Standard (+8%) | Neutral | 28 |
| C | 50% | Ana | -1.23% | -1.33% ±1.6 | Standard (+7%) | Unfavorable | 28 |
| C | 39% | Wrecking Ball | -1.36% | -2.47% ±4.5 | Niche (-50%) | Deterrent | 28 |
| C | 54% | Hanzo | -1.37% | -1.90% ±2.2 | Popular (+30%) | Trap Pick | 28 |
| C | 62% | Mercy | -1.54% | -2.62% ±2.0 | Standard (-3%) | Unfavorable | 26 |
| C | 58% | Mauga | -1.70% | -2.26% ±2.5 | Standard (-17%) | Unfavorable | 27 |
| C | 47% | Jetpack Cat | -1.81% | -2.72% ±3.5 | Niche (-36%) | Deterrent | 28 |
| C | 74% | D.Va | -1.95% | -3.05% ±1.9 | Niche (-50%) | Deterrent | 28 |
| C | 44% | Lúcio | -2.29% | -2.33% ±3.3 | Niche (-40%) | Deterrent | 26 |
| C | 66% | Freja | -2.34% | -3.77% ±2.4 | Standard (+0%) | Unfavorable | 28 |
| C | 45% | Junkrat | -2.40% | -4.47% ±4.0 | Standard (+11%) | Unfavorable | 28 |
| C | 51% | Brigitte | -2.74% | -4.42% ±2.9 | Niche (-42%) | Deterrent | 28 |
| C | 53% | Tracer | -2.89% | -4.04% ±2.0 | Niche (-39%) | Deterrent | 28 |
| D | 69% | Echo | -3.47% | -4.90% ±2.2 | Niche (-41%) | Deterrent | 28 |
| D | 93% | Hazard | -4.53% | -5.78% ±2.4 | Niche (-48%) | Deterrent | 28 |
| D | 100% | Winston | -5.87% | -6.31% ±2.2 | Niche (-55%) | Deterrent | 28 |

### Nepal

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| A | 49% | Symmetra | +3.00% | +3.61% ±1.6 | Map Priority (+84%) | Meta | 52 |
| A | 74% | Torbjörn | +2.42% | +2.74% ±1.5 | Standard (-14%) | Favorable | 51 |
| A | 83% | Pharah | +2.19% | +2.45% ±1.3 | Map Priority (+52%) | Meta | 52 |
| A | 77% | Bastion | +2.13% | +2.56% ±1.6 | Standard (-14%) | Favorable | 52 |
| A | 86% | Reinhardt | +2.06% | +2.16% ±1.2 | Popular (+25%) | Meta | 52 |
| A | 79% | Mauga | +2.04% | +2.55% ±1.6 | Standard (+16%) | Favorable | 51 |
| A | 82% | Lúcio | +1.78% | +1.87% ±1.2 | Popular (+50%) | Meta | 52 |
| A | 73% | Ramattra | +1.78% | +2.21% ±1.6 | Standard (+18%) | Favorable | 52 |
| A | 76% | Jetpack Cat | +1.69% | +1.85% ±1.3 | Standard (+5%) | Favorable | 52 |
| A | 70% | Hazard | +1.67% | +1.98% ±1.6 | Standard (+6%) | Favorable | 52 |
| A | 64% | Orisa | +1.49% | +1.84% ±1.5 | Standard (+12%) | Favorable | 52 |
| A | 35% | Roadhog *(provisional)* | +1.24% | +4.96% ±6.2 | Standard (+4%) | Favorable | 8 |
| B | 56% | Sojourn | +1.13% | +1.35% ±1.0 | Standard (+8%) | Neutral | 52 |
| B | 53% | Junkrat | +1.11% | +1.37% ±2.0 | Standard (+8%) | Neutral | 52 |
| B | 62% | Mizuki | +1.06% | +1.12% ±0.9 | Standard (+15%) | Neutral | 52 |
| B | 88% | Kiriko | +0.82% | +0.87% ±0.7 | Standard (+8%) | Neutral | 52 |
| B | 69% | Brigitte | +0.79% | +1.15% ±1.8 | Standard (+1%) | Neutral | 52 |
| B | 80% | Reaper | +0.69% | +0.97% ±1.3 | Standard (+9%) | Neutral | 52 |
| B | 85% | Doomfist | +0.58% | +0.97% ±1.3 | Standard (+11%) | Neutral | 52 |
| B | 86% | Mei | +0.43% | +0.85% ±1.5 | Standard (-9%) | Neutral | 52 |
| B | 99% | Cassidy | +0.40% | +0.45% ±0.6 | Standard (+13%) | Neutral | 52 |
| B | 84% | Vendetta | +0.35% | +0.57% ±1.8 | Standard (+8%) | Neutral | 49 |
| B | 97% | Zarya | +0.29% | +0.35% ±0.9 | Standard (+17%) | Neutral | 52 |
| B | 77% | Sierra | +0.22% | +1.93% ±2.6 | Standard (-13%) | Neutral | 32 |
| B | 81% | Hanzo | +0.21% | +0.56% ±2.2 | Niche (-37%) | Neutral | 52 |
| B | 95% | Baptiste | +0.17% | +0.43% ±1.3 | Standard (-11%) | Neutral | 52 |
| B | 84% | Lifeweaver | +0.13% | +0.75% ±2.1 | Niche (-24%) | Neutral | 50 |
| B | 100% | Wuyang | +0.12% | +0.15% ±0.8 | Standard (+5%) | Neutral | 52 |
| B | 98% | Zenyatta | +0.09% | +0.20% ±1.1 | Niche (-21%) | Neutral | 52 |
| B | 82% | Venture | +0.04% | +0.91% ±2.3 | Standard (+5%) | Neutral | 52 |
| B | 98% | Emre | +0.03% | +0.35% ±1.1 | Standard (-15%) | Neutral | 52 |
| B | 76% | Moira | -0.10% | +0.36% ±2.5 | Standard (+20%) | Neutral | 52 |
| B | 78% | Domina | -0.13% | +0.03% ±2.0 | Standard (-17%) | Neutral | 50 |
| B | 90% | Freja | -0.31% | -0.24% ±1.5 | Niche (-23%) | Neutral | 52 |
| B | 97% | Illari | -0.32% | -0.42% ±1.0 | Niche (-27%) | Neutral | 51 |
| B | 96% | Sigma | -0.35% | -0.32% ±1.0 | Standard (-16%) | Neutral | 52 |
| B | 86% | Anran | -0.38% | -0.42% ±1.6 | Standard (+13%) | Neutral | 51 |
| B | 93% | Genji | -0.39% | -1.18% ±1.1 | Standard (-5%) | Neutral | 52 |
| B | 85% | Mercy | -0.56% | -0.69% ±1.4 | Standard (-13%) | Neutral | 51 |
| B | 68% | D.Mon | -0.60% | -0.78% ±2.7 | Standard (+11%) | Neutral | 16 |
| B | 52% | Sombra *(provisional)* | -0.60% | -0.26% ±4.6 | Standard (+8%) | Neutral | 8 |
| B | 60% | Junker Queen | -0.73% | -0.67% ±2.5 | Standard (+11%) | Neutral | 48 |
| B | 70% | Ashe | -0.87% | -0.94% ±1.4 | Niche (-44%) | Neutral | 52 |
| B | 79% | Tracer | -0.88% | -0.91% ±0.8 | Standard (+11%) | Neutral | 52 |
| B | 66% | Shion | -1.01% | -1.25% ±1.0 | Standard (+19%) | Neutral | 28 |
| B | 60% | Juno | -1.02% | -1.72% ±1.5 | Standard (+10%) | Neutral | 52 |
| B | 52% | Soldier: 76 | -1.17% | -1.34% ±1.4 | Standard (-10%) | Neutral | 52 |
| B | 50% | D.Va | -1.20% | -1.49% ±1.4 | Standard (-17%) | Neutral | 52 |
| C | 75% | Echo | -1.64% | -1.80% ±1.3 | Standard (+1%) | Unfavorable | 52 |
| C | 53% | Doctrine *(provisional)* | -2.21% | -3.40% ±3.1 | Standard (-2%) | Unfavorable | 8 |
| C | 91% | Ana | -2.51% | -2.56% ±0.7 | Standard (-16%) | Unfavorable | 52 |
| D | 60% | Wrecking Ball | -3.16% | -3.39% ±1.2 | Standard (-0%) | Unfavorable | 52 |
| D | 90% | Winston | -3.80% | -3.87% ±1.2 | Niche (-36%) | Deterrent | 52 |
| D | 100% | Widowmaker | -9.85% | -9.98% ±2.3 | Niche (-71%) | Deterrent | 51 |

### New Junk City

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| S | 70% | Junker Queen | +3.68% | +4.60% ±2.8 | Map Priority (+107%) | Meta | 50 |
| A | 51% | Lúcio | +2.96% | +3.15% ±1.6 | Map Priority (+99%) | Meta | 52 |
| A | 68% | Hazard | +2.40% | +2.93% ±1.8 | Standard (+11%) | Favorable | 51 |
| A | 55% | Symmetra | +2.07% | +3.53% ±2.9 | Standard (+15%) | Favorable | 50 |
| A | 56% | Mizuki | +1.99% | +3.21% ±2.9 | Popular (+48%) | Meta | 52 |
| A | 83% | Vendetta | +1.89% | +2.35% ±1.3 | Map Priority (+51%) | Meta | 48 |
| A | 59% | Moira | +1.57% | +2.60% ±2.2 | Map Priority (+67%) | Meta | 51 |
| A | 53% | D.Mon | +1.35% | +2.34% ±2.2 | Popular (+27%) | Meta | 16 |
| A | 48% | Torbjörn | +1.33% | +1.85% ±2.5 | Standard (-3%) | Favorable | 50 |
| A | 44% | Reinhardt | +1.23% | +1.56% ±2.6 | Popular (+26%) | Meta | 52 |
| B | 45% | Sombra *(provisional)* | +1.10% | +3.72% ±4.8 | Standard (+15%) | Neutral | 8 |
| B | 59% | Mauga | +1.02% | +1.42% ±1.8 | Popular (+47%) | Neutral | 50 |
| B | 66% | Reaper | +0.81% | +1.79% ±2.3 | Popular (+46%) | Neutral | 52 |
| B | 70% | Cassidy | +0.80% | +1.35% ±1.7 | Popular (+32%) | Neutral | 52 |
| B | 79% | Shion | +0.72% | +1.23% ±1.3 | Popular (+45%) | Neutral | 28 |
| B | 61% | Zarya | +0.71% | +1.35% ±2.7 | Popular (+44%) | Neutral | 52 |
| B | 53% | Domina | +0.69% | +1.69% ±3.7 | Niche (-29%) | Neutral | 46 |
| B | 75% | Tracer | +0.68% | +1.06% ±1.7 | Popular (+25%) | Neutral | 52 |
| B | 63% | Wrecking Ball | +0.49% | +0.93% ±2.9 | Standard (-19%) | Neutral | 52 |
| B | 92% | Sojourn | +0.39% | +0.56% ±1.2 | Standard (+17%) | Neutral | 52 |
| B | 76% | Brigitte | +0.37% | +0.77% ±2.3 | Standard (+9%) | Neutral | 51 |
| B | 76% | Anran | +0.35% | +0.87% ±2.6 | Popular (+49%) | Neutral | 51 |
| B | 72% | Orisa | +0.22% | +0.45% ±2.8 | Popular (+35%) | Neutral | 51 |
| B | 90% | Sierra | +0.22% | -1.36% ±1.6 | Niche (-22%) | Neutral | 26 |
| B | 78% | Doomfist | +0.21% | +1.11% ±2.6 | Standard (+2%) | Neutral | 51 |
| B | 77% | Mei | +0.20% | +0.94% ±2.6 | Standard (+19%) | Neutral | 51 |
| B | 83% | Lifeweaver | +0.13% | +0.23% ±2.2 | Niche (-35%) | Neutral | 49 |
| B | 72% | Baptiste | +0.11% | +1.92% ±3.5 | Niche (-25%) | Neutral | 52 |
| B | 70% | Ramattra | +0.09% | +0.54% ±2.8 | Map Priority (+56%) | Neutral | 52 |
| B | 83% | Venture | +0.04% | +1.43% ±2.2 | Popular (+38%) | Neutral | 50 |
| B | 58% | Doctrine *(provisional)* | -0.03% | +0.02% ±4.1 | Standard (-5%) | Neutral | 8 |
| B | 95% | Wuyang | -0.05% | -0.01% ±1.3 | Standard (+12%) | Neutral | 52 |
| B | 84% | Kiriko | -0.09% | -0.06% ±2.1 | Popular (+23%) | Neutral | 52 |
| B | 91% | Emre | -0.11% | +0.28% ±1.6 | Niche (-41%) | Neutral | 51 |
| B | 49% | Roadhog *(provisional)* | -0.16% | +0.61% ±7.2 | Standard (+2%) | Neutral | 8 |
| B | 79% | Genji | -0.23% | -1.19% ±2.4 | Standard (+2%) | Neutral | 52 |
| B | 76% | Mercy | -0.29% | -0.37% ±2.6 | Niche (-32%) | Neutral | 49 |
| B | 89% | Juno | -0.30% | +0.24% ±1.6 | Standard (+2%) | Neutral | 50 |
| B | 73% | Illari | -0.32% | -1.22% ±3.0 | Niche (-49%) | Neutral | 52 |
| B | 71% | Soldier: 76 | -0.68% | -0.84% ±2.1 | Standard (-8%) | Neutral | 51 |
| B | 67% | Junkrat | -0.70% | -0.87% ±2.2 | Standard (+9%) | Neutral | 49 |
| B | 65% | Bastion | -0.77% | -1.07% ±2.2 | Niche (-29%) | Neutral | 48 |
| B | 56% | Jetpack Cat | -0.96% | -1.17% ±2.4 | Standard (-14%) | Neutral | 51 |
| B | 52% | D.Va | -1.12% | -2.42% ±3.2 | Niche (-28%) | Neutral | 52 |
| C | 46% | Hanzo | -1.21% | -1.94% ±2.9 | Niche (-39%) | Deterrent | 51 |
| C | 46% | Ashe | -1.23% | -3.06% ±3.2 | Niche (-74%) | Deterrent | 46 |
| C | 57% | Zenyatta | -1.39% | -1.98% ±1.9 | Niche (-35%) | Deterrent | 50 |
| C | 58% | Echo | -1.47% | -1.81% ±2.0 | Niche (-52%) | Deterrent | 51 |
| C | 54% | Freja | -2.63% | -5.83% ±3.3 | Niche (-58%) | Deterrent | 47 |
| C | 47% | Sigma | -2.98% | -3.10% ±2.0 | Niche (-44%) | Deterrent | 51 |
| D | 84% | Ana | -4.14% | -5.24% ±2.6 | Niche (-36%) | Deterrent | 52 |
| D | 91% | Pharah | -4.83% | -6.66% ±3.2 | Niche (-36%) | Deterrent | 51 |
| D | 100% | Winston | -6.98% | -8.10% ±3.0 | Niche (-56%) | Deterrent | 52 |
| D | 100% | Widowmaker | -18.09% | -19.36% ±4.6 | Niche (-83%) | Deterrent | 29 |

### New Queen Street

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| S | 95% | Soldier: 76 | +4.10% | +5.27% ±1.5 | Map Priority (+134%) | Meta | 52 |
| A | 51% | Torbjörn | +2.98% | +3.37% ±1.5 | Standard (-12%) | Favorable | 51 |
| A | 61% | Junker Queen | +1.73% | +2.00% ±2.0 | Standard (+19%) | Favorable | 49 |
| A | 65% | Kiriko | +1.61% | +2.38% ±1.9 | Standard (+13%) | Favorable | 52 |
| A | 52% | Wrecking Ball | +1.36% | +1.80% ±2.1 | Popular (+42%) | Meta | 52 |
| A | 52% | Mizuki | +1.25% | +1.47% ±1.5 | Standard (+8%) | Favorable | 52 |
| A | 45% | Ramattra | +1.25% | +2.30% ±2.8 | Niche (-35%) | Specialist | 46 |
| B | 47% | Symmetra | +1.13% | +2.95% ±4.1 | Niche (-38%) | Neutral | 41 |
| B | 54% | Wuyang | +1.13% | +1.62% ±1.4 | Standard (+14%) | Neutral | 52 |
| B | 48% | Junkrat | +1.08% | +2.01% ±3.8 | Niche (-41%) | Neutral | 49 |
| B | 64% | Tracer | +1.00% | +1.24% ±1.2 | Popular (+34%) | Neutral | 52 |
| B | 57% | D.Mon | +0.92% | +2.52% ±3.3 | Standard (+9%) | Neutral | 16 |
| B | 62% | Doomfist | +0.89% | +2.62% ±2.3 | Standard (+11%) | Neutral | 52 |
| B | 71% | Zarya | +0.79% | +0.99% ±1.5 | Niche (-21%) | Neutral | 51 |
| B | 63% | Reinhardt | +0.78% | +0.95% ±2.2 | Standard (-3%) | Neutral | 52 |
| B | 66% | Freja | +0.67% | +2.31% ±3.1 | Niche (-33%) | Neutral | 51 |
| B | 67% | Mauga | +0.65% | +1.23% ±2.4 | Popular (+21%) | Neutral | 51 |
| B | 74% | Reaper | +0.61% | +1.26% ±2.0 | Standard (-12%) | Neutral | 52 |
| B | 62% | Hazard | +0.48% | +1.06% ±3.2 | Standard (+10%) | Neutral | 52 |
| B | 77% | Zenyatta | +0.41% | +1.27% ±2.4 | Niche (-30%) | Neutral | 52 |
| B | 79% | Mercy | +0.28% | +0.89% ±2.4 | Standard (-15%) | Neutral | 49 |
| B | 84% | Sierra | +0.22% | -1.07% ±2.0 | Standard (-7%) | Neutral | 34 |
| B | 85% | Hanzo | +0.18% | +0.45% ±1.9 | Niche (-54%) | Neutral | 50 |
| B | 96% | Lúcio | +0.15% | +0.19% ±1.1 | Standard (+16%) | Neutral | 52 |
| B | 75% | Lifeweaver | +0.13% | +1.90% ±3.0 | Standard (-14%) | Neutral | 51 |
| B | 97% | Shion | +0.07% | +0.22% ±1.2 | Popular (+28%) | Neutral | 28 |
| B | 72% | Venture | +0.04% | +0.06% ±3.5 | Standard (-17%) | Neutral | 51 |
| B | 81% | Winston | -0.19% | -0.07% ±1.8 | Standard (+4%) | Neutral | 52 |
| B | 88% | Genji | -0.24% | -0.75% ±1.6 | Standard (-10%) | Neutral | 52 |
| B | 88% | Illari | -0.27% | -0.46% ±1.6 | Standard (-14%) | Neutral | 52 |
| B | 70% | Mei | -0.37% | -1.12% ±3.4 | Niche (-37%) | Neutral | 52 |
| B | 86% | Brigitte | -0.41% | -0.38% ±1.5 | Standard (+9%) | Neutral | 52 |
| B | 81% | Emre | -0.52% | -0.87% ±1.7 | Standard (-5%) | Neutral | 52 |
| B | 66% | Moira | -0.52% | -0.16% ±2.9 | Standard (+5%) | Neutral | 52 |
| B | 72% | D.Va | -0.53% | -0.50% ±2.6 | Standard (+13%) | Neutral | 52 |
| B | 73% | Juno | -0.68% | -0.91% ±2.0 | Standard (+5%) | Neutral | 52 |
| B | 65% | Vendetta | -0.73% | -1.28% ±2.8 | Standard (-5%) | Neutral | 48 |
| B | 64% | Baptiste | -0.80% | -1.11% ±2.5 | Niche (-35%) | Neutral | 52 |
| B | 61% | Echo | -0.80% | -0.92% ±2.8 | Niche (-39%) | Neutral | 52 |
| B | 64% | Ashe | -0.86% | -1.03% ±2.1 | Niche (-47%) | Neutral | 51 |
| B | 71% | Sojourn | -0.88% | -0.98% ±1.2 | Standard (+10%) | Neutral | 52 |
| B | 54% | Pharah | -1.05% | -1.07% ±2.3 | Niche (-39%) | Neutral | 52 |
| B | 44% | Sombra *(provisional)* | -1.17% | -1.62% ±5.0 | Standard (+13%) | Neutral | 8 |
| C | 45% | Bastion | -1.26% | -2.13% ±3.0 | Niche (-26%) | Deterrent | 48 |
| C | 54% | Cassidy | -1.28% | -1.69% ±1.6 | Standard (-1%) | Unfavorable | 52 |
| C | 49% | Orisa | -1.35% | -2.23% ±2.7 | Standard (-3%) | Unfavorable | 52 |
| C | 45% | Doctrine *(provisional)* | -1.45% | -2.39% ±3.4 | Standard (+1%) | Unfavorable | 8 |
| C | 63% | Anran | -1.77% | -2.94% ±2.4 | Standard (-1%) | Unfavorable | 50 |
| C | 39% | Roadhog *(provisional)* | -1.95% | -5.68% ±6.4 | Standard (-0%) | Unfavorable | 8 |
| C | 45% | Domina | -1.99% | -2.46% ±3.6 | Niche (-26%) | Deterrent | 49 |
| C | 66% | Jetpack Cat | -2.51% | -2.86% ±1.8 | Standard (+6%) | Unfavorable | 52 |
| D | 74% | Ana | -3.39% | -3.60% ±1.3 | Standard (-12%) | Unfavorable | 52 |
| D | 98% | Sigma | -5.19% | -5.60% ±2.2 | Niche (-37%) | Deterrent | 52 |
| D | 100% | Widowmaker | -7.58% | -7.64% ±2.2 | Niche (-54%) | Deterrent | 51 |

### Numbani

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| A | 56% | Wrecking Ball | +1.86% | +2.76% ±2.7 | Standard (+6%) | Favorable | 51 |
| A | 40% | Doctrine *(provisional)* | +1.74% | +5.20% ±5.7 | Standard (+4%) | Favorable | 8 |
| A | 53% | Winston | +1.47% | +1.83% ±2.2 | Map Priority (+78%) | Meta | 52 |
| B | 55% | Bastion | +0.90% | +1.69% ±3.4 | Standard (+19%) | Neutral | 51 |
| B | 69% | Ana | +0.59% | +0.82% ±2.2 | Standard (+18%) | Neutral | 52 |
| B | 72% | Mercy | +0.44% | +1.57% ±2.8 | Popular (+38%) | Neutral | 51 |
| B | 83% | Tracer | +0.31% | +0.65% ±1.9 | Standard (-1%) | Neutral | 52 |
| B | 69% | Sierra | +0.22% | +2.14% ±3.9 | Standard (+7%) | Neutral | 32 |
| B | 89% | Kiriko | +0.19% | +0.30% ±1.6 | Standard (+1%) | Neutral | 52 |
| B | 70% | Lifeweaver | +0.13% | +1.04% ±4.0 | Standard (+19%) | Neutral | 51 |
| B | 60% | Junkrat | +0.12% | +0.28% ±3.7 | Standard (-1%) | Neutral | 50 |
| B | 70% | Venture | +0.04% | -3.68% ±4.0 | Standard (-5%) | Neutral | 51 |
| B | 72% | D.Va | -0.07% | +1.33% ±3.6 | Popular (+33%) | Neutral | 51 |
| B | 69% | Freja | -0.23% | +0.51% ±4.0 | Popular (+24%) | Neutral | 52 |
| B | 80% | Ashe | -0.28% | +0.63% ±2.3 | Map Priority (+63%) | Neutral | 52 |
| B | 77% | Hazard | -0.31% | -0.26% ±2.1 | Popular (+34%) | Neutral | 50 |
| B | 80% | Genji | -0.34% | -2.40% ±2.2 | Standard (+9%) | Neutral | 52 |
| B | 71% | Emre | -0.41% | -0.90% ±3.1 | Standard (+12%) | Neutral | 52 |
| B | 78% | Cassidy | -0.55% | -0.70% ±1.9 | Standard (-11%) | Neutral | 52 |
| B | 64% | Anran | -0.63% | -1.29% ±3.8 | Standard (-4%) | Neutral | 50 |
| B | 62% | Mei | -0.63% | -3.39% ±4.4 | Niche (-21%) | Neutral | 50 |
| B | 65% | Doomfist | -0.64% | -1.68% ±3.3 | Standard (+6%) | Neutral | 52 |
| B | 70% | Soldier: 76 | -0.70% | -0.88% ±2.1 | Standard (+5%) | Neutral | 52 |
| B | 63% | Hanzo | -0.71% | -1.01% ±3.1 | Standard (+1%) | Neutral | 52 |
| B | 70% | Illari | -0.72% | -2.33% ±2.1 | Standard (+8%) | Neutral | 52 |
| B | 45% | Sombra *(provisional)* | -0.72% | -0.20% ±7.6 | Standard (-9%) | Neutral | 8 |
| B | 70% | Shion | -0.75% | -1.33% ±1.9 | Standard (-19%) | Neutral | 28 |
| B | 61% | Juno | -0.84% | -2.61% ±3.1 | Standard (-8%) | Neutral | 51 |
| B | 59% | Vendetta | -0.86% | -1.94% ±3.6 | Standard (-1%) | Neutral | 43 |
| B | 55% | Echo | -1.05% | -1.32% ±2.6 | Map Priority (+74%) | Neutral | 52 |
| B | 48% | Torbjörn | -1.16% | -1.75% ±3.1 | Standard (+16%) | Neutral | 50 |
| B | 47% | Jetpack Cat | -1.17% | -1.61% ±3.1 | Standard (+16%) | Neutral | 52 |
| C | 50% | Wuyang | -1.24% | -2.04% ±2.0 | Niche (-20%) | Deterrent | 51 |
| C | 47% | Zenyatta | -1.24% | -2.32% ±2.8 | Niche (-21%) | Deterrent | 52 |
| C | 32% | Roadhog *(provisional)* | -1.25% | -10.23% ±13.4 | Standard (-6%) | Unfavorable | 7 |
| C | 46% | Sigma | -1.34% | -1.28% ±2.5 | Niche (-22%) | Deterrent | 51 |
| C | 50% | Orisa | -1.54% | -3.03% ±3.3 | Niche (-28%) | Deterrent | 51 |
| C | 48% | D.Mon | -1.68% | -6.15% ±5.5 | Niche (-24%) | Deterrent | 16 |
| C | 56% | Baptiste | -1.69% | -4.27% ±3.2 | Standard (-0%) | Unfavorable | 52 |
| C | 56% | Mauga | -1.83% | -2.66% ±2.9 | Standard (-13%) | Unfavorable | 48 |
| C | 60% | Brigitte | -1.90% | -2.72% ±2.6 | Standard (+15%) | Unfavorable | 51 |
| C | 60% | Reaper | -1.96% | -4.50% ±3.2 | Standard (-5%) | Unfavorable | 52 |
| C | 50% | Zarya | -2.16% | -2.88% ±3.3 | Niche (-33%) | Deterrent | 52 |
| C | 61% | Sojourn | -2.41% | -4.63% ±2.8 | Niche (-34%) | Deterrent | 52 |
| C | 50% | Moira | -2.44% | -4.00% ±3.7 | Niche (-27%) | Deterrent | 51 |
| C | 45% | Symmetra | -2.46% | -4.90% ±4.3 | Standard (-18%) | Unfavorable | 46 |
| C | 35% | Reinhardt | -2.94% | -4.23% ±4.4 | Niche (-36%) | Deterrent | 51 |
| D | 57% | Ramattra | -3.22% | -4.89% ±3.3 | Niche (-49%) | Deterrent | 41 |
| D | 59% | Pharah | -3.29% | -4.42% ±3.2 | Standard (-1%) | Unfavorable | 51 |
| D | 65% | Mizuki | -3.36% | -4.46% ±2.1 | Niche (-27%) | Deterrent | 51 |
| D | 68% | Lúcio | -3.84% | -4.28% ±4.0 | Niche (-35%) | Deterrent | 52 |
| D | 83% | Domina | -4.26% | -5.48% ±3.1 | Niche (-25%) | Deterrent | 45 |
| D | 98% | Junker Queen | -6.89% | -10.10% ±4.7 | Niche (-38%) | Deterrent | 39 |
| D | 100% | Widowmaker | -9.36% | -9.48% ±2.4 | Niche (-36%) | Deterrent | 51 |

### Oasis

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| S | 73% | Torbjörn | +3.42% | +3.84% ±1.4 | Standard (-10%) | Favorable | 51 |
| A | 98% | Cassidy | +2.09% | +2.36% ±0.8 | Popular (+45%) | Meta | 52 |
| A | 70% | Orisa | +1.77% | +2.32% ±1.8 | Standard (+6%) | Favorable | 52 |
| A | 67% | Doomfist | +1.48% | +2.37% ±1.4 | Standard (+12%) | Favorable | 52 |
| B | 56% | Jetpack Cat | +1.11% | +1.20% ±1.2 | Standard (+13%) | Neutral | 52 |
| B | 65% | Hazard | +1.00% | +1.10% ±1.1 | Popular (+28%) | Neutral | 52 |
| B | 68% | Mizuki | +0.96% | +1.04% ±1.1 | Popular (+31%) | Neutral | 52 |
| B | 63% | Vendetta | +0.92% | +1.41% ±1.9 | Standard (+18%) | Neutral | 48 |
| B | 63% | Freja | +0.81% | +2.31% ±2.8 | Niche (-31%) | Neutral | 52 |
| B | 83% | Kiriko | +0.81% | +0.89% ±0.8 | Standard (+15%) | Neutral | 52 |
| B | 83% | Brigitte | +0.77% | +0.87% ±0.9 | Popular (+26%) | Neutral | 52 |
| B | 84% | Zarya | +0.57% | +0.70% ±1.3 | Standard (+2%) | Neutral | 52 |
| B | 66% | Mauga | +0.55% | +1.26% ±2.8 | Popular (+20%) | Neutral | 51 |
| B | 81% | Moira | +0.54% | +0.85% ±1.5 | Popular (+24%) | Neutral | 52 |
| B | 91% | Shion | +0.54% | +0.82% ±1.0 | Popular (+28%) | Neutral | 28 |
| B | 87% | Reaper | +0.44% | +0.72% ±1.5 | Popular (+21%) | Neutral | 52 |
| B | 83% | Illari | +0.43% | +1.67% ±1.7 | Niche (-29%) | Neutral | 52 |
| B | 75% | Ramattra | +0.43% | +0.80% ±2.1 | Niche (-25%) | Neutral | 50 |
| B | 50% | Roadhog *(provisional)* | +0.42% | +2.21% ±6.0 | Standard (+2%) | Neutral | 8 |
| B | 75% | Hanzo | +0.39% | +1.00% ±2.5 | Niche (-42%) | Neutral | 52 |
| B | 96% | Soldier: 76 | +0.28% | +0.36% ±1.0 | Standard (-11%) | Neutral | 52 |
| B | 69% | Domina | +0.25% | +0.60% ±2.5 | Niche (-30%) | Neutral | 47 |
| B | 86% | Sierra | +0.22% | +0.52% ±1.8 | Standard (-16%) | Neutral | 32 |
| B | 100% | Tracer | +0.16% | +0.20% ±0.7 | Popular (+29%) | Neutral | 52 |
| B | 84% | Lifeweaver | +0.13% | +0.37% ±2.0 | Niche (-23%) | Neutral | 49 |
| B | 100% | Wuyang | +0.07% | +0.10% ±0.8 | Standard (-8%) | Neutral | 52 |
| B | 86% | Venture | +0.04% | -0.62% ±1.9 | Standard (+1%) | Neutral | 52 |
| B | 100% | Sojourn | -0.02% | +0.02% ±0.8 | Standard (-13%) | Neutral | 52 |
| B | 92% | Mei | -0.05% | +0.03% ±1.5 | Standard (-17%) | Neutral | 52 |
| B | 77% | Anran | -0.06% | +0.14% ±2.7 | Standard (+10%) | Neutral | 52 |
| B | 86% | Junkrat | -0.06% | -0.06% ±1.7 | Standard (-12%) | Neutral | 51 |
| B | 80% | D.Va | -0.21% | +0.23% ±2.4 | Standard (+12%) | Neutral | 52 |
| B | 87% | Symmetra | -0.30% | -0.27% ±1.5 | Standard (+11%) | Neutral | 52 |
| B | 82% | Baptiste | -0.34% | -0.13% ±2.0 | Standard (-18%) | Neutral | 52 |
| B | 82% | Bastion | -0.34% | -0.43% ±1.9 | Standard (-19%) | Neutral | 51 |
| B | 91% | Genji | -0.36% | -1.24% ±1.3 | Standard (-4%) | Neutral | 52 |
| B | 89% | Zenyatta | -0.49% | -0.50% ±1.2 | Niche (-31%) | Neutral | 52 |
| B | 71% | Junker Queen | -0.56% | -0.51% ±2.0 | Popular (+24%) | Neutral | 52 |
| B | 76% | Juno | -0.62% | -0.69% ±1.9 | Standard (-3%) | Neutral | 52 |
| B | 78% | Echo | -0.65% | -0.66% ±1.5 | Standard (-4%) | Neutral | 52 |
| B | 51% | Sombra *(provisional)* | -0.65% | -0.35% ±4.8 | Standard (+16%) | Neutral | 8 |
| B | 84% | Lúcio | -0.72% | -0.70% ±1.0 | Map Priority (+54%) | Neutral | 52 |
| B | 79% | Winston | -0.73% | -0.69% ±1.2 | Standard (-5%) | Neutral | 52 |
| B | 70% | Emre | -0.90% | -1.46% ±1.2 | Niche (-33%) | Neutral | 52 |
| B | 64% | Mercy | -0.95% | -1.31% ±1.5 | Standard (-16%) | Neutral | 51 |
| B | 59% | D.Mon | -0.97% | -1.28% ±2.2 | Standard (+6%) | Neutral | 16 |
| B | 57% | Ashe | -1.03% | -1.51% ±2.2 | Niche (-67%) | Neutral | 52 |
| B | 53% | Pharah | -1.06% | -1.08% ±2.4 | Standard (+18%) | Neutral | 52 |
| B | 52% | Reinhardt | -1.17% | -1.21% ±1.6 | Standard (-9%) | Neutral | 51 |
| C | 97% | Ana | -1.96% | -2.00% ±0.8 | Niche (-23%) | Deterrent | 52 |
| C | 78% | Wrecking Ball | -2.24% | -2.48% ±1.5 | Standard (+14%) | Unfavorable | 52 |
| C | 43% | Doctrine *(provisional)* | -2.81% | -4.89% ±3.6 | Standard (-5%) | Unfavorable | 8 |
| D | 87% | Sigma | -4.12% | -4.34% ±2.0 | Niche (-49%) | Deterrent | 52 |
| D | 100% | Widowmaker | -15.52% | -15.93% ±2.9 | Niche (-78%) | Deterrent | 46 |

### Paraiso

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| A | 41% | Jetpack Cat | +2.08% | +4.69% ±4.8 | Standard (+17%) | Favorable | 16 |
| A | 36% | Doctrine *(provisional)* | +1.91% | +11.86% ±9.2 | Standard (+6%) | Favorable | 8 |
| A | 39% | Bastion | +1.47% | +6.42% ±6.7 | Standard (+8%) | Favorable | 15 |
| A | 48% | Winston | +1.46% | +1.97% ±2.6 | Popular (+40%) | Meta | 16 |
| A | 47% | Ana | +1.25% | +1.68% ±2.3 | Standard (+16%) | Favorable | 16 |
| B | 47% | Pharah | +1.02% | +2.55% ±4.0 | Standard (+3%) | Neutral | 16 |
| B | 55% | Mercy | +0.96% | +5.29% ±4.1 | Map Priority (+56%) | Neutral | 16 |
| B | 59% | Orisa | +0.26% | +1.31% ±5.7 | Niche (-32%) | Neutral | 16 |
| B | 63% | Sierra | +0.22% | +0.25% ±7.5 | Standard (+15%) | Neutral | 11 |
| B | 66% | Vendetta | +0.17% | +1.30% ±5.0 | Standard (-5%) | Neutral | 16 |
| B | 63% | Lifeweaver | +0.13% | +1.03% ±7.2 | Standard (+17%) | Neutral | 16 |
| B | 63% | Venture | +0.04% | -3.40% ±8.6 | Standard (-9%) | Neutral | 15 |
| B | 70% | Echo | -0.00% | +0.68% ±3.3 | Map Priority (+85%) | Neutral | 16 |
| B | 63% | Mei | -0.02% | +2.33% ±7.5 | Niche (-28%) | Neutral | 16 |
| B | 50% | Symmetra | -0.09% | +1.84% ±8.4 | Niche (-21%) | Neutral | 15 |
| B | 77% | Genji | -0.21% | -0.90% ±2.7 | Standard (+10%) | Neutral | 16 |
| B | 71% | Emre | -0.35% | -0.42% ±3.2 | Standard (+19%) | Neutral | 16 |
| B | 59% | Brigitte | -0.38% | -0.08% ±4.9 | Standard (+8%) | Neutral | 16 |
| B | 67% | D.Va | -0.39% | +0.24% ±4.2 | Map Priority (+65%) | Neutral | 16 |
| B | 66% | Illari | -0.40% | -3.31% ±4.3 | Popular (+22%) | Neutral | 16 |
| B | 53% | Mauga | -0.40% | +0.51% ±7.4 | Standard (-11%) | Neutral | 15 |
| B | 62% | Soldier: 76 | -0.41% | -0.59% ±5.1 | Standard (-2%) | Neutral | 16 |
| B | 70% | Zenyatta | -0.48% | -0.53% ±3.0 | Standard (-6%) | Neutral | 16 |
| B | 62% | Doomfist | -0.50% | -2.10% ±5.3 | Standard (-10%) | Neutral | 16 |
| B | 68% | Shion | -0.50% | -1.42% ±3.5 | Niche (-24%) | Neutral | 16 |
| B | 39% | Reinhardt | -0.56% | -0.57% ±7.0 | Standard (-19%) | Neutral | 16 |
| B | 70% | Kiriko | -0.57% | -0.97% ±2.7 | Standard (-6%) | Neutral | 16 |
| B | 60% | D.Mon | -0.60% | -1.11% ±4.7 | Standard (-7%) | Neutral | 16 |
| B | 45% | Junkrat | -0.63% | -2.48% ±7.6 | Standard (+13%) | Neutral | 16 |
| B | 64% | Ashe | -0.66% | -0.14% ±3.6 | Map Priority (+70%) | Neutral | 16 |
| B | 43% | Roadhog *(provisional)* | -0.68% | -3.75% ±13.9 | Standard (-1%) | Neutral | 8 |
| B | 58% | Juno | -0.70% | -3.29% ±6.0 | Standard (-12%) | Neutral | 16 |
| B | 57% | Freja | -0.75% | -2.13% ±6.8 | Standard (+15%) | Neutral | 16 |
| B | 59% | Baptiste | -0.79% | -1.69% ±4.3 | Standard (-2%) | Neutral | 16 |
| B | 57% | Tracer | -0.94% | -1.43% ±3.0 | Standard (-15%) | Neutral | 16 |
| B | 51% | Anran | -1.01% | -6.13% ±7.3 | Standard (-7%) | Neutral | 15 |
| B | 44% | Torbjörn | -1.16% | -2.54% ±4.7 | Standard (+16%) | Neutral | 15 |
| C | 43% | Moira | -1.25% | -1.47% ±3.6 | Standard (-15%) | Unfavorable | 15 |
| C | 35% | Wrecking Ball | -1.29% | -3.49% ±6.6 | Standard (-15%) | Unfavorable | 16 |
| C | 48% | Wuyang | -1.35% | -4.55% ±3.8 | Standard (-11%) | Unfavorable | 16 |
| C | 54% | Cassidy | -1.36% | -2.20% ±2.2 | Standard (-10%) | Unfavorable | 16 |
| C | 46% | Sojourn | -1.36% | -4.47% ±4.7 | Niche (-25%) | Deterrent | 16 |
| C | 43% | Hazard | -1.38% | -2.02% ±3.7 | Popular (+29%) | Trap Pick | 16 |
| C | 35% | Widowmaker | -1.38% | -1.16% ±3.7 | Popular (+25%) | Trap Pick | 16 |
| C | 39% | Mizuki | -1.42% | -5.08% ±6.1 | Niche (-28%) | Deterrent | 16 |
| C | 33% | Sombra *(provisional)* | -1.46% | -7.81% ±13.4 | Standard (+0%) | Unfavorable | 8 |
| C | 51% | Reaper | -1.47% | -3.83% ±3.7 | Standard (-6%) | Unfavorable | 16 |
| C | 36% | Ramattra | -1.56% | -5.55% ±9.2 | Niche (-46%) | Deterrent | 13 |
| C | 57% | Hanzo | -2.01% | -4.18% ±3.5 | Standard (+1%) | Unfavorable | 16 |
| C | 26% | Junker Queen | -2.15% | -4.84% ±10.1 | Niche (-34%) | Deterrent | 14 |
| C | 31% | Domina | -2.66% | -7.36% ±8.6 | Standard (-6%) | Unfavorable | 13 |
| D | 52% | Zarya | -3.08% | -5.69% ±4.7 | Niche (-29%) | Deterrent | 16 |
| D | 54% | Sigma | -3.18% | -3.73% ±4.0 | Standard (-6%) | Unfavorable | 16 |
| D | 83% | Lúcio | -5.64% | -8.70% ±7.3 | Niche (-48%) | Deterrent | 16 |

### Rialto

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| A | 48% | Widowmaker | +2.15% | +2.40% ±2.8 | Map Priority (+110%) | Meta | 52 |
| A | 52% | Ana | +1.42% | +1.87% ±2.3 | Popular (+27%) | Meta | 52 |
| B | 49% | Pharah | +1.16% | +1.84% ±2.6 | Popular (+37%) | Neutral | 52 |
| B | 51% | Sigma | +1.11% | +1.47% ±2.3 | Standard (+13%) | Neutral | 52 |
| B | 63% | Winston | +0.94% | +1.08% ±1.5 | Standard (+7%) | Neutral | 51 |
| B | 57% | Brigitte | +0.91% | +2.06% ±3.0 | Niche (-20%) | Neutral | 52 |
| B | 55% | Bastion | +0.86% | +1.63% ±3.4 | Standard (+14%) | Neutral | 50 |
| B | 77% | Wuyang | +0.48% | +1.05% ±2.1 | Standard (-4%) | Neutral | 52 |
| B | 83% | Hazard | +0.35% | +0.50% ±1.7 | Standard (+1%) | Neutral | 51 |
| B | 83% | Echo | +0.34% | +0.67% ±1.8 | Popular (+48%) | Neutral | 52 |
| B | 91% | Illari | +0.33% | +0.97% ±1.4 | Popular (+27%) | Neutral | 52 |
| B | 83% | Sierra | +0.22% | +0.20% ±2.1 | Standard (+10%) | Neutral | 37 |
| B | 69% | Anran | +0.14% | +0.98% ±4.0 | Standard (-18%) | Neutral | 51 |
| B | 79% | Emre | +0.13% | +2.13% ±2.5 | Popular (+21%) | Neutral | 52 |
| B | 78% | Lifeweaver | +0.13% | -0.85% ±2.6 | Standard (+17%) | Neutral | 50 |
| B | 75% | Freja | +0.11% | +0.92% ±2.9 | Standard (+14%) | Neutral | 52 |
| B | 76% | Venture | +0.04% | -0.96% ±2.9 | Standard (-10%) | Neutral | 51 |
| B | 70% | Zarya | +0.03% | +0.37% ±2.6 | Standard (-10%) | Neutral | 51 |
| B | 85% | D.Va | -0.00% | +0.50% ±2.0 | Popular (+24%) | Neutral | 51 |
| B | 80% | Hanzo | +0.00% | +0.30% ±2.4 | Popular (+26%) | Neutral | 52 |
| B | 77% | Reaper | -0.03% | +0.41% ±2.8 | Niche (-23%) | Neutral | 52 |
| B | 94% | Shion | -0.08% | +0.03% ±1.4 | Niche (-30%) | Neutral | 28 |
| B | 81% | Genji | -0.11% | +0.85% ±2.4 | Standard (-3%) | Neutral | 52 |
| B | 77% | Mei | -0.11% | -0.00% ±2.7 | Standard (+7%) | Neutral | 51 |
| B | 78% | Baptiste | -0.19% | +0.40% ±2.6 | Standard (+5%) | Neutral | 52 |
| B | 80% | Orisa | -0.21% | -0.27% ±2.2 | Standard (+5%) | Neutral | 52 |
| B | 73% | Doomfist | -0.27% | -0.22% ±3.0 | Standard (-1%) | Neutral | 52 |
| B | 85% | Ashe | -0.40% | -0.02% ±1.7 | Popular (+50%) | Neutral | 52 |
| B | 69% | Vendetta | -0.40% | -0.71% ±3.4 | Standard (-20%) | Neutral | 46 |
| B | 68% | D.Mon | -0.45% | -0.52% ±3.1 | Standard (-10%) | Neutral | 16 |
| B | 75% | Mercy | -0.45% | -0.72% ±2.4 | Standard (+20%) | Neutral | 51 |
| B | 89% | Kiriko | -0.48% | -0.54% ±1.2 | Standard (-13%) | Neutral | 52 |
| B | 65% | Junkrat | -0.56% | -0.75% ±2.6 | Standard (+1%) | Neutral | 51 |
| B | 71% | Zenyatta | -0.64% | -0.81% ±2.3 | Popular (+34%) | Neutral | 52 |
| B | 70% | Sojourn | -0.66% | -0.86% ±2.4 | Standard (-9%) | Neutral | 52 |
| B | 66% | Jetpack Cat | -0.71% | -0.82% ±2.1 | Standard (+9%) | Neutral | 51 |
| B | 74% | Mizuki | -0.71% | -0.83% ±1.6 | Niche (-26%) | Neutral | 51 |
| B | 57% | Ramattra | -0.75% | -0.69% ±3.4 | Standard (-15%) | Neutral | 49 |
| B | 57% | Domina | -0.80% | -0.69% ±2.9 | Standard (+9%) | Neutral | 50 |
| B | 42% | Junker Queen | -0.87% | -0.73% ±4.9 | Niche (-28%) | Neutral | 45 |
| B | 61% | Tracer | -0.89% | -1.19% ±2.5 | Niche (-22%) | Neutral | 52 |
| B | 59% | Juno | -0.95% | -2.82% ±2.7 | Niche (-20%) | Neutral | 51 |
| B | 55% | Moira | -1.01% | -1.00% ±2.5 | Niche (-28%) | Neutral | 51 |
| C | 37% | Doctrine *(provisional)* | -1.32% | -3.39% ±5.3 | Standard (+1%) | Unfavorable | 8 |
| C | 33% | Roadhog *(provisional)* | -1.38% | -9.40% ±11.8 | Standard (+11%) | Unfavorable | 8 |
| C | 51% | Reinhardt | -1.43% | -1.56% ±2.3 | Standard (+4%) | Unfavorable | 51 |
| C | 59% | Cassidy | -1.45% | -2.17% ±1.9 | Niche (-28%) | Deterrent | 52 |
| C | 56% | Soldier: 76 | -1.46% | -2.13% ±2.3 | Standard (-15%) | Unfavorable | 51 |
| C | 55% | Mauga | -1.66% | -2.30% ±2.7 | Niche (-22%) | Deterrent | 49 |
| C | 35% | Sombra *(provisional)* | -1.88% | -9.20% ±11.1 | Standard (-16%) | Unfavorable | 8 |
| C | 61% | Torbjörn | -1.94% | -2.53% ±2.3 | Standard (+7%) | Unfavorable | 50 |
| C | 64% | Symmetra | -2.02% | -2.53% ±2.2 | Standard (-18%) | Unfavorable | 49 |
| C | 61% | Wrecking Ball | -2.62% | -3.07% ±1.9 | Standard (-16%) | Unfavorable | 51 |
| D | 99% | Lúcio | -6.33% | -6.82% ±2.7 | Niche (-51%) | Deterrent | 50 |

### Route 66

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| A | 81% | Ana | +2.44% | +2.63% ±1.2 | Standard (+17%) | Favorable | 52 |
| A | 38% | Sombra *(provisional)* | +1.62% | +7.68% ±6.4 | Standard (+13%) | Favorable | 8 |
| B | 54% | Torbjörn | +0.95% | +1.46% ±3.0 | Standard (+15%) | Neutral | 51 |
| B | 64% | Tracer | +0.84% | +1.58% ±2.2 | Standard (-16%) | Neutral | 52 |
| B | 64% | Shion | +0.83% | +2.92% ±2.4 | Niche (-21%) | Neutral | 28 |
| B | 63% | Wrecking Ball | +0.65% | +1.06% ±2.6 | Standard (+2%) | Neutral | 52 |
| B | 60% | Hazard | +0.62% | +1.26% ±3.1 | Standard (+6%) | Neutral | 51 |
| B | 64% | Mercy | +0.62% | +3.03% ±3.6 | Popular (+35%) | Neutral | 51 |
| B | 79% | Cassidy | +0.54% | +1.01% ±1.8 | Standard (-10%) | Neutral | 52 |
| B | 73% | Baptiste | +0.45% | +2.16% ±2.7 | Standard (+15%) | Neutral | 52 |
| B | 77% | Hanzo | +0.34% | +0.84% ±2.3 | Popular (+25%) | Neutral | 51 |
| B | 81% | Sojourn | +0.26% | +0.74% ±2.2 | Standard (-12%) | Neutral | 52 |
| B | 68% | Sierra | +0.22% | +1.77% ±4.4 | Popular (+37%) | Neutral | 36 |
| B | 56% | Doctrine *(provisional)* | +0.20% | +0.50% ±4.4 | Standard (+2%) | Neutral | 8 |
| B | 69% | D.Va | +0.18% | +2.82% ±4.0 | Standard (+18%) | Neutral | 52 |
| B | 83% | Ashe | +0.13% | +1.62% ±2.1 | Map Priority (+58%) | Neutral | 52 |
| B | 78% | Lifeweaver | +0.13% | +1.17% ±2.6 | Popular (+24%) | Neutral | 49 |
| B | 80% | Brigitte | +0.05% | +0.29% ±2.2 | Standard (+3%) | Neutral | 50 |
| B | 71% | Venture | +0.04% | -1.57% ±3.7 | Standard (+0%) | Neutral | 50 |
| B | 73% | Doomfist | -0.00% | +0.87% ±3.3 | Standard (-10%) | Neutral | 51 |
| B | 63% | Mauga | -0.02% | +0.74% ±4.0 | Niche (-24%) | Neutral | 50 |
| B | 70% | Junkrat | -0.03% | -0.01% ±2.7 | Standard (-1%) | Neutral | 48 |
| B | 80% | Illari | -0.10% | +0.22% ±2.4 | Popular (+34%) | Neutral | 52 |
| B | 77% | Freja | -0.15% | +0.28% ±2.8 | Popular (+28%) | Neutral | 52 |
| B | 82% | Wuyang | -0.20% | -0.22% ±2.2 | Standard (-1%) | Neutral | 52 |
| B | 87% | Genji | -0.22% | -0.59% ±1.8 | Standard (+12%) | Neutral | 52 |
| B | 70% | Vendetta | -0.28% | -0.43% ±3.5 | Standard (-8%) | Neutral | 46 |
| B | 61% | Widowmaker | -0.31% | -0.16% ±2.7 | Popular (+39%) | Neutral | 52 |
| B | 45% | Roadhog *(provisional)* | -0.40% | -0.33% ±12.3 | Popular (+29%) | Neutral | 8 |
| B | 77% | Juno | -0.41% | +0.39% ±2.4 | Standard (-8%) | Neutral | 50 |
| B | 84% | Emre | -0.44% | -0.64% ±1.7 | Standard (+19%) | Neutral | 52 |
| B | 58% | Jetpack Cat | -0.44% | -0.58% ±3.6 | Standard (-14%) | Neutral | 52 |
| B | 65% | Anran | -0.51% | -1.03% ±4.0 | Standard (-11%) | Neutral | 49 |
| B | 66% | Mei | -0.62% | -2.02% ±3.1 | Standard (+2%) | Neutral | 52 |
| B | 48% | Zarya | -0.98% | -1.05% ±4.1 | Standard (-17%) | Neutral | 52 |
| B | 52% | Pharah | -1.00% | -1.01% ±3.0 | Niche (-28%) | Neutral | 50 |
| B | 57% | Soldier: 76 | -1.04% | -1.38% ±2.0 | Standard (-15%) | Neutral | 52 |
| B | 50% | Echo | -1.11% | -1.81% ±3.9 | Standard (-2%) | Neutral | 52 |
| B | 52% | Sigma | -1.13% | -1.07% ±2.0 | Popular (+22%) | Neutral | 52 |
| B | 48% | D.Mon | -1.16% | -2.75% ±4.3 | Niche (-21%) | Neutral | 16 |
| B | 50% | Zenyatta | -1.19% | -1.90% ±2.3 | Standard (+5%) | Neutral | 51 |
| C | 53% | Reaper | -1.53% | -3.71% ±3.5 | Standard (-14%) | Unfavorable | 52 |
| C | 52% | Orisa | -1.60% | -2.95% ±3.1 | Niche (-25%) | Deterrent | 51 |
| C | 37% | Junker Queen | -1.62% | -1.86% ±4.3 | Niche (-27%) | Deterrent | 44 |
| C | 48% | Symmetra | -1.74% | -2.87% ±3.6 | Niche (-22%) | Deterrent | 50 |
| C | 49% | Ramattra | -1.81% | -2.61% ±3.6 | Niche (-37%) | Deterrent | 47 |
| C | 46% | Domina | -1.91% | -2.32% ±3.6 | Standard (+1%) | Unfavorable | 51 |
| C | 50% | Moira | -1.99% | -3.25% ±4.0 | Niche (-27%) | Deterrent | 52 |
| C | 44% | Winston | -2.22% | -2.33% ±3.4 | Popular (+35%) | Trap Pick | 52 |
| C | 71% | Kiriko | -2.51% | -3.31% ±1.7 | Standard (-12%) | Unfavorable | 52 |
| C | 62% | Mizuki | -2.52% | -3.30% ±2.1 | Standard (-18%) | Unfavorable | 52 |
| C | 43% | Bastion | -2.94% | -5.61% ±3.4 | Standard (+16%) | Unfavorable | 52 |
| D | 53% | Reinhardt | -3.10% | -3.89% ±3.3 | Niche (-25%) | Deterrent | 50 |
| D | 87% | Lúcio | -4.80% | -5.30% ±3.4 | Niche (-53%) | Deterrent | 48 |

### Runasapi

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| S | 76% | Reinhardt | +3.58% | +3.92% ±1.7 | Standard (+7%) | Favorable | 51 |
| A | 64% | Soldier: 76 | +2.10% | +3.96% ±2.6 | Map Priority (+66%) | Meta | 52 |
| A | 70% | Kiriko | +1.97% | +3.12% ±2.1 | Standard (+17%) | Favorable | 52 |
| A | 64% | Junker Queen | +1.80% | +2.06% ±1.9 | Popular (+28%) | Meta | 50 |
| A | 54% | Mauga | +1.48% | +2.44% ±2.4 | Popular (+41%) | Meta | 50 |
| A | 51% | Mizuki | +1.38% | +2.02% ±2.5 | Standard (+18%) | Favorable | 52 |
| B | 59% | Lúcio | +0.99% | +1.13% ±1.7 | Popular (+48%) | Neutral | 51 |
| B | 59% | Wrecking Ball | +0.90% | +1.31% ±2.4 | Popular (+22%) | Neutral | 51 |
| B | 51% | Domina | +0.89% | +1.84% ±3.4 | Niche (-21%) | Neutral | 49 |
| B | 67% | Anran | +0.86% | +1.31% ±1.8 | Standard (+8%) | Neutral | 49 |
| B | 58% | Torbjörn | +0.74% | +1.17% ±3.0 | Standard (-15%) | Neutral | 49 |
| B | 64% | Vendetta | +0.74% | +1.78% ±3.0 | Standard (+12%) | Neutral | 48 |
| B | 60% | Doctrine *(provisional)* | +0.64% | +1.04% ±3.1 | Standard (+1%) | Neutral | 8 |
| B | 69% | Mei | +0.61% | +2.32% ±2.7 | Niche (-29%) | Neutral | 50 |
| B | 68% | Bastion | +0.55% | +0.82% ±2.6 | Standard (-16%) | Neutral | 48 |
| B | 68% | D.Mon | +0.55% | +1.42% ±2.9 | Standard (+17%) | Neutral | 16 |
| B | 73% | Wuyang | +0.44% | +1.27% ±2.7 | Standard (+9%) | Neutral | 52 |
| B | 88% | Tracer | +0.29% | +0.51% ±1.6 | Popular (+33%) | Neutral | 52 |
| B | 86% | Zarya | +0.29% | +0.45% ±1.6 | Standard (+2%) | Neutral | 50 |
| B | 76% | Sierra | +0.22% | +1.17% ±2.8 | Standard (-8%) | Neutral | 33 |
| B | 61% | Jetpack Cat | +0.15% | +0.37% ±3.4 | Standard (+6%) | Neutral | 52 |
| B | 78% | Lifeweaver | +0.13% | +2.69% ±2.6 | Standard (-16%) | Neutral | 50 |
| B | 87% | Juno | +0.09% | +1.82% ±1.8 | Popular (+26%) | Neutral | 51 |
| B | 72% | Venture | +0.04% | +1.76% ±3.5 | Standard (-6%) | Neutral | 51 |
| B | 75% | Cassidy | -0.03% | +0.39% ±3.0 | Standard (+12%) | Neutral | 52 |
| B | 91% | Genji | -0.05% | +0.74% ±1.6 | Standard (-11%) | Neutral | 51 |
| B | 78% | Illari | -0.11% | +0.21% ±2.7 | Standard (-17%) | Neutral | 51 |
| B | 80% | Emre | -0.24% | +0.15% ±2.3 | Standard (-5%) | Neutral | 52 |
| B | 73% | D.Va | -0.28% | +0.30% ±3.0 | Standard (+0%) | Neutral | 52 |
| B | 98% | Sojourn | -0.28% | -0.26% ±1.0 | Standard (+15%) | Neutral | 52 |
| B | 71% | Winston | -0.31% | -0.12% ±2.3 | Standard (-14%) | Neutral | 52 |
| B | 70% | Brigitte | -0.34% | -0.20% ±2.9 | Standard (+11%) | Neutral | 52 |
| B | 71% | Reaper | -0.42% | -0.47% ±3.0 | Standard (-9%) | Neutral | 51 |
| B | 48% | Roadhog *(provisional)* | -0.52% | -0.78% ±6.5 | Standard (-1%) | Neutral | 8 |
| B | 69% | Orisa | -0.53% | -0.81% ±2.6 | Standard (+3%) | Neutral | 51 |
| B | 73% | Doomfist | -0.55% | -0.95% ±2.4 | Standard (+2%) | Neutral | 51 |
| B | 62% | Symmetra | -0.58% | -0.63% ±3.0 | Niche (-27%) | Neutral | 44 |
| B | 69% | Baptiste | -0.64% | -0.73% ±2.6 | Niche (-33%) | Neutral | 50 |
| B | 68% | Hazard | -0.64% | -0.66% ±2.2 | Standard (+9%) | Neutral | 50 |
| B | 77% | Shion | -0.75% | -1.01% ±1.3 | Popular (+40%) | Neutral | 28 |
| B | 64% | Ashe | -0.76% | -0.74% ±2.8 | Niche (-55%) | Neutral | 51 |
| B | 63% | Junkrat | -0.77% | -0.99% ±2.4 | Niche (-32%) | Neutral | 47 |
| B | 59% | Mercy | -0.94% | -2.08% ±2.7 | Niche (-21%) | Neutral | 49 |
| B | 57% | Zenyatta | -0.97% | -1.72% ±2.9 | Niche (-35%) | Neutral | 52 |
| C | 45% | Moira | -1.24% | -1.41% ±3.0 | Standard (+11%) | Unfavorable | 51 |
| C | 39% | Sombra *(provisional)* | -1.32% | -1.91% ±4.7 | Standard (+19%) | Unfavorable | 8 |
| C | 48% | Pharah | -1.33% | -1.43% ±2.5 | Niche (-30%) | Deterrent | 48 |
| C | 55% | Echo | -1.60% | -2.34% ±2.8 | Niche (-37%) | Deterrent | 51 |
| C | 56% | Hanzo | -1.74% | -3.27% ±3.2 | Niche (-58%) | Deterrent | 50 |
| C | 53% | Ramattra | -1.90% | -2.53% ±3.0 | Standard (-11%) | Unfavorable | 51 |
| C | 61% | Freja | -2.38% | -4.45% ±2.8 | Niche (-33%) | Deterrent | 50 |
| D | 78% | Ana | -3.79% | -4.60% ±2.3 | Niche (-24%) | Deterrent | 52 |
| D | 83% | Sigma | -4.13% | -4.46% ±2.4 | Niche (-32%) | Deterrent | 52 |
| D | 100% | Widowmaker | -16.67% | -17.19% ±3.1 | Niche (-62%) | Deterrent | 52 |

### Samoa

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| A | 83% | Symmetra | +1.93% | +2.20% ±1.3 | Popular (+31%) | Meta | 51 |
| A | 60% | Torbjörn | +1.77% | +2.31% ±2.3 | Standard (-1%) | Favorable | 52 |
| A | 74% | Mizuki | +1.55% | +1.69% ±1.1 | Popular (+23%) | Meta | 52 |
| A | 77% | Cassidy | +1.51% | +1.74% ±0.9 | Popular (+27%) | Meta | 52 |
| A | 57% | Moira | +1.43% | +2.19% ±1.9 | Popular (+22%) | Meta | 52 |
| B | 57% | Tracer | +1.12% | +1.25% ±0.8 | Popular (+26%) | Neutral | 52 |
| B | 55% | Anran | +1.05% | +2.23% ±2.6 | Standard (+18%) | Neutral | 51 |
| B | 64% | Wuyang | +0.97% | +1.41% ±1.4 | Standard (+6%) | Neutral | 52 |
| B | 66% | Junker Queen | +0.77% | +0.94% ±1.9 | Popular (+30%) | Neutral | 51 |
| B | 78% | Zarya | +0.65% | +0.83% ±1.5 | Popular (+21%) | Neutral | 52 |
| B | 70% | Ramattra | +0.60% | +1.05% ±2.2 | Standard (+8%) | Neutral | 50 |
| B | 94% | Kiriko | +0.51% | +0.57% ±0.9 | Standard (+9%) | Neutral | 52 |
| B | 71% | Hazard | +0.49% | +0.79% ±2.3 | Standard (+5%) | Neutral | 52 |
| B | 72% | Mauga | +0.49% | +0.96% ±2.3 | Popular (+22%) | Neutral | 50 |
| B | 91% | Shion | +0.49% | +0.80% ±1.1 | Popular (+28%) | Neutral | 28 |
| B | 81% | Bastion | +0.47% | +0.57% ±1.7 | Standard (-9%) | Neutral | 50 |
| B | 86% | Reinhardt | +0.39% | +0.45% ±1.4 | Standard (+12%) | Neutral | 52 |
| B | 87% | Sojourn | +0.39% | +0.68% ±1.6 | Standard (+8%) | Neutral | 52 |
| B | 95% | Doomfist | +0.32% | +0.52% ±1.1 | Standard (+6%) | Neutral | 52 |
| B | 82% | Orisa | +0.29% | +0.43% ±1.9 | Standard (+16%) | Neutral | 52 |
| B | 86% | Sierra | +0.22% | -0.60% ±1.8 | Standard (-15%) | Neutral | 32 |
| B | 95% | Emre | +0.21% | +0.80% ±1.2 | Standard (-17%) | Neutral | 52 |
| B | 80% | Baptiste | +0.15% | +1.03% ±2.4 | Standard (-16%) | Neutral | 51 |
| B | 89% | Lifeweaver | +0.13% | +2.17% ±1.7 | Standard (-15%) | Neutral | 51 |
| B | 80% | Lúcio | +0.13% | +0.25% ±1.9 | Popular (+33%) | Neutral | 52 |
| B | 95% | Illari | +0.08% | +0.38% ±1.3 | Niche (-22%) | Neutral | 52 |
| B | 64% | Domina | +0.07% | +0.51% ±3.0 | Standard (-16%) | Neutral | 51 |
| B | 80% | Venture | +0.04% | -0.23% ±2.5 | Standard (+9%) | Neutral | 51 |
| B | 51% | Roadhog *(provisional)* | -0.16% | +0.42% ±6.2 | Standard (+0%) | Neutral | 8 |
| B | 88% | Hanzo | -0.19% | -0.10% ±1.7 | Niche (-41%) | Neutral | 51 |
| B | 85% | Brigitte | -0.30% | -0.24% ±1.7 | Standard (+13%) | Neutral | 52 |
| B | 80% | Genji | -0.30% | -2.11% ±2.3 | Standard (-12%) | Neutral | 52 |
| B | 75% | Mei | -0.39% | -0.84% ±2.5 | Standard (-9%) | Neutral | 51 |
| B | 91% | Ashe | -0.41% | -0.21% ±1.2 | Niche (-44%) | Neutral | 52 |
| B | 88% | Zenyatta | -0.46% | -0.46% ±1.3 | Standard (-20%) | Neutral | 52 |
| B | 68% | D.Mon | -0.61% | -0.79% ±2.6 | Popular (+20%) | Neutral | 16 |
| B | 77% | Mercy | -0.65% | -0.90% ±1.7 | Niche (-21%) | Neutral | 50 |
| B | 69% | Reaper | -0.69% | -0.98% ±2.5 | Popular (+22%) | Neutral | 52 |
| B | 66% | Vendetta | -0.69% | -1.23% ±2.9 | Standard (+6%) | Neutral | 48 |
| B | 66% | Juno | -0.75% | -1.50% ±2.6 | Standard (+2%) | Neutral | 52 |
| B | 55% | Freja | -1.05% | -1.49% ±2.5 | Niche (-33%) | Neutral | 52 |
| B | 57% | Soldier: 76 | -1.08% | -1.23% ±1.4 | Standard (-13%) | Neutral | 52 |
| C | 53% | Sigma | -1.28% | -1.26% ±1.5 | Niche (-25%) | Deterrent | 52 |
| C | 54% | Echo | -1.33% | -1.58% ±1.9 | Niche (-32%) | Deterrent | 52 |
| C | 67% | D.Va | -1.50% | -1.94% ±1.4 | Standard (-16%) | Unfavorable | 52 |
| C | 72% | Wrecking Ball | -1.55% | -1.64% ±1.2 | Standard (+5%) | Unfavorable | 51 |
| C | 57% | Pharah | -1.66% | -1.82% ±2.3 | Standard (-14%) | Unfavorable | 51 |
| C | 63% | Junkrat | -1.76% | -2.16% ±2.0 | Standard (-8%) | Unfavorable | 51 |
| C | 54% | Jetpack Cat | -1.81% | -2.38% ±2.7 | Standard (-6%) | Unfavorable | 52 |
| C | 93% | Ana | -2.00% | -2.07% ±1.0 | Standard (-14%) | Unfavorable | 52 |
| C | 44% | Sombra *(provisional)* | -2.05% | -3.45% ±4.5 | Standard (+9%) | Unfavorable | 8 |
| C | 53% | Doctrine *(provisional)* | -2.21% | -3.34% ±3.0 | Standard (-2%) | Unfavorable | 8 |
| C | 53% | Winston | -2.90% | -2.96% ±1.6 | Niche (-30%) | Deterrent | 52 |
| D | 100% | Widowmaker | -6.71% | -6.74% ±1.9 | Niche (-71%) | Deterrent | 44 |

### Shambali Monastery

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| S | 73% | Reinhardt | +3.89% | +5.15% ±3.2 | Popular (+37%) | Meta | 51 |
| A | 63% | Mizuki | +2.45% | +3.25% ±2.1 | Standard (-12%) | Favorable | 51 |
| A | 57% | Ramattra | +2.31% | +3.72% ±2.6 | Map Priority (+88%) | Meta | 51 |
| A | 52% | Sigma | +1.71% | +2.22% ±2.5 | Map Priority (+53%) | Meta | 52 |
| A | 44% | Doctrine *(provisional)* | +1.55% | +3.04% ±3.9 | Standard (+5%) | Favorable | 8 |
| A | 54% | Bastion | +1.48% | +2.11% ±2.4 | Popular (+28%) | Meta | 50 |
| A | 50% | Junkrat | +1.36% | +1.80% ±2.3 | Popular (+44%) | Meta | 49 |
| A | 53% | Wuyang | +1.33% | +2.64% ±2.2 | Standard (+16%) | Favorable | 52 |
| B | 56% | Orisa | +1.07% | +1.50% ±2.0 | Popular (+21%) | Neutral | 52 |
| B | 57% | Pharah | +0.72% | +1.49% ±3.1 | Popular (+34%) | Neutral | 52 |
| B | 58% | Jetpack Cat | +0.65% | +1.06% ±3.1 | Standard (-1%) | Neutral | 52 |
| B | 68% | Mei | +0.65% | +2.41% ±2.7 | Popular (+39%) | Neutral | 51 |
| B | 75% | Echo | +0.31% | +0.92% ±2.5 | Map Priority (+51%) | Neutral | 52 |
| B | 84% | Sierra | +0.22% | -0.75% ±2.0 | Standard (+13%) | Neutral | 36 |
| B | 88% | Hanzo | +0.21% | +0.42% ±1.7 | Popular (+26%) | Neutral | 51 |
| B | 76% | Lifeweaver | +0.13% | -2.92% ±2.9 | Standard (+19%) | Neutral | 50 |
| B | 77% | Baptiste | +0.12% | +1.32% ±2.8 | Popular (+32%) | Neutral | 52 |
| B | 77% | Reaper | +0.12% | +0.74% ±2.8 | Standard (-15%) | Neutral | 51 |
| B | 70% | Vendetta | +0.09% | +0.60% ±3.8 | Standard (-3%) | Neutral | 42 |
| B | 79% | Sojourn | +0.05% | +0.51% ±2.6 | Standard (+4%) | Neutral | 52 |
| B | 74% | Venture | +0.04% | +2.01% ±3.1 | Standard (+18%) | Neutral | 48 |
| B | 75% | D.Va | -0.02% | +1.09% ±3.0 | Niche (-31%) | Neutral | 51 |
| B | 72% | Freja | -0.07% | +0.78% ±3.5 | Standard (+16%) | Neutral | 51 |
| B | 76% | Illari | -0.08% | +0.47% ±2.9 | Popular (+28%) | Neutral | 52 |
| B | 73% | Anran | -0.11% | +0.12% ±3.3 | Standard (+1%) | Neutral | 49 |
| B | 78% | Genji | -0.15% | +0.15% ±2.5 | Standard (-6%) | Neutral | 52 |
| B | 60% | Wrecking Ball | -0.21% | -0.07% ±3.6 | Niche (-25%) | Neutral | 51 |
| B | 77% | Shion | -0.23% | -0.15% ±2.6 | Standard (-15%) | Neutral | 28 |
| B | 79% | Emre | -0.26% | +0.08% ±2.4 | Standard (+17%) | Neutral | 52 |
| B | 76% | Kiriko | -0.42% | -0.62% ±2.4 | Standard (-13%) | Neutral | 52 |
| B | 62% | Brigitte | -0.50% | -0.47% ±3.6 | Niche (-29%) | Neutral | 51 |
| B | 68% | Juno | -0.57% | -0.38% ±3.1 | Standard (+4%) | Neutral | 52 |
| B | 63% | D.Mon | -0.66% | -1.03% ±3.5 | Standard (+15%) | Neutral | 16 |
| B | 68% | Ashe | -0.70% | -0.55% ±2.5 | Standard (+19%) | Neutral | 52 |
| B | 63% | Doomfist | -0.70% | -2.10% ±3.6 | Standard (-13%) | Neutral | 52 |
| B | 57% | Moira | -0.77% | -0.52% ±3.5 | Standard (-10%) | Neutral | 50 |
| B | 62% | Mercy | -0.81% | -2.00% ±3.1 | Standard (+10%) | Neutral | 49 |
| B | 54% | Hazard | -0.82% | -1.00% ±3.4 | Niche (-35%) | Neutral | 51 |
| B | 50% | Zarya | -1.09% | -1.19% ±3.0 | Standard (+15%) | Neutral | 52 |
| B | 49% | Torbjörn | -1.13% | -1.73% ±3.1 | Standard (+5%) | Neutral | 50 |
| B | 51% | Zenyatta | -1.18% | -1.80% ±2.2 | Popular (+22%) | Neutral | 52 |
| C | 43% | Ana | -1.22% | -1.50% ±2.8 | Standard (+7%) | Unfavorable | 52 |
| C | 38% | Domina | -1.25% | -1.33% ±3.9 | Popular (+30%) | Trap Pick | 52 |
| C | 32% | Roadhog *(provisional)* | -1.25% | -9.33% ±12.8 | Standard (-20%) | Unfavorable | 8 |
| C | 49% | Cassidy | -1.27% | -2.48% ±2.7 | Standard (-14%) | Unfavorable | 52 |
| C | 41% | Symmetra | -1.28% | -2.10% ±4.0 | Standard (-1%) | Unfavorable | 49 |
| C | 36% | Junker Queen | -1.45% | -1.60% ±4.2 | Standard (-9%) | Unfavorable | 46 |
| C | 57% | Soldier: 76 | -1.50% | -2.26% ±2.4 | Standard (-19%) | Unfavorable | 52 |
| C | 63% | Tracer | -1.53% | -1.96% ±1.9 | Niche (-32%) | Deterrent | 52 |
| C | 36% | Sombra *(provisional)* | -1.59% | -3.88% ±7.3 | Standard (-15%) | Unfavorable | 8 |
| C | 54% | Widowmaker | -1.60% | -1.53% ±2.2 | Standard (+8%) | Unfavorable | 50 |
| C | 54% | Mauga | -1.70% | -2.42% ±2.9 | Standard (-11%) | Unfavorable | 49 |
| D | 72% | Lúcio | -3.98% | -4.37% ±3.6 | Niche (-41%) | Deterrent | 49 |
| D | 99% | Winston | -5.17% | -5.41% ±1.8 | Niche (-46%) | Deterrent | 51 |

### Suravasa

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| S | 81% | Lúcio | +3.70% | +3.93% ±1.6 | Map Priority (+74%) | Meta | 51 |
| A | 65% | Symmetra | +2.48% | +3.24% ±1.9 | Standard (-4%) | Favorable | 49 |
| A | 53% | Junker Queen | +2.33% | +2.93% ±2.6 | Popular (+47%) | Meta | 50 |
| A | 62% | Wrecking Ball | +2.19% | +2.94% ±2.3 | Popular (+24%) | Meta | 52 |
| A | 69% | Jetpack Cat | +2.09% | +2.49% ±1.9 | Standard (+3%) | Favorable | 51 |
| A | 60% | Domina | +1.97% | +2.63% ±2.3 | Niche (-25%) | Specialist | 51 |
| A | 64% | Pharah | +1.71% | +2.16% ±1.9 | Standard (-19%) | Favorable | 51 |
| A | 59% | Ramattra | +1.66% | +2.47% ±2.2 | Standard (-10%) | Favorable | 50 |
| A | 62% | Kiriko | +1.61% | +2.69% ±2.2 | Standard (+17%) | Favorable | 52 |
| B | 51% | Brigitte | +1.17% | +1.94% ±2.3 | Standard (+16%) | Neutral | 52 |
| B | 61% | Anran | +0.88% | +2.01% ±2.8 | Standard (+19%) | Neutral | 52 |
| B | 71% | Mauga | +0.82% | +1.05% ±1.4 | Popular (+29%) | Neutral | 51 |
| B | 88% | Sojourn | +0.76% | +0.86% ±0.8 | Standard (+20%) | Neutral | 52 |
| B | 84% | Soldier: 76 | +0.67% | +0.82% ±1.1 | Popular (+20%) | Neutral | 51 |
| B | 58% | Reinhardt | +0.66% | +0.93% ±2.9 | Standard (+2%) | Neutral | 52 |
| B | 92% | Shion | +0.58% | +0.80% ±0.9 | Popular (+38%) | Neutral | 28 |
| B | 69% | Winston | +0.55% | +0.80% ±2.2 | Standard (-16%) | Neutral | 52 |
| B | 82% | Hazard | +0.35% | +0.51% ±1.8 | Standard (+15%) | Neutral | 51 |
| B | 86% | Reaper | +0.35% | +0.69% ±1.7 | Popular (+21%) | Neutral | 52 |
| B | 97% | Tracer | +0.27% | +0.37% ±1.0 | Popular (+31%) | Neutral | 52 |
| B | 83% | Sierra | +0.22% | +2.03% ±2.0 | Standard (-14%) | Neutral | 33 |
| B | 83% | Echo | +0.20% | +0.53% ±2.0 | Niche (-36%) | Neutral | 52 |
| B | 90% | Lifeweaver | +0.13% | -1.57% ±1.6 | Niche (-22%) | Neutral | 51 |
| B | 79% | Vendetta | +0.05% | +0.25% ±2.5 | Standard (+17%) | Neutral | 48 |
| B | 79% | D.Mon | +0.04% | +0.32% ±2.4 | Standard (+11%) | Neutral | 16 |
| B | 78% | Venture | +0.04% | -1.12% ±2.7 | Standard (+7%) | Neutral | 51 |
| B | 72% | Torbjörn | +0.03% | +0.06% ±2.5 | Standard (-4%) | Neutral | 52 |
| B | 79% | Doomfist | -0.01% | +0.47% ±2.5 | Standard (+9%) | Neutral | 52 |
| B | 90% | Genji | -0.03% | +1.04% ±1.7 | Standard (-2%) | Neutral | 51 |
| B | 56% | Sombra *(provisional)* | -0.05% | +0.95% ±4.5 | Standard (+17%) | Neutral | 8 |
| B | 86% | Mei | -0.10% | -0.04% ±1.9 | Niche (-21%) | Neutral | 52 |
| B | 85% | Illari | -0.15% | -0.09% ±2.0 | Niche (-30%) | Neutral | 52 |
| B | 84% | Bastion | -0.21% | -0.27% ±1.8 | Niche (-24%) | Neutral | 49 |
| B | 67% | Orisa | -0.32% | -0.57% ±3.4 | Standard (+7%) | Neutral | 52 |
| B | 81% | Wuyang | -0.33% | -0.45% ±2.1 | Standard (+3%) | Neutral | 52 |
| B | 64% | Doctrine *(provisional)* | -0.36% | -0.51% ±3.0 | Standard (-3%) | Neutral | 8 |
| B | 82% | Emre | -0.42% | -0.61% ±1.8 | Niche (-27%) | Neutral | 52 |
| B | 50% | Roadhog *(provisional)* | -0.43% | -0.48% ±6.1 | Standard (+6%) | Neutral | 8 |
| B | 73% | Zenyatta | -0.47% | -0.49% ±2.6 | Niche (-33%) | Neutral | 52 |
| B | 80% | Moira | -0.55% | -0.44% ±1.6 | Popular (+38%) | Neutral | 51 |
| B | 67% | Juno | -0.60% | -0.58% ±3.1 | Standard (+4%) | Neutral | 52 |
| B | 70% | Mercy | -0.63% | -1.14% ±2.4 | Niche (-25%) | Neutral | 51 |
| B | 93% | Cassidy | -0.67% | -0.70% ±0.7 | Standard (+20%) | Neutral | 52 |
| B | 68% | Ashe | -0.81% | -0.87% ±1.9 | Niche (-64%) | Neutral | 51 |
| B | 59% | Zarya | -0.90% | -0.91% ±2.3 | Standard (+7%) | Neutral | 52 |
| B | 56% | Hanzo | -0.96% | -1.61% ±3.3 | Niche (-49%) | Neutral | 52 |
| B | 60% | Junkrat | -0.98% | -1.15% ±1.8 | Standard (-19%) | Neutral | 50 |
| B | 54% | Mizuki | -1.11% | -1.34% ±1.7 | Popular (+33%) | Neutral | 52 |
| B | 51% | Baptiste | -1.18% | -1.79% ±2.1 | Niche (-30%) | Neutral | 52 |
| C | 64% | Freja | -1.87% | -3.08% ±2.5 | Niche (-38%) | Deterrent | 52 |
| C | 77% | D.Va | -2.38% | -3.38% ±1.6 | Standard (-6%) | Unfavorable | 52 |
| C | 54% | Ana | -2.91% | -3.18% ±1.5 | Niche (-28%) | Deterrent | 52 |
| D | 90% | Sigma | -4.30% | -4.56% ±2.1 | Niche (-44%) | Deterrent | 52 |
| D | 100% | Widowmaker | -11.90% | -12.04% ±2.1 | Niche (-79%) | Deterrent | 44 |

### Watchpoint Gibraltar

| Tier | P(tier) | Hero | Delta WR | Raw (95% range) | Presence | Archetype | n |
|---|---|---|---|---|---|---|---|
| A | 56% | Winston | +2.74% | +3.11% ±1.9 | Map Priority (+135%) | Meta | 52 |
| A | 52% | Wrecking Ball | +2.38% | +3.74% ±3.0 | Standard (+8%) | Favorable | 51 |
| A | 78% | Ana | +2.11% | +2.38% ±1.5 | Popular (+24%) | Meta | 52 |
| A | 52% | Junkrat | +1.74% | +2.61% ±2.9 | Standard (+9%) | Favorable | 50 |
| A | 57% | Hazard | +1.50% | +1.97% ±2.0 | Map Priority (+53%) | Meta | 52 |
| A | 55% | Mercy | +1.39% | +3.22% ±2.3 | Popular (+21%) | Meta | 51 |
| A | 53% | D.Va | +1.32% | +3.08% ±2.0 | Popular (+47%) | Meta | 51 |
| B | 52% | Brigitte | +1.13% | +1.79% ±2.1 | Map Priority (+61%) | Neutral | 52 |
| B | 64% | Baptiste | +0.90% | +2.10% ±1.9 | Standard (+1%) | Neutral | 52 |
| B | 63% | Freja | +0.80% | +2.33% ±2.8 | Popular (+31%) | Neutral | 52 |
| B | 45% | Roadhog *(provisional)* | +0.71% | +5.12% ±8.2 | Standard (+9%) | Neutral | 7 |
| B | 76% | Bastion | +0.46% | +0.61% ±2.1 | Standard (-1%) | Neutral | 50 |
| B | 86% | Tracer | +0.44% | +0.68% ±1.5 | Standard (+10%) | Neutral | 52 |
| B | 87% | Ashe | +0.34% | +1.39% ±1.6 | Map Priority (+83%) | Neutral | 52 |
| B | 81% | Sierra | +0.22% | -0.26% ±2.3 | Standard (+9%) | Neutral | 36 |
| B | 69% | Anran | +0.15% | +1.05% ±4.1 | Standard (-15%) | Neutral | 49 |
| B | 71% | Lifeweaver | +0.13% | -0.60% ±3.6 | Popular (+31%) | Neutral | 52 |
| B | 81% | Echo | +0.11% | +0.45% ±2.1 | Popular (+21%) | Neutral | 52 |
| B | 53% | Doctrine *(provisional)* | +0.10% | +0.39% ±5.3 | Standard (-3%) | Neutral | 8 |
| B | 72% | Venture | +0.04% | -2.05% ±3.5 | Standard (-3%) | Neutral | 50 |
| B | 89% | Illari | +0.03% | +0.42% ±1.7 | Standard (+16%) | Neutral | 52 |
| B | 92% | Cassidy | +0.02% | +0.15% ±1.5 | Standard (-14%) | Neutral | 52 |
| B | 72% | Shion | -0.02% | +0.96% ±3.5 | Niche (-40%) | Neutral | 28 |
| B | 96% | Genji | -0.07% | +0.38% ±1.3 | Popular (+21%) | Neutral | 52 |
| B | 87% | Emre | -0.09% | +0.54% ±1.9 | Standard (+11%) | Neutral | 52 |
| B | 65% | Jetpack Cat | -0.13% | -0.08% ±3.0 | Standard (+20%) | Neutral | 52 |
| B | 75% | Mei | -0.23% | -0.41% ±2.9 | Niche (-37%) | Neutral | 47 |
| B | 67% | Soldier: 76 | -0.32% | -0.26% ±3.8 | Standard (-5%) | Neutral | 52 |
| B | 71% | Doomfist | -0.53% | -1.03% ±2.8 | Standard (+0%) | Neutral | 52 |
| B | 65% | Juno | -0.60% | -0.55% ±3.6 | Standard (-18%) | Neutral | 49 |
| B | 78% | Widowmaker | -0.62% | -0.58% ±1.4 | Map Priority (+52%) | Neutral | 51 |
| B | 78% | Wuyang | -0.64% | -0.86% ±1.6 | Niche (-29%) | Neutral | 52 |
| B | 76% | Kiriko | -0.65% | -0.83% ±1.7 | Standard (-4%) | Neutral | 52 |
| B | 66% | Hanzo | -0.66% | -0.86% ±2.8 | Standard (+13%) | Neutral | 52 |
| B | 55% | Pharah | -0.75% | -0.62% ±3.4 | Niche (-37%) | Neutral | 51 |
| B | 62% | Mizuki | -0.87% | -1.17% ±2.2 | Niche (-25%) | Neutral | 52 |
| B | 54% | D.Mon | -0.88% | -2.30% ±5.1 | Niche (-40%) | Neutral | 16 |
| B | 55% | Reaper | -1.05% | -1.70% ±2.5 | Standard (+17%) | Neutral | 52 |
| B | 48% | Moira | -1.13% | -1.27% ±4.1 | Niche (-37%) | Neutral | 52 |
| C | 44% | Ramattra | -1.33% | -1.70% ±3.4 | Niche (-69%) | Deterrent | 18 |
| C | 53% | Sojourn | -1.33% | -2.00% ±2.2 | Niche (-52%) | Deterrent | 52 |
| C | 53% | Zenyatta | -1.45% | -2.97% ±2.9 | Niche (-23%) | Deterrent | 52 |
| C | 36% | Sombra *(provisional)* | -1.50% | -3.33% ±7.0 | Standard (-1%) | Unfavorable | 8 |
| C | 48% | Torbjörn | -1.59% | -2.47% ±3.2 | Standard (+5%) | Unfavorable | 52 |
| C | 54% | Vendetta | -1.69% | -4.45% ±3.8 | Standard (-1%) | Unfavorable | 46 |
| C | 35% | Junker Queen | -1.73% | -2.10% ±4.9 | Niche (-49%) | Deterrent | 38 |
| C | 55% | Orisa | -2.10% | -4.26% ±3.4 | Niche (-50%) | Deterrent | 52 |
| C | 53% | Mauga | -2.11% | -3.49% ±3.4 | Niche (-26%) | Deterrent | 49 |
| C | 50% | Symmetra | -2.32% | -3.86% ±3.5 | Niche (-31%) | Deterrent | 47 |
| D | 59% | Domina | -3.36% | -4.66% ±3.8 | Niche (-44%) | Deterrent | 42 |
| D | 77% | Zarya | -3.91% | -5.36% ±3.0 | Niche (-59%) | Deterrent | 52 |
| D | 94% | Reinhardt | -5.22% | -6.58% ±3.2 | Niche (-52%) | Deterrent | 48 |
| D | 99% | Lúcio | -6.19% | -6.78% ±3.0 | Niche (-54%) | Deterrent | 47 |
| D | 100% | Sigma | -6.74% | -7.53% ±2.6 | Niche (-44%) | Deterrent | 52 |

