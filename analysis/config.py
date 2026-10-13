SEASON_MAP = {
    1: 21,
    2: 22,
    3: 23,
    4: 24,
    5: 25,
}

# The season currently in progress. Until it has run long enough for its data
# to settle, its slices are left out of every hero-map pair that already has
# data from earlier seasons. Pairs that only exist in this season (new or
# reworked heroes, new maps) still use it, flagged as provisional.
CURRENT_SEASON = 5
CURRENT_SEASON_MATURE = False

MIN_PICK_RATE = 1.0

# A hero-map pair needs at least this many qualifying season/tier/region
# slices before we'll report a delta for it. Below this, a single fluky
# slice (e.g. a 0% win rate from a handful of real games) can swing the
# average by dozens of points and look like a real result when it isn't.
MIN_SAMPLE_SIZE = 3

# Earliest season we accept data from for a hero: their release, or their
# most recent rework. Keyed by canonical slug (see canonical_slug).
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


def season_usable(hero_slug, map_slug, season):
    """Whether data from this season counts for this hero-map pair."""
    earliest = valid_from(hero_slug, map_slug)
    if season < earliest:
        return False
    if season == CURRENT_SEASON and not CURRENT_SEASON_MATURE:
        return earliest >= CURRENT_SEASON
    return True


def is_provisional(hero_slug, map_slug):
    """True when a pair's only usable data is the still-immature current season."""
    return not CURRENT_SEASON_MATURE and valid_from(hero_slug, map_slug) >= CURRENT_SEASON
