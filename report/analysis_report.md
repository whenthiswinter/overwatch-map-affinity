# Overwatch Map Affinity Report

Timeless per-hero, per-map win rate deltas, computed relative to each hero's baseline win rate in the same rank/region/patch slice, then averaged across every slice collected. Each average is then adjusted for noise: pulled toward the hero's mean in proportion to how much its slices disagree, so thin or inconsistent numbers don't land in extreme tiers by chance. The raw average and its 95% range are listed next to it.

## Contents
1. [Map Sensitivity (Volatility)](#1-map-sensitivity-volatility)
2. [Rank Divergence](#2-rank-divergence)
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

## 2. Rank Divergence

Heroes whose map performance differs by 2.5% or more between Masters and GM+ (raw averages).

| Hero | Map | Masters | GM+ | Diff | Better In |
|---|---|---|---|---|---|
| Roadhog | numbani | +0.48% | -24.52% | -25.00% | Better in Masters |
| Roadhog | paraiso | +8.70% | -16.21% | -24.91% | Better in Masters |
| Lifeweaver | eichenwalde | -11.70% | +11.24% | +22.94% | Better in GM+ |
| Sierra | eichenwalde | -4.67% | +15.12% | +19.79% | Better in GM+ |
| Roadhog | hollywood | -4.26% | +13.06% | +17.32% | Better in GM+ |
| Sombra | circuit-royal | -5.72% | -22.67% | -16.95% | Better in Masters |
| Lúcio | grimsvotn | -2.72% | +13.79% | +16.51% | Better in GM+ |
| Sierra | paraiso | +4.55% | -11.22% | -15.77% | Better in Masters |
| Wrecking Ball | grimsvotn | -7.60% | +7.67% | +15.27% | Better in GM+ |
| Freja | eichenwalde | +6.08% | -7.29% | -13.37% | Better in Masters |
| Anran | grimsvotn | +0.08% | +13.14% | +13.06% | Better in GM+ |
| Roadhog | eichenwalde | +0.88% | +13.32% | +12.44% | Better in GM+ |
| Bastion | paraiso | +0.68% | +12.98% | +12.30% | Better in GM+ |
| Roadhog | junkertown | -7.95% | +4.04% | +11.99% | Better in GM+ |
| Reinhardt | eichenwalde | +1.30% | -10.47% | -11.77% | Better in Masters |
| Anran | paraiso | -0.75% | -12.28% | -11.53% | Better in Masters |
| Mei | paraiso | -3.41% | +8.06% | +11.47% | Better in GM+ |
| Illari | grimsvotn | +2.25% | -9.19% | -11.44% | Better in Masters |
| Juno | paraiso | +2.38% | -8.97% | -11.35% | Better in Masters |
| Freja | paraiso | +3.46% | -7.72% | -11.18% | Better in Masters |
| Doctrine | blizzard-world | +3.04% | +13.78% | +10.74% | Better in GM+ |
| Symmetra | paraiso | -2.83% | +7.17% | +10.00% | Better in GM+ |
| Soldier: 76 | eichenwalde | -4.47% | +5.52% | +9.99% | Better in GM+ |
| Symmetra | eichenwalde | -2.02% | -11.96% | -9.94% | Better in Masters |
| Mizuki | grimsvotn | +2.27% | +12.11% | +9.84% | Better in GM+ |
| Moira | grimsvotn | -0.47% | -10.15% | -9.68% | Better in Masters |
| Sombra | rialto | -4.37% | -14.02% | -9.65% | Better in Masters |
| Roadhog | watchpoint-gibraltar | +9.13% | -0.22% | -9.35% | Better in Masters |
| D.Va | eichenwalde | +3.75% | -5.60% | -9.35% | Better in Masters |
| Soldier: 76 | grimsvotn | -5.04% | +4.22% | +9.26% | Better in GM+ |
| Wrecking Ball | paraiso | -8.09% | +1.10% | +9.19% | Better in GM+ |
| Symmetra | grimsvotn | -2.30% | +6.78% | +9.08% | Better in GM+ |
| Junker Queen | havana | -2.48% | -11.41% | -8.93% | Better in Masters |
| Moira | route-66 | +1.18% | -7.68% | -8.86% | Better in Masters |
| Vendetta | esperanca | -2.48% | +6.23% | +8.71% | Better in GM+ |
| Sombra | numbani | -4.52% | +4.13% | +8.65% | Better in GM+ |
| Orisa | paraiso | -2.97% | +5.59% | +8.56% | Better in GM+ |
| Brigitte | grimsvotn | -1.94% | +6.59% | +8.53% | Better in GM+ |
| Zenyatta | eichenwalde | -6.19% | +2.33% | +8.52% | Better in GM+ |
| Torbjörn | neon-junction | -4.06% | +4.40% | +8.46% | Better in GM+ |
| Jetpack Cat | paraiso | +0.49% | +8.89% | +8.40% | Better in GM+ |
| Doctrine | eichenwalde | -4.63% | +3.75% | +8.38% | Better in GM+ |
| Wuyang | paraiso | -0.39% | -8.70% | -8.31% | Better in Masters |
| Orisa | watchpoint-gibraltar | -8.41% | -0.11% | +8.30% | Better in GM+ |
| Sierra | grimsvotn | +6.08% | -2.09% | -8.17% | Better in Masters |
| Doctrine | numbani | +1.12% | +9.28% | +8.16% | Better in GM+ |
| Reinhardt | midtown | +0.38% | -7.76% | -8.14% | Better in Masters |
| Shion | eichenwalde | +1.42% | -6.69% | -8.11% | Better in Masters |
| Roadhog | rialto | -5.40% | -13.41% | -8.01% | Better in Masters |
| Sombra | dorado | -3.39% | +4.58% | +7.97% | Better in GM+ |
| Mercy | paraiso | +1.35% | +9.22% | +7.87% | Better in GM+ |
| Ramattra | blizzard-world | -2.16% | -9.88% | -7.72% | Better in Masters |
| Roadhog | busan | +1.13% | +8.84% | +7.71% | Better in GM+ |
| Vendetta | dorado | +0.95% | -6.76% | -7.71% | Better in Masters |
| Doctrine | grimsvotn | +2.39% | -5.17% | -7.56% | Better in Masters |
| Echo | route-66 | +1.96% | -5.58% | -7.54% | Better in Masters |
| Freja | grimsvotn | -0.72% | -8.22% | -7.50% | Better in Masters |
| D.Mon | eichenwalde | +2.13% | +9.62% | +7.49% | Better in GM+ |
| Sierra | midtown | +3.04% | -4.39% | -7.43% | Better in Masters |
| D.Va | grimsvotn | +3.17% | -4.23% | -7.40% | Better in Masters |
| Junkrat | busan | -4.22% | -11.51% | -7.29% | Better in Masters |
| Doctrine | kings-row | -1.73% | -9.02% | -7.29% | Better in Masters |
| Pharah | numbani | -0.71% | -7.98% | -7.27% | Better in Masters |
| Hazard | paraiso | +1.52% | -5.55% | -7.07% | Better in Masters |
| Vendetta | colosseo | -0.11% | +6.96% | +7.07% | Better in GM+ |
| D.Va | junkertown | +2.71% | -4.33% | -7.04% | Better in Masters |
| Moira | eichenwalde | -4.98% | -11.96% | -6.98% | Better in Masters |
| Lifeweaver | blizzard-world | -3.34% | +3.63% | +6.97% | Better in GM+ |
| Roadhog | blizzard-world | -2.27% | +4.69% | +6.96% | Better in GM+ |
| Sombra | shambali-monastery | -0.42% | -7.35% | -6.93% | Better in Masters |
| Orisa | numbani | -6.56% | +0.36% | +6.92% | Better in GM+ |
| Zarya | eichenwalde | -2.19% | -9.11% | -6.92% | Better in Masters |
| Illari | paraiso | +0.15% | -6.76% | -6.91% | Better in Masters |
| Emre | busan | -0.42% | +6.47% | +6.89% | Better in GM+ |
| Widowmaker | new-junk-city | -14.42% | -21.24% | -6.82% | Better in Masters |
| Sojourn | eichenwalde | -3.89% | +2.91% | +6.80% | Better in GM+ |
| Jetpack Cat | grimsvotn | +1.28% | +8.06% | +6.78% | Better in GM+ |
| Wrecking Ball | eichenwalde | +1.40% | -5.28% | -6.68% | Better in Masters |
| Roadhog | new-queen-street | -2.40% | -8.96% | -6.56% | Better in Masters |
| D.Mon | havana | -0.43% | -6.95% | -6.52% | Better in Masters |
| Hazard | grimsvotn | -1.58% | +4.94% | +6.52% | Better in GM+ |
| Torbjörn | blizzard-world | -3.82% | -10.34% | -6.52% | Better in Masters |
| Roadhog | antarctic-peninsula | +3.00% | -3.46% | -6.46% | Better in Masters |
| Wrecking Ball | havana | -0.87% | -7.33% | -6.46% | Better in Masters |
| Roadhog | esperanca | -5.62% | +0.82% | +6.44% | Better in GM+ |
| Roadhog | grimsvotn | +4.85% | -1.48% | -6.33% | Better in Masters |
| Vendetta | eichenwalde | +3.59% | -2.74% | -6.33% | Better in Masters |
| Doomfist | grimsvotn | +2.68% | -3.59% | -6.27% | Better in Masters |
| Domina | new-junk-city | -1.43% | +4.82% | +6.25% | Better in GM+ |
| Symmetra | esperanca | -2.89% | +3.36% | +6.25% | Better in GM+ |
| Symmetra | circuit-royal | -0.58% | +5.67% | +6.25% | Better in GM+ |
| Pharah | blizzard-world | -6.72% | -0.48% | +6.24% | Better in GM+ |
| Reinhardt | hollywood | -6.42% | -12.63% | -6.21% | Better in Masters |
| Moira | havana | +0.74% | -5.44% | -6.18% | Better in Masters |
| Sierra | busan | -1.05% | -7.23% | -6.18% | Better in Masters |
| Freja | new-junk-city | -2.94% | -9.12% | -6.18% | Better in Masters |
| Anran | dorado | -4.06% | +2.10% | +6.16% | Better in GM+ |
| Reaper | paraiso | -0.75% | -6.91% | -6.16% | Better in Masters |
| Sierra | dorado | +0.29% | -5.87% | -6.16% | Better in Masters |
| Widowmaker | oasis | -12.46% | -18.59% | -6.13% | Better in Masters |
| Genji | midtown | +0.00% | +6.12% | +6.12% | Better in GM+ |
| Hanzo | lijiang-tower | +3.33% | -2.79% | -6.12% | Better in Masters |
| Roadhog | midtown | -4.92% | -11.03% | -6.11% | Better in Masters |
| Junker Queen | circuit-royal | -6.00% | -12.10% | -6.10% | Better in Masters |
| Doomfist | numbani | -4.71% | +1.36% | +6.07% | Better in GM+ |
| Venture | junkertown | -2.48% | +3.59% | +6.07% | Better in GM+ |
| Sombra | junkertown | +1.98% | -4.07% | -6.05% | Better in Masters |
| Emre | grimsvotn | +1.63% | -4.38% | -6.01% | Better in Masters |
| D.Mon | paraiso | +1.89% | -4.11% | -6.00% | Better in Masters |
| Sombra | new-queen-street | +1.38% | -4.62% | -6.00% | Better in Masters |
| Doomfist | eichenwalde | -1.68% | +4.30% | +5.98% | Better in GM+ |
| Winston | grimsvotn | -6.36% | -0.42% | +5.94% | Better in GM+ |
| Doctrine | neon-junction | +1.22% | -4.72% | -5.94% | Better in Masters |
| Sombra | route-66 | +4.73% | +10.63% | +5.90% | Better in GM+ |
| Mauga | dorado | -1.55% | +4.30% | +5.85% | Better in GM+ |
| Mauga | junkertown | +2.22% | -3.63% | -5.85% | Better in Masters |
| Vendetta | numbani | +0.50% | -5.32% | -5.82% | Better in Masters |
| Emre | junkertown | +2.42% | -3.37% | -5.79% | Better in Masters |
| Mei | dorado | -5.20% | +0.59% | +5.79% | Better in GM+ |
| Venture | runasapi | -1.08% | +4.71% | +5.79% | Better in GM+ |
| Venture | new-queen-street | +2.98% | -2.75% | -5.73% | Better in Masters |
| Sombra | grimsvotn | -1.07% | +4.65% | +5.72% | Better in GM+ |
| Jetpack Cat | havana | -3.38% | -9.09% | -5.71% | Better in Masters |
| D.Mon | blizzard-world | -0.53% | +5.17% | +5.70% | Better in GM+ |
| Hazard | midtown | -1.16% | -6.81% | -5.65% | Better in Masters |
| D.Mon | hollywood | -0.01% | -5.65% | -5.64% | Better in Masters |
| Soldier: 76 | circuit-royal | +0.27% | -5.37% | -5.64% | Better in Masters |
| Junkrat | new-junk-city | +1.78% | -3.86% | -5.64% | Better in Masters |
| Reaper | route-66 | -0.92% | -6.51% | -5.59% | Better in Masters |
| Hanzo | numbani | -3.80% | +1.78% | +5.58% | Better in GM+ |
| D.Mon | circuit-royal | -1.60% | -7.17% | -5.57% | Better in Masters |
| Doctrine | new-junk-city | -2.76% | +2.80% | +5.56% | Better in GM+ |
| Juno | eichenwalde | -3.77% | +1.76% | +5.53% | Better in GM+ |
| Mei | hollywood | -3.69% | +1.82% | +5.51% | Better in GM+ |
| D.Mon | rialto | -3.26% | +2.22% | +5.48% | Better in GM+ |
| Zarya | paraiso | -2.95% | -8.42% | -5.47% | Better in Masters |
| Wrecking Ball | busan | -2.58% | +2.87% | +5.45% | Better in GM+ |
| Hazard | eichenwalde | -3.28% | +2.17% | +5.45% | Better in GM+ |
| Vendetta | paraiso | -1.42% | +4.02% | +5.44% | Better in GM+ |
| Mercy | new-junk-city | -3.01% | +2.37% | +5.38% | Better in GM+ |
| Sombra | eichenwalde | +1.33% | -4.05% | -5.38% | Better in Masters |
| Echo | shambali-monastery | -1.77% | +3.60% | +5.37% | Better in GM+ |
| Echo | new-queen-street | +1.76% | -3.61% | -5.37% | Better in Masters |
| Soldier: 76 | hollywood | -0.99% | -6.36% | -5.37% | Better in Masters |
| Sigma | numbani | +1.34% | -4.01% | -5.35% | Better in Masters |
| Sombra | oasis | +2.33% | -3.02% | -5.35% | Better in Masters |
| Pharah | paraiso | -0.12% | +5.22% | +5.34% | Better in GM+ |
| Vendetta | watchpoint-gibraltar | -2.13% | -7.47% | -5.34% | Better in Masters |
| Sierra | junkertown | -0.86% | +4.45% | +5.31% | Better in GM+ |
| Sombra | hollywood | +0.84% | -4.47% | -5.31% | Better in Masters |
| Junkrat | midtown | -3.35% | +1.93% | +5.28% | Better in GM+ |
| Venture | grimsvotn | -0.75% | +4.53% | +5.28% | Better in GM+ |
| Doctrine | paraiso | +9.22% | +14.50% | +5.28% | Better in GM+ |
| Bastion | midtown | -2.97% | -8.22% | -5.25% | Better in Masters |
| D.Mon | runasapi | +4.04% | -1.20% | -5.24% | Better in Masters |
| Doctrine | oasis | -2.28% | -7.50% | -5.22% | Better in Masters |
| Vendetta | runasapi | -0.61% | +4.61% | +5.22% | Better in GM+ |
| D.Va | runasapi | -2.31% | +2.90% | +5.21% | Better in GM+ |
| Illari | runasapi | +2.76% | -2.45% | -5.21% | Better in Masters |
| Widowmaker | eichenwalde | -4.45% | +0.73% | +5.18% | Better in GM+ |
| Illari | neon-junction | -3.20% | +1.95% | +5.15% | Better in GM+ |
| Lifeweaver | paraiso | -1.55% | +3.60% | +5.15% | Better in GM+ |
| Domina | colosseo | -2.10% | -7.24% | -5.14% | Better in Masters |
| Mauga | blizzard-world | -2.78% | -7.92% | -5.14% | Better in Masters |
| Doomfist | paraiso | +0.47% | -4.67% | -5.14% | Better in Masters |
| Ramattra | eichenwalde | -2.51% | +2.63% | +5.14% | Better in GM+ |
| Sombra | watchpoint-gibraltar | -0.77% | -5.90% | -5.13% | Better in Masters |
| Domina | lijiang-tower | -0.29% | +4.84% | +5.13% | Better in GM+ |
| Ashe | paraiso | +2.42% | -2.70% | -5.12% | Better in Masters |
| Sombra | midtown | -5.97% | -0.85% | +5.12% | Better in GM+ |
| Domina | shambali-monastery | +1.22% | -3.88% | -5.10% | Better in Masters |
| Genji | havana | +2.87% | -2.23% | -5.10% | Better in Masters |
| Doomfist | midtown | -2.97% | +2.12% | +5.09% | Better in GM+ |
| Lúcio | shambali-monastery | -1.77% | -6.86% | -5.09% | Better in Masters |
| Mizuki | circuit-royal | -0.59% | +4.50% | +5.09% | Better in GM+ |
| Orisa | runasapi | -3.30% | +1.78% | +5.08% | Better in GM+ |
| Baptiste | numbani | -1.74% | -6.80% | -5.06% | Better in Masters |
| Bastion | junkertown | +1.55% | -3.51% | -5.06% | Better in Masters |
| Brigitte | rialto | -0.47% | +4.59% | +5.06% | Better in GM+ |
| Echo | junkertown | +1.49% | -3.56% | -5.05% | Better in Masters |
| Zarya | blizzard-world | -1.02% | -6.05% | -5.03% | Better in Masters |
| Bastion | hollywood | -3.30% | +1.72% | +5.02% | Better in GM+ |
| Ramattra | watchpoint-gibraltar | -3.10% | +1.92% | +5.02% | Better in GM+ |
| Jetpack Cat | runasapi | +2.87% | -2.14% | -5.01% | Better in Masters |
| Echo | grimsvotn | +0.12% | +5.10% | +4.98% | Better in GM+ |
| Junker Queen | paraiso | -6.97% | -1.99% | +4.98% | Better in GM+ |
| Doctrine | rialto | -0.91% | -5.87% | -4.96% | Better in Masters |
| D.Va | route-66 | +5.30% | +0.34% | -4.96% | Better in Masters |
| Hazard | shambali-monastery | -3.42% | +1.52% | +4.94% | Better in GM+ |
| Lifeweaver | new-junk-city | +2.65% | -2.29% | -4.94% | Better in Masters |
| Doctrine | dorado | +1.37% | +6.28% | +4.91% | Better in GM+ |
| Pharah | route-66 | +1.35% | -3.56% | -4.91% | Better in Masters |
| Mei | junkertown | -3.59% | +1.31% | +4.90% | Better in GM+ |
| Wrecking Ball | colosseo | +3.26% | -1.63% | -4.89% | Better in Masters |
| Baptiste | colosseo | +0.25% | -4.62% | -4.87% | Better in Masters |
| Zenyatta | new-queen-street | -1.16% | +3.69% | +4.85% | Better in GM+ |
| Orisa | new-queen-street | +0.19% | -4.65% | -4.84% | Better in Masters |
| Echo | samoa | -4.00% | +0.84% | +4.84% | Better in GM+ |
| Mei | new-queen-street | +1.30% | -3.54% | -4.84% | Better in Masters |
| Wuyang | junkertown | +0.39% | -4.44% | -4.83% | Better in Masters |
| Sierra | ilios | -1.97% | +2.84% | +4.81% | Better in GM+ |
| Wuyang | eichenwalde | +0.11% | +4.90% | +4.79% | Better in GM+ |
| Baptiste | paraiso | -4.08% | +0.70% | +4.78% | Better in GM+ |
| Pharah | grimsvotn | -1.51% | -6.28% | -4.77% | Better in Masters |
| Jetpack Cat | busan | +0.69% | -4.08% | -4.77% | Better in Masters |
| Junkrat | watchpoint-gibraltar | +0.33% | +5.08% | +4.75% | Better in GM+ |
| Torbjörn | esperanca | -0.80% | +3.95% | +4.75% | Better in GM+ |
| Juno | route-66 | -1.97% | +2.74% | +4.71% | Better in GM+ |
| Wrecking Ball | blizzard-world | -0.79% | +3.91% | +4.70% | Better in GM+ |
| Moira | esperanca | -0.97% | +3.72% | +4.69% | Better in GM+ |
| Ramattra | rialto | -2.89% | +1.80% | +4.69% | Better in GM+ |
| Doomfist | shambali-monastery | +0.24% | -4.44% | -4.68% | Better in Masters |
| Mizuki | new-junk-city | +0.87% | +5.55% | +4.68% | Better in GM+ |
| Moira | rialto | -3.30% | +1.38% | +4.68% | Better in GM+ |
| Juno | numbani | -0.23% | -4.90% | -4.67% | Better in Masters |
| Torbjörn | runasapi | +3.36% | -1.31% | -4.67% | Better in Masters |
| D.Mon | kings-row | -0.61% | +4.04% | +4.65% | Better in GM+ |
| Reinhardt | blizzard-world | -8.13% | -3.49% | +4.64% | Better in GM+ |
| Torbjörn | busan | +1.16% | -3.48% | -4.64% | Better in Masters |
| Venture | suravasa | +1.15% | -3.48% | -4.63% | Better in Masters |
| Hanzo | antarctic-peninsula | -2.99% | +1.63% | +4.62% | Better in GM+ |
| Zarya | midtown | +2.56% | -2.06% | -4.62% | Better in Masters |
| Brigitte | neon-junction | -2.11% | -6.72% | -4.61% | Better in Masters |
| D.Mon | shambali-monastery | +1.27% | -3.33% | -4.60% | Better in Masters |
| Emre | numbani | -3.20% | +1.40% | +4.60% | Better in GM+ |
| Anran | hollywood | +0.02% | -4.57% | -4.59% | Better in Masters |
| Illari | havana | -0.90% | +3.68% | +4.58% | Better in GM+ |
| Zarya | rialto | -1.87% | +2.71% | +4.58% | Better in GM+ |
| Venture | rialto | +1.28% | -3.29% | -4.57% | Better in Masters |
| Wrecking Ball | numbani | +0.43% | +5.00% | +4.57% | Better in GM+ |
| Genji | shambali-monastery | +2.43% | -2.13% | -4.56% | Better in Masters |
| Reaper | colosseo | +0.65% | -3.91% | -4.56% | Better in Masters |
| Sombra | blizzard-world | +6.46% | +1.90% | -4.56% | Better in Masters |
| Junker Queen | shambali-monastery | +0.58% | -3.97% | -4.55% | Better in Masters |
| Mizuki | eichenwalde | +1.41% | -3.13% | -4.54% | Better in Masters |
| Moira | nepal | +2.63% | -1.91% | -4.54% | Better in Masters |
| Torbjörn | midtown | -4.39% | +0.15% | +4.54% | Better in GM+ |
| Winston | aatlis | -2.96% | -7.50% | -4.54% | Better in Masters |
| Lifeweaver | shambali-monastery | -0.75% | -5.28% | -4.53% | Better in Masters |
| Zarya | route-66 | +1.22% | -3.31% | -4.53% | Better in Masters |
| Doomfist | new-junk-city | +3.32% | -1.20% | -4.52% | Better in Masters |
| Tracer | route-66 | -0.68% | +3.84% | +4.52% | Better in GM+ |
| Sierra | route-66 | -0.36% | +4.15% | +4.51% | Better in GM+ |
| Vendetta | busan | -2.01% | +2.50% | +4.51% | Better in GM+ |
| Zarya | new-junk-city | +3.61% | -0.90% | -4.51% | Better in Masters |
| Lifeweaver | colosseo | -1.27% | +3.22% | +4.49% | Better in GM+ |
| Brigitte | lijiang-tower | +2.52% | -1.96% | -4.48% | Better in Masters |
| Bastion | route-66 | -3.37% | -7.85% | -4.48% | Better in Masters |
| Brigitte | midtown | -0.58% | +3.90% | +4.48% | Better in GM+ |
| Bastion | new-queen-street | +0.01% | -4.46% | -4.47% | Better in Masters |
| Ashe | ilios | -2.77% | +1.69% | +4.46% | Better in GM+ |
| Baptiste | new-queen-street | -3.33% | +1.11% | +4.44% | Better in GM+ |
| Torbjörn | circuit-royal | -5.36% | -0.93% | +4.43% | Better in GM+ |
| Zarya | hollywood | +0.13% | +4.56% | +4.43% | Better in GM+ |
| Sierra | colosseo | -0.92% | +3.50% | +4.42% | Better in GM+ |
| Venture | route-66 | -3.78% | +0.64% | +4.42% | Better in GM+ |
| Mauga | samoa | -1.15% | +3.24% | +4.39% | Better in GM+ |
| Ramattra | neon-junction | -1.04% | +3.35% | +4.39% | Better in GM+ |
| Wrecking Ball | runasapi | +3.46% | -0.93% | -4.39% | Better in Masters |
| Emre | paraiso | +1.77% | -2.61% | -4.38% | Better in Masters |
| Sojourn | havana | +2.28% | -2.10% | -4.38% | Better in Masters |
| D.Mon | midtown | -4.10% | +0.27% | +4.37% | Better in GM+ |
| Orisa | suravasa | -2.75% | +1.61% | +4.36% | Better in GM+ |
| Winston | new-junk-city | -5.92% | -10.28% | -4.36% | Better in Masters |
| Mizuki | watchpoint-gibraltar | -3.34% | +1.01% | +4.35% | Better in GM+ |
| Moira | watchpoint-gibraltar | +0.91% | -3.44% | -4.35% | Better in Masters |
| Domina | watchpoint-gibraltar | -6.73% | -2.39% | +4.34% | Better in GM+ |
| Lúcio | neon-junction | -4.33% | +0.00% | +4.33% | Better in GM+ |
| Torbjörn | suravasa | +2.23% | -2.10% | -4.33% | Better in Masters |
| Emre | eichenwalde | -2.32% | -6.62% | -4.30% | Better in Masters |
| Sierra | neon-junction | +3.32% | -0.98% | -4.30% | Better in Masters |
| Sigma | kings-row | -2.79% | +1.51% | +4.30% | Better in GM+ |
| Soldier: 76 | watchpoint-gibraltar | -2.41% | +1.88% | +4.29% | Better in GM+ |
| Soldier: 76 | neon-junction | -1.80% | +2.48% | +4.28% | Better in GM+ |
| Junkrat | hollywood | -0.74% | -5.02% | -4.28% | Better in Masters |
| Ashe | new-junk-city | -1.01% | -5.28% | -4.27% | Better in Masters |
| Junker Queen | junkertown | -3.44% | -7.71% | -4.27% | Better in Masters |
| Sierra | numbani | +3.88% | -0.39% | -4.27% | Better in Masters |
| Kiriko | eichenwalde | -0.01% | -4.27% | -4.26% | Better in Masters |
| Ramattra | busan | +0.49% | -3.77% | -4.26% | Better in Masters |
| Lúcio | junkertown | -7.64% | -3.39% | +4.25% | Better in GM+ |
| Ashe | aatlis | -2.08% | -6.32% | -4.24% | Better in Masters |
| Hazard | numbani | +1.86% | -2.37% | -4.23% | Better in Masters |
| Reinhardt | suravasa | +3.05% | -1.18% | -4.23% | Better in Masters |
| Sigma | watchpoint-gibraltar | -5.43% | -9.64% | -4.21% | Better in Masters |
| D.Mon | new-queen-street | +0.42% | +4.62% | +4.20% | Better in GM+ |
| Jetpack Cat | neon-junction | -4.82% | -0.62% | +4.20% | Better in GM+ |
| Reaper | junkertown | -3.30% | +0.90% | +4.20% | Better in GM+ |
| Juno | blizzard-world | -1.26% | +2.90% | +4.16% | Better in GM+ |
| Mauga | neon-junction | -4.26% | -0.10% | +4.16% | Better in GM+ |
| Soldier: 76 | junkertown | -1.41% | -5.57% | -4.16% | Better in Masters |
| Reinhardt | kings-row | +2.10% | -2.04% | -4.14% | Better in Masters |
| Ana | new-junk-city | -3.17% | -7.31% | -4.14% | Better in Masters |
| Echo | watchpoint-gibraltar | +2.51% | -1.62% | -4.13% | Better in Masters |
| Mercy | grimsvotn | -1.09% | -5.22% | -4.13% | Better in Masters |
| Vendetta | grimsvotn | +2.59% | +6.72% | +4.13% | Better in GM+ |
| Widowmaker | ilios | -1.57% | +2.56% | +4.13% | Better in GM+ |
| Reaper | midtown | +2.31% | -1.81% | -4.12% | Better in Masters |
| Doctrine | watchpoint-gibraltar | +2.44% | -1.67% | -4.11% | Better in Masters |
| Zarya | dorado | -5.72% | -9.81% | -4.09% | Better in Masters |
| Illari | dorado | +0.77% | -3.29% | -4.06% | Better in Masters |
| Wrecking Ball | dorado | +7.09% | +3.04% | -4.05% | Better in Masters |
| Hanzo | suravasa | -3.63% | +0.41% | +4.04% | Better in GM+ |
| Junkrat | blizzard-world | -3.34% | -7.37% | -4.03% | Better in Masters |
| Reaper | shambali-monastery | +2.72% | -1.31% | -4.03% | Better in Masters |
| Ashe | dorado | +1.65% | +5.67% | +4.02% | Better in GM+ |
| Roadhog | circuit-royal | +5.50% | +9.52% | +4.02% | Better in GM+ |
| Domina | ilios | -4.27% | -8.28% | -4.01% | Better in Masters |
| Hazard | busan | -2.78% | +1.23% | +4.01% | Better in GM+ |
| Bastion | numbani | -0.35% | +3.65% | +4.00% | Better in GM+ |
| Wrecking Ball | circuit-royal | +0.51% | -3.49% | -4.00% | Better in Masters |
| Freja | junkertown | +1.80% | +5.79% | +3.99% | Better in GM+ |
| Orisa | dorado | -3.16% | -7.15% | -3.99% | Better in Masters |
| Venture | colosseo | +1.52% | -2.46% | -3.98% | Better in Masters |
| Reinhardt | new-junk-city | -0.42% | +3.55% | +3.97% | Better in GM+ |
| Mauga | watchpoint-gibraltar | -1.63% | -5.59% | -3.96% | Better in Masters |
| Ramattra | ilios | -0.92% | -4.88% | -3.96% | Better in Masters |
| Junkrat | grimsvotn | +6.40% | +10.36% | +3.96% | Better in GM+ |
| Anran | new-queen-street | -1.05% | -4.98% | -3.93% | Better in Masters |
| Tracer | midtown | +0.71% | -3.22% | -3.93% | Better in Masters |
| Juno | suravasa | +1.38% | -2.55% | -3.93% | Better in Masters |
| Sojourn | hollywood | -1.88% | -5.80% | -3.92% | Better in Masters |
| Emre | rialto | +0.18% | +4.09% | +3.91% | Better in GM+ |
| Juno | busan | +1.69% | -2.21% | -3.90% | Better in Masters |
| Moira | neon-junction | -1.25% | +2.64% | +3.89% | Better in GM+ |
| Sojourn | shambali-monastery | -1.43% | +2.45% | +3.88% | Better in GM+ |
| Pharah | midtown | -4.86% | -1.00% | +3.86% | Better in GM+ |
| Junker Queen | antarctic-peninsula | +1.15% | +5.01% | +3.86% | Better in GM+ |
| Lúcio | numbani | -6.21% | -2.35% | +3.86% | Better in GM+ |
| Mizuki | midtown | -2.31% | +1.54% | +3.85% | Better in GM+ |
| Vendetta | neon-junction | +1.18% | +5.02% | +3.84% | Better in GM+ |
| Mei | blizzard-world | +1.18% | -2.64% | -3.82% | Better in Masters |
| Reinhardt | rialto | +0.39% | -3.43% | -3.82% | Better in Masters |
| Emre | aatlis | -1.83% | +1.98% | +3.81% | Better in GM+ |
| Junkrat | eichenwalde | +3.45% | +7.26% | +3.81% | Better in GM+ |
| Junker Queen | eichenwalde | +1.00% | +4.80% | +3.80% | Better in GM+ |
| Echo | esperanca | -0.76% | +3.03% | +3.79% | Better in GM+ |
| Reinhardt | busan | +2.37% | -1.41% | -3.78% | Better in Masters |
| Torbjörn | watchpoint-gibraltar | -4.36% | -0.58% | +3.78% | Better in GM+ |
| Wrecking Ball | new-junk-city | +2.82% | -0.96% | -3.78% | Better in Masters |
| Orisa | rialto | +1.62% | -2.15% | -3.77% | Better in Masters |
| Soldier: 76 | kings-row | -3.70% | +0.07% | +3.77% | Better in GM+ |
| Moira | hollywood | -3.37% | +0.39% | +3.76% | Better in GM+ |
| Moira | numbani | -5.91% | -2.15% | +3.76% | Better in GM+ |
| Reaper | kings-row | -0.10% | +3.66% | +3.76% | Better in GM+ |
| Mauga | eichenwalde | -1.57% | +2.19% | +3.76% | Better in GM+ |
| Sigma | esperanca | -3.94% | -7.69% | -3.75% | Better in Masters |
| Hanzo | shambali-monastery | +2.26% | -1.49% | -3.75% | Better in Masters |
| Brigitte | numbani | -4.55% | -0.81% | +3.74% | Better in GM+ |
| Sigma | hollywood | -1.06% | -4.80% | -3.74% | Better in Masters |
| Hazard | junkertown | -1.15% | +2.58% | +3.73% | Better in GM+ |
| Mizuki | blizzard-world | -2.93% | -6.65% | -3.72% | Better in Masters |
| Sierra | nepal | +0.30% | +4.01% | +3.71% | Better in GM+ |
| Sombra | colosseo | +2.53% | +6.23% | +3.70% | Better in GM+ |
| Mei | rialto | +1.81% | -1.89% | -3.70% | Better in Masters |
| Lúcio | aatlis | +4.65% | +0.96% | -3.69% | Better in Masters |
| Venture | oasis | -2.47% | +1.22% | +3.69% | Better in GM+ |
| Shion | grimsvotn | +0.23% | -3.45% | -3.68% | Better in Masters |
| Tracer | rialto | +0.65% | -3.03% | -3.68% | Better in Masters |
| Reaper | dorado | -1.56% | +2.11% | +3.67% | Better in GM+ |
| Kiriko | route-66 | -1.48% | -5.14% | -3.66% | Better in Masters |
| Pharah | colosseo | +0.89% | -2.75% | -3.64% | Better in Masters |
| D.Mon | numbani | -4.33% | -7.96% | -3.63% | Better in Masters |
| Mercy | blizzard-world | -1.96% | +1.67% | +3.63% | Better in GM+ |
| Zenyatta | junkertown | +1.84% | +5.47% | +3.63% | Better in GM+ |
| Baptiste | circuit-royal | +4.11% | +0.50% | -3.61% | Better in Masters |
| Domina | dorado | -5.43% | -9.04% | -3.61% | Better in Masters |
| Mei | runasapi | +0.59% | +4.19% | +3.60% | Better in GM+ |
| Moira | shambali-monastery | +1.21% | -2.39% | -3.60% | Better in Masters |
| Torbjörn | hollywood | -0.43% | -4.03% | -3.60% | Better in Masters |
| Reinhardt | new-queen-street | -0.84% | +2.75% | +3.59% | Better in GM+ |
| Winston | suravasa | +2.60% | -0.99% | -3.59% | Better in Masters |
| Mizuki | dorado | -3.05% | +0.53% | +3.58% | Better in GM+ |
| Genji | junkertown | -0.79% | +2.78% | +3.57% | Better in GM+ |
| Torbjörn | paraiso | -4.21% | -0.64% | +3.57% | Better in GM+ |
| Cassidy | circuit-royal | +0.87% | -2.69% | -3.56% | Better in Masters |
| Torbjörn | aatlis | +1.76% | -1.80% | -3.56% | Better in Masters |
| Cassidy | route-66 | -0.76% | +2.78% | +3.54% | Better in GM+ |
| Jetpack Cat | eichenwalde | +7.18% | +3.64% | -3.54% | Better in Masters |
| Bastion | shambali-monastery | +3.81% | +0.28% | -3.53% | Better in Masters |
| Mei | suravasa | +1.73% | -1.80% | -3.53% | Better in Masters |
| Mercy | busan | -1.16% | +2.37% | +3.53% | Better in GM+ |
| Doomfist | kings-row | +0.81% | -2.71% | -3.52% | Better in Masters |
| Reinhardt | neon-junction | +0.38% | +3.90% | +3.52% | Better in GM+ |
| Mizuki | neon-junction | +1.75% | +5.27% | +3.52% | Better in GM+ |
| Cassidy | junkertown | +0.44% | -3.05% | -3.49% | Better in Masters |
| Zarya | watchpoint-gibraltar | -7.10% | -3.61% | +3.49% | Better in GM+ |
| Mauga | shambali-monastery | -0.72% | -4.20% | -3.48% | Better in Masters |
| Pharah | watchpoint-gibraltar | -2.39% | +1.09% | +3.48% | Better in GM+ |
| Juno | junkertown | -0.95% | -4.43% | -3.48% | Better in Masters |
| Widowmaker | kings-row | +2.87% | -0.60% | -3.47% | Better in Masters |
| Jetpack Cat | shambali-monastery | -0.67% | +2.80% | +3.47% | Better in GM+ |
| Tracer | eichenwalde | -0.78% | +2.69% | +3.47% | Better in GM+ |
| Baptiste | oasis | +1.59% | -1.86% | -3.45% | Better in Masters |
| Junker Queen | hollywood | -6.54% | -3.09% | +3.45% | Better in GM+ |
| Vendetta | lijiang-tower | +0.77% | -2.68% | -3.45% | Better in Masters |
| Doomfist | dorado | +0.16% | +3.61% | +3.45% | Better in GM+ |
| Jetpack Cat | rialto | -2.51% | +0.94% | +3.45% | Better in GM+ |
| Bastion | lijiang-tower | +1.46% | -1.98% | -3.44% | Better in Masters |
| D.Va | havana | -1.62% | +1.81% | +3.43% | Better in GM+ |
| Zarya | lijiang-tower | +0.91% | +4.33% | +3.42% | Better in GM+ |
| Lifeweaver | new-queen-street | +0.23% | +3.64% | +3.41% | Better in GM+ |
| Vendetta | junkertown | -4.75% | -1.34% | +3.41% | Better in GM+ |
| Pharah | aatlis | -6.09% | -2.68% | +3.41% | Better in GM+ |
| Brigitte | paraiso | +1.62% | -1.78% | -3.40% | Better in Masters |
| Mei | lijiang-tower | +1.82% | +5.22% | +3.40% | Better in GM+ |
| Junker Queen | esperanca | +0.27% | +3.66% | +3.39% | Better in GM+ |
| Pharah | oasis | +0.61% | -2.78% | -3.39% | Better in Masters |
| Juno | neon-junction | +0.00% | -3.38% | -3.38% | Better in Masters |
| Symmetra | blizzard-world | -0.17% | -3.55% | -3.38% | Better in Masters |
| Winston | midtown | -4.28% | -7.66% | -3.38% | Better in Masters |
| Freja | rialto | -0.77% | +2.60% | +3.37% | Better in GM+ |
| Reaper | aatlis | +2.31% | -1.06% | -3.37% | Better in Masters |
| Tracer | hollywood | -2.05% | +1.32% | +3.37% | Better in GM+ |
| Wrecking Ball | junkertown | +1.42% | +4.79% | +3.37% | Better in GM+ |
| D.Va | oasis | -1.45% | +1.91% | +3.36% | Better in GM+ |
| Ashe | eichenwalde | +0.21% | -3.14% | -3.35% | Better in Masters |
| Brigitte | ilios | +0.94% | -2.41% | -3.35% | Better in Masters |
| D.Va | nepal | -3.17% | +0.18% | +3.35% | Better in GM+ |
| Lúcio | havana | -7.73% | -11.07% | -3.34% | Better in Masters |
| Junker Queen | grimsvotn | -1.53% | +1.80% | +3.33% | Better in GM+ |
| Vendetta | route-66 | -1.88% | +1.45% | +3.33% | Better in GM+ |
| Bastion | rialto | -0.03% | +3.29% | +3.32% | Better in GM+ |
| Doomfist | watchpoint-gibraltar | +0.63% | -2.68% | -3.31% | Better in Masters |
| Sigma | new-queen-street | -7.25% | -3.94% | +3.31% | Better in GM+ |
| Soldier: 76 | paraiso | -2.25% | +1.06% | +3.31% | Better in GM+ |
| Vendetta | samoa | +0.36% | -2.95% | -3.31% | Better in Masters |
| Wrecking Ball | ilios | -0.98% | +2.33% | +3.31% | Better in GM+ |
| Wrecking Ball | neon-junction | -4.12% | -0.81% | +3.31% | Better in GM+ |
| Doomfist | route-66 | -0.75% | +2.55% | +3.30% | Better in GM+ |
| Sombra | ilios | +0.08% | +3.38% | +3.30% | Better in GM+ |
| Ramattra | paraiso | -7.07% | -3.78% | +3.29% | Better in GM+ |
| Junkrat | dorado | -0.40% | -3.69% | -3.29% | Better in Masters |
| Reaper | grimsvotn | +2.57% | -0.72% | -3.29% | Better in Masters |
| Ramattra | grimsvotn | +1.72% | +4.99% | +3.27% | Better in GM+ |
| Reinhardt | paraiso | -2.20% | +1.07% | +3.27% | Better in GM+ |
| Freja | shambali-monastery | -0.82% | +2.45% | +3.27% | Better in GM+ |
| Anran | blizzard-world | +0.53% | +3.79% | +3.26% | Better in GM+ |
| Domina | paraiso | -8.87% | -5.61% | +3.26% | Better in GM+ |
| Moira | runasapi | -3.00% | +0.24% | +3.24% | Better in GM+ |
| Roadhog | oasis | +3.83% | +0.59% | -3.24% | Better in Masters |
| Zenyatta | midtown | -0.23% | -3.47% | -3.24% | Better in Masters |
| Reaper | esperanca | +1.69% | -1.54% | -3.23% | Better in Masters |
| Widowmaker | midtown | +2.61% | -0.62% | -3.23% | Better in Masters |
| Ramattra | samoa | -0.56% | +2.66% | +3.22% | Better in GM+ |
| Junkrat | antarctic-peninsula | -1.09% | -4.31% | -3.22% | Better in Masters |
| Kiriko | havana | -1.88% | -5.09% | -3.21% | Better in Masters |
| Mercy | suravasa | +0.43% | -2.77% | -3.20% | Better in Masters |
| Sojourn | paraiso | -2.88% | -6.07% | -3.19% | Better in Masters |
| Ana | paraiso | +0.08% | +3.27% | +3.19% | Better in GM+ |
| Zarya | suravasa | -2.49% | +0.68% | +3.17% | Better in GM+ |
| Hazard | havana | -3.45% | -0.28% | +3.17% | Better in GM+ |
| Illari | watchpoint-gibraltar | +2.01% | -1.16% | -3.17% | Better in Masters |
| Anran | midtown | -2.20% | +0.96% | +3.16% | Better in GM+ |
| Roadhog | route-66 | +1.25% | -1.91% | -3.16% | Better in Masters |
| Domina | midtown | +1.53% | -1.62% | -3.15% | Better in Masters |
| Sierra | circuit-royal | +0.92% | +4.07% | +3.15% | Better in GM+ |
| Symmetra | kings-row | +0.51% | -2.64% | -3.15% | Better in Masters |
| Ramattra | midtown | -0.42% | -3.57% | -3.15% | Better in Masters |
| Zenyatta | grimsvotn | -3.29% | -0.14% | +3.15% | Better in GM+ |
| Doomfist | hollywood | +0.90% | -2.24% | -3.14% | Better in Masters |
| Winston | junkertown | -2.05% | +1.07% | +3.12% | Better in GM+ |
| Mei | numbani | -4.94% | -1.84% | +3.10% | Better in GM+ |
| Brigitte | junkertown | -0.36% | +2.74% | +3.10% | Better in GM+ |
| Illari | suravasa | -1.64% | +1.46% | +3.10% | Better in GM+ |
| Mizuki | route-66 | -1.75% | -4.85% | -3.10% | Better in Masters |
| Orisa | lijiang-tower | +1.04% | +4.14% | +3.10% | Better in GM+ |
| Anran | esperanca | -0.63% | -3.71% | -3.08% | Better in Masters |
| Anran | eichenwalde | -4.80% | -7.88% | -3.08% | Better in Masters |
| Jetpack Cat | suravasa | +4.00% | +0.92% | -3.08% | Better in Masters |
| Venture | dorado | +2.20% | -0.86% | -3.06% | Better in Masters |
| Domina | new-queen-street | -0.96% | -4.02% | -3.06% | Better in Masters |
| Wrecking Ball | midtown | -4.00% | -7.06% | -3.06% | Better in Masters |
| Sierra | runasapi | -0.12% | +2.93% | +3.05% | Better in GM+ |
| Emre | dorado | -0.54% | -3.59% | -3.05% | Better in Masters |
| Pharah | shambali-monastery | +3.01% | -0.04% | -3.05% | Better in Masters |
| Freja | esperanca | -2.26% | +0.78% | +3.04% | Better in GM+ |
| Wuyang | runasapi | -0.25% | +2.79% | +3.04% | Better in GM+ |
| Wuyang | rialto | -0.46% | +2.57% | +3.03% | Better in GM+ |
| Shion | dorado | -1.71% | +1.31% | +3.02% | Better in GM+ |
| Mauga | numbani | -1.22% | -4.23% | -3.01% | Better in Masters |
| Hazard | new-queen-street | +2.56% | -0.45% | -3.01% | Better in Masters |
| Zenyatta | dorado | -0.41% | -3.42% | -3.01% | Better in Masters |
| Brigitte | watchpoint-gibraltar | +3.29% | +0.29% | -3.00% | Better in Masters |
| Echo | kings-row | -2.51% | +0.49% | +3.00% | Better in GM+ |
| Zenyatta | busan | +0.28% | +3.28% | +3.00% | Better in GM+ |
| Hanzo | route-66 | +2.31% | -0.68% | -2.99% | Better in Masters |
| Winston | paraiso | +0.48% | +3.47% | +2.99% | Better in GM+ |
| Anran | watchpoint-gibraltar | +2.45% | -0.53% | -2.98% | Better in Masters |
| Lifeweaver | kings-row | +0.02% | -2.95% | -2.97% | Better in Masters |
| Pharah | dorado | +3.52% | +0.55% | -2.97% | Better in Masters |
| D.Mon | junkertown | -3.02% | -5.98% | -2.96% | Better in Masters |
| Doomfist | junkertown | -0.97% | -3.93% | -2.96% | Better in Masters |
| Hazard | samoa | +2.27% | -0.69% | -2.96% | Better in Masters |
| Zenyatta | colosseo | -1.30% | +1.66% | +2.96% | Better in GM+ |
| Reaper | havana | -3.90% | -0.95% | +2.95% | Better in GM+ |
| Sierra | havana | +3.12% | +0.17% | -2.95% | Better in Masters |
| Sombra | esperanca | +2.43% | -0.52% | -2.95% | Better in Masters |
| Emre | esperanca | +2.24% | -0.70% | -2.94% | Better in Masters |
| Kiriko | runasapi | +1.65% | +4.59% | +2.94% | Better in GM+ |
| Brigitte | blizzard-world | -4.77% | -7.70% | -2.93% | Better in Masters |
| Junker Queen | samoa | +2.37% | -0.56% | -2.93% | Better in Masters |
| Widowmaker | neon-junction | -0.99% | +1.94% | +2.93% | Better in GM+ |
| Freja | nepal | -1.70% | +1.22% | +2.92% | Better in GM+ |
| Lifeweaver | suravasa | -0.14% | -3.06% | -2.92% | Better in Masters |
| Vendetta | midtown | +1.19% | -1.72% | -2.91% | Better in Masters |
| Zarya | ilios | -4.11% | -1.20% | +2.91% | Better in GM+ |
| Domina | route-66 | -0.84% | -3.74% | -2.90% | Better in Masters |
| Mizuki | runasapi | +3.47% | +0.57% | -2.90% | Better in Masters |
| Sojourn | dorado | -1.76% | -4.65% | -2.89% | Better in Masters |
| D.Mon | dorado | +1.98% | +4.87% | +2.89% | Better in GM+ |
| Mauga | new-queen-street | -0.18% | +2.70% | +2.88% | Better in GM+ |
| Bastion | dorado | -0.95% | -3.83% | -2.88% | Better in Masters |
| Junkrat | numbani | -1.10% | +1.77% | +2.87% | Better in GM+ |
| Venture | blizzard-world | +2.00% | +4.87% | +2.87% | Better in GM+ |
| Jetpack Cat | numbani | -3.04% | -0.19% | +2.85% | Better in GM+ |
| Wuyang | kings-row | -2.99% | -0.14% | +2.85% | Better in GM+ |
| Zenyatta | kings-row | +0.35% | -2.49% | -2.84% | Better in Masters |
| Mizuki | havana | -3.94% | -1.10% | +2.84% | Better in GM+ |
| Mercy | esperanca | +1.38% | -1.45% | -2.83% | Better in Masters |
| Venture | circuit-royal | -2.41% | +0.42% | +2.83% | Better in GM+ |
| Anran | neon-junction | -0.36% | -3.18% | -2.82% | Better in Masters |
| Junkrat | junkertown | +0.90% | +3.72% | +2.82% | Better in GM+ |
| Sojourn | rialto | +0.55% | -2.27% | -2.82% | Better in Masters |
| Bastion | neon-junction | -0.38% | +2.44% | +2.82% | Better in GM+ |
| Venture | ilios | +0.81% | -2.01% | -2.82% | Better in Masters |
| Freja | circuit-royal | +0.93% | -1.87% | -2.80% | Better in Masters |
| Reinhardt | shambali-monastery | +3.78% | +6.58% | +2.80% | Better in GM+ |
| Symmetra | watchpoint-gibraltar | -2.55% | -5.35% | -2.80% | Better in Masters |
| Brigitte | kings-row | -0.26% | -3.05% | -2.79% | Better in Masters |
| D.Va | new-junk-city | -3.81% | -1.02% | +2.79% | Better in GM+ |
| Ramattra | esperanca | -1.76% | -4.55% | -2.79% | Better in Masters |
| Shion | hollywood | +1.42% | -1.37% | -2.79% | Better in Masters |
| Zenyatta | suravasa | -1.88% | +0.91% | +2.79% | Better in GM+ |
| Baptiste | esperanca | -0.24% | -3.02% | -2.78% | Better in Masters |
| Mizuki | ilios | +0.17% | -2.61% | -2.78% | Better in Masters |
| Mei | route-66 | -0.63% | -3.40% | -2.77% | Better in Masters |
| Sombra | neon-junction | -2.04% | +0.73% | +2.77% | Better in GM+ |
| Emre | ilios | -1.51% | +1.25% | +2.76% | Better in GM+ |
| Sigma | eichenwalde | -3.13% | -0.37% | +2.76% | Better in GM+ |
| Hazard | nepal | +0.60% | +3.35% | +2.75% | Better in GM+ |
| Torbjörn | numbani | -0.38% | -3.13% | -2.75% | Better in Masters |
| Roadhog | suravasa | -1.85% | +0.89% | +2.74% | Better in GM+ |
| Sierra | new-queen-street | +0.06% | -2.67% | -2.73% | Better in Masters |
| Mei | havana | -1.17% | -3.89% | -2.72% | Better in Masters |
| Brigitte | runasapi | +1.16% | -1.56% | -2.72% | Better in Masters |
| Cassidy | new-queen-street | -3.05% | -0.33% | +2.72% | Better in GM+ |
| Venture | numbani | -5.01% | -2.29% | +2.72% | Better in GM+ |
| Kiriko | new-junk-city | +1.29% | -1.42% | -2.71% | Better in Masters |
| Sombra | samoa | -2.09% | -4.80% | -2.71% | Better in Masters |
| Mercy | dorado | +1.58% | -1.12% | -2.70% | Better in Masters |
| Sigma | dorado | -6.80% | -9.50% | -2.70% | Better in Masters |
| Echo | havana | -4.29% | -1.62% | +2.67% | Better in GM+ |
| Reaper | runasapi | +0.83% | -1.84% | -2.67% | Better in Masters |
| Vendetta | rialto | -1.87% | +0.78% | +2.65% | Better in GM+ |
| Ashe | new-queen-street | +0.27% | -2.38% | -2.65% | Better in Masters |
| Baptiste | lijiang-tower | +0.81% | -1.83% | -2.64% | Better in Masters |
| Genji | eichenwalde | +0.63% | -2.01% | -2.64% | Better in Masters |
| Reaper | neon-junction | +0.78% | +3.42% | +2.64% | Better in GM+ |
| Sierra | suravasa | +0.99% | +3.63% | +2.64% | Better in GM+ |
| Kiriko | numbani | +1.62% | -1.01% | -2.63% | Better in Masters |
| Mercy | aatlis | -2.69% | -0.06% | +2.63% | Better in GM+ |
| Orisa | grimsvotn | +3.24% | +0.63% | -2.61% | Better in Masters |
| Ramattra | lijiang-tower | +2.30% | -0.31% | -2.61% | Better in Masters |
| Widowmaker | havana | +4.89% | +7.49% | +2.60% | Better in GM+ |
| Anran | shambali-monastery | -1.10% | +1.50% | +2.60% | Better in GM+ |
| Symmetra | junkertown | -0.37% | -2.97% | -2.60% | Better in Masters |
| Kiriko | junkertown | -0.51% | +2.09% | +2.60% | Better in GM+ |
| Junker Queen | route-66 | -0.68% | -3.27% | -2.59% | Better in Masters |
| Ramattra | kings-row | +0.62% | -1.97% | -2.59% | Better in Masters |
| Winston | route-66 | -1.04% | -3.63% | -2.59% | Better in Masters |
| Orisa | hollywood | -0.83% | -3.41% | -2.58% | Better in Masters |
| Reinhardt | junkertown | -1.14% | +1.44% | +2.58% | Better in GM+ |
| Freja | hollywood | -1.81% | +0.76% | +2.57% | Better in GM+ |
| Ana | neon-junction | -0.04% | -2.61% | -2.57% | Better in Masters |
| Doomfist | busan | -0.10% | -2.67% | -2.57% | Better in Masters |
| Brigitte | new-junk-city | -0.48% | +2.08% | +2.56% | Better in GM+ |
| Hazard | suravasa | -0.79% | +1.77% | +2.56% | Better in GM+ |
| Hanzo | runasapi | -1.99% | -4.55% | -2.56% | Better in Masters |
| Mei | circuit-royal | +2.04% | +4.60% | +2.56% | Better in GM+ |
| Sojourn | ilios | -0.17% | -2.72% | -2.55% | Better in Masters |
| Junkrat | lijiang-tower | -0.83% | +1.72% | +2.55% | Better in GM+ |
| Venture | samoa | +1.02% | -1.53% | -2.55% | Better in Masters |
| Reinhardt | numbani | -5.47% | -2.94% | +2.53% | Better in GM+ |
| Symmetra | samoa | +0.91% | +3.44% | +2.53% | Better in GM+ |
| Mercy | watchpoint-gibraltar | +4.45% | +1.93% | -2.52% | Better in Masters |
| Domina | rialto | -1.90% | +0.62% | +2.52% | Better in GM+ |
| Lifeweaver | nepal | -0.46% | +2.06% | +2.52% | Better in GM+ |
| Doctrine | ilios | -4.81% | -7.32% | -2.51% | Better in Masters |
| Reinhardt | watchpoint-gibraltar | -5.43% | -7.94% | -2.51% | Better in Masters |
| Lúcio | suravasa | +5.16% | +2.65% | -2.51% | Better in Masters |
| Zarya | aatlis | +1.26% | +3.77% | +2.51% | Better in GM+ |
| Orisa | busan | +1.12% | -1.38% | -2.50% | Better in Masters |
| Vendetta | ilios | +0.54% | +3.04% | +2.50% | Better in GM+ |
| Wuyang | shambali-monastery | +1.39% | +3.89% | +2.50% | Better in GM+ |

---

## 3. Map Tier Lists

### Aatlis

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| S | Junker Queen | +3.95% | +4.48% ±2.0 | Popular (+2.5%) | Meta | - | 51 |
| A | Lúcio | +2.68% | +2.80% ±1.3 | Map Priority (+8.4%) | Meta | Better in Masters | 52 |
| A | Mauga | +2.61% | +3.73% ±2.1 | Popular (+2.4%) | Meta | - | 52 |
| A | Anran | +2.08% | +4.00% ±2.5 | Popular (+2.5%) | Meta | - | 52 |
| A | Junkrat | +1.91% | +2.31% ±1.9 | Standard (+0.6%) | Favorable | - | 50 |
| A | Zarya | +1.85% | +2.52% ±2.1 | Popular (+2.3%) | Meta | Better in GM+ | 52 |
| A | Reinhardt | +1.63% | +2.10% ±2.8 | Standard (+0.9%) | Favorable | - | 50 |
| A | D.Mon | +1.56% | +2.80% ±2.4 | Popular (+2.4%) | Meta | - | 16 |
| A | Vendetta | +1.48% | +2.77% ±2.5 | Popular (+1.8%) | Favorable | - | 52 |
| A | Moira | +1.40% | +1.94% ±1.6 | Map Priority (+6.7%) | Favorable | - | 52 |
| A | Brigitte | +1.31% | +2.17% ±2.3 | Popular (+2.4%) | Favorable | - | 52 |
| B | Sombra *(provisional)* | +1.03% | +2.99% ±4.2 | Map Priority (+5.1%) | Neutral | - | 8 |
| B | Ramattra | +0.99% | +1.28% ±1.6 | Popular (+1.3%) | Neutral | - | 52 |
| B | Mizuki | +0.97% | +1.33% ±2.2 | Map Priority (+5.8%) | Neutral | - | 52 |
| B | Cassidy | +0.71% | +1.45% ±2.1 | Map Priority (+8.8%) | Neutral | - | 52 |
| B | Wrecking Ball | +0.71% | +0.82% ±1.4 | Standard (-0.3%) | Neutral | - | 51 |
| B | Jetpack Cat | +0.46% | +0.66% ±2.4 | Standard (-0.3%) | Neutral | - | 52 |
| B | Shion | +0.45% | +0.83% ±1.3 | Map Priority (+7.8%) | Neutral | - | 28 |
| B | Doomfist | +0.42% | +1.04% ±1.8 | Popular (+1.6%) | Neutral | - | 52 |
| B | Sierra | +0.22% | -1.67% ±1.6 | Niche (-1.2%) | Neutral | - | 27 |
| B | Hazard | +0.20% | +0.25% ±1.2 | Popular (+2.7%) | Neutral | - | 51 |
| B | Lifeweaver | +0.13% | +0.35% ±3.2 | Niche (-2.2%) | Neutral | - | 51 |
| B | Reaper | +0.08% | +0.62% ±2.7 | Map Priority (+5.6%) | Neutral | Better in Masters | 52 |
| B | Venture | +0.04% | +1.06% ±2.7 | Popular (+1.7%) | Neutral | - | 52 |
| B | Torbjörn | +0.03% | +0.05% ±1.9 | Standard (-0.2%) | Neutral | Better in Masters | 50 |
| B | Illari | -0.04% | +0.20% ±1.6 | Niche (-4.9%) | Neutral | - | 51 |
| B | Tracer | -0.11% | +0.12% ±2.4 | Map Priority (+6.6%) | Neutral | - | 52 |
| B | Genji | -0.13% | +0.29% ±1.9 | Standard (+0.7%) | Neutral | - | 52 |
| B | Kiriko | -0.14% | -0.14% ±0.9 | Map Priority (+9.6%) | Neutral | - | 51 |
| B | Emre | -0.26% | +0.08% ±2.4 | Niche (-4.5%) | Neutral | Better in GM+ | 52 |
| B | Mei | -0.28% | -0.47% ±2.2 | Standard (+0.4%) | Neutral | - | 52 |
| B | Symmetra | -0.36% | -0.33% ±1.8 | Standard (+0.3%) | Neutral | - | 51 |
| B | Sojourn | -0.38% | -0.36% ±2.1 | Standard (+0.3%) | Neutral | - | 52 |
| B | Soldier: 76 | -0.38% | -0.39% ±1.8 | Niche (-2.6%) | Neutral | - | 51 |
| B | Juno | -0.40% | +0.08% ±1.8 | Standard (+0.3%) | Neutral | - | 52 |
| B | Zenyatta | -0.64% | -0.72% ±1.6 | Niche (-4.8%) | Neutral | - | 51 |
| B | Mercy | -0.72% | -1.45% ±2.7 | Niche (-3.6%) | Neutral | Better in GM+ | 49 |
| B | Baptiste | -0.74% | -1.09% ±3.1 | Niche (-1.9%) | Neutral | - | 51 |
| B | Wuyang | -0.99% | -1.67% ±2.1 | Popular (+1.1%) | Neutral | - | 52 |
| B | Roadhog *(provisional)* | -1.05% | -2.80% ±6.8 | Standard (+0.2%) | Neutral | - | 8 |
| C | Ashe | -1.40% | -3.92% ±3.2 | Niche (-8.1%) | Unfavorable | Better in Masters | 37 |
| C | Doctrine *(provisional)* | -1.51% | -2.46% ±3.3 | Niche (-5.0%) | Deterrent | - | 8 |
| C | Domina | -1.55% | -1.81% ±3.8 | Niche (-1.2%) | Deterrent | - | 46 |
| C | Bastion | -1.73% | -2.06% ±1.6 | Niche (-1.4%) | Deterrent | - | 49 |
| C | D.Va | -1.84% | -3.17% ±2.1 | Niche (-1.7%) | Deterrent | - | 52 |
| C | Hanzo | -2.07% | -3.24% ±2.5 | Niche (-3.1%) | Deterrent | - | 51 |
| C | Freja | -2.11% | -3.26% ±2.3 | Niche (-2.9%) | Deterrent | - | 46 |
| C | Orisa | -2.31% | -2.67% ±1.3 | Popular (+1.1%) | Trap Pick | - | 51 |
| C | Echo | -2.91% | -3.61% ±1.8 | Niche (-2.9%) | Deterrent | - | 51 |
| D | Ana | -3.38% | -3.98% ±2.1 | Niche (-16.4%) | Deterrent | - | 52 |
| D | Pharah | -3.65% | -4.42% ±2.5 | Niche (-1.0%) | Deterrent | Better in GM+ | 51 |
| D | Sigma | -4.50% | -5.00% ±2.8 | Niche (-5.5%) | Deterrent | - | 52 |
| D | Winston | -4.75% | -5.18% ±2.5 | Niche (-6.3%) | Deterrent | Better in Masters | 51 |
| D | Widowmaker | -19.32% | -24.04% ±8.4 | Niche (-7.4%) | Deterrent | Better in GM+ | 9 |

### Antarctic Peninsula

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| S | Cassidy | +3.16% | +3.60% ±0.8 | Map Priority (+9.3%) | Meta | - | 40 |
| A | Junker Queen | +2.77% | +3.08% ±1.8 | Popular (+1.1%) | Favorable | Better in GM+ | 40 |
| A | Torbjörn | +2.39% | +3.22% ±2.4 | Standard (-0.1%) | Specialist | - | 40 |
| A | Ramattra | +2.03% | +2.40% ±1.4 | Standard (+0.9%) | Favorable | - | 40 |
| A | Symmetra | +1.76% | +2.19% ±1.7 | Standard (+0.5%) | Favorable | - | 40 |
| A | Mauga | +1.66% | +2.20% ±1.7 | Popular (+1.3%) | Favorable | - | 40 |
| A | Zarya | +1.54% | +1.84% ±1.5 | Popular (+1.4%) | Favorable | - | 40 |
| A | Bastion | +1.53% | +1.71% ±1.2 | Standard (-0.6%) | Specialist | - | 39 |
| A | Moira | +1.45% | +1.76% ±1.2 | Popular (+2.5%) | Favorable | - | 40 |
| A | Reinhardt | +1.45% | +1.57% ±1.5 | Standard (+0.8%) | Favorable | - | 40 |
| A | Tracer | +1.28% | +1.46% ±0.9 | Map Priority (+4.5%) | Favorable | - | 40 |
| A | Domina | +1.23% | +1.73% ±2.3 | Standard (-0.7%) | Favorable | - | 39 |
| B | Kiriko | +1.17% | +1.26% ±0.8 | Map Priority (+5.5%) | Neutral | - | 40 |
| B | Soldier: 76 | +0.92% | +1.17% ±1.3 | Standard (-0.7%) | Neutral | - | 40 |
| B | Brigitte | +0.74% | +0.96% ±1.4 | Standard (+0.9%) | Neutral | - | 40 |
| B | Mizuki | +0.60% | +0.69% ±1.5 | Popular (+2.8%) | Neutral | - | 40 |
| B | Orisa | +0.54% | +0.72% ±1.8 | Popular (+1.4%) | Neutral | - | 40 |
| B | Wuyang | +0.53% | +0.64% ±0.9 | Popular (+1.6%) | Neutral | - | 40 |
| B | Vendetta | +0.51% | +0.76% ±1.7 | Standard (+0.4%) | Neutral | - | 37 |
| B | Baptiste | +0.41% | +0.98% ±1.6 | Standard (-0.8%) | Neutral | - | 40 |
| B | Illari | +0.30% | +1.29% ±1.8 | Niche (-2.3%) | Neutral | - | 40 |
| B | Sierra | +0.22% | -0.89% ±2.1 | Standard (-0.3%) | Neutral | - | 31 |
| B | Mei | +0.18% | +0.57% ±2.0 | Standard (+0.2%) | Neutral | - | 40 |
| B | Lifeweaver | +0.13% | +0.96% ±2.2 | Niche (-1.5%) | Neutral | - | 40 |
| B | Reaper | +0.06% | +0.25% ±1.6 | Popular (+2.0%) | Neutral | - | 40 |
| B | D.Mon | +0.04% | +0.32% ±2.4 | Popular (+2.4%) | Neutral | - | 16 |
| B | Venture | +0.04% | -1.50% ±1.8 | Standard (+0.2%) | Neutral | - | 39 |
| B | Zenyatta | +0.03% | +0.17% ±1.3 | Niche (-2.5%) | Neutral | - | 40 |
| B | Doomfist | -0.17% | -0.10% ±1.5 | Standard (+0.1%) | Neutral | - | 40 |
| B | Sojourn | -0.18% | -0.15% ±0.9 | Standard (+0.3%) | Neutral | - | 40 |
| B | Lúcio | -0.27% | -0.22% ±1.4 | Map Priority (+3.2%) | Neutral | - | 40 |
| B | Roadhog *(provisional)* | -0.37% | -0.23% ±7.3 | Standard (+0.2%) | Neutral | Better in Masters | 8 |
| B | Anran | -0.45% | -0.59% ±2.4 | Standard (+0.6%) | Neutral | - | 39 |
| B | Genji | -0.52% | -1.77% ±1.1 | Standard (-0.9%) | Neutral | - | 40 |
| B | Emre | -0.53% | -0.77% ±1.4 | Niche (-2.2%) | Neutral | - | 40 |
| B | Hanzo | -0.61% | -0.68% ±1.9 | Niche (-2.5%) | Neutral | Better in GM+ | 40 |
| B | Freja | -0.66% | -0.75% ±2.2 | Niche (-1.6%) | Neutral | - | 40 |
| B | Shion | -0.69% | -0.83% ±1.0 | Map Priority (+6.7%) | Neutral | - | 28 |
| B | Ashe | -0.71% | -0.66% ±1.6 | Niche (-5.3%) | Neutral | - | 40 |
| B | Juno | -0.71% | -1.05% ±2.0 | Standard (+0.7%) | Neutral | - | 40 |
| B | Mercy | -0.90% | -1.62% ±2.2 | Niche (-1.5%) | Neutral | - | 39 |
| B | Echo | -0.94% | -1.00% ±1.4 | Niche (-1.9%) | Neutral | - | 40 |
| B | Wrecking Ball | -1.18% | -1.28% ±1.5 | Standard (-0.2%) | Neutral | - | 40 |
| C | D.Va | -1.22% | -1.82% ±2.0 | Niche (-1.1%) | Unfavorable | - | 40 |
| C | Sombra *(provisional)* | -1.24% | -1.72% ±4.7 | Map Priority (+3.4%) | Unfavorable | - | 8 |
| C | Doctrine *(provisional)* | -1.34% | -2.41% ±3.8 | Niche (-1.4%) | Unfavorable | - | 8 |
| C | Jetpack Cat | -1.41% | -1.52% ±1.3 | Standard (-0.4%) | Unfavorable | - | 40 |
| C | Sigma | -1.71% | -1.70% ±1.3 | Niche (-2.5%) | Deterrent | - | 40 |
| C | Ana | -1.78% | -1.83% ±0.9 | Niche (-8.2%) | Deterrent | - | 40 |
| C | Junkrat | -2.12% | -2.70% ±2.2 | Standard (-0.2%) | Deterrent | Better in Masters | 40 |
| C | Hazard | -2.30% | -2.44% ±1.2 | Standard (+0.7%) | Unfavorable | - | 40 |
| C | Winston | -2.81% | -2.85% ±1.2 | Niche (-4.6%) | Deterrent | - | 40 |
| D | Pharah | -4.04% | -4.50% ±1.8 | Standard (-0.7%) | Deterrent | - | 40 |
| D | Widowmaker | -9.23% | -9.32% ±2.0 | Niche (-5.5%) | Deterrent | - | 34 |

### Blizzard World

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| A | Doctrine *(provisional)* | +1.80% | +8.41% ±7.7 | Popular (+2.1%) | Meta | Better in GM+ | 8 |
| B | Wrecking Ball | +0.96% | +1.51% ±2.7 | Popular (+1.3%) | Neutral | Better in GM+ | 51 |
| B | Anran | +0.60% | +2.13% ±3.7 | Standard (-0.6%) | Neutral | Better in GM+ | 51 |
| B | D.Va | +0.47% | +1.34% ±1.9 | Standard (+0.7%) | Neutral | - | 52 |
| B | Jetpack Cat | +0.46% | +0.86% ±3.4 | Standard (-0.6%) | Neutral | - | 52 |
| B | Winston | +0.37% | +0.48% ±1.5 | Map Priority (+3.3%) | Neutral | - | 52 |
| B | Sojourn | +0.32% | +0.57% ±1.5 | Popular (+1.4%) | Neutral | - | 52 |
| B | Sierra | +0.22% | -3.02% ±4.1 | Standard (+0.5%) | Neutral | - | 38 |
| B | Sombra *(provisional)* | +0.17% | +4.18% ±8.1 | Standard (-0.8%) | Neutral | Better in Masters | 8 |
| B | Ana | +0.14% | +0.22% ±1.7 | Map Priority (+7.0%) | Neutral | - | 52 |
| B | Lifeweaver | +0.13% | +0.15% ±3.6 | Standard (+0.7%) | Neutral | Better in GM+ | 52 |
| B | Venture | +0.04% | +3.37% ±3.7 | Standard (-0.3%) | Neutral | Better in GM+ | 50 |
| B | Wuyang | +0.04% | +0.10% ±1.3 | Standard (+0.0%) | Neutral | - | 52 |
| B | D.Mon | +0.02% | +2.32% ±7.1 | Niche (-1.1%) | Neutral | Better in GM+ | 16 |
| B | Bastion | -0.10% | -0.16% ±2.7 | Standard (-0.0%) | Neutral | - | 51 |
| B | Illari | -0.17% | -0.16% ±1.5 | Popular (+1.6%) | Neutral | - | 52 |
| B | Roadhog *(provisional)* | -0.18% | +1.21% ±10.1 | Standard (+0.9%) | Neutral | Better in GM+ | 8 |
| B | Mercy | -0.21% | -0.18% ±2.9 | Popular (+1.2%) | Neutral | Better in GM+ | 51 |
| B | Orisa | -0.21% | -0.28% ±2.7 | Standard (-0.5%) | Neutral | - | 52 |
| B | Genji | -0.27% | -0.93% ±1.6 | Standard (-0.8%) | Neutral | - | 52 |
| B | Mei | -0.29% | -0.69% ±3.2 | Standard (-0.2%) | Neutral | Better in Masters | 51 |
| B | Emre | -0.33% | -0.28% ±2.2 | Popular (+1.9%) | Neutral | - | 52 |
| B | Juno | -0.45% | +0.78% ±3.4 | Niche (-1.3%) | Neutral | Better in GM+ | 51 |
| B | Shion | -0.45% | -0.88% ±2.7 | Niche (-2.6%) | Neutral | - | 28 |
| B | Widowmaker | -0.48% | -0.42% ±1.7 | Map Priority (+5.8%) | Neutral | - | 52 |
| B | Ashe | -0.74% | -0.71% ±1.8 | Popular (+2.7%) | Neutral | - | 52 |
| B | Zenyatta | -0.84% | -1.05% ±1.7 | Popular (+1.7%) | Neutral | - | 51 |
| B | Reaper | -0.86% | -1.57% ±3.1 | Niche (-2.1%) | Neutral | - | 52 |
| B | Freja | -0.90% | -1.20% ±2.5 | Standard (+0.7%) | Neutral | - | 50 |
| B | Echo | -0.92% | -1.21% ±3.2 | Niche (-2.0%) | Neutral | - | 52 |
| B | Doomfist | -0.97% | -2.07% ±2.5 | Standard (-0.0%) | Neutral | - | 52 |
| B | Hanzo | -1.13% | -1.52% ±2.2 | Popular (+1.3%) | Neutral | - | 52 |
| B | Kiriko | -1.16% | -1.49% ±1.6 | Niche (-2.6%) | Neutral | - | 52 |
| C | Sigma | -1.22% | -1.19% ±1.6 | Popular (+2.6%) | Unfavorable | - | 52 |
| C | Soldier: 76 | -1.25% | -1.74% ±2.2 | Standard (+0.1%) | Unfavorable | - | 52 |
| C | Symmetra | -1.27% | -1.83% ±3.3 | Standard (-0.3%) | Unfavorable | Better in Masters | 51 |
| C | Baptiste | -1.37% | -2.77% ±2.8 | Standard (-0.4%) | Unfavorable | - | 52 |
| C | Tracer | -1.57% | -1.95% ±1.7 | Standard (+0.7%) | Unfavorable | - | 52 |
| C | Cassidy | -1.66% | -1.99% ±1.2 | Niche (-5.4%) | Deterrent | - | 52 |
| C | Domina | -1.90% | -2.14% ±2.8 | Standard (+0.5%) | Unfavorable | - | 51 |
| C | Vendetta | -2.21% | -4.59% ±3.0 | Standard (-0.6%) | Deterrent | - | 44 |
| C | Pharah | -2.58% | -3.60% ±3.7 | Niche (-1.8%) | Deterrent | Better in GM+ | 52 |
| C | Zarya | -2.62% | -3.49% ±3.1 | Niche (-1.2%) | Deterrent | Better in Masters | 51 |
| C | Junkrat | -2.82% | -5.35% ±4.0 | Standard (-0.8%) | Deterrent | Better in Masters | 52 |
| D | Hazard | -3.07% | -4.47% ±3.1 | Niche (-2.0%) | Deterrent | - | 51 |
| D | Mauga | -3.21% | -5.25% ±3.1 | Niche (-1.1%) | Deterrent | Better in Masters | 50 |
| D | Moira | -3.42% | -5.26% ±3.1 | Niche (-1.9%) | Deterrent | - | 52 |
| D | Mizuki | -3.52% | -4.79% ±2.2 | Niche (-2.0%) | Deterrent | Better in Masters | 52 |
| D | Ramattra | -3.72% | -5.78% ±3.3 | Standard (-0.8%) | Deterrent | Better in Masters | 49 |
| D | Brigitte | -4.08% | -6.24% ±2.6 | Standard (-0.7%) | Deterrent | Better in Masters | 52 |
| D | Junker Queen | -4.13% | -5.14% ±3.6 | Standard (-1.0%) | Deterrent | - | 43 |
| D | Reinhardt | -4.21% | -5.81% ±4.0 | Standard (-0.9%) | Deterrent | Better in GM+ | 52 |
| D | Torbjörn | -4.42% | -6.95% ±3.2 | Standard (+0.5%) | Unfavorable | Better in Masters | 50 |
| D | Lúcio | -6.65% | -7.09% ±2.5 | Niche (-3.0%) | Deterrent | - | 51 |

### Busan

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| A | Soldier: 76 | +1.81% | +3.33% ±2.5 | Popular (+3.0%) | Meta | - | 16 |
| B | Junker Queen | +1.09% | +2.10% ±4.3 | Standard (+0.5%) | Neutral | - | 16 |
| B | Mauga | +1.06% | +1.90% ±2.5 | Standard (+0.7%) | Neutral | - | 16 |
| B | Widowmaker | +0.95% | +1.17% ±2.9 | Standard (-0.1%) | Neutral | - | 16 |
| B | Roadhog *(provisional)* | +0.94% | +4.98% ±7.1 | Standard (+0.0%) | Neutral | Better in GM+ | 8 |
| B | Cassidy | +0.93% | +1.57% ±1.7 | Map Priority (+3.4%) | Neutral | - | 16 |
| B | Moira | +0.88% | +2.29% ±3.0 | Popular (+1.9%) | Neutral | - | 16 |
| B | Freja | +0.80% | +2.81% ±3.2 | Niche (-1.8%) | Neutral | - | 16 |
| B | Zenyatta | +0.68% | +1.78% ±2.3 | Niche (-1.3%) | Neutral | Better in GM+ | 16 |
| B | Anran | +0.66% | +2.07% ±3.4 | Standard (+0.3%) | Neutral | - | 15 |
| B | Echo | +0.53% | +2.23% ±3.8 | Niche (-2.9%) | Neutral | - | 16 |
| B | Zarya | +0.38% | +0.87% ±2.7 | Standard (-0.6%) | Neutral | - | 16 |
| B | Kiriko | +0.36% | +0.51% ±1.6 | Map Priority (+3.5%) | Neutral | - | 16 |
| B | Emre | +0.25% | +3.02% ±2.6 | Standard (-0.3%) | Neutral | Better in GM+ | 16 |
| B | Sierra | +0.22% | -2.90% ±4.3 | Standard (-0.2%) | Neutral | Better in Masters | 10 |
| B | Reinhardt | +0.17% | +0.48% ±4.0 | Standard (-0.0%) | Neutral | Better in Masters | 16 |
| B | Lifeweaver | +0.13% | +4.67% ±4.9 | Standard (-0.9%) | Neutral | - | 16 |
| B | D.Va | +0.11% | +1.31% ±2.8 | Standard (+0.6%) | Neutral | - | 16 |
| B | Illari | +0.11% | +1.02% ±2.1 | Niche (-2.2%) | Neutral | - | 16 |
| B | Mizuki | +0.08% | +0.12% ±2.2 | Popular (+1.6%) | Neutral | - | 16 |
| B | Venture | +0.04% | +1.93% ±3.6 | Standard (-0.2%) | Neutral | - | 16 |
| B | Vendetta | +0.00% | +0.24% ±3.1 | Standard (+0.4%) | Neutral | Better in GM+ | 16 |
| B | Wrecking Ball | -0.02% | +0.14% ±2.8 | Popular (+1.9%) | Neutral | Better in GM+ | 16 |
| B | Tracer | -0.05% | +0.08% ±1.6 | Map Priority (+6.5%) | Neutral | - | 16 |
| B | Reaper | -0.08% | +0.29% ±2.8 | Standard (+0.4%) | Neutral | - | 16 |
| B | Orisa | -0.12% | -0.13% ±2.5 | Standard (+0.2%) | Neutral | Better in Masters | 16 |
| B | Winston | -0.14% | +0.08% ±2.4 | Standard (-0.7%) | Neutral | - | 16 |
| B | Mercy | -0.15% | +0.20% ±4.5 | Niche (-1.3%) | Neutral | Better in GM+ | 13 |
| B | Sojourn | -0.16% | -0.02% ±1.9 | Niche (-1.1%) | Neutral | - | 16 |
| B | Genji | -0.25% | -1.85% ±2.8 | Niche (-1.2%) | Neutral | - | 16 |
| B | D.Mon | -0.28% | -0.23% ±2.1 | Popular (+2.2%) | Neutral | - | 16 |
| B | Wuyang | -0.28% | -0.33% ±1.8 | Standard (+0.2%) | Neutral | - | 16 |
| B | Pharah | -0.31% | -0.05% ±2.8 | Niche (-2.6%) | Neutral | - | 16 |
| B | Ana | -0.39% | -0.38% ±1.6 | Niche (-2.7%) | Neutral | - | 16 |
| B | Mei | -0.47% | -1.72% ±3.6 | Standard (-0.7%) | Neutral | - | 16 |
| B | Sombra *(provisional)* | -0.47% | +0.00% ±4.5 | Map Priority (+3.5%) | Neutral | - | 8 |
| B | Symmetra | -0.48% | -0.47% ±3.9 | Standard (+0.4%) | Neutral | - | 16 |
| B | Shion | -0.49% | -0.73% ±1.8 | Map Priority (+4.5%) | Neutral | - | 16 |
| B | Juno | -0.55% | -0.26% ±2.8 | Standard (-0.7%) | Neutral | Better in Masters | 16 |
| B | Torbjörn | -0.62% | -1.16% ±4.2 | Standard (-0.3%) | Neutral | Better in Masters | 16 |
| B | Doomfist | -0.66% | -1.39% ±2.7 | Standard (+0.4%) | Neutral | Better in Masters | 16 |
| B | Hazard | -0.71% | -0.77% ±2.5 | Standard (-0.1%) | Neutral | Better in GM+ | 16 |
| B | Ashe | -0.73% | -0.62% ±3.1 | Niche (-3.2%) | Neutral | - | 16 |
| B | Baptiste | -0.73% | -1.03% ±3.1 | Niche (-1.6%) | Neutral | - | 16 |
| B | Bastion | -0.73% | -1.52% ±3.7 | Standard (-0.9%) | Neutral | - | 16 |
| B | Domina | -1.10% | -1.09% ±4.3 | Standard (-0.6%) | Neutral | - | 15 |
| C | Hanzo | -1.24% | -2.83% ±4.1 | Niche (-2.7%) | Unfavorable | - | 16 |
| C | Jetpack Cat | -1.25% | -1.70% ±3.0 | Standard (+0.6%) | Unfavorable | Better in Masters | 16 |
| C | Ramattra | -1.28% | -1.64% ±3.5 | Standard (-0.6%) | Unfavorable | Better in Masters | 16 |
| C | Brigitte | -1.50% | -2.23% ±2.9 | Popular (+1.2%) | Trap Pick | - | 16 |
| C | Sigma | -1.65% | -1.64% ±2.5 | Niche (-3.7%) | Deterrent | - | 16 |
| C | Doctrine *(provisional)* | -1.76% | -2.71% ±3.1 | Standard (-0.6%) | Deterrent | - | 8 |
| C | Lúcio | -1.87% | -1.85% ±2.9 | Popular (+1.8%) | Trap Pick | - | 16 |
| D | Junkrat | -3.19% | -7.87% ±5.1 | Niche (-1.1%) | Deterrent | Better in Masters | 16 |

### Circuit Royal

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| S | Sigma | +7.45% | +8.02% ±1.6 | Map Priority (+17.9%) | Meta | - | 52 |
| S | Domina | +5.64% | +6.60% ±1.9 | Map Priority (+4.5%) | Meta | - | 52 |
| S | Widowmaker | +5.63% | +5.92% ±2.5 | Map Priority (+8.3%) | Meta | - | 52 |
| S | Doctrine *(provisional)* | +3.09% | +6.31% ±4.1 | Map Priority (+3.4%) | Meta | - | 8 |
| A | Bastion | +2.61% | +4.27% ±2.9 | Map Priority (+3.0%) | Meta | - | 52 |
| A | Sojourn | +1.88% | +2.47% ±1.3 | Map Priority (+12.8%) | Meta | - | 52 |
| A | Symmetra | +1.68% | +2.48% ±2.3 | Standard (+0.3%) | Favorable | Better in GM+ | 51 |
| B | Mizuki | +1.20% | +1.91% ±2.8 | Niche (-5.2%) | Neutral | Better in GM+ | 51 |
| B | Mei | +1.19% | +3.29% ±2.3 | Map Priority (+3.3%) | Neutral | Better in GM+ | 51 |
| B | Reinhardt | +1.16% | +1.43% ±2.4 | Popular (+1.1%) | Neutral | - | 51 |
| B | Juno | +1.11% | +4.14% ±1.5 | Map Priority (+4.8%) | Neutral | - | 52 |
| B | Roadhog *(provisional)* | +1.01% | +7.51% ±8.8 | Niche (-2.0%) | Neutral | Better in GM+ | 8 |
| B | Zenyatta | +0.96% | +1.65% ±1.6 | Map Priority (+10.7%) | Neutral | - | 52 |
| B | Ramattra | +0.91% | +1.12% ±1.4 | Map Priority (+4.4%) | Neutral | - | 51 |
| B | Orisa | +0.78% | +1.26% ±2.4 | Standard (+1.0%) | Neutral | - | 51 |
| B | Illari | +0.75% | +1.85% ±1.3 | Map Priority (+6.2%) | Neutral | - | 52 |
| B | Baptiste | +0.62% | +2.30% ±2.5 | Map Priority (+8.1%) | Neutral | Better in Masters | 52 |
| B | Hanzo | +0.34% | +0.71% ±2.0 | Map Priority (+7.7%) | Neutral | - | 52 |
| B | Sierra | +0.22% | +2.45% ±1.8 | Popular (+1.5%) | Neutral | Better in GM+ | 39 |
| B | Lifeweaver | +0.13% | -0.27% ±2.5 | Popular (+1.3%) | Neutral | - | 51 |
| B | Wuyang | +0.07% | +0.33% ±2.3 | Standard (-0.3%) | Neutral | - | 52 |
| B | Venture | +0.04% | -1.00% ±3.1 | Standard (-0.5%) | Neutral | Better in GM+ | 52 |
| B | Reaper | -0.10% | +0.58% ±3.8 | Niche (-4.9%) | Neutral | - | 52 |
| B | Mercy | -0.13% | +0.02% ±2.6 | Popular (+1.7%) | Neutral | - | 51 |
| B | Genji | -0.15% | +0.05% ±2.0 | Standard (-0.9%) | Neutral | - | 52 |
| B | Emre | -0.19% | +0.28% ±2.1 | Map Priority (+5.0%) | Neutral | - | 52 |
| B | Ana | -0.41% | -0.41% ±1.4 | Map Priority (+7.7%) | Neutral | - | 52 |
| B | Freja | -0.50% | -0.47% ±2.4 | Map Priority (+5.4%) | Neutral | Better in Masters | 52 |
| B | Ashe | -0.55% | -0.02% ±2.6 | Map Priority (+7.9%) | Neutral | - | 52 |
| B | Cassidy | -0.67% | -0.87% ±1.8 | Niche (-15.9%) | Neutral | Better in Masters | 51 |
| B | Vendetta | -0.78% | -1.67% ±3.5 | Niche (-1.3%) | Neutral | - | 35 |
| B | Wrecking Ball | -1.07% | -1.41% ±3.0 | Niche (-2.6%) | Neutral | Better in Masters | 50 |
| C | Zarya | -1.22% | -1.29% ±1.9 | Standard (+0.6%) | Unfavorable | - | 52 |
| C | Doomfist | -1.35% | -4.16% ±3.1 | Niche (-2.2%) | Unfavorable | - | 52 |
| C | Junkrat | -1.40% | -1.72% ±2.1 | Standard (+0.1%) | Unfavorable | - | 52 |
| C | D.Va | -1.57% | -3.46% ±2.8 | Niche (-2.7%) | Deterrent | - | 52 |
| C | D.Mon | -1.65% | -4.38% ±4.4 | Niche (-3.5%) | Deterrent | Better in Masters | 16 |
| C | Moira | -1.65% | -2.31% ±3.6 | Niche (-3.3%) | Deterrent | - | 51 |
| C | Soldier: 76 | -1.77% | -2.50% ±2.1 | Niche (-2.7%) | Deterrent | Better in Masters | 51 |
| C | Anran | -1.78% | -3.09% ±2.6 | Niche (-1.9%) | Deterrent | - | 41 |
| C | Jetpack Cat | -1.86% | -2.54% ±2.9 | Niche (-2.1%) | Deterrent | - | 52 |
| C | Torbjörn | -1.93% | -3.15% ±3.4 | Standard (-0.6%) | Deterrent | Better in GM+ | 50 |
| C | Shion | -2.07% | -4.18% ±1.9 | Niche (-12.7%) | Deterrent | - | 28 |
| C | Echo | -2.40% | -3.11% ±2.0 | Niche (-1.1%) | Deterrent | - | 51 |
| C | Pharah | -2.55% | -3.09% ±2.7 | Popular (+2.3%) | Trap Pick | - | 51 |
| C | Kiriko | -2.78% | -3.63% ±1.6 | Niche (-18.1%) | Deterrent | - | 52 |
| C | Sombra *(provisional)* | -2.99% | -14.20% ±9.4 | Niche (-12.7%) | Deterrent | Better in Masters | 8 |
| D | Mauga | -3.54% | -4.78% ±2.3 | Niche (-2.3%) | Deterrent | - | 47 |
| D | Brigitte | -4.19% | -6.47% ±2.6 | Niche (-6.1%) | Deterrent | - | 48 |
| D | Tracer | -4.55% | -6.33% ±1.9 | Niche (-19.0%) | Deterrent | - | 51 |
| D | Hazard | -5.45% | -8.40% ±3.3 | Niche (-5.8%) | Deterrent | - | 43 |
| D | Junker Queen | -6.53% | -8.44% ±3.7 | Niche (-2.0%) | Deterrent | Better in Masters | 35 |
| D | Winston | -8.81% | -9.57% ±2.2 | Niche (-8.0%) | Deterrent | - | 51 |
| D | Lúcio | -9.30% | -9.93% ±2.4 | Niche (-6.3%) | Deterrent | - | 43 |

### Colosseo

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| S | Reinhardt | +3.95% | +4.49% ±2.1 | Standard (+0.3%) | Favorable | - | 51 |
| A | Lúcio | +2.60% | +2.89% ±2.0 | Popular (+1.4%) | Favorable | - | 52 |
| A | Torbjörn | +2.09% | +2.83% ±2.5 | Standard (-0.3%) | Specialist | - | 51 |
| A | Jetpack Cat | +2.08% | +2.57% ±2.1 | Standard (+0.3%) | Favorable | - | 52 |
| A | Junkrat | +2.07% | +2.76% ±2.4 | Standard (-0.6%) | Specialist | - | 51 |
| A | Doomfist | +1.74% | +3.12% ±1.6 | Standard (+1.0%) | Favorable | - | 52 |
| A | Tracer | +1.61% | +1.85% ±1.0 | Map Priority (+5.5%) | Meta | - | 52 |
| A | Anran | +1.42% | +2.48% ±2.2 | Standard (+0.2%) | Favorable | - | 49 |
| A | Sombra *(provisional)* | +1.25% | +4.38% ±5.0 | Popular (+2.7%) | Favorable | Better in GM+ | 8 |
| B | Junker Queen | +1.19% | +1.37% ±1.8 | Standard (+0.8%) | Neutral | - | 50 |
| B | Vendetta | +1.08% | +3.20% ±3.6 | Standard (+0.0%) | Neutral | Better in GM+ | 47 |
| B | Winston | +0.97% | +1.17% ±1.8 | Standard (+0.3%) | Neutral | - | 52 |
| B | Sojourn | +0.90% | +1.61% ±1.9 | Map Priority (+3.2%) | Neutral | - | 52 |
| B | Hazard | +0.77% | +0.90% ±1.3 | Standard (+0.4%) | Neutral | - | 51 |
| B | Shion | +0.67% | +1.08% ±1.2 | Map Priority (+4.6%) | Neutral | - | 28 |
| B | Freja | +0.61% | +1.25% ±1.9 | Standard (-1.0%) | Neutral | - | 51 |
| B | Kiriko | +0.61% | +0.84% ±1.6 | Popular (+2.3%) | Neutral | - | 52 |
| B | Wuyang | +0.57% | +1.24% ±2.2 | Standard (+0.8%) | Neutral | - | 52 |
| B | Illari | +0.53% | +1.15% ±1.1 | Standard (-0.5%) | Neutral | - | 52 |
| B | Wrecking Ball | +0.52% | +0.81% ±2.4 | Popular (+1.1%) | Neutral | Better in Masters | 52 |
| B | Mercy | +0.42% | +1.59% ±2.9 | Standard (-0.4%) | Neutral | - | 51 |
| B | Mei | +0.37% | +1.17% ±2.2 | Niche (-1.2%) | Neutral | - | 51 |
| B | Echo | +0.22% | +0.48% ±1.7 | Standard (-1.0%) | Neutral | - | 52 |
| B | Sierra | +0.22% | +1.05% ±3.6 | Standard (-0.1%) | Neutral | Better in GM+ | 36 |
| B | Soldier: 76 | +0.18% | +0.58% ±2.6 | Popular (+1.2%) | Neutral | - | 52 |
| B | D.Mon | +0.15% | +0.60% ±2.7 | Popular (+1.7%) | Neutral | - | 16 |
| B | Hanzo | +0.13% | +0.37% ±1.9 | Niche (-2.3%) | Neutral | - | 51 |
| B | Lifeweaver | +0.13% | +0.93% ±3.2 | Standard (-0.3%) | Neutral | Better in GM+ | 51 |
| B | Mizuki | +0.06% | +0.07% ±1.0 | Standard (+1.0%) | Neutral | - | 52 |
| B | Venture | +0.04% | -0.47% ±3.6 | Standard (-0.2%) | Neutral | Better in Masters | 52 |
| B | Juno | -0.15% | +0.67% ±1.6 | Standard (+0.8%) | Neutral | - | 51 |
| B | Genji | -0.16% | -0.06% ±2.2 | Niche (-1.1%) | Neutral | - | 52 |
| B | Zenyatta | -0.16% | +0.18% ±2.5 | Niche (-1.8%) | Neutral | Better in GM+ | 52 |
| B | Brigitte | -0.49% | -0.48% ±2.2 | Standard (-0.0%) | Neutral | - | 52 |
| B | Emre | -0.55% | -1.11% ±2.0 | Popular (+1.0%) | Neutral | - | 52 |
| B | Zarya | -0.67% | -0.60% ±2.5 | Standard (-0.2%) | Neutral | - | 52 |
| B | Mauga | -0.84% | -0.90% ±1.8 | Standard (+0.6%) | Neutral | - | 51 |
| B | Ashe | -0.89% | -0.99% ±1.5 | Niche (-2.8%) | Neutral | - | 51 |
| B | Roadhog *(provisional)* | -0.89% | -2.19% ±6.8 | Standard (-0.3%) | Neutral | - | 8 |
| B | Reaper | -0.92% | -1.63% ±2.9 | Standard (-0.8%) | Neutral | Better in Masters | 52 |
| B | Pharah | -0.95% | -0.93% ±3.1 | Standard (-0.2%) | Neutral | Better in Masters | 52 |
| B | Doctrine *(provisional)* | -1.15% | -2.41% ±4.5 | Popular (+2.0%) | Neutral | - | 8 |
| C | D.Va | -1.31% | -3.05% ±3.1 | Standard (-0.6%) | Unfavorable | - | 52 |
| C | Moira | -1.39% | -1.56% ±2.4 | Standard (+0.3%) | Unfavorable | - | 51 |
| C | Bastion | -1.45% | -1.88% ±1.9 | Niche (-1.0%) | Unfavorable | - | 49 |
| C | Baptiste | -1.48% | -2.19% ±1.9 | Niche (-1.7%) | Unfavorable | Better in Masters | 52 |
| C | Cassidy | -1.51% | -1.92% ±1.4 | Standard (+0.6%) | Unfavorable | - | 52 |
| C | Ramattra | -1.91% | -2.34% ±2.5 | Standard (-0.7%) | Deterrent | - | 50 |
| C | Symmetra | -2.35% | -3.63% ±3.2 | Standard (-0.9%) | Deterrent | - | 43 |
| C | Orisa | -2.49% | -2.83% ±1.2 | Standard (-0.1%) | Deterrent | - | 51 |
| C | Ana | -2.80% | -2.88% ±0.9 | Niche (-2.3%) | Deterrent | - | 52 |
| D | Sigma | -3.50% | -3.71% ±2.2 | Niche (-3.0%) | Deterrent | - | 52 |
| D | Domina | -3.68% | -4.56% ±2.9 | Standard (-0.3%) | Deterrent | Better in Masters | 48 |
| D | Widowmaker | -4.57% | -4.56% ±2.7 | Niche (-1.6%) | Deterrent | - | 52 |

### Dorado

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| S | Ana | +4.05% | +4.87% ±2.0 | Map Priority (+8.0%) | Meta | - | 52 |
| S | Winston | +3.88% | +4.29% ±1.8 | Map Priority (+13.8%) | Meta | - | 52 |
| S | Wrecking Ball | +3.74% | +5.02% ±2.3 | Standard (+0.9%) | Favorable | Better in Masters | 51 |
| A | Echo | +2.05% | +4.33% ±2.9 | Map Priority (+5.1%) | Meta | - | 52 |
| A | Doctrine *(provisional)* | +1.81% | +3.82% ±4.2 | Niche (-3.6%) | Specialist | Better in GM+ | 8 |
| A | Wuyang | +1.32% | +2.46% ±2.0 | Niche (-3.2%) | Favorable | - | 52 |
| A | Pharah | +1.29% | +2.03% ±2.6 | Standard (+0.0%) | Favorable | Better in Masters | 50 |
| B | Ashe | +0.96% | +3.66% ±2.1 | Map Priority (+6.6%) | Neutral | Better in GM+ | 52 |
| B | D.Mon | +0.70% | +3.42% ±4.7 | Niche (-3.3%) | Neutral | Better in GM+ | 16 |
| B | Doomfist | +0.64% | +1.92% ±2.2 | Standard (+0.4%) | Neutral | Better in GM+ | 51 |
| B | D.Va | +0.34% | +1.65% ±2.5 | Map Priority (+3.3%) | Neutral | - | 52 |
| B | Mauga | +0.29% | +1.31% ±3.8 | Niche (-1.1%) | Neutral | Better in GM+ | 49 |
| B | Sierra | +0.22% | -2.62% ±3.0 | Standard (+0.2%) | Neutral | Better in Masters | 36 |
| B | Hanzo | +0.21% | +0.59% ±2.2 | Standard (-0.6%) | Neutral | - | 52 |
| B | Lifeweaver | +0.13% | +2.13% ±2.9 | Popular (+1.6%) | Neutral | - | 49 |
| B | Venture | +0.04% | +0.67% ±3.7 | Standard (-0.1%) | Neutral | Better in Masters | 50 |
| B | Brigitte | -0.02% | +0.24% ±2.5 | Map Priority (+3.8%) | Neutral | - | 52 |
| B | Freja | -0.03% | +0.54% ±2.8 | Popular (+1.9%) | Neutral | - | 51 |
| B | Mercy | -0.07% | +0.23% ±2.9 | Popular (+2.3%) | Neutral | Better in Masters | 52 |
| B | Jetpack Cat | -0.08% | +0.00% ±3.5 | Popular (+1.5%) | Neutral | - | 52 |
| B | Genji | -0.09% | +0.77% ±1.9 | Popular (+2.5%) | Neutral | - | 51 |
| B | Roadhog *(provisional)* | -0.09% | +5.02% ±16.2 | Standard (-0.5%) | Neutral | - | 8 |
| B | Reaper | -0.11% | +0.28% ±3.0 | Popular (+1.9%) | Neutral | Better in GM+ | 52 |
| B | Soldier: 76 | -0.17% | -0.05% ±2.3 | Standard (+0.4%) | Neutral | - | 52 |
| B | Shion | -0.24% | -0.20% ±2.4 | Niche (-5.3%) | Neutral | Better in GM+ | 28 |
| B | Illari | -0.38% | -1.26% ±2.5 | Popular (+1.6%) | Neutral | Better in Masters | 52 |
| B | Sombra *(provisional)* | -0.43% | +0.59% ±6.2 | Standard (+0.1%) | Neutral | Better in GM+ | 8 |
| B | Mei | -0.59% | -2.36% ±3.6 | Standard (-0.9%) | Neutral | Better in GM+ | 51 |
| B | Anran | -0.61% | -1.17% ±3.5 | Standard (-0.5%) | Neutral | Better in GM+ | 49 |
| B | Cassidy | -0.62% | -0.67% ±0.9 | Niche (-1.4%) | Neutral | - | 52 |
| B | Emre | -0.65% | -2.07% ±2.6 | Standard (-0.3%) | Neutral | Better in Masters | 52 |
| B | Juno | -0.68% | -1.03% ±2.4 | Niche (-1.9%) | Neutral | - | 48 |
| B | Mizuki | -0.69% | -1.26% ±3.5 | Niche (-2.1%) | Neutral | Better in GM+ | 52 |
| B | Tracer | -0.85% | -0.98% ±1.7 | Niche (-1.7%) | Neutral | - | 52 |
| B | Vendetta | -0.98% | -2.74% ±4.2 | Standard (-0.2%) | Neutral | Better in Masters | 48 |
| B | Zenyatta | -1.03% | -1.91% ±3.0 | Niche (-2.2%) | Neutral | Better in Masters | 52 |
| C | Junkrat | -1.30% | -2.04% ±3.3 | Standard (+0.6%) | Unfavorable | Better in Masters | 50 |
| C | Bastion | -1.53% | -2.36% ±2.6 | Standard (+0.3%) | Unfavorable | Better in Masters | 49 |
| C | Baptiste | -1.78% | -3.80% ±2.8 | Standard (-0.6%) | Deterrent | - | 51 |
| C | Kiriko | -1.93% | -2.68% ±1.9 | Niche (-2.4%) | Deterrent | - | 52 |
| C | Hazard | -1.95% | -2.64% ±2.9 | Popular (+2.2%) | Trap Pick | - | 51 |
| C | Moira | -1.97% | -2.57% ±2.8 | Niche (-2.1%) | Deterrent | - | 50 |
| C | Symmetra | -1.99% | -3.09% ±3.3 | Standard (-0.7%) | Deterrent | - | 48 |
| C | Sojourn | -2.26% | -3.20% ±1.9 | Niche (-9.0%) | Deterrent | Better in Masters | 52 |
| C | Reinhardt | -2.56% | -3.05% ±3.0 | Niche (-2.4%) | Deterrent | - | 49 |
| C | Torbjörn | -2.64% | -3.69% ±2.7 | Standard (-0.1%) | Deterrent | - | 49 |
| C | Orisa | -2.65% | -5.19% ±3.3 | Niche (-3.3%) | Deterrent | Better in Masters | 51 |
| D | Ramattra | -3.74% | -6.85% ±4.1 | Niche (-2.5%) | Deterrent | - | 28 |
| D | Widowmaker | -3.97% | -3.95% ±2.4 | Standard (-0.3%) | Deterrent | - | 52 |
| D | Junker Queen | -4.38% | -5.62% ±3.9 | Niche (-1.5%) | Deterrent | - | 40 |
| D | Lúcio | -4.39% | -4.83% ±3.4 | Niche (-4.2%) | Deterrent | - | 49 |
| D | Domina | -5.38% | -7.15% ±3.2 | Niche (-1.5%) | Deterrent | Better in Masters | 44 |
| D | Zarya | -6.21% | -7.73% ±2.3 | Niche (-3.3%) | Deterrent | Better in Masters | 49 |
| D | Sigma | -6.99% | -8.15% ±3.1 | Niche (-4.4%) | Deterrent | Better in Masters | 52 |

### Eichenwalde

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| A | Ana | +2.55% | +3.71% ±2.9 | Map Priority (+3.5%) | Meta | - | 16 |
| A | Jetpack Cat | +1.93% | +5.41% ±5.8 | Standard (+0.5%) | Favorable | Better in Masters | 16 |
| A | Junkrat | +1.59% | +5.35% ±6.3 | Popular (+2.8%) | Meta | Better in GM+ | 16 |
| A | D.Mon | +1.41% | +5.87% ±4.7 | Popular (+1.5%) | Favorable | Better in GM+ | 16 |
| B | Roadhog *(provisional)* | +1.01% | +7.10% ±8.5 | Standard (-0.1%) | Neutral | Better in GM+ | 8 |
| B | Echo | +0.93% | +2.96% ±3.6 | Map Priority (+4.7%) | Neutral | - | 16 |
| B | Orisa | +0.72% | +1.65% ±3.5 | Popular (+1.7%) | Neutral | - | 16 |
| B | Junker Queen | +0.62% | +2.90% ±7.3 | Standard (-0.1%) | Neutral | Better in GM+ | 16 |
| B | Wuyang | +0.54% | +2.50% ±3.8 | Standard (-0.1%) | Neutral | Better in GM+ | 16 |
| B | Pharah | +0.39% | +2.09% ±5.1 | Map Priority (+3.3%) | Neutral | - | 16 |
| B | Sierra | +0.22% | +1.26% ±6.5 | Standard (+0.1%) | Neutral | Better in GM+ | 10 |
| B | Tracer | +0.15% | +0.95% ±3.3 | Niche (-3.7%) | Neutral | Better in GM+ | 16 |
| B | Lifeweaver | +0.13% | -0.23% ±12.7 | Standard (-0.2%) | Neutral | Better in GM+ | 16 |
| B | Mercy | +0.08% | +1.65% ±4.9 | Standard (+0.6%) | Neutral | - | 14 |
| B | Venture | +0.04% | +2.71% ±9.3 | Standard (+0.3%) | Neutral | - | 16 |
| B | Bastion | +0.01% | -0.01% ±5.2 | Popular (+1.0%) | Neutral | - | 16 |
| B | Vendetta | +0.00% | +0.64% ±5.1 | Standard (-0.0%) | Neutral | Better in Masters | 15 |
| B | Mei | -0.02% | +1.95% ±6.8 | Standard (+0.9%) | Neutral | - | 16 |
| B | Illari | -0.10% | +0.71% ±4.0 | Standard (-0.0%) | Neutral | - | 16 |
| B | Doomfist | -0.12% | +1.31% ±5.5 | Standard (-0.3%) | Neutral | Better in GM+ | 16 |
| B | Doctrine *(provisional)* | -0.19% | -0.44% ±5.9 | Standard (-0.4%) | Neutral | Better in GM+ | 8 |
| B | Genji | -0.19% | -0.69% ±3.3 | Standard (+0.6%) | Neutral | Better in Masters | 16 |
| B | Soldier: 76 | -0.25% | +0.53% ±8.1 | Niche (-2.6%) | Neutral | Better in GM+ | 16 |
| B | Mauga | -0.41% | +0.18% ±6.2 | Standard (-0.3%) | Neutral | Better in GM+ | 15 |
| B | Mizuki | -0.41% | -0.86% ±4.2 | Standard (-0.4%) | Neutral | Better in Masters | 16 |
| B | Sojourn | -0.44% | -0.49% ±4.2 | Niche (-4.5%) | Neutral | Better in GM+ | 16 |
| B | Domina | -0.46% | +0.28% ±5.2 | Standard (+0.2%) | Neutral | - | 16 |
| B | Emre | -0.55% | -4.47% ±5.2 | Niche (-1.0%) | Neutral | Better in Masters | 16 |
| B | Freja | -0.55% | -0.61% ±8.4 | Standard (+0.5%) | Neutral | Better in Masters | 16 |
| B | Hazard | -0.55% | -0.55% ±4.1 | Niche (-1.5%) | Neutral | Better in GM+ | 16 |
| B | D.Va | -0.59% | -0.92% ±6.5 | Standard (-0.6%) | Neutral | Better in Masters | 16 |
| B | Juno | -0.62% | -1.01% ±4.7 | Standard (-0.6%) | Neutral | Better in GM+ | 16 |
| B | Ramattra | -0.65% | -0.11% ±6.8 | Standard (+0.5%) | Neutral | Better in GM+ | 15 |
| B | Zenyatta | -0.65% | -1.93% ±6.1 | Popular (+1.7%) | Neutral | Better in GM+ | 16 |
| B | Cassidy | -0.66% | -1.01% ±2.4 | Map Priority (+4.8%) | Neutral | - | 16 |
| B | Ashe | -0.82% | -1.47% ±5.3 | Niche (-1.7%) | Neutral | Better in Masters | 16 |
| B | Shion | -0.82% | -2.63% ±3.2 | Niche (-3.6%) | Neutral | Better in Masters | 16 |
| B | Wrecking Ball | -0.87% | -1.94% ±6.3 | Standard (-0.7%) | Neutral | Better in Masters | 16 |
| B | Kiriko | -0.89% | -2.14% ±3.7 | Niche (-2.4%) | Neutral | Better in Masters | 16 |
| B | Torbjörn | -0.94% | -1.63% ±3.8 | Popular (+1.6%) | Neutral | - | 15 |
| B | Brigitte | -0.98% | -2.84% ±6.7 | Niche (-1.1%) | Neutral | - | 15 |
| B | Sombra *(provisional)* | -0.98% | -1.36% ±7.4 | Niche (-1.5%) | Neutral | Better in Masters | 8 |
| B | Anran | -1.07% | -6.24% ±7.0 | Standard (-0.2%) | Neutral | Better in Masters | 15 |
| B | Baptiste | -1.13% | -3.02% ±3.9 | Popular (+1.3%) | Neutral | - | 16 |
| C | Reaper | -1.46% | -4.23% ±4.0 | Standard (-0.1%) | Unfavorable | - | 16 |
| C | Symmetra | -1.49% | -5.84% ±8.0 | Standard (-0.4%) | Unfavorable | Better in Masters | 13 |
| C | Sigma | -1.74% | -1.75% ±4.3 | Standard (-0.6%) | Deterrent | Better in GM+ | 16 |
| C | Widowmaker | -2.14% | -1.86% ±4.8 | Niche (-2.9%) | Deterrent | Better in GM+ | 16 |
| C | Zarya | -2.18% | -5.65% ±7.1 | Popular (+1.4%) | Trap Pick | Better in Masters | 16 |
| C | Moira | -2.56% | -8.47% ±6.8 | Standard (-0.9%) | Deterrent | Better in Masters | 16 |
| C | Reinhardt | -2.73% | -4.59% ±5.5 | Popular (+1.5%) | Trap Pick | Better in Masters | 16 |
| C | Hanzo | -2.75% | -7.25% ±4.1 | Standard (+0.8%) | Unfavorable | - | 16 |
| D | Winston | -3.31% | -3.95% ±4.3 | Niche (-3.1%) | Deterrent | - | 16 |
| D | Lúcio | -3.84% | -4.44% ±4.6 | Niche (-1.3%) | Deterrent | - | 16 |

### Esperanca

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| A | Lúcio | +2.97% | +3.34% ±2.2 | Map Priority (+3.0%) | Meta | - | 52 |
| A | Winston | +2.22% | +2.50% ±1.7 | Map Priority (+4.0%) | Meta | - | 52 |
| A | Junker Queen | +1.61% | +1.93% ±2.2 | Standard (+0.8%) | Favorable | Better in GM+ | 49 |
| A | Soldier: 76 | +1.53% | +2.22% ±1.8 | Map Priority (+3.7%) | Meta | - | 51 |
| A | Kiriko | +1.50% | +1.69% ±1.0 | Map Priority (+7.4%) | Favorable | - | 52 |
| B | Reinhardt | +1.19% | +1.44% ±2.3 | Standard (-0.8%) | Neutral | - | 51 |
| B | Junkrat | +1.13% | +1.71% ±2.9 | Standard (-0.8%) | Neutral | - | 50 |
| B | Torbjörn | +0.99% | +1.48% ±2.9 | Standard (-0.5%) | Neutral | Better in GM+ | 50 |
| B | D.Mon | +0.96% | +2.30% ±3.0 | Standard (+0.9%) | Neutral | - | 16 |
| B | Echo | +0.77% | +1.14% ±1.6 | Standard (+0.4%) | Neutral | Better in GM+ | 52 |
| B | Hanzo | +0.69% | +1.45% ±2.4 | Niche (-3.4%) | Neutral | - | 49 |
| B | Jetpack Cat | +0.57% | +0.86% ±2.8 | Popular (+1.4%) | Neutral | - | 52 |
| B | Mauga | +0.56% | +0.93% ±2.0 | Popular (+1.4%) | Neutral | - | 51 |
| B | Shion | +0.51% | +0.69% ±0.8 | Map Priority (+6.4%) | Neutral | - | 28 |
| B | Vendetta | +0.50% | +1.41% ±3.2 | Standard (+0.3%) | Neutral | Better in GM+ | 47 |
| B | Moira | +0.45% | +1.37% ±2.8 | Standard (+0.9%) | Neutral | Better in GM+ | 52 |
| B | Doctrine *(provisional)* | +0.43% | +0.74% ±3.2 | Standard (+0.7%) | Neutral | - | 8 |
| B | Mei | +0.35% | +2.32% ±3.6 | Niche (-1.3%) | Neutral | - | 51 |
| B | Brigitte | +0.34% | +0.48% ±1.3 | Popular (+1.4%) | Neutral | - | 51 |
| B | Wrecking Ball | +0.33% | +0.54% ±2.2 | Popular (+1.7%) | Neutral | - | 52 |
| B | Bastion | +0.24% | +0.44% ±3.4 | Niche (-1.3%) | Neutral | - | 50 |
| B | Sierra | +0.22% | +0.88% ±2.5 | Standard (-0.3%) | Neutral | - | 33 |
| B | Mizuki | +0.15% | +0.18% ±1.4 | Popular (+1.0%) | Neutral | - | 52 |
| B | Lifeweaver | +0.13% | +1.05% ±2.7 | Standard (-0.7%) | Neutral | - | 50 |
| B | Wuyang | +0.09% | +0.39% ±2.5 | Standard (+0.1%) | Neutral | - | 52 |
| B | Venture | +0.04% | +0.61% ±2.2 | Standard (-0.3%) | Neutral | - | 48 |
| B | Sombra *(provisional)* | -0.00% | +0.95% ±4.3 | Map Priority (+5.7%) | Neutral | Better in Masters | 8 |
| B | Mercy | -0.05% | +0.06% ±1.6 | Standard (-0.7%) | Neutral | Better in Masters | 49 |
| B | Tracer | -0.07% | -0.00% ±1.2 | Map Priority (+8.8%) | Neutral | - | 52 |
| B | Symmetra | -0.08% | +0.31% ±3.7 | Standard (-0.8%) | Neutral | Better in GM+ | 45 |
| B | Doomfist | -0.10% | +0.10% ±2.0 | Standard (+0.3%) | Neutral | - | 52 |
| B | Emre | -0.10% | +0.77% ±2.3 | Standard (+0.5%) | Neutral | Better in Masters | 52 |
| B | Pharah | -0.10% | +0.18% ±2.6 | Standard (-0.9%) | Neutral | - | 50 |
| B | Sojourn | -0.10% | -0.06% ±0.9 | Standard (+0.0%) | Neutral | - | 52 |
| B | Genji | -0.11% | +0.53% ±1.9 | Standard (-0.7%) | Neutral | - | 52 |
| B | Reaper | -0.12% | +0.11% ±2.3 | Standard (-0.2%) | Neutral | Better in Masters | 51 |
| B | Hazard | -0.14% | -0.07% ±1.7 | Popular (+1.7%) | Neutral | - | 51 |
| B | Illari | -0.41% | -0.73% ±1.4 | Standard (-0.9%) | Neutral | - | 52 |
| B | Cassidy | -0.52% | -0.58% ±1.4 | Map Priority (+3.5%) | Neutral | - | 52 |
| B | Orisa | -0.57% | -0.96% ±3.0 | Niche (-1.1%) | Neutral | - | 52 |
| B | Ashe | -0.61% | -0.53% ±1.3 | Niche (-4.0%) | Neutral | - | 51 |
| B | Freja | -0.65% | -0.77% ±2.8 | Niche (-1.1%) | Neutral | Better in GM+ | 49 |
| B | Juno | -0.69% | -1.33% ±3.2 | Popular (+1.6%) | Neutral | - | 51 |
| B | Roadhog *(provisional)* | -0.97% | -2.40% ±6.6 | Standard (-0.3%) | Neutral | Better in GM+ | 8 |
| B | Baptiste | -1.00% | -1.61% ±2.6 | Niche (-2.6%) | Neutral | Better in Masters | 51 |
| C | Anran | -1.23% | -2.14% ±2.7 | Standard (+0.2%) | Unfavorable | Better in Masters | 49 |
| C | D.Va | -1.47% | -2.25% ±1.9 | Popular (+1.5%) | Unfavorable | - | 51 |
| C | Zarya | -1.63% | -1.98% ±3.0 | Niche (-1.3%) | Deterrent | - | 52 |
| C | Zenyatta | -1.67% | -2.36% ±1.8 | Niche (-4.0%) | Deterrent | - | 51 |
| C | Ana | -1.97% | -2.29% ±2.1 | Niche (-7.7%) | Deterrent | - | 52 |
| C | Domina | -2.32% | -2.91% ±3.5 | Niche (-1.4%) | Deterrent | - | 47 |
| C | Ramattra | -2.35% | -3.19% ±2.9 | Niche (-1.6%) | Deterrent | Better in Masters | 47 |
| D | Sigma | -4.99% | -5.81% ±3.3 | Niche (-5.7%) | Deterrent | Better in Masters | 52 |
| D | Widowmaker | -15.34% | -15.60% ±2.3 | Niche (-4.5%) | Deterrent | - | 49 |

### Grimsvotn

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| S | Junkrat *(provisional)* | +3.76% | +8.38% ±4.6 | Popular (+1.4%) | Favorable | Better in GM+ | 8 |
| A | Mizuki *(provisional)* | +2.04% | +7.19% ±5.8 | Standard (-0.7%) | Specialist | Better in GM+ | 8 |
| A | Jetpack Cat *(provisional)* | +1.53% | +4.67% ±6.1 | Niche (-2.9%) | Specialist | Better in GM+ | 8 |
| A | Lúcio *(provisional)* | +1.47% | +5.54% ±8.6 | Niche (-1.2%) | Favorable | Better in GM+ | 6 |
| A | Ana *(provisional)* | +1.28% | +1.89% ±2.8 | Popular (+2.9%) | Favorable | - | 8 |
| A | Hanzo *(provisional)* | +1.26% | +5.07% ±4.3 | Map Priority (+3.3%) | Favorable | - | 8 |
| B | Ramattra *(provisional)* | +0.67% | +3.35% ±5.2 | Popular (+2.2%) | Neutral | Better in GM+ | 8 |
| B | Orisa *(provisional)* | +0.61% | +1.93% ±4.5 | Map Priority (+4.1%) | Neutral | Better in Masters | 8 |
| B | Vendetta *(provisional)* | +0.59% | +4.66% ±6.4 | Standard (-0.6%) | Neutral | Better in GM+ | 8 |
| B | Anran *(provisional)* | +0.42% | +5.68% ±7.7 | Standard (-0.3%) | Neutral | Better in GM+ | 7 |
| B | Hazard *(provisional)* | +0.33% | +1.68% ±5.2 | Niche (-3.8%) | Neutral | Better in GM+ | 8 |
| B | Brigitte *(provisional)* | +0.26% | +2.32% ±5.4 | Niche (-2.0%) | Neutral | Better in GM+ | 8 |
| B | Sierra *(provisional)* | +0.22% | +2.00% ±5.4 | Standard (+0.5%) | Neutral | Better in Masters | 8 |
| B | Kiriko *(provisional)* | +0.18% | +0.56% ±3.1 | Niche (-2.5%) | Neutral | - | 8 |
| B | Bastion *(provisional)* | +0.14% | +0.37% ±4.8 | Popular (+1.6%) | Neutral | - | 8 |
| B | Lifeweaver *(provisional)* | +0.13% | -2.05% ±5.2 | Standard (+0.1%) | Neutral | - | 8 |
| B | Torbjörn *(provisional)* | +0.13% | +0.40% ±4.8 | Standard (+0.4%) | Neutral | - | 8 |
| B | Symmetra *(provisional)* | +0.09% | +2.24% ±7.3 | Standard (-0.0%) | Neutral | Better in GM+ | 8 |
| B | Roadhog *(provisional)* | +0.05% | +1.68% ±7.7 | Standard (+0.6%) | Neutral | Better in Masters | 8 |
| B | Venture *(provisional)* | +0.04% | +1.89% ±5.7 | Standard (-0.0%) | Neutral | Better in GM+ | 8 |
| B | Reinhardt *(provisional)* | +0.03% | +0.37% ±4.5 | Popular (+2.1%) | Neutral | - | 8 |
| B | Sigma *(provisional)* | +0.03% | +0.66% ±3.9 | Map Priority (+6.2%) | Neutral | - | 8 |
| B | Sombra *(provisional)* | -0.10% | +1.79% ±6.4 | Niche (-4.1%) | Neutral | Better in GM+ | 8 |
| B | Echo *(provisional)* | -0.12% | +2.61% ±7.3 | Niche (-1.1%) | Neutral | Better in GM+ | 8 |
| B | Genji *(provisional)* | -0.15% | +0.72% ±3.6 | Standard (-0.9%) | Neutral | - | 8 |
| B | Cassidy *(provisional)* | -0.16% | +0.07% ±3.0 | Niche (-1.2%) | Neutral | - | 8 |
| B | Mei *(provisional)* | -0.16% | -0.19% ±8.7 | Popular (+2.0%) | Neutral | - | 8 |
| B | Illari *(provisional)* | -0.21% | -3.47% ±11.2 | Standard (-0.1%) | Neutral | Better in Masters | 8 |
| B | Reaper *(provisional)* | -0.21% | +0.93% ±6.4 | Standard (-0.8%) | Neutral | Better in Masters | 8 |
| B | Sojourn *(provisional)* | -0.30% | -0.17% ±2.8 | Map Priority (+5.6%) | Neutral | - | 8 |
| B | Wuyang *(provisional)* | -0.30% | -0.75% ±4.5 | Popular (+2.8%) | Neutral | - | 8 |
| B | Doomfist *(provisional)* | -0.31% | -0.46% ±6.0 | Standard (-0.8%) | Neutral | Better in Masters | 8 |
| B | Wrecking Ball *(provisional)* | -0.31% | +0.03% ±8.0 | Niche (-2.2%) | Neutral | Better in GM+ | 8 |
| B | Zarya *(provisional)* | -0.31% | +0.52% ±5.2 | Popular (+2.9%) | Neutral | - | 8 |
| B | Soldier: 76 *(provisional)* | -0.36% | -0.41% ±6.7 | Niche (-1.9%) | Neutral | Better in GM+ | 8 |
| B | Tracer *(provisional)* | -0.39% | -0.25% ±3.7 | Niche (-9.8%) | Neutral | - | 8 |
| B | Emre *(provisional)* | -0.41% | -1.37% ±4.4 | Standard (+0.7%) | Neutral | Better in Masters | 8 |
| B | D.Va *(provisional)* | -0.55% | -0.53% ±5.4 | Niche (-3.8%) | Neutral | Better in Masters | 8 |
| B | Junker Queen *(provisional)* | -0.58% | -0.10% ±6.0 | Standard (+0.1%) | Neutral | Better in GM+ | 7 |
| B | D.Mon *(provisional)* | -0.59% | -1.02% ±4.4 | Standard (-0.1%) | Neutral | - | 8 |
| B | Juno *(provisional)* | -0.59% | -0.32% ±5.8 | Standard (-0.1%) | Neutral | - | 7 |
| B | Doctrine *(provisional)* | -0.62% | -1.39% ±4.9 | Map Priority (+4.1%) | Neutral | Better in Masters | 8 |
| B | Shion *(provisional)* | -0.67% | -1.61% ±2.7 | Standard (-0.9%) | Neutral | Better in Masters | 8 |
| B | Zenyatta *(provisional)* | -0.67% | -1.71% ±5.3 | Map Priority (+3.9%) | Neutral | Better in GM+ | 8 |
| B | Mercy *(provisional)* | -0.68% | -2.86% ±4.8 | Standard (-0.4%) | Neutral | Better in Masters | 7 |
| B | Mauga *(provisional)* | -0.75% | -1.28% ±6.7 | Standard (-0.3%) | Neutral | - | 6 |
| B | Baptiste *(provisional)* | -0.82% | -3.11% ±6.5 | Standard (+0.9%) | Neutral | - | 8 |
| B | Freja *(provisional)* | -1.01% | -4.47% ±7.2 | Standard (+0.0%) | Neutral | Better in Masters | 8 |
| C | Domina *(provisional)* | -1.21% | -1.33% ±5.6 | Map Priority (+3.1%) | Unfavorable | - | 8 |
| C | Ashe *(provisional)* | -1.27% | -4.27% ±4.0 | Standard (+0.8%) | Unfavorable | - | 8 |
| C | Moira *(provisional)* | -2.04% | -5.31% ±6.3 | Standard (-0.8%) | Deterrent | Better in Masters | 8 |
| C | Pharah *(provisional)* | -2.38% | -3.90% ±4.8 | Standard (+0.1%) | Unfavorable | Better in Masters | 8 |
| C | Winston *(provisional)* | -2.88% | -3.39% ±4.5 | Niche (-10.1%) | Deterrent | Better in GM+ | 8 |
| D | Widowmaker *(provisional)* | -3.17% | -3.03% ±4.3 | Popular (+1.4%) | Trap Pick | - | 8 |

### Havana

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| S | Widowmaker | +5.88% | +6.19% ±2.5 | Map Priority (+11.9%) | Meta | Better in GM+ | 52 |
| S | Sigma | +5.72% | +6.19% ±1.6 | Map Priority (+16.1%) | Meta | - | 51 |
| S | Zenyatta | +3.33% | +4.93% ±1.5 | Map Priority (+11.6%) | Meta | - | 51 |
| A | Ana | +1.81% | +2.00% ±1.3 | Map Priority (+13.3%) | Meta | - | 51 |
| A | Doctrine *(provisional)* | +1.56% | +3.52% ±4.5 | Standard (+0.3%) | Favorable | - | 8 |
| A | Domina | +1.38% | +2.08% ±2.6 | Map Priority (+4.6%) | Favorable | - | 50 |
| A | Orisa | +1.24% | +2.49% ±3.2 | Standard (+0.3%) | Favorable | - | 51 |
| B | Bastion | +1.15% | +1.58% ±2.2 | Standard (+1.0%) | Neutral | - | 49 |
| B | Hanzo | +0.51% | +1.00% ±2.1 | Map Priority (+9.7%) | Neutral | - | 52 |
| B | Soldier: 76 | +0.48% | +1.35% ±3.0 | Standard (-0.7%) | Neutral | - | 51 |
| B | Baptiste | +0.31% | +1.29% ±2.2 | Map Priority (+3.7%) | Neutral | - | 51 |
| B | Sierra | +0.22% | +1.77% ±3.4 | Popular (+1.4%) | Neutral | Better in Masters | 37 |
| B | Illari | +0.21% | +1.39% ±2.1 | Map Priority (+6.0%) | Neutral | Better in GM+ | 52 |
| B | Emre | +0.15% | +0.89% ±1.5 | Map Priority (+3.9%) | Neutral | - | 52 |
| B | Lifeweaver | +0.13% | +1.28% ±2.6 | Popular (+1.2%) | Neutral | - | 50 |
| B | Ashe | +0.07% | +1.03% ±1.8 | Map Priority (+8.1%) | Neutral | - | 51 |
| B | Venture | +0.04% | -0.77% ±4.0 | Standard (-0.6%) | Neutral | - | 47 |
| B | Torbjörn | +0.02% | +0.06% ±2.9 | Standard (+0.2%) | Neutral | - | 50 |
| B | Tracer | -0.08% | +0.28% ±2.8 | Niche (-11.6%) | Neutral | - | 52 |
| B | Sojourn | -0.14% | +0.09% ±2.3 | Map Priority (+7.1%) | Neutral | Better in Masters | 52 |
| B | Freja | -0.15% | +0.30% ±2.9 | Popular (+2.1%) | Neutral | - | 51 |
| B | Genji | -0.15% | +0.32% ±3.2 | Standard (+0.9%) | Neutral | Better in Masters | 52 |
| B | Sombra *(provisional)* | -0.17% | +1.93% ±7.1 | Niche (-5.6%) | Neutral | - | 8 |
| B | Roadhog *(provisional)* | -0.25% | +1.60% ±14.0 | Standard (-0.5%) | Neutral | - | 8 |
| B | D.Va | -0.30% | +0.06% ±2.5 | Niche (-1.8%) | Neutral | Better in GM+ | 51 |
| B | Juno | -0.48% | +0.21% ±2.8 | Niche (-2.0%) | Neutral | - | 49 |
| B | Mercy | -0.58% | -1.40% ±3.3 | Popular (+1.9%) | Neutral | - | 50 |
| B | Shion | -0.71% | -2.05% ±3.0 | Niche (-10.0%) | Neutral | - | 28 |
| B | Mei | -0.72% | -2.51% ±3.2 | Standard (+0.9%) | Neutral | Better in Masters | 51 |
| B | D.Mon | -0.83% | -3.47% ±7.3 | Niche (-2.4%) | Neutral | Better in Masters | 15 |
| B | Anran | -0.90% | -2.06% ±3.8 | Standard (-1.0%) | Neutral | - | 46 |
| B | Reaper | -1.07% | -2.45% ±3.5 | Niche (-4.2%) | Neutral | Better in GM+ | 51 |
| B | Junkrat | -1.10% | -2.04% ±4.0 | Niche (-1.0%) | Neutral | - | 49 |
| B | Wuyang | -1.15% | -2.78% ±3.0 | Niche (-1.4%) | Neutral | - | 52 |
| C | Cassidy | -1.32% | -2.21% ±2.3 | Niche (-13.4%) | Unfavorable | - | 51 |
| C | Hazard | -1.33% | -1.94% ±3.7 | Niche (-5.1%) | Unfavorable | Better in GM+ | 46 |
| C | Symmetra | -1.34% | -2.12% ±3.7 | Standard (+0.2%) | Unfavorable | - | 48 |
| C | Mauga | -1.35% | -1.88% ±3.0 | Niche (-2.1%) | Unfavorable | - | 47 |
| C | Doomfist | -1.43% | -3.19% ±2.4 | Niche (-1.4%) | Unfavorable | - | 51 |
| C | Vendetta | -1.47% | -4.03% ±4.0 | Standard (-1.0%) | Unfavorable | - | 37 |
| C | Moira | -1.55% | -2.23% ±4.0 | Niche (-3.3%) | Deterrent | Better in Masters | 50 |
| C | Mizuki | -1.64% | -2.57% ±2.9 | Niche (-4.9%) | Deterrent | Better in GM+ | 50 |
| C | Ramattra | -1.83% | -2.28% ±2.6 | Popular (+1.5%) | Trap Pick | - | 50 |
| C | Brigitte | -2.00% | -3.02% ±2.8 | Niche (-4.5%) | Deterrent | - | 48 |
| C | Zarya | -2.01% | -2.50% ±2.9 | Standard (-0.8%) | Deterrent | - | 50 |
| C | Echo | -2.10% | -3.04% ±2.5 | Niche (-3.8%) | Deterrent | Better in GM+ | 47 |
| C | Kiriko | -2.18% | -3.48% ±2.3 | Niche (-12.8%) | Deterrent | Better in Masters | 52 |
| C | Wrecking Ball | -2.29% | -4.10% ±4.1 | Niche (-2.5%) | Deterrent | Better in Masters | 50 |
| C | Pharah | -2.85% | -4.03% ±3.7 | Niche (-2.2%) | Deterrent | - | 49 |
| D | Reinhardt | -3.20% | -3.87% ±3.0 | Standard (+0.5%) | Unfavorable | - | 51 |
| D | Jetpack Cat | -3.39% | -6.18% ±4.3 | Niche (-2.6%) | Deterrent | Better in Masters | 51 |
| D | Junker Queen | -4.87% | -6.24% ±3.8 | Niche (-1.7%) | Deterrent | Better in Masters | 38 |
| D | Winston | -6.74% | -7.42% ±2.4 | Niche (-5.0%) | Deterrent | - | 51 |
| D | Lúcio | -8.62% | -9.40% ±2.7 | Niche (-5.7%) | Deterrent | Better in Masters | 46 |

### Hollywood

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| A | Zarya | +1.43% | +2.30% ±2.6 | Popular (+1.0%) | Favorable | Better in GM+ | 51 |
| B | Ana | +0.99% | +1.11% ±1.3 | Map Priority (+7.5%) | Neutral | - | 52 |
| B | Sierra | +0.22% | -0.56% ±2.9 | Standard (+0.1%) | Neutral | - | 34 |
| B | Lifeweaver | +0.13% | -1.88% ±2.5 | Popular (+1.0%) | Neutral | - | 50 |
| B | Venture | +0.04% | -4.47% ±3.9 | Standard (-0.3%) | Neutral | - | 50 |
| B | Hanzo | +0.01% | +0.64% ±3.5 | Popular (+1.8%) | Neutral | - | 52 |
| B | D.Va | -0.09% | +0.44% ±2.2 | Standard (+0.2%) | Neutral | - | 51 |
| B | Doctrine *(provisional)* | -0.10% | -0.12% ±4.1 | Standard (+0.2%) | Neutral | - | 6 |
| B | Roadhog *(provisional)* | -0.13% | +4.40% ±16.4 | Standard (+0.4%) | Neutral | Better in GM+ | 6 |
| B | Genji | -0.15% | +0.13% ±2.2 | Popular (+1.5%) | Neutral | - | 51 |
| B | Shion | -0.20% | +0.02% ±3.1 | Niche (-4.1%) | Neutral | Better in Masters | 28 |
| B | Winston | -0.22% | -0.12% ±1.7 | Popular (+2.9%) | Neutral | - | 52 |
| B | Wuyang | -0.25% | -0.35% ±2.8 | Standard (-0.5%) | Neutral | - | 52 |
| B | Ashe | -0.31% | +0.58% ±2.3 | Map Priority (+4.3%) | Neutral | - | 52 |
| B | Doomfist | -0.37% | -0.64% ±3.5 | Standard (-0.6%) | Neutral | Better in Masters | 51 |
| B | Emre | -0.37% | -0.54% ±3.2 | Standard (-0.1%) | Neutral | - | 52 |
| B | Kiriko | -0.37% | -0.49% ±2.0 | Niche (-4.7%) | Neutral | - | 52 |
| B | Mei | -0.39% | -0.99% ±2.9 | Standard (+0.6%) | Neutral | Better in GM+ | 51 |
| B | Illari | -0.40% | -1.72% ±2.9 | Standard (+1.0%) | Neutral | - | 52 |
| B | Tracer | -0.40% | -0.37% ±2.1 | Niche (-3.3%) | Neutral | Better in GM+ | 52 |
| B | Mercy | -0.45% | -0.87% ±3.0 | Popular (+1.2%) | Neutral | - | 51 |
| B | Bastion | -0.52% | -0.84% ±2.8 | Standard (+0.6%) | Neutral | Better in GM+ | 51 |
| B | Freja | -0.55% | -0.55% ±2.9 | Standard (+0.3%) | Neutral | Better in GM+ | 51 |
| B | Domina | -0.61% | -0.41% ±3.2 | Standard (+0.3%) | Neutral | - | 52 |
| B | Zenyatta | -0.66% | -0.98% ±2.9 | Popular (+1.7%) | Neutral | - | 52 |
| B | Ramattra | -0.69% | -0.53% ±4.3 | Standard (-0.5%) | Neutral | - | 51 |
| B | Juno | -0.85% | -2.51% ±3.0 | Standard (-0.9%) | Neutral | - | 52 |
| B | Baptiste | -0.87% | -1.32% ±2.7 | Standard (+0.8%) | Neutral | - | 52 |
| B | Hazard | -0.87% | -1.04% ±3.0 | Standard (-0.6%) | Neutral | - | 50 |
| B | D.Mon | -0.94% | -2.83% ±5.5 | Standard (-0.7%) | Neutral | Better in Masters | 16 |
| B | Anran | -1.01% | -2.27% ±3.6 | Standard (-0.2%) | Neutral | Better in Masters | 52 |
| B | Sombra *(provisional)* | -1.10% | -1.82% ±7.2 | Niche (-3.6%) | Neutral | Better in Masters | 6 |
| B | Echo | -1.11% | -1.37% ±2.3 | Standard (+0.3%) | Neutral | - | 52 |
| C | Reaper | -1.25% | -2.67% ±3.2 | Standard (-0.2%) | Unfavorable | - | 52 |
| C | Mizuki | -1.29% | -1.55% ±1.7 | Standard (-1.0%) | Unfavorable | - | 52 |
| C | Wrecking Ball | -1.29% | -1.53% ±2.2 | Standard (-1.0%) | Unfavorable | - | 50 |
| C | Cassidy | -1.30% | -1.71% ±1.6 | Niche (-1.4%) | Unfavorable | - | 52 |
| C | Orisa | -1.31% | -2.12% ±2.7 | Standard (-0.4%) | Unfavorable | Better in Masters | 52 |
| C | Moira | -1.35% | -1.53% ±2.5 | Standard (-1.0%) | Unfavorable | Better in GM+ | 51 |
| C | Pharah | -1.45% | -1.55% ±2.1 | Standard (-0.3%) | Unfavorable | - | 50 |
| C | Torbjörn | -1.58% | -2.19% ±2.6 | Standard (+0.9%) | Unfavorable | Better in Masters | 51 |
| C | Brigitte | -1.62% | -2.07% ±2.1 | Standard (-0.7%) | Deterrent | - | 51 |
| C | Vendetta | -1.85% | -2.97% ±2.3 | Standard (-0.1%) | Deterrent | - | 46 |
| C | Soldier: 76 | -2.09% | -3.56% ±2.7 | Niche (-2.1%) | Deterrent | Better in Masters | 50 |
| C | Junkrat | -2.18% | -2.79% ±2.3 | Standard (+0.7%) | Unfavorable | Better in Masters | 50 |
| C | Widowmaker | -2.18% | -2.15% ±1.5 | Popular (+2.4%) | Trap Pick | - | 52 |
| C | Symmetra | -2.50% | -4.86% ±4.2 | Standard (-0.1%) | Deterrent | - | 51 |
| C | Sojourn | -2.60% | -3.84% ±2.0 | Niche (-2.7%) | Deterrent | Better in Masters | 52 |
| C | Sigma | -2.77% | -2.93% ±2.6 | Popular (+1.5%) | Trap Pick | Better in Masters | 52 |
| C | Jetpack Cat | -2.80% | -4.29% ±3.5 | Standard (-0.8%) | Deterrent | - | 52 |
| D | Mauga | -3.73% | -4.91% ±2.2 | Niche (-1.1%) | Deterrent | - | 47 |
| D | Junker Queen | -3.96% | -5.01% ±3.8 | Standard (-0.8%) | Deterrent | Better in GM+ | 45 |
| D | Lúcio | -5.21% | -5.38% ±1.8 | Niche (-3.5%) | Deterrent | - | 47 |
| D | Reinhardt | -7.77% | -9.47% ±2.9 | Standard (-0.6%) | Deterrent | Better in Masters | 51 |

### Ilios

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| S | Lúcio | +4.31% | +4.71% ±2.0 | Map Priority (+6.4%) | Meta | - | 52 |
| S | Hazard | +3.18% | +3.42% ±1.1 | Map Priority (+3.9%) | Meta | - | 51 |
| A | Jetpack Cat | +2.90% | +4.20% ±2.9 | Map Priority (+3.2%) | Meta | - | 52 |
| A | Torbjörn | +2.29% | +2.77% ±1.9 | Standard (-0.4%) | Specialist | - | 51 |
| A | Pharah | +1.86% | +2.05% ±1.2 | Popular (+1.7%) | Meta | - | 51 |
| A | Echo | +1.75% | +2.04% ±1.1 | Map Priority (+5.6%) | Meta | - | 52 |
| A | Junkrat | +1.58% | +2.22% ±2.6 | Standard (-0.8%) | Specialist | - | 51 |
| A | Junker Queen | +1.31% | +1.78% ±2.8 | Standard (+0.2%) | Favorable | - | 47 |
| A | Winston | +1.30% | +1.46% ±1.5 | Map Priority (+5.7%) | Favorable | - | 52 |
| B | Vendetta | +1.17% | +1.65% ±1.7 | Standard (+0.3%) | Neutral | Better in GM+ | 47 |
| B | Kiriko | +0.80% | +1.01% ±1.3 | Map Priority (+5.4%) | Neutral | - | 52 |
| B | Mercy | +0.71% | +1.12% ±1.4 | Standard (-0.3%) | Neutral | - | 50 |
| B | Anran | +0.64% | +0.93% ±1.6 | Standard (+0.5%) | Neutral | - | 49 |
| B | Freja | +0.56% | +1.12% ±1.9 | Popular (+2.2%) | Neutral | - | 52 |
| B | Reaper | +0.41% | +0.65% ±1.4 | Popular (+2.6%) | Neutral | - | 52 |
| B | Widowmaker | +0.41% | +0.49% ±1.9 | Standard (-0.7%) | Neutral | Better in GM+ | 52 |
| B | Wrecking Ball | +0.41% | +0.67% ±2.4 | Popular (+2.5%) | Neutral | Better in GM+ | 52 |
| B | Sombra *(provisional)* | +0.32% | +1.73% ±4.5 | Map Priority (+4.9%) | Neutral | Better in GM+ | 8 |
| B | Bastion | +0.29% | +0.37% ±1.9 | Niche (-1.6%) | Neutral | - | 48 |
| B | Zenyatta | +0.27% | +0.41% ±1.0 | Niche (-4.1%) | Neutral | - | 50 |
| B | Sierra | +0.22% | -0.01% ±2.0 | Standard (-0.8%) | Neutral | Better in GM+ | 32 |
| B | Symmetra | +0.17% | +0.33% ±1.9 | Standard (-0.0%) | Neutral | - | 52 |
| B | Lifeweaver | +0.13% | -1.64% ±1.6 | Standard (-0.5%) | Neutral | - | 50 |
| B | Venture | +0.04% | -0.60% ±2.3 | Standard (+0.4%) | Neutral | Better in Masters | 52 |
| B | D.Va | -0.06% | +0.57% ±2.4 | Popular (+2.8%) | Neutral | - | 52 |
| B | Juno | -0.08% | +0.30% ±1.0 | Standard (+0.4%) | Neutral | - | 51 |
| B | Genji | -0.09% | +0.80% ±1.9 | Standard (+0.3%) | Neutral | - | 52 |
| B | Moira | -0.18% | -0.09% ±1.1 | Standard (+1.0%) | Neutral | - | 51 |
| B | Doomfist | -0.24% | -0.20% ±1.7 | Standard (+0.9%) | Neutral | - | 52 |
| B | Emre | -0.29% | -0.13% ±2.1 | Niche (-3.1%) | Neutral | Better in GM+ | 52 |
| B | Cassidy | -0.30% | -0.30% ±1.0 | Map Priority (+5.5%) | Neutral | - | 52 |
| B | Shion | -0.48% | -0.53% ±0.9 | Popular (+1.7%) | Neutral | - | 28 |
| B | Ashe | -0.67% | -0.58% ±1.5 | Niche (-4.2%) | Neutral | Better in GM+ | 51 |
| B | Brigitte | -0.67% | -0.74% ±2.2 | Map Priority (+3.4%) | Neutral | Better in Masters | 52 |
| B | Roadhog *(provisional)* | -0.67% | -1.19% ±5.9 | Popular (+1.1%) | Neutral | - | 8 |
| B | Baptiste | -0.71% | -0.80% ±1.7 | Niche (-2.0%) | Neutral | - | 51 |
| B | Illari | -0.79% | -2.34% ±1.9 | Niche (-2.9%) | Neutral | - | 52 |
| B | D.Mon | -0.81% | -1.11% ±2.5 | Niche (-1.1%) | Neutral | - | 16 |
| B | Hanzo | -0.82% | -0.96% ±1.8 | Niche (-3.0%) | Neutral | - | 52 |
| B | Orisa | -0.99% | -1.10% ±1.1 | Niche (-1.0%) | Neutral | - | 50 |
| B | Mizuki | -1.02% | -1.22% ±1.7 | Popular (+1.4%) | Neutral | Better in Masters | 52 |
| B | Sojourn | -1.11% | -1.44% ±1.8 | Niche (-7.6%) | Neutral | Better in Masters | 52 |
| C | Tracer | -1.26% | -1.73% ±2.2 | Map Priority (+6.5%) | Unfavorable | - | 52 |
| C | Reinhardt | -1.33% | -1.38% ±1.6 | Niche (-2.0%) | Unfavorable | - | 50 |
| C | Wuyang | -1.45% | -1.83% ±1.3 | Niche (-3.5%) | Unfavorable | - | 52 |
| C | Ana | -1.59% | -1.61% ±0.7 | Niche (-7.5%) | Deterrent | - | 52 |
| C | Mei | -1.75% | -3.82% ±2.1 | Niche (-1.6%) | Deterrent | - | 50 |
| C | Soldier: 76 | -2.04% | -2.80% ±2.0 | Niche (-3.5%) | Deterrent | - | 51 |
| C | Ramattra | -2.06% | -2.57% ±2.5 | Niche (-2.4%) | Deterrent | Better in Masters | 36 |
| C | Mauga | -2.13% | -2.48% ±1.7 | Standard (-0.2%) | Deterrent | - | 49 |
| C | Zarya | -2.51% | -2.71% ±1.5 | Niche (-2.7%) | Deterrent | Better in GM+ | 50 |
| D | Doctrine *(provisional)* | -3.75% | -6.06% ±3.3 | Niche (-5.3%) | Deterrent | Better in Masters | 8 |
| D | Domina | -4.57% | -6.23% ±3.4 | Niche (-2.0%) | Deterrent | Better in Masters | 43 |
| D | Sigma | -4.59% | -4.73% ±1.5 | Niche (-7.6%) | Deterrent | - | 51 |

### Junkertown

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| S | Widowmaker | +5.82% | +6.00% ±1.9 | Map Priority (+8.1%) | Meta | - | 52 |
| A | Sigma | +2.61% | +3.13% ±2.3 | Map Priority (+9.6%) | Meta | - | 52 |
| A | Ana | +2.29% | +2.90% ±2.2 | Map Priority (+11.0%) | Meta | - | 52 |
| A | Wrecking Ball | +1.79% | +3.07% ±3.2 | Standard (+0.6%) | Favorable | Better in GM+ | 51 |
| A | Hanzo | +1.47% | +2.02% ±1.6 | Map Priority (+4.6%) | Favorable | - | 51 |
| A | Junkrat | +1.41% | +2.19% ±3.0 | Standard (-0.7%) | Favorable | Better in GM+ | 48 |
| B | Zenyatta | +1.02% | +3.65% ±3.1 | Map Priority (+5.1%) | Neutral | Better in GM+ | 52 |
| B | Freja | +0.90% | +3.76% ±3.7 | Popular (+1.4%) | Neutral | Better in GM+ | 51 |
| B | Sojourn | +0.50% | +0.95% ±1.8 | Standard (+0.4%) | Neutral | - | 52 |
| B | Brigitte | +0.38% | +1.16% ±3.1 | Niche (-1.6%) | Neutral | Better in GM+ | 51 |
| B | Kiriko | +0.35% | +0.79% ±2.7 | Niche (-8.0%) | Neutral | Better in GM+ | 52 |
| B | Torbjörn | +0.35% | +0.64% ±3.4 | Standard (+0.3%) | Neutral | - | 49 |
| B | Hazard | +0.29% | +0.67% ±2.9 | Niche (-2.3%) | Neutral | Better in GM+ | 51 |
| B | Illari | +0.26% | +1.92% ±2.4 | Map Priority (+4.9%) | Neutral | - | 52 |
| B | Sierra | +0.22% | +1.57% ±3.9 | Popular (+1.0%) | Neutral | Better in GM+ | 35 |
| B | Orisa | +0.21% | +0.50% ±3.2 | Niche (-1.4%) | Neutral | - | 50 |
| B | Lifeweaver | +0.13% | -2.26% ±3.6 | Popular (+1.4%) | Neutral | - | 50 |
| B | Venture | +0.04% | +0.43% ±4.1 | Standard (-0.3%) | Neutral | Better in GM+ | 50 |
| B | Shion | +0.01% | +0.80% ±3.0 | Niche (-6.0%) | Neutral | - | 28 |
| B | Reinhardt | -0.06% | +0.07% ±3.0 | Niche (-1.2%) | Neutral | Better in GM+ | 49 |
| B | Genji | -0.13% | +1.00% ±3.1 | Popular (+1.8%) | Neutral | Better in GM+ | 52 |
| B | Mercy | -0.13% | +0.01% ±2.6 | Popular (+1.9%) | Neutral | - | 51 |
| B | Tracer | -0.13% | +0.03% ±2.0 | Niche (-7.1%) | Neutral | - | 52 |
| B | Anran | -0.15% | +0.10% ±4.1 | Standard (-0.9%) | Neutral | - | 50 |
| B | Doctrine *(provisional)* | -0.24% | -0.50% ±5.1 | Standard (+0.5%) | Neutral | - | 8 |
| B | Baptiste | -0.27% | +0.30% ±2.9 | Standard (+0.9%) | Neutral | - | 51 |
| B | Emre | -0.36% | -0.48% ±3.1 | Popular (+2.3%) | Neutral | Better in Masters | 52 |
| B | Mei | -0.37% | -1.24% ±3.6 | Standard (-0.4%) | Neutral | Better in GM+ | 50 |
| B | Bastion | -0.44% | -0.88% ±3.5 | Standard (+0.4%) | Neutral | Better in Masters | 50 |
| B | Roadhog *(provisional)* | -0.56% | -1.95% ±12.6 | Standard (+1.0%) | Neutral | Better in GM+ | 8 |
| B | Winston | -0.59% | -0.49% ±1.9 | Popular (+1.1%) | Neutral | Better in GM+ | 52 |
| B | D.Va | -0.62% | -0.81% ±3.3 | Standard (+0.7%) | Neutral | Better in Masters | 52 |
| B | Mauga | -0.63% | -0.65% ±4.0 | Niche (-1.1%) | Neutral | Better in Masters | 51 |
| B | Reaper | -0.73% | -1.24% ±3.1 | Niche (-2.1%) | Neutral | Better in GM+ | 51 |
| B | Jetpack Cat | -0.75% | -1.09% ±3.7 | Niche (-1.7%) | Neutral | - | 51 |
| B | Echo | -0.76% | -0.93% ±3.6 | Niche (-2.5%) | Neutral | Better in Masters | 50 |
| B | Juno | -0.82% | -2.62% ±3.3 | Niche (-2.2%) | Neutral | Better in Masters | 50 |
| B | Cassidy | -0.85% | -1.31% ±2.2 | Niche (-6.9%) | Neutral | Better in Masters | 52 |
| B | Doomfist | -0.89% | -2.42% ±3.0 | Niche (-1.1%) | Neutral | Better in Masters | 51 |
| B | Sombra *(provisional)* | -0.91% | -1.05% ±8.2 | Niche (-4.1%) | Neutral | Better in Masters | 8 |
| B | D.Mon | -0.96% | -4.50% ±7.4 | Niche (-2.1%) | Neutral | Better in Masters | 16 |
| B | Symmetra | -1.03% | -1.64% ±4.1 | Niche (-1.0%) | Neutral | Better in Masters | 45 |
| B | Ashe | -1.09% | -1.46% ±1.7 | Map Priority (+6.3%) | Neutral | - | 51 |
| B | Wuyang | -1.11% | -2.02% ±2.3 | Standard (-0.6%) | Neutral | Better in Masters | 52 |
| B | Vendetta | -1.13% | -3.28% ±4.2 | Standard (-0.3%) | Neutral | Better in GM+ | 44 |
| C | Mizuki | -1.64% | -2.84% ±3.2 | Niche (-3.2%) | Deterrent | - | 51 |
| C | Moira | -1.75% | -2.42% ±3.3 | Niche (-2.4%) | Deterrent | - | 51 |
| C | Soldier: 76 | -1.89% | -3.49% ±3.0 | Popular (+2.3%) | Trap Pick | Better in Masters | 52 |
| C | Domina | -1.93% | -2.30% ±3.3 | Popular (+1.1%) | Trap Pick | - | 50 |
| C | Zarya | -2.43% | -3.43% ±3.5 | Niche (-2.3%) | Deterrent | - | 51 |
| C | Ramattra | -2.45% | -3.20% ±2.7 | Niche (-1.3%) | Deterrent | - | 46 |
| D | Pharah | -3.92% | -5.70% ±3.6 | Niche (-2.7%) | Deterrent | - | 49 |
| D | Junker Queen | -4.00% | -5.26% ±4.2 | Niche (-1.2%) | Deterrent | Better in Masters | 40 |
| D | Lúcio | -5.01% | -5.56% ±3.4 | Niche (-5.4%) | Deterrent | Better in GM+ | 47 |

### Kings Row

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| A | Junkrat | +2.19% | +2.40% ±1.3 | Popular (+1.4%) | Favorable | - | 51 |
| A | Orisa | +2.10% | +4.17% ±3.2 | Popular (+1.5%) | Meta | - | 52 |
| A | Ana | +1.50% | +1.62% ±1.2 | Map Priority (+4.7%) | Favorable | - | 52 |
| A | Hanzo | +1.48% | +2.12% ±1.7 | Map Priority (+3.4%) | Favorable | - | 52 |
| B | Reaper | +1.06% | +1.78% ±1.8 | Standard (-0.4%) | Neutral | Better in GM+ | 52 |
| B | Widowmaker | +0.99% | +1.13% ±2.3 | Map Priority (+3.5%) | Neutral | Better in Masters | 52 |
| B | Pharah | +0.98% | +1.33% ±1.9 | Popular (+2.5%) | Neutral | - | 52 |
| B | Zarya | +0.82% | +1.27% ±2.2 | Map Priority (+3.6%) | Neutral | - | 52 |
| B | D.Mon | +0.75% | +1.72% ±2.7 | Standard (+0.1%) | Neutral | Better in GM+ | 16 |
| B | Sierra | +0.22% | +0.87% ±1.6 | Standard (+0.2%) | Neutral | - | 35 |
| B | Lifeweaver | +0.13% | -1.44% ±2.3 | Standard (+0.0%) | Neutral | Better in Masters | 51 |
| B | Domina | +0.11% | +0.19% ±1.3 | Standard (+0.9%) | Neutral | - | 51 |
| B | Mizuki | +0.09% | +0.12% ±1.8 | Standard (-0.5%) | Neutral | - | 52 |
| B | Venture | +0.04% | +2.12% ±2.9 | Standard (+0.2%) | Neutral | - | 51 |
| B | Cassidy | +0.01% | +0.13% ±1.5 | Niche (-1.9%) | Neutral | - | 52 |
| B | Reinhardt | -0.03% | +0.03% ±2.1 | Popular (+2.4%) | Neutral | Better in Masters | 52 |
| B | Genji | -0.11% | +0.02% ±0.9 | Standard (+0.7%) | Neutral | - | 52 |
| B | Anran | -0.19% | -0.11% ±3.0 | Standard (-0.2%) | Neutral | - | 52 |
| B | Roadhog *(provisional)* | -0.22% | +0.32% ±6.9 | Standard (-0.6%) | Neutral | - | 8 |
| B | Kiriko | -0.24% | -0.25% ±0.9 | Niche (-4.9%) | Neutral | - | 52 |
| B | Baptiste | -0.39% | -0.35% ±1.1 | Map Priority (+3.2%) | Neutral | - | 52 |
| B | Mei | -0.42% | -0.68% ±1.8 | Popular (+2.8%) | Neutral | - | 52 |
| B | Bastion | -0.52% | -0.62% ±1.6 | Popular (+2.4%) | Neutral | - | 51 |
| B | Juno | -0.58% | -0.56% ±1.5 | Standard (+0.0%) | Neutral | - | 51 |
| B | Shion | -0.58% | -0.72% ±1.2 | Niche (-4.3%) | Neutral | - | 28 |
| B | Doomfist | -0.67% | -0.95% ±1.7 | Standard (-0.5%) | Neutral | Better in Masters | 52 |
| B | Ramattra | -0.67% | -0.65% ±1.5 | Popular (+2.4%) | Neutral | Better in Masters | 51 |
| B | D.Va | -0.72% | -0.93% ±2.3 | Niche (-1.2%) | Neutral | - | 52 |
| B | Sojourn | -0.75% | -0.82% ±1.2 | Popular (+1.2%) | Neutral | - | 52 |
| B | Sigma | -0.78% | -0.64% ±2.5 | Popular (+2.3%) | Neutral | Better in GM+ | 52 |
| B | Hazard | -0.79% | -0.86% ±2.3 | Niche (-2.3%) | Neutral | - | 51 |
| B | Illari | -0.86% | -1.47% ±1.1 | Standard (-0.6%) | Neutral | - | 52 |
| B | Zenyatta | -0.86% | -1.07% ±1.7 | Map Priority (+3.8%) | Neutral | Better in Masters | 52 |
| B | Freja | -0.90% | -1.05% ±1.7 | Standard (+0.5%) | Neutral | - | 52 |
| B | Sombra *(provisional)* | -0.90% | -0.96% ±5.3 | Niche (-4.3%) | Neutral | - | 8 |
| B | Symmetra | -0.91% | -1.03% ±2.1 | Standard (+0.3%) | Neutral | Better in Masters | 51 |
| B | Echo | -0.92% | -1.01% ±1.7 | Standard (+0.3%) | Neutral | Better in GM+ | 52 |
| B | Emre | -0.95% | -2.77% ±2.1 | Niche (-1.3%) | Neutral | - | 52 |
| B | Mauga | -1.08% | -1.17% ±1.5 | Standard (-1.0%) | Neutral | - | 51 |
| B | Soldier: 76 | -1.16% | -1.85% ±2.7 | Niche (-4.3%) | Neutral | Better in GM+ | 51 |
| C | Lúcio | -1.22% | -1.11% ±3.0 | Niche (-2.4%) | Unfavorable | - | 52 |
| C | Moira | -1.24% | -1.27% ±1.3 | Standard (-0.7%) | Unfavorable | - | 51 |
| C | Brigitte | -1.26% | -1.65% ±2.5 | Niche (-2.9%) | Unfavorable | Better in Masters | 52 |
| C | Wuyang | -1.27% | -1.56% ±1.2 | Popular (+1.6%) | Unfavorable | Better in GM+ | 52 |
| C | Vendetta | -1.39% | -2.27% ±2.4 | Standard (-0.2%) | Unfavorable | - | 49 |
| C | Mercy | -1.41% | -2.26% ±1.8 | Standard (-0.7%) | Unfavorable | - | 52 |
| C | Ashe | -1.47% | -1.81% ±1.1 | Standard (-0.5%) | Unfavorable | - | 52 |
| C | Torbjörn | -1.74% | -2.06% ±1.8 | Standard (+0.2%) | Unfavorable | - | 50 |
| C | Doctrine *(provisional)* | -1.93% | -5.38% ±5.6 | Standard (-0.2%) | Deterrent | Better in Masters | 8 |
| C | Jetpack Cat | -2.41% | -3.18% ±2.7 | Niche (-1.2%) | Deterrent | - | 52 |
| C | Tracer | -2.67% | -3.00% ±1.1 | Niche (-8.1%) | Deterrent | - | 52 |
| D | Junker Queen | -3.06% | -3.22% ±1.8 | Standard (-0.1%) | Deterrent | - | 48 |
| D | Winston | -3.94% | -4.02% ±1.2 | Niche (-4.7%) | Deterrent | - | 52 |
| D | Wrecking Ball | -4.01% | -5.70% ±2.9 | Niche (-2.6%) | Deterrent | - | 52 |

### Lijiang Tower

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| S | Pharah | +4.54% | +4.84% ±1.1 | Map Priority (+5.0%) | Meta | - | 52 |
| S | Torbjörn | +3.26% | +3.61% ±1.4 | Standard (-0.7%) | Specialist | - | 47 |
| S | Reinhardt | +3.13% | +3.34% ±1.4 | Popular (+2.0%) | Meta | - | 52 |
| A | Lúcio | +2.70% | +2.78% ±1.1 | Map Priority (+6.8%) | Meta | - | 51 |
| A | Symmetra | +2.58% | +3.11% ±1.6 | Popular (+2.7%) | Meta | - | 52 |
| A | Zarya | +1.97% | +2.62% ±2.1 | Popular (+2.2%) | Meta | Better in GM+ | 52 |
| A | Reaper | +1.79% | +2.57% ±1.5 | Popular (+1.4%) | Favorable | - | 52 |
| A | Domina | +1.65% | +2.23% ±2.3 | Niche (-1.1%) | Specialist | Better in GM+ | 51 |
| A | Orisa | +1.40% | +2.59% ±2.9 | Popular (+2.4%) | Favorable | Better in GM+ | 52 |
| A | Mizuki | +1.20% | +1.35% ±1.3 | Popular (+2.5%) | Favorable | - | 52 |
| B | Jetpack Cat | +1.00% | +1.25% ±2.0 | Standard (+0.8%) | Neutral | - | 52 |
| B | Hazard | +0.92% | +0.99% ±0.9 | Standard (+0.1%) | Neutral | - | 51 |
| B | Kiriko | +0.90% | +1.03% ±1.0 | Map Priority (+4.9%) | Neutral | - | 52 |
| B | Mei | +0.81% | +3.52% ±3.0 | Standard (+0.3%) | Neutral | Better in GM+ | 52 |
| B | Moira | +0.78% | +1.25% ±1.8 | Popular (+2.1%) | Neutral | - | 51 |
| B | Ramattra | +0.72% | +1.00% ±1.7 | Popular (+1.3%) | Neutral | Better in Masters | 52 |
| B | Sojourn | +0.62% | +0.95% ±1.4 | Popular (+1.0%) | Neutral | - | 52 |
| B | Cassidy | +0.45% | +0.54% ±0.8 | Map Priority (+6.0%) | Neutral | - | 52 |
| B | Junkrat | +0.35% | +0.42% ±1.7 | Standard (+0.9%) | Neutral | Better in GM+ | 51 |
| B | Doomfist | +0.24% | +0.64% ±1.7 | Popular (+1.3%) | Neutral | - | 52 |
| B | Sierra | +0.22% | -0.58% ±1.4 | Standard (-0.7%) | Neutral | - | 33 |
| B | Lifeweaver | +0.13% | -1.49% ±2.4 | Niche (-1.2%) | Neutral | - | 49 |
| B | Venture | +0.04% | -1.30% ±2.4 | Standard (+0.2%) | Neutral | - | 51 |
| B | Zenyatta | -0.04% | +0.39% ±2.4 | Niche (-2.4%) | Neutral | - | 52 |
| B | Brigitte | -0.07% | +0.28% ±3.0 | Standard (-0.3%) | Neutral | Better in Masters | 52 |
| B | Genji | -0.13% | -0.02% ±0.9 | Niche (-1.2%) | Neutral | - | 51 |
| B | Hanzo | -0.13% | +0.27% ±3.2 | Niche (-2.4%) | Neutral | Better in Masters | 52 |
| B | Bastion | -0.16% | -0.26% ±2.6 | Standard (-0.5%) | Neutral | Better in Masters | 52 |
| B | Junker Queen | -0.28% | -0.21% ±1.8 | Standard (+0.9%) | Neutral | - | 51 |
| B | Illari | -0.29% | -0.46% ±1.4 | Niche (-3.6%) | Neutral | - | 52 |
| B | Roadhog *(provisional)* | -0.33% | -0.13% ±6.2 | Standard (+0.0%) | Neutral | - | 8 |
| B | Wuyang | -0.42% | -0.47% ±1.0 | Standard (-0.0%) | Neutral | - | 52 |
| B | Shion | -0.45% | -0.52% ±1.1 | Popular (+3.0%) | Neutral | - | 28 |
| B | Baptiste | -0.52% | -0.49% ±1.6 | Niche (-1.3%) | Neutral | Better in Masters | 51 |
| B | Vendetta | -0.52% | -0.85% ±2.8 | Standard (+0.4%) | Neutral | Better in Masters | 49 |
| B | Emre | -0.61% | -1.16% ±1.7 | Niche (-2.4%) | Neutral | - | 52 |
| B | D.Mon | -0.63% | -0.75% ±2.1 | Popular (+1.5%) | Neutral | - | 16 |
| B | Sombra *(provisional)* | -0.80% | -0.73% ±4.2 | Map Priority (+3.8%) | Neutral | - | 8 |
| B | Juno | -0.95% | -1.75% ±1.7 | Standard (+0.7%) | Neutral | - | 51 |
| B | D.Va | -1.09% | -1.95% ±2.6 | Niche (-1.5%) | Neutral | - | 52 |
| B | Mercy | -1.12% | -1.59% ±1.6 | Standard (-1.0%) | Neutral | - | 51 |
| B | Mauga | -1.17% | -1.44% ±2.4 | Popular (+1.3%) | Neutral | - | 52 |
| C | Freja | -1.38% | -1.70% ±1.7 | Niche (-1.2%) | Unfavorable | - | 50 |
| C | Soldier: 76 | -1.39% | -1.57% ±1.2 | Niche (-2.2%) | Unfavorable | - | 51 |
| C | Tracer | -1.46% | -1.57% ±1.0 | Popular (+2.1%) | Unfavorable | - | 52 |
| C | Anran | -1.47% | -2.35% ±2.4 | Standard (+0.4%) | Unfavorable | - | 51 |
| C | Wrecking Ball | -1.50% | -1.67% ±1.7 | Standard (+0.9%) | Unfavorable | - | 52 |
| C | Ana | -1.66% | -1.82% ±1.7 | Niche (-7.7%) | Deterrent | - | 52 |
| C | Ashe | -1.66% | -3.47% ±2.3 | Niche (-6.1%) | Deterrent | - | 50 |
| C | Winston | -1.68% | -1.67% ±1.7 | Niche (-5.3%) | Deterrent | - | 52 |
| C | Sigma | -1.81% | -1.81% ±1.8 | Niche (-5.0%) | Deterrent | - | 52 |
| C | Echo | -2.16% | -3.21% ±2.6 | Standard (+0.1%) | Unfavorable | - | 52 |
| C | Doctrine *(provisional)* | -2.81% | -4.74% ±3.5 | Niche (-1.9%) | Deterrent | - | 8 |
| D | Widowmaker | -7.37% | -7.42% ±1.9 | Niche (-4.4%) | Deterrent | - | 49 |

### Midtown

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| B | Orisa | +1.04% | +1.84% ±2.7 | Standard (+0.7%) | Neutral | - | 52 |
| B | Widowmaker | +0.67% | +0.99% ±3.6 | Map Priority (+3.7%) | Neutral | Better in Masters | 52 |
| B | Doctrine *(provisional)* | +0.55% | +1.25% ±4.4 | Popular (+2.8%) | Neutral | - | 8 |
| B | Brigitte | +0.48% | +1.66% ±3.6 | Niche (-3.0%) | Neutral | Better in GM+ | 52 |
| B | Sierra | +0.22% | -0.15% ±3.9 | Standard (+0.4%) | Neutral | Better in Masters | 35 |
| B | Lifeweaver | +0.13% | -0.59% ±3.6 | Standard (+0.8%) | Neutral | - | 51 |
| B | Venture | +0.04% | +1.88% ±4.1 | Standard (+0.3%) | Neutral | - | 51 |
| B | Illari | +0.02% | +0.79% ±2.4 | Popular (+1.9%) | Neutral | - | 52 |
| B | Baptiste | +0.00% | +0.66% ±2.3 | Popular (+2.9%) | Neutral | - | 52 |
| B | Genji | -0.03% | +3.06% ±2.9 | Niche (-1.4%) | Neutral | Better in GM+ | 52 |
| B | Wuyang | -0.07% | +0.07% ±2.6 | Popular (+2.8%) | Neutral | - | 52 |
| B | Vendetta | -0.14% | -0.06% ±3.6 | Standard (-0.6%) | Neutral | Better in Masters | 42 |
| B | Reaper | -0.15% | +0.25% ±3.3 | Niche (-2.1%) | Neutral | Better in Masters | 52 |
| B | Zarya | -0.15% | +0.25% ±3.2 | Popular (+2.8%) | Neutral | Better in Masters | 52 |
| B | Sigma | -0.17% | +0.05% ±2.5 | Map Priority (+9.3%) | Neutral | - | 52 |
| B | Emre | -0.18% | +0.65% ±2.7 | Popular (+2.2%) | Neutral | - | 52 |
| B | Mizuki | -0.27% | -0.39% ±2.6 | Niche (-1.5%) | Neutral | Better in GM+ | 52 |
| B | Sojourn | -0.28% | -0.21% ±1.8 | Map Priority (+4.5%) | Neutral | - | 52 |
| B | Domina | -0.32% | -0.04% ±2.9 | Popular (+2.4%) | Neutral | Better in Masters | 52 |
| B | Doomfist | -0.32% | -0.42% ±3.7 | Niche (-2.0%) | Neutral | Better in GM+ | 52 |
| B | Juno | -0.35% | +1.96% ±3.5 | Standard (+0.1%) | Neutral | - | 51 |
| B | Anran | -0.39% | -0.72% ±4.6 | Standard (-0.1%) | Neutral | Better in GM+ | 49 |
| B | Junkrat | -0.39% | -0.71% ±4.2 | Standard (+0.4%) | Neutral | Better in GM+ | 52 |
| B | Freja | -0.44% | -0.26% ±3.6 | Standard (-0.6%) | Neutral | - | 50 |
| B | Hanzo | -0.45% | -0.45% ±1.4 | Popular (+2.7%) | Neutral | - | 50 |
| B | D.Va | -0.47% | -0.32% ±2.9 | Niche (-2.0%) | Neutral | - | 50 |
| B | Shion | -0.55% | -0.96% ±2.1 | Niche (-3.4%) | Neutral | - | 28 |
| B | Mei | -0.70% | -2.83% ±3.6 | Popular (+1.4%) | Neutral | - | 52 |
| B | Ana | -0.77% | -0.83% ±2.0 | Map Priority (+4.6%) | Neutral | - | 52 |
| B | D.Mon | -0.80% | -1.92% ±4.9 | Standard (-0.8%) | Neutral | Better in GM+ | 16 |
| B | Moira | -0.80% | -0.56% ±3.6 | Niche (-1.4%) | Neutral | - | 51 |
| B | Mercy | -0.89% | -2.04% ±2.9 | Standard (+0.2%) | Neutral | - | 50 |
| B | Ashe | -0.99% | -1.50% ±2.5 | Map Priority (+3.4%) | Neutral | - | 52 |
| B | Tracer | -1.00% | -1.25% ±2.0 | Niche (-6.0%) | Neutral | Better in Masters | 52 |
| B | Cassidy | -1.06% | -1.26% ±1.2 | Niche (-4.7%) | Neutral | - | 52 |
| B | Zenyatta | -1.13% | -1.85% ±2.4 | Map Priority (+3.9%) | Neutral | Better in Masters | 52 |
| B | Soldier: 76 | -1.15% | -1.60% ±2.2 | Niche (-1.2%) | Neutral | - | 51 |
| C | Torbjörn | -1.22% | -2.21% ±3.9 | Standard (+0.6%) | Unfavorable | Better in GM+ | 50 |
| C | Symmetra | -1.23% | -1.70% ±3.1 | Popular (+1.1%) | Unfavorable | - | 52 |
| C | Roadhog *(provisional)* | -1.30% | -7.98% ±11.3 | Standard (-0.5%) | Unfavorable | Better in Masters | 8 |
| C | Ramattra | -1.46% | -1.99% ±3.6 | Popular (+2.0%) | Unfavorable | Better in Masters | 52 |
| C | Kiriko | -1.60% | -1.94% ±1.4 | Niche (-4.7%) | Deterrent | - | 52 |
| C | Sombra *(provisional)* | -1.64% | -3.41% ±6.2 | Niche (-4.2%) | Deterrent | Better in GM+ | 8 |
| C | Echo | -1.87% | -3.16% ±3.2 | Niche (-1.9%) | Deterrent | - | 52 |
| C | Mauga | -2.08% | -3.30% ±3.2 | Niche (-1.4%) | Deterrent | - | 48 |
| C | Pharah | -2.21% | -2.97% ±3.7 | Standard (-0.3%) | Deterrent | Better in GM+ | 51 |
| C | Hazard | -2.44% | -3.93% ±3.7 | Niche (-3.7%) | Deterrent | Better in Masters | 49 |
| C | Junker Queen | -2.63% | -3.10% ±3.5 | Standard (-0.6%) | Deterrent | - | 45 |
| C | Bastion | -2.66% | -5.60% ±3.8 | Standard (+1.0%) | Unfavorable | Better in Masters | 52 |
| C | Reinhardt | -2.89% | -3.69% ±3.5 | Standard (+0.7%) | Unfavorable | Better in Masters | 52 |
| D | Wrecking Ball | -3.35% | -5.47% ±3.6 | Niche (-2.4%) | Deterrent | Better in Masters | 50 |
| D | Jetpack Cat | -4.24% | -6.55% ±3.5 | Niche (-2.6%) | Deterrent | - | 52 |
| D | Winston | -5.16% | -5.97% ±3.2 | Niche (-5.1%) | Deterrent | Better in Masters | 52 |
| D | Lúcio | -6.08% | -6.85% ±3.5 | Niche (-4.1%) | Deterrent | - | 45 |

### Neon Junction

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| A | Mizuki | +2.77% | +3.51% ±1.9 | Standard (-0.0%) | Specialist | Better in GM+ | 28 |
| A | Reinhardt | +1.74% | +2.14% ±2.5 | Popular (+2.4%) | Meta | Better in GM+ | 28 |
| A | Vendetta | +1.55% | +3.10% ±2.6 | Standard (-0.5%) | Specialist | Better in GM+ | 28 |
| B | Orisa | +1.09% | +1.49% ±1.9 | Popular (+1.9%) | Neutral | - | 28 |
| B | Shion | +1.06% | +1.64% ±1.2 | Popular (+2.8%) | Neutral | - | 28 |
| B | Zarya | +0.92% | +1.44% ±2.3 | Popular (+2.8%) | Neutral | - | 28 |
| B | Sigma | +0.78% | +0.94% ±1.6 | Map Priority (+7.5%) | Neutral | - | 28 |
| B | Reaper | +0.66% | +2.10% ±2.9 | Niche (-1.5%) | Neutral | Better in GM+ | 28 |
| B | Bastion | +0.63% | +1.03% ±2.9 | Popular (+2.4%) | Neutral | Better in GM+ | 28 |
| B | Ramattra | +0.59% | +1.16% ±2.5 | Map Priority (+3.4%) | Neutral | Better in GM+ | 28 |
| B | Widowmaker | +0.40% | +0.47% ±1.7 | Map Priority (+3.1%) | Neutral | Better in GM+ | 28 |
| B | Sierra | +0.22% | +1.35% ±3.3 | Standard (+0.4%) | Neutral | Better in Masters | 24 |
| B | Lifeweaver | +0.13% | -1.09% ±2.4 | Standard (+0.5%) | Neutral | - | 28 |
| B | Zenyatta | +0.08% | +0.35% ±1.7 | Map Priority (+4.0%) | Neutral | - | 28 |
| B | Soldier: 76 | +0.07% | +0.34% ±2.4 | Niche (-2.4%) | Neutral | Better in GM+ | 28 |
| B | Junker Queen | +0.06% | +0.36% ±3.2 | Standard (-0.2%) | Neutral | - | 26 |
| B | Symmetra | +0.06% | +0.34% ±2.8 | Standard (+0.5%) | Neutral | - | 28 |
| B | Venture | +0.04% | +2.16% ±3.5 | Standard (-0.0%) | Neutral | - | 28 |
| B | Moira | +0.00% | +0.70% ±2.9 | Standard (-0.8%) | Neutral | Better in GM+ | 28 |
| B | Torbjörn | -0.03% | +0.02% ±4.0 | Standard (+0.3%) | Neutral | Better in GM+ | 27 |
| B | Genji | -0.22% | -0.48% ±1.5 | Niche (-1.6%) | Neutral | - | 28 |
| B | Kiriko | -0.22% | -0.26% ±2.0 | Niche (-3.1%) | Neutral | - | 28 |
| B | Illari | -0.26% | -0.63% ±2.5 | Standard (-0.6%) | Neutral | Better in GM+ | 28 |
| B | Sojourn | -0.36% | -0.34% ±1.5 | Map Priority (+5.1%) | Neutral | - | 28 |
| B | Emre | -0.42% | -0.60% ±1.9 | Standard (+0.9%) | Neutral | - | 28 |
| B | Cassidy | -0.50% | -0.57% ±1.5 | Niche (-3.1%) | Neutral | - | 28 |
| B | Mei | -0.55% | -1.28% ±2.5 | Popular (+2.7%) | Neutral | - | 28 |
| B | Roadhog *(provisional)* | -0.56% | -1.09% ±7.7 | Standard (-0.3%) | Neutral | - | 8 |
| B | Doctrine *(provisional)* | -0.60% | -1.75% ±6.1 | Popular (+1.5%) | Neutral | Better in Masters | 8 |
| B | Anran | -0.68% | -1.77% ±4.5 | Standard (-0.3%) | Neutral | Better in Masters | 28 |
| B | D.Mon | -0.71% | -1.00% ±2.8 | Standard (+0.7%) | Neutral | - | 16 |
| B | Juno | -0.77% | -1.69% ±2.7 | Popular (+1.0%) | Neutral | Better in Masters | 28 |
| B | Sombra *(provisional)* | -0.80% | -0.66% ±5.6 | Niche (-5.9%) | Neutral | Better in GM+ | 8 |
| B | Baptiste | -0.89% | -1.55% ±3.1 | Popular (+1.6%) | Neutral | - | 28 |
| B | Domina | -0.89% | -0.82% ±2.6 | Popular (+1.3%) | Neutral | - | 28 |
| B | Pharah | -0.96% | -0.94% ±2.7 | Standard (+0.3%) | Neutral | - | 28 |
| B | Doomfist | -1.01% | -2.05% ±2.3 | Niche (-1.5%) | Neutral | - | 28 |
| B | Wuyang | -1.06% | -1.69% ±2.0 | Map Priority (+3.7%) | Neutral | - | 28 |
| B | Ashe | -1.12% | -1.48% ±1.6 | Standard (+0.8%) | Neutral | - | 28 |
| C | Ana | -1.23% | -1.33% ±1.6 | Map Priority (+3.1%) | Unfavorable | Better in Masters | 28 |
| C | Wrecking Ball | -1.36% | -2.47% ±4.5 | Niche (-2.9%) | Unfavorable | Better in GM+ | 28 |
| C | Hanzo | -1.37% | -1.90% ±2.2 | Popular (+1.8%) | Unfavorable | - | 28 |
| C | Mercy | -1.54% | -2.62% ±2.0 | Standard (-0.5%) | Deterrent | - | 26 |
| C | Mauga | -1.70% | -2.26% ±2.5 | Standard (-0.9%) | Deterrent | Better in GM+ | 27 |
| C | Jetpack Cat | -1.81% | -2.72% ±3.5 | Niche (-2.9%) | Deterrent | Better in GM+ | 28 |
| C | D.Va | -1.95% | -3.05% ±1.9 | Niche (-3.1%) | Deterrent | - | 28 |
| C | Lúcio | -2.29% | -2.33% ±3.3 | Niche (-2.5%) | Deterrent | Better in GM+ | 26 |
| C | Freja | -2.34% | -3.77% ±2.4 | Standard (+0.0%) | Unfavorable | - | 28 |
| C | Junkrat | -2.40% | -4.47% ±4.0 | Standard (+0.4%) | Unfavorable | - | 28 |
| C | Brigitte | -2.74% | -4.42% ±2.9 | Niche (-3.5%) | Deterrent | Better in Masters | 28 |
| C | Tracer | -2.89% | -4.04% ±2.0 | Niche (-9.0%) | Deterrent | - | 28 |
| D | Echo | -3.47% | -4.90% ±2.2 | Niche (-2.4%) | Deterrent | - | 28 |
| D | Hazard | -4.53% | -5.78% ±2.4 | Niche (-3.6%) | Deterrent | - | 28 |
| D | Winston | -5.87% | -6.31% ±2.2 | Niche (-6.5%) | Deterrent | - | 28 |

### Nepal

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| A | Symmetra | +3.00% | +3.61% ±1.6 | Popular (+2.2%) | Meta | - | 52 |
| A | Torbjörn | +2.42% | +2.74% ±1.5 | Standard (-0.5%) | Specialist | - | 51 |
| A | Pharah | +2.19% | +2.45% ±1.3 | Popular (+2.6%) | Meta | - | 52 |
| A | Bastion | +2.13% | +2.56% ±1.6 | Standard (-0.7%) | Specialist | - | 52 |
| A | Reinhardt | +2.06% | +2.16% ±1.2 | Popular (+1.4%) | Favorable | - | 52 |
| A | Mauga | +2.04% | +2.55% ±1.6 | Standard (+0.9%) | Favorable | - | 51 |
| A | Lúcio | +1.78% | +1.87% ±1.2 | Map Priority (+3.9%) | Meta | - | 52 |
| A | Ramattra | +1.78% | +2.21% ±1.6 | Standard (+0.6%) | Favorable | - | 52 |
| A | Jetpack Cat | +1.69% | +1.85% ±1.3 | Standard (+0.4%) | Favorable | - | 52 |
| A | Hazard | +1.67% | +1.98% ±1.6 | Standard (+0.5%) | Favorable | Better in GM+ | 52 |
| A | Orisa | +1.49% | +1.84% ±1.5 | Standard (+0.9%) | Favorable | - | 52 |
| A | Roadhog *(provisional)* | +1.24% | +4.96% ±6.2 | Standard (+0.2%) | Favorable | - | 8 |
| B | Sojourn | +1.13% | +1.35% ±1.0 | Popular (+1.5%) | Neutral | - | 52 |
| B | Junkrat | +1.11% | +1.37% ±2.0 | Standard (+0.3%) | Neutral | - | 52 |
| B | Mizuki | +1.06% | +1.12% ±0.9 | Popular (+1.5%) | Neutral | - | 52 |
| B | Kiriko | +0.82% | +0.87% ±0.7 | Map Priority (+3.9%) | Neutral | - | 52 |
| B | Brigitte | +0.79% | +1.15% ±1.8 | Standard (+0.1%) | Neutral | - | 52 |
| B | Reaper | +0.69% | +0.97% ±1.3 | Standard (+0.8%) | Neutral | - | 52 |
| B | Doomfist | +0.58% | +0.97% ±1.3 | Popular (+1.1%) | Neutral | - | 52 |
| B | Mei | +0.43% | +0.85% ±1.5 | Standard (-0.4%) | Neutral | - | 52 |
| B | Cassidy | +0.40% | +0.45% ±0.6 | Map Priority (+3.5%) | Neutral | - | 52 |
| B | Vendetta | +0.35% | +0.57% ±1.8 | Standard (+0.2%) | Neutral | - | 49 |
| B | Zarya | +0.29% | +0.35% ±0.9 | Popular (+1.1%) | Neutral | - | 52 |
| B | Sierra | +0.22% | +1.93% ±2.6 | Standard (-0.5%) | Neutral | Better in GM+ | 32 |
| B | Hanzo | +0.21% | +0.56% ±2.2 | Niche (-2.3%) | Neutral | - | 52 |
| B | Baptiste | +0.17% | +0.43% ±1.3 | Standard (-0.8%) | Neutral | - | 52 |
| B | Lifeweaver | +0.13% | +0.75% ±2.1 | Niche (-1.2%) | Neutral | Better in GM+ | 50 |
| B | Wuyang | +0.12% | +0.15% ±0.8 | Popular (+1.1%) | Neutral | - | 52 |
| B | Zenyatta | +0.09% | +0.20% ±1.1 | Niche (-2.1%) | Neutral | - | 52 |
| B | Venture | +0.04% | +0.91% ±2.3 | Standard (+0.1%) | Neutral | - | 52 |
| B | Emre | +0.03% | +0.35% ±1.1 | Niche (-1.1%) | Neutral | - | 52 |
| B | Moira | -0.10% | +0.36% ±2.5 | Popular (+1.7%) | Neutral | Better in Masters | 52 |
| B | Domina | -0.13% | +0.03% ±2.0 | Standard (-0.3%) | Neutral | - | 50 |
| B | Freja | -0.31% | -0.24% ±1.5 | Niche (-1.1%) | Neutral | Better in GM+ | 52 |
| B | Illari | -0.32% | -0.42% ±1.0 | Niche (-2.6%) | Neutral | - | 51 |
| B | Sigma | -0.35% | -0.32% ±1.0 | Niche (-1.7%) | Neutral | - | 52 |
| B | Anran | -0.38% | -0.42% ±1.6 | Standard (+0.4%) | Neutral | - | 51 |
| B | Genji | -0.39% | -1.18% ±1.1 | Standard (-0.6%) | Neutral | - | 52 |
| B | Mercy | -0.56% | -0.69% ±1.4 | Standard (-0.9%) | Neutral | - | 51 |
| B | D.Mon | -0.60% | -0.78% ±2.7 | Popular (+1.0%) | Neutral | - | 16 |
| B | Sombra *(provisional)* | -0.60% | -0.26% ±4.6 | Popular (+2.1%) | Neutral | - | 8 |
| B | Junker Queen | -0.73% | -0.67% ±2.5 | Standard (+0.3%) | Neutral | - | 48 |
| B | Ashe | -0.87% | -0.94% ±1.4 | Niche (-4.2%) | Neutral | - | 52 |
| B | Tracer | -0.88% | -0.91% ±0.8 | Popular (+2.6%) | Neutral | - | 52 |
| B | Shion | -1.01% | -1.25% ±1.0 | Map Priority (+3.6%) | Neutral | - | 28 |
| B | Juno | -1.02% | -1.72% ±1.5 | Standard (+0.9%) | Neutral | - | 52 |
| B | Soldier: 76 | -1.17% | -1.34% ±1.4 | Standard (-0.8%) | Neutral | - | 52 |
| B | D.Va | -1.20% | -1.49% ±1.4 | Niche (-1.1%) | Neutral | Better in GM+ | 52 |
| C | Echo | -1.64% | -1.80% ±1.3 | Standard (+0.1%) | Unfavorable | - | 52 |
| C | Doctrine *(provisional)* | -2.21% | -3.40% ±3.1 | Standard (-0.9%) | Deterrent | - | 8 |
| C | Ana | -2.51% | -2.56% ±0.7 | Niche (-6.2%) | Deterrent | - | 52 |
| D | Wrecking Ball | -3.16% | -3.39% ±1.2 | Standard (-0.0%) | Deterrent | - | 52 |
| D | Winston | -3.80% | -3.87% ±1.2 | Niche (-4.6%) | Deterrent | - | 52 |
| D | Widowmaker | -9.85% | -9.98% ±2.3 | Niche (-4.8%) | Deterrent | - | 51 |

### New Junk City

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| S | Junker Queen | +3.68% | +4.60% ±2.8 | Map Priority (+3.4%) | Meta | - | 50 |
| A | Lúcio | +2.96% | +3.15% ±1.6 | Map Priority (+7.4%) | Meta | - | 52 |
| A | Hazard | +2.40% | +2.93% ±1.8 | Standard (+1.0%) | Favorable | - | 51 |
| A | Symmetra | +2.07% | +3.53% ±2.9 | Standard (+0.5%) | Favorable | - | 50 |
| A | Mizuki | +1.99% | +3.21% ±2.9 | Map Priority (+5.0%) | Meta | Better in GM+ | 52 |
| A | Vendetta | +1.89% | +2.35% ±1.3 | Popular (+1.5%) | Meta | - | 48 |
| A | Moira | +1.57% | +2.60% ±2.2 | Map Priority (+5.3%) | Meta | - | 51 |
| A | D.Mon | +1.35% | +2.34% ±2.2 | Popular (+2.7%) | Favorable | - | 16 |
| A | Torbjörn | +1.33% | +1.85% ±2.5 | Standard (-0.1%) | Favorable | - | 50 |
| A | Reinhardt | +1.23% | +1.56% ±2.6 | Popular (+1.5%) | Favorable | Better in GM+ | 52 |
| B | Sombra *(provisional)* | +1.10% | +3.72% ±4.8 | Map Priority (+3.7%) | Neutral | - | 8 |
| B | Mauga | +1.02% | +1.42% ±1.8 | Popular (+2.5%) | Neutral | - | 50 |
| B | Reaper | +0.81% | +1.79% ±2.3 | Map Priority (+4.1%) | Neutral | - | 52 |
| B | Cassidy | +0.80% | +1.35% ±1.7 | Map Priority (+8.3%) | Neutral | - | 52 |
| B | Shion | +0.72% | +1.23% ±1.3 | Map Priority (+8.3%) | Neutral | - | 28 |
| B | Zarya | +0.71% | +1.35% ±2.7 | Popular (+2.8%) | Neutral | Better in Masters | 52 |
| B | Domina | +0.69% | +1.69% ±3.7 | Standard (-0.9%) | Neutral | Better in GM+ | 46 |
| B | Tracer | +0.68% | +1.06% ±1.7 | Map Priority (+5.7%) | Neutral | - | 52 |
| B | Wrecking Ball | +0.49% | +0.93% ±2.9 | Niche (-1.1%) | Neutral | Better in Masters | 52 |
| B | Sojourn | +0.39% | +0.56% ±1.2 | Map Priority (+3.3%) | Neutral | - | 52 |
| B | Brigitte | +0.37% | +0.77% ±2.3 | Standard (+0.9%) | Neutral | Better in GM+ | 51 |
| B | Anran | +0.35% | +0.87% ±2.6 | Popular (+1.8%) | Neutral | - | 51 |
| B | Orisa | +0.22% | +0.45% ±2.8 | Popular (+2.5%) | Neutral | - | 51 |
| B | Sierra | +0.22% | -1.36% ±1.6 | Standard (-1.0%) | Neutral | - | 26 |
| B | Doomfist | +0.21% | +1.11% ±2.6 | Standard (+0.2%) | Neutral | Better in Masters | 51 |
| B | Mei | +0.20% | +0.94% ±2.6 | Standard (+0.9%) | Neutral | - | 51 |
| B | Lifeweaver | +0.13% | +0.23% ±2.2 | Niche (-2.0%) | Neutral | Better in Masters | 49 |
| B | Baptiste | +0.11% | +1.92% ±3.5 | Niche (-1.8%) | Neutral | - | 52 |
| B | Ramattra | +0.09% | +0.54% ±2.8 | Popular (+1.8%) | Neutral | - | 52 |
| B | Venture | +0.04% | +1.43% ±2.2 | Popular (+1.1%) | Neutral | - | 50 |
| B | Doctrine *(provisional)* | -0.03% | +0.02% ±4.1 | Niche (-2.8%) | Neutral | Better in GM+ | 8 |
| B | Wuyang | -0.05% | -0.01% ±1.3 | Popular (+2.3%) | Neutral | - | 52 |
| B | Kiriko | -0.09% | -0.06% ±2.1 | Map Priority (+10.4%) | Neutral | Better in Masters | 52 |
| B | Emre | -0.11% | +0.28% ±1.6 | Niche (-3.9%) | Neutral | - | 51 |
| B | Roadhog *(provisional)* | -0.16% | +0.61% ±7.2 | Standard (+0.1%) | Neutral | - | 8 |
| B | Genji | -0.23% | -1.19% ±2.4 | Standard (+0.3%) | Neutral | - | 52 |
| B | Mercy | -0.29% | -0.37% ±2.6 | Niche (-3.1%) | Neutral | Better in GM+ | 49 |
| B | Juno | -0.30% | +0.24% ±1.6 | Standard (+0.3%) | Neutral | - | 50 |
| B | Illari | -0.32% | -1.22% ±3.0 | Niche (-4.9%) | Neutral | - | 52 |
| B | Soldier: 76 | -0.68% | -0.84% ±2.1 | Standard (-0.8%) | Neutral | - | 51 |
| B | Junkrat | -0.70% | -0.87% ±2.2 | Standard (+0.3%) | Neutral | Better in Masters | 49 |
| B | Bastion | -0.77% | -1.07% ±2.2 | Niche (-1.6%) | Neutral | - | 48 |
| B | Jetpack Cat | -0.96% | -1.17% ±2.4 | Standard (-0.9%) | Neutral | - | 51 |
| B | D.Va | -1.12% | -2.42% ±3.2 | Niche (-1.8%) | Neutral | Better in GM+ | 52 |
| C | Hanzo | -1.21% | -1.94% ±2.9 | Niche (-2.4%) | Unfavorable | - | 51 |
| C | Ashe | -1.23% | -3.06% ±3.2 | Niche (-7.1%) | Unfavorable | Better in Masters | 46 |
| C | Zenyatta | -1.39% | -1.98% ±1.9 | Niche (-3.5%) | Unfavorable | - | 50 |
| C | Echo | -1.47% | -1.81% ±2.0 | Niche (-3.5%) | Unfavorable | - | 51 |
| C | Freja | -2.63% | -5.83% ±3.3 | Niche (-3.0%) | Deterrent | Better in Masters | 47 |
| C | Sigma | -2.98% | -3.10% ±2.0 | Niche (-5.2%) | Deterrent | - | 51 |
| D | Ana | -4.14% | -5.24% ±2.6 | Niche (-14.8%) | Deterrent | Better in Masters | 52 |
| D | Pharah | -4.83% | -6.66% ±3.2 | Niche (-1.7%) | Deterrent | - | 51 |
| D | Winston | -6.98% | -8.10% ±3.0 | Niche (-7.1%) | Deterrent | Better in Masters | 52 |
| D | Widowmaker | -18.09% | -19.36% ±4.6 | Niche (-6.4%) | Deterrent | Better in Masters | 29 |

### New Queen Street

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| S | Soldier: 76 | +4.10% | +5.27% ±1.5 | Map Priority (+13.1%) | Meta | - | 52 |
| A | Torbjörn | +2.98% | +3.37% ±1.5 | Standard (-0.4%) | Specialist | - | 51 |
| A | Junker Queen | +1.73% | +2.00% ±2.0 | Standard (+0.7%) | Favorable | - | 49 |
| A | Kiriko | +1.61% | +2.38% ±1.9 | Map Priority (+6.1%) | Meta | - | 52 |
| A | Wrecking Ball | +1.36% | +1.80% ±2.1 | Popular (+2.5%) | Favorable | - | 52 |
| A | Mizuki | +1.25% | +1.47% ±1.5 | Standard (+0.7%) | Favorable | - | 52 |
| A | Ramattra | +1.25% | +2.30% ±2.8 | Niche (-1.3%) | Favorable | - | 46 |
| B | Symmetra | +1.13% | +2.95% ±4.1 | Niche (-1.1%) | Neutral | - | 41 |
| B | Wuyang | +1.13% | +1.62% ±1.4 | Popular (+2.3%) | Neutral | - | 52 |
| B | Junkrat | +1.08% | +2.01% ±3.8 | Niche (-1.5%) | Neutral | - | 49 |
| B | Tracer | +1.00% | +1.24% ±1.2 | Map Priority (+7.8%) | Neutral | - | 52 |
| B | D.Mon | +0.92% | +2.52% ±3.3 | Standard (+0.8%) | Neutral | Better in GM+ | 16 |
| B | Doomfist | +0.89% | +2.62% ±2.3 | Popular (+1.1%) | Neutral | - | 52 |
| B | Zarya | +0.79% | +0.99% ±1.5 | Niche (-1.4%) | Neutral | - | 51 |
| B | Reinhardt | +0.78% | +0.95% ±2.2 | Standard (-0.1%) | Neutral | Better in GM+ | 52 |
| B | Freja | +0.67% | +2.31% ±3.1 | Niche (-1.6%) | Neutral | - | 51 |
| B | Mauga | +0.65% | +1.23% ±2.4 | Popular (+1.2%) | Neutral | Better in GM+ | 51 |
| B | Reaper | +0.61% | +1.26% ±2.0 | Niche (-1.1%) | Neutral | - | 52 |
| B | Hazard | +0.48% | +1.06% ±3.2 | Standard (+0.8%) | Neutral | Better in Masters | 52 |
| B | Zenyatta | +0.41% | +1.27% ±2.4 | Niche (-3.0%) | Neutral | Better in GM+ | 52 |
| B | Mercy | +0.28% | +0.89% ±2.4 | Standard (-0.8%) | Neutral | - | 49 |
| B | Sierra | +0.22% | -1.07% ±2.0 | Standard (-0.1%) | Neutral | Better in Masters | 34 |
| B | Hanzo | +0.18% | +0.45% ±1.9 | Niche (-3.2%) | Neutral | - | 50 |
| B | Lúcio | +0.15% | +0.19% ±1.1 | Popular (+1.4%) | Neutral | - | 52 |
| B | Lifeweaver | +0.13% | +1.90% ±3.0 | Standard (-0.7%) | Neutral | Better in GM+ | 51 |
| B | Shion | +0.07% | +0.22% ±1.2 | Map Priority (+5.2%) | Neutral | - | 28 |
| B | Venture | +0.04% | +0.06% ±3.5 | Standard (-0.5%) | Neutral | Better in Masters | 51 |
| B | Winston | -0.19% | -0.07% ±1.8 | Standard (+0.6%) | Neutral | - | 52 |
| B | Genji | -0.24% | -0.75% ±1.6 | Niche (-1.3%) | Neutral | - | 52 |
| B | Illari | -0.27% | -0.46% ±1.6 | Niche (-1.4%) | Neutral | - | 52 |
| B | Mei | -0.37% | -1.12% ±3.4 | Niche (-1.5%) | Neutral | Better in Masters | 52 |
| B | Brigitte | -0.41% | -0.38% ±1.5 | Standard (+0.9%) | Neutral | - | 52 |
| B | Emre | -0.52% | -0.87% ±1.7 | Standard (-0.0%) | Neutral | - | 52 |
| B | Moira | -0.52% | -0.16% ±2.9 | Standard (+0.5%) | Neutral | - | 52 |
| B | D.Va | -0.53% | -0.50% ±2.6 | Standard (+0.8%) | Neutral | - | 52 |
| B | Juno | -0.68% | -0.91% ±2.0 | Standard (+0.8%) | Neutral | - | 52 |
| B | Vendetta | -0.73% | -1.28% ±2.8 | Standard (-0.2%) | Neutral | - | 48 |
| B | Baptiste | -0.80% | -1.11% ±2.5 | Niche (-2.6%) | Neutral | Better in GM+ | 52 |
| B | Echo | -0.80% | -0.92% ±2.8 | Niche (-2.7%) | Neutral | Better in Masters | 52 |
| B | Ashe | -0.86% | -1.03% ±2.1 | Niche (-4.4%) | Neutral | Better in Masters | 51 |
| B | Sojourn | -0.88% | -0.98% ±1.2 | Popular (+1.9%) | Neutral | - | 52 |
| B | Pharah | -1.05% | -1.07% ±2.3 | Niche (-1.9%) | Neutral | - | 52 |
| B | Sombra *(provisional)* | -1.17% | -1.62% ±5.0 | Map Priority (+3.3%) | Neutral | Better in Masters | 8 |
| C | Bastion | -1.26% | -2.13% ±3.0 | Niche (-1.5%) | Unfavorable | Better in Masters | 48 |
| C | Cassidy | -1.28% | -1.69% ±1.6 | Standard (-0.2%) | Unfavorable | Better in GM+ | 52 |
| C | Orisa | -1.35% | -2.23% ±2.7 | Standard (-0.2%) | Unfavorable | Better in Masters | 52 |
| C | Doctrine *(provisional)* | -1.45% | -2.39% ±3.4 | Standard (+0.8%) | Unfavorable | - | 8 |
| C | Anran | -1.77% | -2.94% ±2.4 | Standard (-0.0%) | Deterrent | Better in Masters | 50 |
| C | Roadhog *(provisional)* | -1.95% | -5.68% ±6.4 | Standard (-0.0%) | Deterrent | Better in Masters | 8 |
| C | Domina | -1.99% | -2.46% ±3.6 | Standard (-0.9%) | Deterrent | Better in Masters | 49 |
| C | Jetpack Cat | -2.51% | -2.86% ±1.8 | Standard (+0.5%) | Unfavorable | - | 52 |
| D | Ana | -3.39% | -3.60% ±1.3 | Niche (-4.9%) | Deterrent | - | 52 |
| D | Sigma | -5.19% | -5.60% ±2.2 | Niche (-4.4%) | Deterrent | Better in GM+ | 52 |
| D | Widowmaker | -7.58% | -7.64% ±2.2 | Niche (-3.7%) | Deterrent | - | 51 |

### Numbani

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| A | Wrecking Ball | +1.86% | +2.76% ±2.7 | Standard (+0.5%) | Favorable | Better in GM+ | 51 |
| A | Doctrine *(provisional)* | +1.74% | +5.20% ±5.7 | Popular (+2.2%) | Meta | Better in GM+ | 8 |
| A | Winston | +1.47% | +1.83% ±2.2 | Map Priority (+9.6%) | Favorable | - | 52 |
| B | Bastion | +0.90% | +1.69% ±3.4 | Popular (+1.1%) | Neutral | Better in GM+ | 51 |
| B | Ana | +0.59% | +0.82% ±2.2 | Map Priority (+7.3%) | Neutral | - | 52 |
| B | Mercy | +0.44% | +1.57% ±2.8 | Popular (+2.3%) | Neutral | - | 51 |
| B | Tracer | +0.31% | +0.65% ±1.9 | Standard (+0.2%) | Neutral | - | 52 |
| B | Sierra | +0.22% | +2.14% ±3.9 | Standard (+0.2%) | Neutral | Better in Masters | 32 |
| B | Kiriko | +0.19% | +0.30% ±1.6 | Standard (+0.4%) | Neutral | Better in Masters | 52 |
| B | Lifeweaver | +0.13% | +1.04% ±4.0 | Popular (+1.1%) | Neutral | - | 51 |
| B | Junkrat | +0.12% | +0.28% ±3.7 | Standard (-0.0%) | Neutral | Better in GM+ | 50 |
| B | Venture | +0.04% | -3.68% ±4.0 | Standard (-0.1%) | Neutral | Better in GM+ | 51 |
| B | D.Va | -0.07% | +1.33% ±3.6 | Popular (+2.1%) | Neutral | - | 51 |
| B | Freja | -0.23% | +0.51% ±4.0 | Popular (+1.1%) | Neutral | - | 52 |
| B | Ashe | -0.28% | +0.63% ±2.3 | Map Priority (+5.8%) | Neutral | - | 52 |
| B | Hazard | -0.31% | -0.26% ±2.1 | Popular (+2.4%) | Neutral | Better in Masters | 50 |
| B | Genji | -0.34% | -2.40% ±2.2 | Popular (+1.2%) | Neutral | - | 52 |
| B | Emre | -0.41% | -0.90% ±3.1 | Standard (+0.7%) | Neutral | Better in GM+ | 52 |
| B | Cassidy | -0.55% | -0.70% ±1.9 | Niche (-2.8%) | Neutral | - | 52 |
| B | Anran | -0.63% | -1.29% ±3.8 | Standard (-0.4%) | Neutral | - | 50 |
| B | Mei | -0.63% | -3.39% ±4.4 | Standard (-0.8%) | Neutral | Better in GM+ | 50 |
| B | Doomfist | -0.64% | -1.68% ±3.3 | Standard (+0.6%) | Neutral | Better in GM+ | 52 |
| B | Soldier: 76 | -0.70% | -0.88% ±2.1 | Standard (+0.5%) | Neutral | - | 52 |
| B | Hanzo | -0.71% | -1.01% ±3.1 | Standard (+0.1%) | Neutral | Better in GM+ | 52 |
| B | Illari | -0.72% | -2.33% ±2.1 | Standard (+0.7%) | Neutral | - | 52 |
| B | Sombra *(provisional)* | -0.72% | -0.20% ±7.6 | Niche (-1.7%) | Neutral | Better in GM+ | 8 |
| B | Shion | -0.75% | -1.33% ±1.9 | Niche (-3.4%) | Neutral | - | 28 |
| B | Juno | -0.84% | -2.61% ±3.1 | Standard (-0.6%) | Neutral | Better in Masters | 51 |
| B | Vendetta | -0.86% | -1.94% ±3.6 | Standard (-0.1%) | Neutral | Better in Masters | 43 |
| B | Echo | -1.05% | -1.32% ±2.6 | Map Priority (+5.1%) | Neutral | - | 52 |
| B | Torbjörn | -1.16% | -1.75% ±3.1 | Standard (+0.6%) | Neutral | Better in Masters | 50 |
| B | Jetpack Cat | -1.17% | -1.61% ±3.1 | Popular (+1.2%) | Neutral | Better in GM+ | 52 |
| C | Wuyang | -1.24% | -2.04% ±2.0 | Niche (-3.1%) | Unfavorable | - | 51 |
| C | Zenyatta | -1.24% | -2.32% ±2.8 | Niche (-2.1%) | Unfavorable | - | 52 |
| C | Roadhog *(provisional)* | -1.25% | -10.23% ±13.4 | Standard (-0.3%) | Unfavorable | Better in Masters | 7 |
| C | Sigma | -1.34% | -1.28% ±2.5 | Niche (-2.7%) | Unfavorable | Better in Masters | 51 |
| C | Orisa | -1.54% | -3.03% ±3.3 | Niche (-1.9%) | Deterrent | Better in GM+ | 51 |
| C | D.Mon | -1.68% | -6.15% ±5.5 | Niche (-2.4%) | Deterrent | Better in Masters | 16 |
| C | Baptiste | -1.69% | -4.27% ±3.2 | Standard (-0.1%) | Deterrent | Better in Masters | 52 |
| C | Mauga | -1.83% | -2.66% ±2.9 | Standard (-0.7%) | Deterrent | Better in Masters | 48 |
| C | Brigitte | -1.90% | -2.72% ±2.6 | Popular (+1.2%) | Trap Pick | Better in GM+ | 51 |
| C | Reaper | -1.96% | -4.50% ±3.2 | Standard (-0.5%) | Deterrent | - | 52 |
| C | Zarya | -2.16% | -2.88% ±3.3 | Niche (-2.2%) | Deterrent | - | 52 |
| C | Sojourn | -2.41% | -4.63% ±2.8 | Niche (-6.4%) | Deterrent | - | 52 |
| C | Moira | -2.44% | -4.00% ±3.7 | Niche (-2.3%) | Deterrent | Better in GM+ | 51 |
| C | Symmetra | -2.46% | -4.90% ±4.3 | Standard (-0.6%) | Deterrent | - | 46 |
| C | Reinhardt | -2.94% | -4.23% ±4.4 | Niche (-2.1%) | Deterrent | Better in GM+ | 51 |
| D | Ramattra | -3.22% | -4.89% ±3.3 | Niche (-1.9%) | Deterrent | - | 41 |
| D | Pharah | -3.29% | -4.42% ±3.2 | Standard (-0.1%) | Deterrent | Better in Masters | 51 |
| D | Mizuki | -3.36% | -4.46% ±2.1 | Niche (-2.8%) | Deterrent | - | 51 |
| D | Lúcio | -3.84% | -4.28% ±4.0 | Niche (-2.6%) | Deterrent | Better in GM+ | 52 |
| D | Domina | -4.26% | -5.48% ±3.1 | Standard (-0.9%) | Deterrent | - | 45 |
| D | Junker Queen | -6.89% | -10.10% ±4.7 | Niche (-1.5%) | Deterrent | - | 39 |
| D | Widowmaker | -9.36% | -9.48% ±2.4 | Niche (-2.6%) | Deterrent | - | 51 |

### Oasis

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| S | Torbjörn | +3.42% | +3.84% ±1.4 | Standard (-0.3%) | Specialist | - | 51 |
| A | Cassidy | +2.09% | +2.36% ±0.8 | Map Priority (+11.6%) | Meta | - | 52 |
| A | Orisa | +1.77% | +2.32% ±1.8 | Standard (+0.5%) | Favorable | - | 52 |
| A | Doomfist | +1.48% | +2.37% ±1.4 | Popular (+1.1%) | Favorable | - | 52 |
| B | Jetpack Cat | +1.11% | +1.20% ±1.2 | Popular (+1.0%) | Neutral | - | 52 |
| B | Hazard | +1.00% | +1.10% ±1.1 | Popular (+2.3%) | Neutral | - | 52 |
| B | Mizuki | +0.96% | +1.04% ±1.1 | Map Priority (+3.1%) | Neutral | - | 52 |
| B | Vendetta | +0.92% | +1.41% ±1.9 | Standard (+0.5%) | Neutral | - | 48 |
| B | Freja | +0.81% | +2.31% ±2.8 | Niche (-1.5%) | Neutral | - | 52 |
| B | Kiriko | +0.81% | +0.89% ±0.8 | Map Priority (+7.0%) | Neutral | - | 52 |
| B | Brigitte | +0.77% | +0.87% ±0.9 | Popular (+2.2%) | Neutral | - | 52 |
| B | Zarya | +0.57% | +0.70% ±1.3 | Standard (+0.1%) | Neutral | - | 52 |
| B | Mauga | +0.55% | +1.26% ±2.8 | Popular (+1.1%) | Neutral | - | 51 |
| B | Moira | +0.54% | +0.85% ±1.5 | Popular (+2.0%) | Neutral | - | 52 |
| B | Shion | +0.54% | +0.82% ±1.0 | Map Priority (+5.2%) | Neutral | - | 28 |
| B | Reaper | +0.44% | +0.72% ±1.5 | Popular (+1.8%) | Neutral | - | 52 |
| B | Illari | +0.43% | +1.67% ±1.7 | Niche (-2.9%) | Neutral | - | 52 |
| B | Ramattra | +0.43% | +0.80% ±2.1 | Standard (-0.9%) | Neutral | - | 50 |
| B | Roadhog *(provisional)* | +0.42% | +2.21% ±6.0 | Standard (+0.2%) | Neutral | Better in Masters | 8 |
| B | Hanzo | +0.39% | +1.00% ±2.5 | Niche (-2.6%) | Neutral | - | 52 |
| B | Soldier: 76 | +0.28% | +0.36% ±1.0 | Niche (-1.1%) | Neutral | - | 52 |
| B | Domina | +0.25% | +0.60% ±2.5 | Standard (-0.9%) | Neutral | - | 47 |
| B | Sierra | +0.22% | +0.52% ±1.8 | Standard (-0.6%) | Neutral | - | 32 |
| B | Tracer | +0.16% | +0.20% ±0.7 | Map Priority (+6.8%) | Neutral | - | 52 |
| B | Lifeweaver | +0.13% | +0.37% ±2.0 | Niche (-1.2%) | Neutral | - | 49 |
| B | Wuyang | +0.07% | +0.10% ±0.8 | Standard (-0.8%) | Neutral | - | 52 |
| B | Venture | +0.04% | -0.62% ±1.9 | Standard (+0.0%) | Neutral | Better in GM+ | 52 |
| B | Sojourn | -0.02% | +0.02% ±0.8 | Niche (-2.4%) | Neutral | - | 52 |
| B | Mei | -0.05% | +0.03% ±1.5 | Standard (-0.7%) | Neutral | - | 52 |
| B | Anran | -0.06% | +0.14% ±2.7 | Standard (+0.4%) | Neutral | - | 52 |
| B | Junkrat | -0.06% | -0.06% ±1.7 | Standard (-0.4%) | Neutral | - | 51 |
| B | D.Va | -0.21% | +0.23% ±2.4 | Standard (+0.8%) | Neutral | Better in GM+ | 52 |
| B | Symmetra | -0.30% | -0.27% ±1.5 | Standard (+0.3%) | Neutral | - | 52 |
| B | Baptiste | -0.34% | -0.13% ±2.0 | Niche (-1.3%) | Neutral | Better in Masters | 52 |
| B | Bastion | -0.34% | -0.43% ±1.9 | Niche (-1.0%) | Neutral | - | 51 |
| B | Genji | -0.36% | -1.24% ±1.3 | Standard (-0.5%) | Neutral | - | 52 |
| B | Zenyatta | -0.49% | -0.50% ±1.2 | Niche (-3.1%) | Neutral | - | 52 |
| B | Junker Queen | -0.56% | -0.51% ±2.0 | Standard (+0.8%) | Neutral | - | 52 |
| B | Juno | -0.62% | -0.69% ±1.9 | Standard (+0.0%) | Neutral | - | 52 |
| B | Echo | -0.65% | -0.66% ±1.5 | Standard (-0.3%) | Neutral | - | 52 |
| B | Sombra *(provisional)* | -0.65% | -0.35% ±4.8 | Map Priority (+3.7%) | Neutral | Better in Masters | 8 |
| B | Lúcio | -0.72% | -0.70% ±1.0 | Map Priority (+4.0%) | Neutral | - | 52 |
| B | Winston | -0.73% | -0.69% ±1.2 | Standard (-0.6%) | Neutral | - | 52 |
| B | Emre | -0.90% | -1.46% ±1.2 | Niche (-3.2%) | Neutral | - | 52 |
| B | Mercy | -0.95% | -1.31% ±1.5 | Niche (-1.1%) | Neutral | - | 51 |
| B | D.Mon | -0.97% | -1.28% ±2.2 | Standard (+0.6%) | Neutral | - | 16 |
| B | Ashe | -1.03% | -1.51% ±2.2 | Niche (-6.4%) | Neutral | - | 52 |
| B | Pharah | -1.06% | -1.08% ±2.4 | Standard (+0.9%) | Neutral | Better in Masters | 52 |
| B | Reinhardt | -1.17% | -1.21% ±1.6 | Standard (-0.5%) | Neutral | - | 51 |
| C | Ana | -1.96% | -2.00% ±0.8 | Niche (-9.2%) | Deterrent | - | 52 |
| C | Wrecking Ball | -2.24% | -2.48% ±1.5 | Standard (+0.8%) | Unfavorable | - | 52 |
| C | Doctrine *(provisional)* | -2.81% | -4.89% ±3.6 | Niche (-2.8%) | Deterrent | Better in Masters | 8 |
| D | Sigma | -4.12% | -4.34% ±2.0 | Niche (-6.0%) | Deterrent | - | 52 |
| D | Widowmaker | -15.52% | -15.93% ±2.9 | Niche (-5.5%) | Deterrent | Better in Masters | 46 |

### Paraiso

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| A | Jetpack Cat | +2.08% | +4.69% ±4.8 | Popular (+1.6%) | Meta | Better in GM+ | 16 |
| A | Doctrine *(provisional)* | +1.91% | +11.86% ±9.2 | Map Priority (+3.9%) | Meta | Better in GM+ | 8 |
| A | Bastion | +1.47% | +6.42% ±6.7 | Standard (+0.4%) | Favorable | Better in GM+ | 15 |
| A | Winston | +1.46% | +1.97% ±2.6 | Map Priority (+4.6%) | Favorable | Better in GM+ | 16 |
| A | Ana | +1.25% | +1.68% ±2.3 | Map Priority (+7.5%) | Favorable | Better in GM+ | 16 |
| B | Pharah | +1.02% | +2.55% ±4.0 | Standard (+0.1%) | Neutral | Better in GM+ | 16 |
| B | Mercy | +0.96% | +5.29% ±4.1 | Popular (+1.9%) | Neutral | Better in GM+ | 16 |
| B | Orisa | +0.26% | +1.31% ±5.7 | Niche (-2.4%) | Neutral | Better in GM+ | 16 |
| B | Sierra | +0.22% | +0.25% ±7.5 | Standard (+0.3%) | Neutral | Better in Masters | 11 |
| B | Vendetta | +0.17% | +1.30% ±5.0 | Standard (-0.2%) | Neutral | Better in GM+ | 16 |
| B | Lifeweaver | +0.13% | +1.03% ±7.2 | Standard (+0.9%) | Neutral | Better in GM+ | 16 |
| B | Venture | +0.04% | -3.40% ±8.6 | Standard (-0.2%) | Neutral | - | 15 |
| B | Echo | -0.00% | +0.68% ±3.3 | Map Priority (+5.0%) | Neutral | - | 16 |
| B | Mei | -0.02% | +2.33% ±7.5 | Niche (-1.0%) | Neutral | Better in GM+ | 16 |
| B | Symmetra | -0.09% | +1.84% ±8.4 | Standard (-0.6%) | Neutral | Better in GM+ | 15 |
| B | Genji | -0.21% | -0.90% ±2.7 | Popular (+1.4%) | Neutral | - | 16 |
| B | Emre | -0.35% | -0.42% ±3.2 | Popular (+1.3%) | Neutral | Better in Masters | 16 |
| B | Brigitte | -0.38% | -0.08% ±4.9 | Standard (+0.5%) | Neutral | Better in Masters | 16 |
| B | D.Va | -0.39% | +0.24% ±4.2 | Map Priority (+4.4%) | Neutral | - | 16 |
| B | Illari | -0.40% | -3.31% ±4.3 | Popular (+1.4%) | Neutral | Better in Masters | 16 |
| B | Mauga | -0.40% | +0.51% ±7.4 | Standard (-0.6%) | Neutral | - | 15 |
| B | Soldier: 76 | -0.41% | -0.59% ±5.1 | Standard (-0.3%) | Neutral | Better in GM+ | 16 |
| B | Zenyatta | -0.48% | -0.53% ±3.0 | Standard (-0.9%) | Neutral | - | 16 |
| B | Doomfist | -0.50% | -2.10% ±5.3 | Standard (-0.9%) | Neutral | Better in Masters | 16 |
| B | Shion | -0.50% | -1.42% ±3.5 | Niche (-4.1%) | Neutral | - | 16 |
| B | Reinhardt | -0.56% | -0.57% ±7.0 | Niche (-1.2%) | Neutral | Better in GM+ | 16 |
| B | Kiriko | -0.57% | -0.97% ±2.7 | Niche (-2.7%) | Neutral | - | 16 |
| B | D.Mon | -0.60% | -1.11% ±4.7 | Standard (-0.6%) | Neutral | Better in Masters | 16 |
| B | Junkrat | -0.63% | -2.48% ±7.6 | Standard (+0.5%) | Neutral | - | 16 |
| B | Ashe | -0.66% | -0.14% ±3.6 | Map Priority (+6.4%) | Neutral | Better in Masters | 16 |
| B | Roadhog *(provisional)* | -0.68% | -3.75% ±13.9 | Standard (-0.2%) | Neutral | Better in Masters | 8 |
| B | Juno | -0.70% | -3.29% ±6.0 | Standard (-0.8%) | Neutral | Better in Masters | 16 |
| B | Freja | -0.75% | -2.13% ±6.8 | Standard (+0.9%) | Neutral | Better in Masters | 16 |
| B | Baptiste | -0.79% | -1.69% ±4.3 | Standard (-0.2%) | Neutral | Better in GM+ | 16 |
| B | Tracer | -0.94% | -1.43% ±3.0 | Niche (-3.7%) | Neutral | - | 16 |
| B | Anran | -1.01% | -6.13% ±7.3 | Standard (-0.2%) | Neutral | Better in Masters | 15 |
| B | Torbjörn | -1.16% | -2.54% ±4.7 | Standard (+0.5%) | Neutral | Better in GM+ | 15 |
| C | Moira | -1.25% | -1.47% ±3.6 | Niche (-1.6%) | Unfavorable | - | 15 |
| C | Wrecking Ball | -1.29% | -3.49% ±6.6 | Standard (-0.7%) | Unfavorable | Better in GM+ | 16 |
| C | Wuyang | -1.35% | -4.55% ±3.8 | Niche (-2.2%) | Unfavorable | Better in Masters | 16 |
| C | Cassidy | -1.36% | -2.20% ±2.2 | Niche (-2.9%) | Unfavorable | - | 16 |
| C | Sojourn | -1.36% | -4.47% ±4.7 | Niche (-4.7%) | Unfavorable | Better in Masters | 16 |
| C | Hazard | -1.38% | -2.02% ±3.7 | Popular (+2.0%) | Unfavorable | Better in Masters | 16 |
| C | Widowmaker | -1.38% | -1.16% ±3.7 | Popular (+2.1%) | Unfavorable | - | 16 |
| C | Mizuki | -1.42% | -5.08% ±6.1 | Niche (-2.4%) | Unfavorable | - | 16 |
| C | Sombra *(provisional)* | -1.46% | -7.81% ±13.4 | Standard (-0.1%) | Unfavorable | - | 8 |
| C | Reaper | -1.47% | -3.83% ±3.7 | Standard (-0.3%) | Unfavorable | Better in Masters | 16 |
| C | Ramattra | -1.56% | -5.55% ±9.2 | Niche (-1.7%) | Deterrent | Better in GM+ | 13 |
| C | Hanzo | -2.01% | -4.18% ±3.5 | Standard (+0.1%) | Unfavorable | - | 16 |
| C | Junker Queen | -2.15% | -4.84% ±10.1 | Niche (-1.1%) | Deterrent | Better in GM+ | 14 |
| C | Domina | -2.66% | -7.36% ±8.6 | Standard (-0.1%) | Deterrent | Better in GM+ | 13 |
| D | Zarya | -3.08% | -5.69% ±4.7 | Niche (-1.7%) | Deterrent | Better in Masters | 16 |
| D | Sigma | -3.18% | -3.73% ±4.0 | Standard (-0.7%) | Deterrent | - | 16 |
| D | Lúcio | -5.64% | -8.70% ±7.3 | Niche (-3.0%) | Deterrent | - | 16 |

### Rialto

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| A | Widowmaker | +2.15% | +2.40% ±2.8 | Map Priority (+7.5%) | Meta | - | 52 |
| A | Ana | +1.42% | +1.87% ±2.3 | Map Priority (+10.6%) | Favorable | - | 52 |
| B | Pharah | +1.16% | +1.84% ±2.6 | Popular (+1.8%) | Neutral | - | 52 |
| B | Sigma | +1.11% | +1.47% ±2.3 | Popular (+1.3%) | Neutral | - | 52 |
| B | Winston | +0.94% | +1.08% ±1.5 | Popular (+1.1%) | Neutral | - | 51 |
| B | Brigitte | +0.91% | +2.06% ±3.0 | Niche (-1.8%) | Neutral | Better in GM+ | 52 |
| B | Bastion | +0.86% | +1.63% ±3.4 | Standard (+0.8%) | Neutral | Better in GM+ | 50 |
| B | Wuyang | +0.48% | +1.05% ±2.1 | Niche (-1.3%) | Neutral | Better in GM+ | 52 |
| B | Hazard | +0.35% | +0.50% ±1.7 | Standard (+0.2%) | Neutral | - | 51 |
| B | Echo | +0.34% | +0.67% ±1.8 | Map Priority (+3.2%) | Neutral | - | 52 |
| B | Illari | +0.33% | +0.97% ±1.4 | Map Priority (+3.2%) | Neutral | - | 52 |
| B | Sierra | +0.22% | +0.20% ±2.1 | Standard (+0.3%) | Neutral | - | 37 |
| B | Anran | +0.14% | +0.98% ±4.0 | Standard (-0.7%) | Neutral | - | 51 |
| B | Emre | +0.13% | +2.13% ±2.5 | Popular (+1.7%) | Neutral | Better in GM+ | 52 |
| B | Lifeweaver | +0.13% | -0.85% ±2.6 | Standard (+1.0%) | Neutral | - | 50 |
| B | Freja | +0.11% | +0.92% ±2.9 | Standard (+0.7%) | Neutral | Better in GM+ | 52 |
| B | Venture | +0.04% | -0.96% ±2.9 | Standard (-0.3%) | Neutral | Better in Masters | 51 |
| B | Zarya | +0.03% | +0.37% ±2.6 | Standard (-0.7%) | Neutral | Better in GM+ | 51 |
| B | D.Va | -0.00% | +0.50% ±2.0 | Popular (+1.6%) | Neutral | - | 51 |
| B | Hanzo | +0.00% | +0.30% ±2.4 | Popular (+1.6%) | Neutral | - | 52 |
| B | Reaper | -0.03% | +0.41% ±2.8 | Niche (-2.0%) | Neutral | - | 52 |
| B | Shion | -0.08% | +0.03% ±1.4 | Niche (-5.6%) | Neutral | - | 28 |
| B | Genji | -0.11% | +0.85% ±2.4 | Standard (-0.4%) | Neutral | - | 52 |
| B | Mei | -0.11% | -0.00% ±2.7 | Standard (+0.3%) | Neutral | Better in Masters | 51 |
| B | Baptiste | -0.19% | +0.40% ±2.6 | Standard (+0.6%) | Neutral | - | 52 |
| B | Orisa | -0.21% | -0.27% ±2.2 | Standard (+0.1%) | Neutral | Better in Masters | 52 |
| B | Doomfist | -0.27% | -0.22% ±3.0 | Standard (-0.1%) | Neutral | - | 52 |
| B | Ashe | -0.40% | -0.02% ±1.7 | Map Priority (+4.8%) | Neutral | - | 52 |
| B | Vendetta | -0.40% | -0.71% ±3.4 | Standard (-0.6%) | Neutral | Better in GM+ | 46 |
| B | D.Mon | -0.45% | -0.52% ±3.1 | Niche (-1.0%) | Neutral | Better in GM+ | 16 |
| B | Mercy | -0.45% | -0.72% ±2.4 | Popular (+1.3%) | Neutral | - | 51 |
| B | Kiriko | -0.48% | -0.54% ±1.2 | Niche (-6.2%) | Neutral | - | 52 |
| B | Junkrat | -0.56% | -0.75% ±2.6 | Standard (+0.0%) | Neutral | - | 51 |
| B | Zenyatta | -0.64% | -0.81% ±2.3 | Map Priority (+3.4%) | Neutral | - | 52 |
| B | Sojourn | -0.66% | -0.86% ±2.4 | Niche (-1.6%) | Neutral | Better in Masters | 52 |
| B | Jetpack Cat | -0.71% | -0.82% ±2.1 | Standard (+0.5%) | Neutral | Better in GM+ | 51 |
| B | Mizuki | -0.71% | -0.83% ±1.6 | Niche (-2.7%) | Neutral | - | 51 |
| B | Ramattra | -0.75% | -0.69% ±3.4 | Standard (-0.5%) | Neutral | Better in GM+ | 49 |
| B | Domina | -0.80% | -0.69% ±2.9 | Standard (+0.3%) | Neutral | Better in GM+ | 50 |
| B | Junker Queen | -0.87% | -0.73% ±4.9 | Standard (-1.0%) | Neutral | - | 45 |
| B | Tracer | -0.89% | -1.19% ±2.5 | Niche (-4.7%) | Neutral | Better in Masters | 52 |
| B | Juno | -0.95% | -2.82% ±2.7 | Niche (-1.8%) | Neutral | - | 51 |
| B | Moira | -1.01% | -1.00% ±2.5 | Niche (-2.3%) | Neutral | Better in GM+ | 51 |
| C | Doctrine *(provisional)* | -1.32% | -3.39% ±5.3 | Standard (+0.4%) | Unfavorable | Better in Masters | 8 |
| C | Roadhog *(provisional)* | -1.38% | -9.40% ±11.8 | Standard (+0.8%) | Unfavorable | Better in Masters | 8 |
| C | Reinhardt | -1.43% | -1.56% ±2.3 | Standard (+0.3%) | Unfavorable | Better in Masters | 51 |
| C | Cassidy | -1.45% | -2.17% ±1.9 | Niche (-7.3%) | Unfavorable | - | 52 |
| C | Soldier: 76 | -1.46% | -2.13% ±2.3 | Niche (-1.5%) | Unfavorable | - | 51 |
| C | Mauga | -1.66% | -2.30% ±2.7 | Niche (-1.2%) | Deterrent | - | 49 |
| C | Sombra *(provisional)* | -1.88% | -9.20% ±11.1 | Niche (-4.3%) | Deterrent | Better in Masters | 8 |
| C | Torbjörn | -1.94% | -2.53% ±2.3 | Standard (+0.3%) | Unfavorable | - | 50 |
| C | Symmetra | -2.02% | -2.53% ±2.2 | Standard (-0.5%) | Deterrent | - | 49 |
| C | Wrecking Ball | -2.62% | -3.07% ±1.9 | Standard (-1.0%) | Deterrent | - | 51 |
| D | Lúcio | -6.33% | -6.82% ±2.7 | Niche (-4.0%) | Deterrent | - | 50 |

### Route 66

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| A | Ana | +2.44% | +2.63% ±1.2 | Map Priority (+7.3%) | Meta | - | 52 |
| A | Sombra *(provisional)* | +1.62% | +7.68% ±6.4 | Popular (+2.7%) | Meta | Better in GM+ | 8 |
| B | Torbjörn | +0.95% | +1.46% ±3.0 | Standard (+0.5%) | Neutral | - | 51 |
| B | Tracer | +0.84% | +1.58% ±2.2 | Niche (-3.6%) | Neutral | Better in GM+ | 52 |
| B | Shion | +0.83% | +2.92% ±2.4 | Niche (-3.7%) | Neutral | - | 28 |
| B | Wrecking Ball | +0.65% | +1.06% ±2.6 | Standard (+0.0%) | Neutral | - | 52 |
| B | Hazard | +0.62% | +1.26% ±3.1 | Standard (+0.4%) | Neutral | - | 51 |
| B | Mercy | +0.62% | +3.03% ±3.6 | Popular (+2.6%) | Neutral | - | 51 |
| B | Cassidy | +0.54% | +1.01% ±1.8 | Niche (-2.7%) | Neutral | Better in GM+ | 52 |
| B | Baptiste | +0.45% | +2.16% ±2.7 | Popular (+1.2%) | Neutral | - | 52 |
| B | Hanzo | +0.34% | +0.84% ±2.3 | Popular (+1.5%) | Neutral | Better in Masters | 51 |
| B | Sojourn | +0.26% | +0.74% ±2.2 | Niche (-2.2%) | Neutral | - | 52 |
| B | Sierra | +0.22% | +1.77% ±4.4 | Standard (+0.8%) | Neutral | Better in GM+ | 36 |
| B | Doctrine *(provisional)* | +0.20% | +0.50% ±4.4 | Popular (+1.4%) | Neutral | - | 8 |
| B | D.Va | +0.18% | +2.82% ±4.0 | Popular (+1.1%) | Neutral | Better in Masters | 52 |
| B | Ashe | +0.13% | +1.62% ±2.1 | Map Priority (+5.3%) | Neutral | - | 52 |
| B | Lifeweaver | +0.13% | +1.17% ±2.6 | Popular (+1.3%) | Neutral | - | 49 |
| B | Brigitte | +0.05% | +0.29% ±2.2 | Standard (+0.2%) | Neutral | - | 50 |
| B | Venture | +0.04% | -1.57% ±3.7 | Standard (-0.0%) | Neutral | Better in GM+ | 50 |
| B | Doomfist | -0.00% | +0.87% ±3.3 | Standard (-1.0%) | Neutral | Better in GM+ | 51 |
| B | Mauga | -0.02% | +0.74% ±4.0 | Niche (-1.4%) | Neutral | - | 50 |
| B | Junkrat | -0.03% | -0.01% ±2.7 | Standard (-0.1%) | Neutral | - | 48 |
| B | Illari | -0.10% | +0.22% ±2.4 | Map Priority (+3.2%) | Neutral | - | 52 |
| B | Freja | -0.15% | +0.28% ±2.8 | Popular (+1.4%) | Neutral | - | 52 |
| B | Wuyang | -0.20% | -0.22% ±2.2 | Standard (-0.2%) | Neutral | - | 52 |
| B | Genji | -0.22% | -0.59% ±1.8 | Popular (+1.6%) | Neutral | - | 52 |
| B | Vendetta | -0.28% | -0.43% ±3.5 | Standard (-0.2%) | Neutral | Better in GM+ | 46 |
| B | Widowmaker | -0.31% | -0.16% ±2.7 | Popular (+2.6%) | Neutral | - | 52 |
| B | Roadhog *(provisional)* | -0.40% | -0.33% ±12.3 | Popular (+1.4%) | Neutral | Better in Masters | 8 |
| B | Juno | -0.41% | +0.39% ±2.4 | Standard (-0.7%) | Neutral | Better in GM+ | 50 |
| B | Emre | -0.44% | -0.64% ±1.7 | Popular (+2.1%) | Neutral | - | 52 |
| B | Jetpack Cat | -0.44% | -0.58% ±3.6 | Standard (-1.0%) | Neutral | - | 52 |
| B | Anran | -0.51% | -1.03% ±4.0 | Standard (-0.4%) | Neutral | - | 49 |
| B | Mei | -0.62% | -2.02% ±3.1 | Standard (+0.1%) | Neutral | Better in Masters | 52 |
| B | Zarya | -0.98% | -1.05% ±4.1 | Niche (-1.2%) | Neutral | Better in Masters | 52 |
| B | Pharah | -1.00% | -1.01% ±3.0 | Niche (-1.4%) | Neutral | Better in Masters | 50 |
| B | Soldier: 76 | -1.04% | -1.38% ±2.0 | Niche (-1.4%) | Neutral | - | 52 |
| B | Echo | -1.11% | -1.81% ±3.9 | Standard (-0.2%) | Neutral | Better in Masters | 52 |
| B | Sigma | -1.13% | -1.07% ±2.0 | Popular (+2.7%) | Neutral | - | 52 |
| B | D.Mon | -1.16% | -2.75% ±4.3 | Niche (-2.0%) | Neutral | - | 16 |
| B | Zenyatta | -1.19% | -1.90% ±2.3 | Standard (+0.5%) | Neutral | - | 51 |
| C | Reaper | -1.53% | -3.71% ±3.5 | Niche (-1.2%) | Deterrent | Better in Masters | 52 |
| C | Orisa | -1.60% | -2.95% ±3.1 | Niche (-1.8%) | Deterrent | - | 51 |
| C | Junker Queen | -1.62% | -1.86% ±4.3 | Standard (-0.9%) | Deterrent | Better in Masters | 44 |
| C | Symmetra | -1.74% | -2.87% ±3.6 | Standard (-0.6%) | Deterrent | - | 50 |
| C | Ramattra | -1.81% | -2.61% ±3.6 | Niche (-1.4%) | Deterrent | - | 47 |
| C | Domina | -1.91% | -2.32% ±3.6 | Standard (-0.1%) | Deterrent | Better in Masters | 51 |
| C | Moira | -1.99% | -3.25% ±4.0 | Niche (-2.2%) | Deterrent | Better in Masters | 52 |
| C | Winston | -2.22% | -2.33% ±3.4 | Map Priority (+4.2%) | Trap Pick | Better in Masters | 52 |
| C | Kiriko | -2.51% | -3.31% ±1.7 | Niche (-5.7%) | Deterrent | Better in Masters | 52 |
| C | Mizuki | -2.52% | -3.30% ±2.1 | Niche (-1.9%) | Deterrent | Better in Masters | 52 |
| C | Bastion | -2.94% | -5.61% ±3.4 | Standard (+0.6%) | Unfavorable | Better in Masters | 52 |
| D | Reinhardt | -3.10% | -3.89% ±3.3 | Niche (-1.4%) | Deterrent | - | 50 |
| D | Lúcio | -4.80% | -5.30% ±3.4 | Niche (-4.1%) | Deterrent | - | 48 |

### Runasapi

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| S | Reinhardt | +3.58% | +3.92% ±1.7 | Standard (+0.4%) | Favorable | - | 51 |
| A | Soldier: 76 | +2.10% | +3.96% ±2.6 | Map Priority (+6.8%) | Meta | - | 52 |
| A | Kiriko | +1.97% | +3.12% ±2.1 | Map Priority (+7.8%) | Meta | Better in GM+ | 52 |
| A | Junker Queen | +1.80% | +2.06% ±1.9 | Standard (+1.0%) | Favorable | - | 50 |
| A | Mauga | +1.48% | +2.44% ±2.4 | Popular (+2.2%) | Favorable | - | 50 |
| A | Mizuki | +1.38% | +2.02% ±2.5 | Popular (+2.1%) | Favorable | Better in Masters | 52 |
| B | Lúcio | +0.99% | +1.13% ±1.7 | Map Priority (+3.7%) | Neutral | - | 51 |
| B | Wrecking Ball | +0.90% | +1.31% ±2.4 | Popular (+1.3%) | Neutral | Better in Masters | 51 |
| B | Domina | +0.89% | +1.84% ±3.4 | Standard (-0.5%) | Neutral | - | 49 |
| B | Anran | +0.86% | +1.31% ±1.8 | Standard (+0.3%) | Neutral | - | 49 |
| B | Torbjörn | +0.74% | +1.17% ±3.0 | Standard (-0.5%) | Neutral | Better in Masters | 49 |
| B | Vendetta | +0.74% | +1.78% ±3.0 | Standard (+0.7%) | Neutral | Better in GM+ | 48 |
| B | Doctrine *(provisional)* | +0.64% | +1.04% ±3.1 | Standard (+0.6%) | Neutral | - | 8 |
| B | Mei | +0.61% | +2.32% ±2.7 | Niche (-1.2%) | Neutral | Better in GM+ | 50 |
| B | Bastion | +0.55% | +0.82% ±2.6 | Standard (-0.9%) | Neutral | - | 48 |
| B | D.Mon | +0.55% | +1.42% ±2.9 | Popular (+1.8%) | Neutral | Better in Masters | 16 |
| B | Wuyang | +0.44% | +1.27% ±2.7 | Popular (+1.9%) | Neutral | Better in GM+ | 52 |
| B | Tracer | +0.29% | +0.51% ±1.6 | Map Priority (+7.5%) | Neutral | - | 52 |
| B | Zarya | +0.29% | +0.45% ±1.6 | Standard (+0.1%) | Neutral | - | 50 |
| B | Sierra | +0.22% | +1.17% ±2.8 | Standard (-0.2%) | Neutral | Better in GM+ | 33 |
| B | Jetpack Cat | +0.15% | +0.37% ±3.4 | Standard (+0.5%) | Neutral | Better in Masters | 52 |
| B | Lifeweaver | +0.13% | +2.69% ±2.6 | Standard (-0.9%) | Neutral | - | 50 |
| B | Juno | +0.09% | +1.82% ±1.8 | Popular (+2.8%) | Neutral | - | 51 |
| B | Venture | +0.04% | +1.76% ±3.5 | Standard (-0.0%) | Neutral | Better in GM+ | 51 |
| B | Cassidy | -0.03% | +0.39% ±3.0 | Map Priority (+3.4%) | Neutral | - | 52 |
| B | Genji | -0.05% | +0.74% ±1.6 | Niche (-1.6%) | Neutral | - | 51 |
| B | Illari | -0.11% | +0.21% ±2.7 | Niche (-1.5%) | Neutral | Better in Masters | 51 |
| B | Emre | -0.24% | +0.15% ±2.3 | Standard (+0.6%) | Neutral | - | 52 |
| B | D.Va | -0.28% | +0.30% ±3.0 | Standard (+0.1%) | Neutral | Better in GM+ | 52 |
| B | Sojourn | -0.28% | -0.26% ±1.0 | Popular (+3.0%) | Neutral | - | 52 |
| B | Winston | -0.31% | -0.12% ±2.3 | Niche (-1.6%) | Neutral | - | 52 |
| B | Brigitte | -0.34% | -0.20% ±2.9 | Standard (+1.0%) | Neutral | Better in Masters | 52 |
| B | Reaper | -0.42% | -0.47% ±3.0 | Standard (-0.7%) | Neutral | Better in Masters | 51 |
| B | Roadhog *(provisional)* | -0.52% | -0.78% ±6.5 | Standard (-0.1%) | Neutral | - | 8 |
| B | Orisa | -0.53% | -0.81% ±2.6 | Standard (+0.3%) | Neutral | Better in GM+ | 51 |
| B | Doomfist | -0.55% | -0.95% ±2.4 | Standard (+0.2%) | Neutral | - | 51 |
| B | Symmetra | -0.58% | -0.63% ±3.0 | Standard (-0.8%) | Neutral | - | 44 |
| B | Baptiste | -0.64% | -0.73% ±2.6 | Niche (-2.3%) | Neutral | - | 50 |
| B | Hazard | -0.64% | -0.66% ±2.2 | Standard (+0.7%) | Neutral | - | 50 |
| B | Shion | -0.75% | -1.01% ±1.3 | Map Priority (+7.5%) | Neutral | - | 28 |
| B | Ashe | -0.76% | -0.74% ±2.8 | Niche (-5.2%) | Neutral | - | 51 |
| B | Junkrat | -0.77% | -0.99% ±2.4 | Niche (-1.1%) | Neutral | - | 47 |
| B | Mercy | -0.94% | -2.08% ±2.7 | Niche (-1.5%) | Neutral | - | 49 |
| B | Zenyatta | -0.97% | -1.72% ±2.9 | Niche (-3.6%) | Neutral | - | 52 |
| C | Moira | -1.24% | -1.41% ±3.0 | Standard (+0.8%) | Unfavorable | Better in GM+ | 51 |
| C | Sombra *(provisional)* | -1.32% | -1.91% ±4.7 | Map Priority (+4.6%) | Unfavorable | - | 8 |
| C | Pharah | -1.33% | -1.43% ±2.5 | Niche (-1.5%) | Unfavorable | - | 48 |
| C | Echo | -1.60% | -2.34% ±2.8 | Niche (-2.5%) | Deterrent | - | 51 |
| C | Hanzo | -1.74% | -3.27% ±3.2 | Niche (-3.5%) | Deterrent | Better in Masters | 50 |
| C | Ramattra | -1.90% | -2.53% ±3.0 | Standard (-0.3%) | Deterrent | - | 51 |
| C | Freja | -2.38% | -4.45% ±2.8 | Niche (-1.6%) | Deterrent | - | 50 |
| D | Ana | -3.79% | -4.60% ±2.3 | Niche (-9.8%) | Deterrent | - | 52 |
| D | Sigma | -4.13% | -4.46% ±2.4 | Niche (-3.4%) | Deterrent | - | 52 |
| D | Widowmaker | -16.67% | -17.19% ±3.1 | Niche (-4.2%) | Deterrent | - | 52 |

### Samoa

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| A | Symmetra | +1.93% | +2.20% ±1.3 | Standard (+0.9%) | Favorable | Better in GM+ | 51 |
| A | Torbjörn | +1.77% | +2.31% ±2.3 | Standard (-0.1%) | Specialist | - | 52 |
| A | Mizuki | +1.55% | +1.69% ±1.1 | Popular (+2.2%) | Meta | - | 52 |
| A | Cassidy | +1.51% | +1.74% ±0.9 | Map Priority (+7.1%) | Meta | - | 52 |
| A | Moira | +1.43% | +2.19% ±1.9 | Popular (+1.7%) | Favorable | - | 52 |
| B | Tracer | +1.12% | +1.25% ±0.8 | Map Priority (+6.2%) | Neutral | - | 52 |
| B | Anran | +1.05% | +2.23% ±2.6 | Standard (+0.7%) | Neutral | - | 51 |
| B | Wuyang | +0.97% | +1.41% ±1.4 | Popular (+1.3%) | Neutral | - | 52 |
| B | Junker Queen | +0.77% | +0.94% ±1.9 | Popular (+1.0%) | Neutral | Better in Masters | 51 |
| B | Zarya | +0.65% | +0.83% ±1.5 | Popular (+1.4%) | Neutral | - | 52 |
| B | Ramattra | +0.60% | +1.05% ±2.2 | Standard (+0.3%) | Neutral | Better in GM+ | 50 |
| B | Kiriko | +0.51% | +0.57% ±0.9 | Map Priority (+4.0%) | Neutral | - | 52 |
| B | Hazard | +0.49% | +0.79% ±2.3 | Standard (+0.4%) | Neutral | Better in Masters | 52 |
| B | Mauga | +0.49% | +0.96% ±2.3 | Popular (+1.3%) | Neutral | Better in GM+ | 50 |
| B | Shion | +0.49% | +0.80% ±1.1 | Map Priority (+5.2%) | Neutral | - | 28 |
| B | Bastion | +0.47% | +0.57% ±1.7 | Standard (-0.5%) | Neutral | - | 50 |
| B | Reinhardt | +0.39% | +0.45% ±1.4 | Standard (+0.7%) | Neutral | - | 52 |
| B | Sojourn | +0.39% | +0.68% ±1.6 | Popular (+1.5%) | Neutral | - | 52 |
| B | Doomfist | +0.32% | +0.52% ±1.1 | Standard (+0.6%) | Neutral | - | 52 |
| B | Orisa | +0.29% | +0.43% ±1.9 | Popular (+1.1%) | Neutral | - | 52 |
| B | Sierra | +0.22% | -0.60% ±1.8 | Standard (-0.5%) | Neutral | - | 32 |
| B | Emre | +0.21% | +0.80% ±1.2 | Niche (-1.1%) | Neutral | - | 52 |
| B | Baptiste | +0.15% | +1.03% ±2.4 | Niche (-1.1%) | Neutral | - | 51 |
| B | Lifeweaver | +0.13% | +2.17% ±1.7 | Standard (-0.9%) | Neutral | - | 51 |
| B | Lúcio | +0.13% | +0.25% ±1.9 | Popular (+2.5%) | Neutral | - | 52 |
| B | Illari | +0.08% | +0.38% ±1.3 | Niche (-2.0%) | Neutral | - | 52 |
| B | Domina | +0.07% | +0.51% ±3.0 | Standard (-0.3%) | Neutral | - | 51 |
| B | Venture | +0.04% | -0.23% ±2.5 | Standard (+0.2%) | Neutral | Better in Masters | 51 |
| B | Roadhog *(provisional)* | -0.16% | +0.42% ±6.2 | Standard (+0.1%) | Neutral | - | 8 |
| B | Hanzo | -0.19% | -0.10% ±1.7 | Niche (-2.5%) | Neutral | - | 51 |
| B | Brigitte | -0.30% | -0.24% ±1.7 | Popular (+1.1%) | Neutral | - | 52 |
| B | Genji | -0.30% | -2.11% ±2.3 | Niche (-1.6%) | Neutral | - | 52 |
| B | Mei | -0.39% | -0.84% ±2.5 | Standard (-0.3%) | Neutral | - | 51 |
| B | Ashe | -0.41% | -0.21% ±1.2 | Niche (-4.2%) | Neutral | - | 52 |
| B | Zenyatta | -0.46% | -0.46% ±1.3 | Niche (-2.0%) | Neutral | - | 52 |
| B | D.Mon | -0.61% | -0.79% ±2.6 | Popular (+2.0%) | Neutral | - | 16 |
| B | Mercy | -0.65% | -0.90% ±1.7 | Niche (-1.7%) | Neutral | - | 50 |
| B | Reaper | -0.69% | -0.98% ±2.5 | Popular (+1.9%) | Neutral | - | 52 |
| B | Vendetta | -0.69% | -1.23% ±2.9 | Standard (+0.1%) | Neutral | Better in Masters | 48 |
| B | Juno | -0.75% | -1.50% ±2.6 | Standard (+0.5%) | Neutral | - | 52 |
| B | Freja | -1.05% | -1.49% ±2.5 | Niche (-1.6%) | Neutral | - | 52 |
| B | Soldier: 76 | -1.08% | -1.23% ±1.4 | Niche (-1.4%) | Neutral | - | 52 |
| C | Sigma | -1.28% | -1.26% ±1.5 | Niche (-3.0%) | Unfavorable | - | 52 |
| C | Echo | -1.33% | -1.58% ±1.9 | Niche (-2.2%) | Unfavorable | Better in GM+ | 52 |
| C | D.Va | -1.50% | -1.94% ±1.4 | Niche (-1.1%) | Deterrent | - | 52 |
| C | Wrecking Ball | -1.55% | -1.64% ±1.2 | Standard (+0.3%) | Unfavorable | - | 51 |
| C | Pharah | -1.66% | -1.82% ±2.3 | Standard (-0.7%) | Deterrent | - | 51 |
| C | Junkrat | -1.76% | -2.16% ±2.0 | Standard (-0.3%) | Deterrent | - | 51 |
| C | Jetpack Cat | -1.81% | -2.38% ±2.7 | Standard (-0.3%) | Deterrent | - | 52 |
| C | Ana | -2.00% | -2.07% ±1.0 | Niche (-5.7%) | Deterrent | - | 52 |
| C | Sombra *(provisional)* | -2.05% | -3.45% ±4.5 | Popular (+2.1%) | Trap Pick | Better in Masters | 8 |
| C | Doctrine *(provisional)* | -2.21% | -3.34% ±3.0 | Niche (-1.2%) | Deterrent | - | 8 |
| C | Winston | -2.90% | -2.96% ±1.6 | Niche (-3.8%) | Deterrent | - | 52 |
| D | Widowmaker | -6.71% | -6.74% ±1.9 | Niche (-5.0%) | Deterrent | - | 44 |

### Shambali Monastery

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| S | Reinhardt | +3.89% | +5.15% ±3.2 | Popular (+2.0%) | Meta | Better in GM+ | 51 |
| A | Mizuki | +2.45% | +3.25% ±2.1 | Niche (-1.1%) | Specialist | - | 51 |
| A | Ramattra | +2.31% | +3.72% ±2.6 | Map Priority (+3.1%) | Meta | - | 51 |
| A | Sigma | +1.71% | +2.22% ±2.5 | Map Priority (+6.6%) | Meta | - | 52 |
| A | Doctrine *(provisional)* | +1.55% | +3.04% ±3.9 | Map Priority (+3.1%) | Meta | - | 8 |
| A | Bastion | +1.48% | +2.11% ±2.4 | Popular (+1.3%) | Favorable | Better in Masters | 50 |
| A | Junkrat | +1.36% | +1.80% ±2.3 | Popular (+1.6%) | Favorable | - | 49 |
| A | Wuyang | +1.33% | +2.64% ±2.2 | Popular (+2.3%) | Favorable | Better in GM+ | 52 |
| B | Orisa | +1.07% | +1.50% ±2.0 | Popular (+1.4%) | Neutral | - | 52 |
| B | Pharah | +0.72% | +1.49% ±3.1 | Popular (+1.7%) | Neutral | Better in Masters | 52 |
| B | Jetpack Cat | +0.65% | +1.06% ±3.1 | Standard (-0.0%) | Neutral | Better in GM+ | 52 |
| B | Mei | +0.65% | +2.41% ±2.7 | Popular (+1.6%) | Neutral | - | 51 |
| B | Echo | +0.31% | +0.92% ±2.5 | Map Priority (+3.6%) | Neutral | Better in GM+ | 52 |
| B | Sierra | +0.22% | -0.75% ±2.0 | Standard (+0.3%) | Neutral | - | 36 |
| B | Hanzo | +0.21% | +0.42% ±1.7 | Popular (+1.6%) | Neutral | Better in Masters | 51 |
| B | Lifeweaver | +0.13% | -2.92% ±2.9 | Standard (+0.9%) | Neutral | Better in Masters | 50 |
| B | Baptiste | +0.12% | +1.32% ±2.8 | Popular (+2.2%) | Neutral | - | 52 |
| B | Reaper | +0.12% | +0.74% ±2.8 | Niche (-1.3%) | Neutral | Better in Masters | 51 |
| B | Vendetta | +0.09% | +0.60% ±3.8 | Standard (-0.0%) | Neutral | - | 42 |
| B | Sojourn | +0.05% | +0.51% ±2.6 | Standard (+0.6%) | Neutral | Better in GM+ | 52 |
| B | Venture | +0.04% | +2.01% ±3.1 | Standard (+0.5%) | Neutral | - | 48 |
| B | D.Va | -0.02% | +1.09% ±3.0 | Niche (-2.1%) | Neutral | - | 51 |
| B | Freja | -0.07% | +0.78% ±3.5 | Standard (+0.8%) | Neutral | Better in GM+ | 51 |
| B | Illari | -0.08% | +0.47% ±2.9 | Popular (+2.7%) | Neutral | - | 52 |
| B | Anran | -0.11% | +0.12% ±3.3 | Standard (+0.1%) | Neutral | Better in GM+ | 49 |
| B | Genji | -0.15% | +0.15% ±2.5 | Standard (-0.8%) | Neutral | Better in Masters | 52 |
| B | Wrecking Ball | -0.21% | -0.07% ±3.6 | Niche (-1.6%) | Neutral | - | 51 |
| B | Shion | -0.23% | -0.15% ±2.6 | Niche (-2.7%) | Neutral | - | 28 |
| B | Emre | -0.26% | +0.08% ±2.4 | Popular (+2.4%) | Neutral | - | 52 |
| B | Kiriko | -0.42% | -0.62% ±2.4 | Niche (-5.9%) | Neutral | - | 52 |
| B | Brigitte | -0.50% | -0.47% ±3.6 | Niche (-2.4%) | Neutral | - | 51 |
| B | Juno | -0.57% | -0.38% ±3.1 | Standard (-0.1%) | Neutral | - | 52 |
| B | D.Mon | -0.66% | -1.03% ±3.5 | Popular (+1.6%) | Neutral | Better in Masters | 16 |
| B | Ashe | -0.70% | -0.55% ±2.5 | Popular (+1.7%) | Neutral | - | 52 |
| B | Doomfist | -0.70% | -2.10% ±3.6 | Niche (-1.3%) | Neutral | Better in Masters | 52 |
| B | Moira | -0.77% | -0.52% ±3.5 | Standard (-0.8%) | Neutral | Better in Masters | 50 |
| B | Mercy | -0.81% | -2.00% ±3.1 | Standard (+0.7%) | Neutral | - | 49 |
| B | Hazard | -0.82% | -1.00% ±3.4 | Niche (-2.7%) | Neutral | Better in GM+ | 51 |
| B | Zarya | -1.09% | -1.19% ±3.0 | Standard (+1.0%) | Neutral | - | 52 |
| B | Torbjörn | -1.13% | -1.73% ±3.1 | Standard (+0.2%) | Neutral | - | 50 |
| B | Zenyatta | -1.18% | -1.80% ±2.2 | Popular (+2.3%) | Neutral | - | 52 |
| C | Ana | -1.22% | -1.50% ±2.8 | Map Priority (+3.1%) | Unfavorable | - | 52 |
| C | Domina | -1.25% | -1.33% ±3.9 | Popular (+1.4%) | Unfavorable | Better in Masters | 52 |
| C | Roadhog *(provisional)* | -1.25% | -9.33% ±12.8 | Niche (-1.1%) | Unfavorable | - | 8 |
| C | Cassidy | -1.27% | -2.48% ±2.7 | Niche (-3.7%) | Unfavorable | - | 52 |
| C | Symmetra | -1.28% | -2.10% ±4.0 | Standard (-0.1%) | Unfavorable | - | 49 |
| C | Junker Queen | -1.45% | -1.60% ±4.2 | Standard (-0.4%) | Unfavorable | Better in Masters | 46 |
| C | Soldier: 76 | -1.50% | -2.26% ±2.4 | Niche (-2.0%) | Unfavorable | - | 52 |
| C | Tracer | -1.53% | -1.96% ±1.9 | Niche (-7.4%) | Deterrent | - | 52 |
| C | Sombra *(provisional)* | -1.59% | -3.88% ±7.3 | Niche (-3.5%) | Deterrent | Better in Masters | 8 |
| C | Widowmaker | -1.60% | -1.53% ±2.2 | Standard (+0.6%) | Unfavorable | - | 50 |
| C | Mauga | -1.70% | -2.42% ±2.9 | Standard (-0.7%) | Deterrent | Better in Masters | 49 |
| D | Lúcio | -3.98% | -4.37% ±3.6 | Niche (-3.4%) | Deterrent | Better in Masters | 49 |
| D | Winston | -5.17% | -5.41% ±1.8 | Niche (-5.8%) | Deterrent | - | 51 |

### Suravasa

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| S | Lúcio | +3.70% | +3.93% ±1.6 | Map Priority (+5.5%) | Meta | Better in Masters | 51 |
| A | Symmetra | +2.48% | +3.24% ±1.9 | Standard (-0.2%) | Specialist | - | 49 |
| A | Junker Queen | +2.33% | +2.93% ±2.6 | Popular (+1.6%) | Meta | - | 50 |
| A | Wrecking Ball | +2.19% | +2.94% ±2.3 | Popular (+1.4%) | Favorable | - | 52 |
| A | Jetpack Cat | +2.09% | +2.49% ±1.9 | Standard (+0.4%) | Favorable | Better in Masters | 51 |
| A | Domina | +1.97% | +2.63% ±2.3 | Standard (-0.5%) | Specialist | - | 51 |
| A | Pharah | +1.71% | +2.16% ±1.9 | Standard (-0.9%) | Specialist | - | 51 |
| A | Ramattra | +1.66% | +2.47% ±2.2 | Standard (-0.3%) | Specialist | - | 50 |
| A | Kiriko | +1.61% | +2.69% ±2.2 | Map Priority (+8.1%) | Meta | - | 52 |
| B | Brigitte | +1.17% | +1.94% ±2.3 | Popular (+1.4%) | Neutral | - | 52 |
| B | Anran | +0.88% | +2.01% ±2.8 | Standard (+0.7%) | Neutral | - | 52 |
| B | Mauga | +0.82% | +1.05% ±1.4 | Popular (+1.6%) | Neutral | - | 51 |
| B | Sojourn | +0.76% | +0.86% ±0.8 | Map Priority (+3.8%) | Neutral | - | 52 |
| B | Soldier: 76 | +0.67% | +0.82% ±1.1 | Popular (+2.0%) | Neutral | - | 51 |
| B | Reinhardt | +0.66% | +0.93% ±2.9 | Standard (+0.2%) | Neutral | Better in Masters | 52 |
| B | Shion | +0.58% | +0.80% ±0.9 | Map Priority (+6.9%) | Neutral | - | 28 |
| B | Winston | +0.55% | +0.80% ±2.2 | Niche (-2.0%) | Neutral | Better in Masters | 52 |
| B | Hazard | +0.35% | +0.51% ±1.8 | Popular (+1.1%) | Neutral | Better in GM+ | 51 |
| B | Reaper | +0.35% | +0.69% ±1.7 | Popular (+1.9%) | Neutral | - | 52 |
| B | Tracer | +0.27% | +0.37% ±1.0 | Map Priority (+7.3%) | Neutral | - | 52 |
| B | Sierra | +0.22% | +2.03% ±2.0 | Standard (-0.5%) | Neutral | Better in GM+ | 33 |
| B | Echo | +0.20% | +0.53% ±2.0 | Niche (-2.5%) | Neutral | - | 52 |
| B | Lifeweaver | +0.13% | -1.57% ±1.6 | Niche (-1.2%) | Neutral | Better in Masters | 51 |
| B | Vendetta | +0.05% | +0.25% ±2.5 | Standard (+0.4%) | Neutral | - | 48 |
| B | D.Mon | +0.04% | +0.32% ±2.4 | Standard (+1.0%) | Neutral | - | 16 |
| B | Venture | +0.04% | -1.12% ±2.7 | Standard (+0.2%) | Neutral | Better in Masters | 51 |
| B | Torbjörn | +0.03% | +0.06% ±2.5 | Standard (-0.1%) | Neutral | Better in Masters | 52 |
| B | Doomfist | -0.01% | +0.47% ±2.5 | Standard (+0.9%) | Neutral | - | 52 |
| B | Genji | -0.03% | +1.04% ±1.7 | Standard (-0.2%) | Neutral | - | 51 |
| B | Sombra *(provisional)* | -0.05% | +0.95% ±4.5 | Map Priority (+3.9%) | Neutral | - | 8 |
| B | Mei | -0.10% | -0.04% ±1.9 | Standard (-0.8%) | Neutral | Better in Masters | 52 |
| B | Illari | -0.15% | -0.09% ±2.0 | Niche (-2.8%) | Neutral | Better in GM+ | 52 |
| B | Bastion | -0.21% | -0.27% ±1.8 | Niche (-1.3%) | Neutral | - | 49 |
| B | Orisa | -0.32% | -0.57% ±3.4 | Standard (+0.5%) | Neutral | Better in GM+ | 52 |
| B | Wuyang | -0.33% | -0.45% ±2.1 | Standard (+0.8%) | Neutral | - | 52 |
| B | Doctrine *(provisional)* | -0.36% | -0.51% ±3.0 | Niche (-1.7%) | Neutral | - | 8 |
| B | Emre | -0.42% | -0.61% ±1.8 | Niche (-2.2%) | Neutral | - | 52 |
| B | Roadhog *(provisional)* | -0.43% | -0.48% ±6.1 | Standard (+0.4%) | Neutral | Better in GM+ | 8 |
| B | Zenyatta | -0.47% | -0.49% ±2.6 | Niche (-3.4%) | Neutral | Better in GM+ | 52 |
| B | Moira | -0.55% | -0.44% ±1.6 | Map Priority (+3.2%) | Neutral | - | 51 |
| B | Juno | -0.60% | -0.58% ±3.1 | Standard (+0.6%) | Neutral | Better in Masters | 52 |
| B | Mercy | -0.63% | -1.14% ±2.4 | Niche (-2.1%) | Neutral | Better in Masters | 51 |
| B | Cassidy | -0.67% | -0.70% ±0.7 | Map Priority (+5.2%) | Neutral | - | 52 |
| B | Ashe | -0.81% | -0.87% ±1.9 | Niche (-6.0%) | Neutral | - | 51 |
| B | Zarya | -0.90% | -0.91% ±2.3 | Standard (+0.5%) | Neutral | Better in GM+ | 52 |
| B | Hanzo | -0.96% | -1.61% ±3.3 | Niche (-3.0%) | Neutral | Better in GM+ | 52 |
| B | Junkrat | -0.98% | -1.15% ±1.8 | Standard (-0.7%) | Neutral | - | 50 |
| B | Mizuki | -1.11% | -1.34% ±1.7 | Map Priority (+3.3%) | Neutral | - | 52 |
| B | Baptiste | -1.18% | -1.79% ±2.1 | Niche (-2.2%) | Neutral | - | 52 |
| C | Freja | -1.87% | -3.08% ±2.5 | Niche (-1.9%) | Deterrent | - | 52 |
| C | D.Va | -2.38% | -3.38% ±1.6 | Standard (-0.3%) | Deterrent | - | 52 |
| C | Ana | -2.91% | -3.18% ±1.5 | Niche (-11.3%) | Deterrent | - | 52 |
| D | Sigma | -4.30% | -4.56% ±2.1 | Niche (-5.2%) | Deterrent | - | 52 |
| D | Widowmaker | -11.90% | -12.04% ±2.1 | Niche (-5.5%) | Deterrent | - | 44 |

### Watchpoint Gibraltar

| Tier | Hero | Delta WR | Raw (95% range) | Presence | Archetype | Rank | n |
|---|---|---|---|---|---|---|---|
| A | Winston | +2.74% | +3.11% ±1.9 | Map Priority (+16.5%) | Meta | - | 52 |
| A | Wrecking Ball | +2.38% | +3.74% ±3.0 | Standard (+0.6%) | Favorable | - | 51 |
| A | Ana | +2.11% | +2.38% ±1.5 | Map Priority (+9.7%) | Meta | - | 52 |
| A | Junkrat | +1.74% | +2.61% ±2.9 | Standard (+0.4%) | Favorable | Better in GM+ | 50 |
| A | Hazard | +1.50% | +1.97% ±2.0 | Map Priority (+3.9%) | Favorable | - | 52 |
| A | Mercy | +1.39% | +3.22% ±2.3 | Popular (+1.6%) | Favorable | Better in Masters | 51 |
| A | D.Va | +1.32% | +3.08% ±2.0 | Popular (+2.9%) | Favorable | - | 51 |
| B | Brigitte | +1.13% | +1.79% ±2.1 | Map Priority (+5.0%) | Neutral | Better in Masters | 52 |
| B | Baptiste | +0.90% | +2.10% ±1.9 | Standard (-0.2%) | Neutral | - | 52 |
| B | Freja | +0.80% | +2.33% ±2.8 | Popular (+1.5%) | Neutral | - | 52 |
| B | Roadhog *(provisional)* | +0.71% | +5.12% ±8.2 | Standard (+0.5%) | Neutral | Better in Masters | 7 |
| B | Bastion | +0.46% | +0.61% ±2.1 | Standard (-0.0%) | Neutral | - | 50 |
| B | Tracer | +0.44% | +0.68% ±1.5 | Popular (+2.5%) | Neutral | - | 52 |
| B | Ashe | +0.34% | +1.39% ±1.6 | Map Priority (+7.6%) | Neutral | - | 52 |
| B | Sierra | +0.22% | -0.26% ±2.3 | Standard (+0.1%) | Neutral | - | 36 |
| B | Anran | +0.15% | +1.05% ±4.1 | Standard (-0.7%) | Neutral | Better in Masters | 49 |
| B | Lifeweaver | +0.13% | -0.60% ±3.6 | Popular (+1.6%) | Neutral | - | 52 |
| B | Echo | +0.11% | +0.45% ±2.1 | Popular (+1.3%) | Neutral | Better in Masters | 52 |
| B | Doctrine *(provisional)* | +0.10% | +0.39% ±5.3 | Niche (-2.0%) | Neutral | Better in Masters | 8 |
| B | Venture | +0.04% | -2.05% ±3.5 | Standard (-0.1%) | Neutral | - | 50 |
| B | Illari | +0.03% | +0.42% ±1.7 | Popular (+1.1%) | Neutral | Better in Masters | 52 |
| B | Cassidy | +0.02% | +0.15% ±1.5 | Niche (-3.6%) | Neutral | - | 52 |
| B | Shion | -0.02% | +0.96% ±3.5 | Niche (-7.4%) | Neutral | - | 28 |
| B | Genji | -0.07% | +0.38% ±1.3 | Popular (+2.9%) | Neutral | - | 52 |
| B | Emre | -0.09% | +0.54% ±1.9 | Standard (+0.6%) | Neutral | - | 52 |
| B | Jetpack Cat | -0.13% | -0.08% ±3.0 | Popular (+1.3%) | Neutral | - | 52 |
| B | Mei | -0.23% | -0.41% ±2.9 | Niche (-1.5%) | Neutral | - | 47 |
| B | Soldier: 76 | -0.32% | -0.26% ±3.8 | Standard (-0.4%) | Neutral | Better in GM+ | 52 |
| B | Doomfist | -0.53% | -1.03% ±2.8 | Standard (+0.0%) | Neutral | Better in Masters | 52 |
| B | Juno | -0.60% | -0.55% ±3.6 | Niche (-1.4%) | Neutral | - | 49 |
| B | Widowmaker | -0.62% | -0.58% ±1.4 | Map Priority (+3.5%) | Neutral | - | 51 |
| B | Wuyang | -0.64% | -0.86% ±1.6 | Niche (-4.8%) | Neutral | - | 52 |
| B | Kiriko | -0.65% | -0.83% ±1.7 | Niche (-2.1%) | Neutral | - | 52 |
| B | Hanzo | -0.66% | -0.86% ±2.8 | Standard (+0.9%) | Neutral | - | 52 |
| B | Pharah | -0.75% | -0.62% ±3.4 | Niche (-1.9%) | Neutral | Better in GM+ | 51 |
| B | Mizuki | -0.87% | -1.17% ±2.2 | Niche (-2.6%) | Neutral | Better in GM+ | 52 |
| B | D.Mon | -0.88% | -2.30% ±5.1 | Niche (-4.0%) | Neutral | - | 16 |
| B | Reaper | -1.05% | -1.70% ±2.5 | Popular (+1.4%) | Neutral | - | 52 |
| B | Moira | -1.13% | -1.27% ±4.1 | Niche (-3.0%) | Neutral | Better in Masters | 52 |
| C | Ramattra | -1.33% | -1.70% ±3.4 | Niche (-3.0%) | Unfavorable | Better in GM+ | 18 |
| C | Sojourn | -1.33% | -2.00% ±2.2 | Niche (-9.8%) | Unfavorable | - | 52 |
| C | Zenyatta | -1.45% | -2.97% ±2.9 | Niche (-2.3%) | Unfavorable | - | 52 |
| C | Sombra *(provisional)* | -1.50% | -3.33% ±7.0 | Standard (+0.0%) | Unfavorable | Better in Masters | 8 |
| C | Torbjörn | -1.59% | -2.47% ±3.2 | Standard (+0.1%) | Unfavorable | Better in GM+ | 52 |
| C | Vendetta | -1.69% | -4.45% ±3.8 | Standard (-0.2%) | Deterrent | Better in Masters | 46 |
| C | Junker Queen | -1.73% | -2.10% ±4.9 | Niche (-1.9%) | Deterrent | - | 38 |
| C | Orisa | -2.10% | -4.26% ±3.4 | Niche (-3.5%) | Deterrent | Better in GM+ | 52 |
| C | Mauga | -2.11% | -3.49% ±3.4 | Niche (-1.4%) | Deterrent | Better in Masters | 49 |
| C | Symmetra | -2.32% | -3.86% ±3.5 | Standard (-0.9%) | Deterrent | Better in Masters | 47 |
| D | Domina | -3.36% | -4.66% ±3.8 | Niche (-2.0%) | Deterrent | Better in GM+ | 42 |
| D | Zarya | -3.91% | -5.36% ±3.0 | Niche (-4.0%) | Deterrent | Better in GM+ | 52 |
| D | Reinhardt | -5.22% | -6.58% ±3.2 | Niche (-3.1%) | Deterrent | Better in Masters | 48 |
| D | Lúcio | -6.19% | -6.78% ±3.0 | Niche (-4.5%) | Deterrent | - | 47 |
| D | Sigma | -6.74% | -7.53% ±2.6 | Niche (-5.6%) | Deterrent | Better in Masters | 52 |

