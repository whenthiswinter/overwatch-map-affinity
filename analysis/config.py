import datetime
import json
import os

SEASON_MAP = {
    1: 21,
    2: 22,
    3: 23,
    4: 24,
    5: 25,
}

# The patch in progress lives in data/snapshots/state.json, which
# detect_patch.py updates when Blizzard's numbers reset. Each patch has an id
# ("S5", "S5-mid", "S5-mid-2" for a later reset in the same half) plus the
# season / midseason label its slices are filed under.
PATCH_STATE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "snapshots", "state.json")


def load_patch_state():
    with open(PATCH_STATE_PATH, encoding="utf-8") as f:
        return json.load(f)


def current_patch(state=None):
    state = state or load_patch_state()
    return next(p for p in state["patches"] if p["id"] == state["current"])


# The patch currently in progress (a season or a midseason half). Until it has
# run long enough for its data to settle, its slices are left out of every
# hero-map pair that has data from earlier patches. Pairs whose only data is
# this patch (new or reworked heroes, new maps, in a season's first half) still
# use it, flagged as provisional.
#
# "Settled" = MATURITY_DAYS since the patch started, counted to the newest
# snapshot. At 13-15 days into S5, per-slice deltas still moved ~3 points
# between refreshes (vs ~5 between two whole patches), so 14 was too early.
# 21 is a conservative placeholder until a full half has been observed
# (PLAN.md phase 5).
MATURITY_DAYS = 21

SNAPSHOT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "snapshots")


def latest_snapshot_date():
    dates = [f[:10] for f in os.listdir(SNAPSHOT_DIR) if f.endswith(".json.gz")] if os.path.isdir(SNAPSHOT_DIR) else []
    return max(dates) if dates else None


_current = current_patch()
CURRENT_PATCH = _current
CURRENT_SEASON = _current["season"]
CURRENT_IS_MIDSEASON = _current["is_midseason"]
DATA_THROUGH = latest_snapshot_date()
DAYS_INTO_PATCH = (
    (datetime.date.fromisoformat(DATA_THROUGH) - datetime.date.fromisoformat(_current["started"])).days
    if DATA_THROUGH else 0
)
CURRENT_PATCH_MATURE = DAYS_INTO_PATCH >= MATURITY_DAYS

# Map slices with a pick rate below this (%) are dropped. Checked 2026-10-21:
# such slices scatter 3-5x more than normal ones and sit systematically lower
# (heroes get dropped where they're losing). Of the options tested, 1% gave the
# most reproducible pair averages (split-half r 0.547; no cut 0.543, 2% 0.459,
# 3% 0.379, pick-rate weighting 0.519), and its selection bias averages 0.08.
MIN_PICK_RATE = 1.0

# A hero-map pair needs at least this many qualifying season/tier/region
# slices before we'll report a delta for it (unless fewer are even possible,
# see build_dataset.max_possible_slices). Checked 2026-10-21: pairs it hides
# are thin because the hero is rarely played there, their slices are much
# noisier than the noise model assumes, and there's too little held-out data
# to validate the model on them. In the main view it hides nothing.
MIN_SAMPLE_SIZE = 3

# Earliest season we accept data from for a hero: their release, or their
# most recent rework. Keyed by canonical slug (see canonical_slug). Use x.5
# for a midseason release or rework (5.5 = from S5 midseason on).
HERO_VALID_FROM_SEASON = {
    "sierra": 2,
    "shion": 3,
    "dmon": 4,
    "doctrine": 5,
    "sombra": 5,   # reworked, Damage -> Support
    "roadhog": 5,  # reworked
}

MAP_VALID_FROM_SEASON = {
    "watchpoint-gibraltar": 1,
    "antarctic-peninsula": 2,
    "neon-junction": 3,
    "paraiso": 4,
    "eichenwalde": 4,
    "busan": 4,
    "grimsvotn": 5,
}

MAP_SLUGS = [
    "circuit-royal", "dorado", "grimsvotn", "havana", "junkertown", "rialto", "route-66", "shambali-monastery", "watchpoint-gibraltar",
    "blizzard-world", "eichenwalde", "hollywood", "kings-row", "midtown", "neon-junction", "numbani", "paraiso",
    "antarctic-peninsula", "busan", "ilios", "lijiang-tower", "nepal", "oasis", "samoa",
    "colosseo", "esperanca", "new-queen-street", "runasapi",
    "aatlis", "new-junk-city", "suravasa",
]

MAP_MODES = {
    "circuit-royal": "Escort", "dorado": "Escort", "grimsvotn": "Escort", "havana": "Escort", "junkertown": "Escort",
    "rialto": "Escort", "route-66": "Escort", "shambali-monastery": "Escort", "watchpoint-gibraltar": "Escort",
    "blizzard-world": "Hybrid", "eichenwalde": "Hybrid", "hollywood": "Hybrid", "kings-row": "Hybrid",
    "midtown": "Hybrid", "neon-junction": "Hybrid", "numbani": "Hybrid", "paraiso": "Hybrid",
    "antarctic-peninsula": "Control", "busan": "Control", "ilios": "Control", "lijiang-tower": "Control",
    "nepal": "Control", "oasis": "Control", "samoa": "Control",
    "colosseo": "Push", "esperanca": "Push", "new-queen-street": "Push", "runasapi": "Push",
    "aatlis": "Flashpoint", "new-junk-city": "Flashpoint", "suravasa": "Flashpoint",
}

# Canonical hero slugs follow Blizzard's rates page (overwatch.blizzard.com/rates),
# which is where live data comes from. Older OWTics caches use other spellings.
SLUG_ALIASES = {
    "jetpackcat": "jetpack-cat",
    "junkerqueen": "junker-queen",
    "soldier76": "soldier-76",
    "wreckingball": "wrecking-ball",
    "lúcio": "lucio",
    "torbjörn": "torbjorn",
}

HERO_NAMES = {
    "dmon": "D.Mon", "dva": "D.Va", "lucio": "Lúcio", "soldier-76": "Soldier: 76", "torbjorn": "Torbjörn",
}

HERO_ROLES = {
    "dmon": "Tank", "domina": "Tank", "doomfist": "Tank", "dva": "Tank", "hazard": "Tank",
    "junker-queen": "Tank", "mauga": "Tank", "orisa": "Tank", "ramattra": "Tank", "reinhardt": "Tank",
    "roadhog": "Tank", "sigma": "Tank", "winston": "Tank", "wrecking-ball": "Tank", "zarya": "Tank",

    "anran": "Damage", "ashe": "Damage", "bastion": "Damage", "cassidy": "Damage",
    "echo": "Damage", "emre": "Damage", "freja": "Damage", "genji": "Damage",
    "hanzo": "Damage", "junkrat": "Damage", "mei": "Damage", "pharah": "Damage",
    "reaper": "Damage", "shion": "Damage", "sierra": "Damage", "sojourn": "Damage",
    "soldier-76": "Damage", "symmetra": "Damage", "torbjorn": "Damage", "tracer": "Damage",
    "vendetta": "Damage", "venture": "Damage", "widowmaker": "Damage",

    "ana": "Support", "baptiste": "Support", "brigitte": "Support", "doctrine": "Support",
    "illari": "Support", "jetpack-cat": "Support", "juno": "Support", "kiriko": "Support",
    "lifeweaver": "Support", "lucio": "Support", "mercy": "Support", "mizuki": "Support",
    "moira": "Support", "sombra": "Support", "wuyang": "Support", "zenyatta": "Support",
}

TIERS = ["MASTER", "GRANDMASTER_AND_CHAMPION"]
REGIONS = ["AMER", "EU", "ASIA", "KOREA"]


def canonical_slug(slug):
    key = slug.strip().lower().replace(" ", "-").replace("_", "-").replace(":", "").replace(".", "")
    return SLUG_ALIASES.get(key, key)


def hero_role(slug):
    return HERO_ROLES.get(canonical_slug(slug), "Damage")


def hero_name(slug):
    slug = canonical_slug(slug)
    return HERO_NAMES.get(slug, slug.replace("-", " ").title())


def valid_from(hero_slug, map_slug):
    return max(HERO_VALID_FROM_SEASON.get(canonical_slug(hero_slug), 1), MAP_VALID_FROM_SEASON.get(map_slug, 1))


def period(season, is_midseason=False):
    """Seasons and their midseason halves on one scale: S5 = 5, S5 midseason = 5.5.
    Valid-from entries can use either, e.g. 5.5 for a midseason rework."""
    return season + (0.5 if is_midseason else 0)


CURRENT_PERIOD = period(CURRENT_SEASON, CURRENT_IS_MIDSEASON)


def is_provisional(hero_slug, map_slug):
    """True when a pair's only usable data is the still-immature current patch."""
    return not CURRENT_PATCH_MATURE and valid_from(hero_slug, map_slug) >= CURRENT_PERIOD


def in_current_patch(hero_slug, map_slug, season, is_midseason=False):
    """For the "this patch only" view: current-period slices the pair is valid for."""
    p = period(season, is_midseason)
    return p == CURRENT_PERIOD and p >= valid_from(hero_slug, map_slug)


def season_usable(hero_slug, map_slug, season, is_midseason=False):
    """Whether a slice from this season / half counts for this hero-map pair."""
    p = period(season, is_midseason)
    if p < valid_from(hero_slug, map_slug):
        return False
    if p == CURRENT_PERIOD and not CURRENT_PATCH_MATURE:
        return is_provisional(hero_slug, map_slug)
    return True
