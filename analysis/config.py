SEASON_MAP = {
    1: 21,
    2: 22,
    3: 23,
    4: 24,
}

MIN_PICK_RATE = 1.0

# A hero-map pair needs at least this many qualifying season/tier/region
# slices before we'll report a delta for it. Below this, a single fluky
# slice (e.g. a 0% win rate from a handful of real games) can swing the
# average by dozens of points and look like a real result when it isn't.
MIN_SAMPLE_SIZE = 3

HERO_RELEASE_SEASON = {
    "Sierra": 2,
    "Shion": 3,
    "D.Mon": 4,
}

MAP_VALID_FROM_SEASON = {
    "watchpoint-gibraltar": 1,
    "antarctic-peninsula": 2,
    "neon-junction": 3,
    "paraiso": 4,
    "eichenwalde": 4,
    "busan": 4,
}

MAP_SLUGS = [
    "circuit-royal", "dorado", "havana", "junkertown", "rialto", "route-66", "shambali-monastery", "watchpoint-gibraltar",
    "blizzard-world", "eichenwalde", "hollywood", "kings-row", "midtown", "neon-junction", "numbani", "paraiso",
    "antarctic-peninsula", "busan", "ilios", "lijiang-tower", "nepal", "oasis", "samoa",
    "colosseo", "esperanca", "new-queen-street", "runasapi",
    "aatlis", "new-junk-city", "suravasa",
]

MAP_MODES = {
    "circuit-royal": "Escort", "dorado": "Escort", "havana": "Escort", "junkertown": "Escort",
    "rialto": "Escort", "route-66": "Escort", "shambali-monastery": "Escort", "watchpoint-gibraltar": "Escort",
    "blizzard-world": "Hybrid", "eichenwalde": "Hybrid", "hollywood": "Hybrid", "kings-row": "Hybrid",
    "midtown": "Hybrid", "neon-junction": "Hybrid", "numbani": "Hybrid", "paraiso": "Hybrid",
    "antarctic-peninsula": "Control", "busan": "Control", "ilios": "Control", "lijiang-tower": "Control",
    "nepal": "Control", "oasis": "Control", "samoa": "Control",
    "colosseo": "Push", "esperanca": "Push", "new-queen-street": "Push", "runasapi": "Push",
    "aatlis": "Flashpoint", "new-junk-city": "Flashpoint", "suravasa": "Flashpoint",
}

HERO_ROLES = {
    "d.mon": "Tank", "dmon": "Tank", "d.va": "Tank", "dva": "Tank", "domina": "Tank",
    "doomfist": "Tank", "hazard": "Tank", "junker-queen": "Tank", "junkerqueen": "Tank",
    "mauga": "Tank", "orisa": "Tank", "ramattra": "Tank", "reinhardt": "Tank",
    "roadhog": "Tank", "sigma": "Tank", "winston": "Tank", "wrecking-ball": "Tank",
    "wreckingball": "Tank", "zarya": "Tank",

    "anran": "Damage", "ashe": "Damage", "bastion": "Damage", "cassidy": "Damage",
    "echo": "Damage", "emre": "Damage", "freja": "Damage", "genji": "Damage",
    "hanzo": "Damage", "junkrat": "Damage", "mei": "Damage", "pharah": "Damage",
    "reaper": "Damage", "shion": "Damage", "sierra": "Damage", "sojourn": "Damage",
    "soldier-76": "Damage", "soldier:_76": "Damage", "soldier76": "Damage",
    "sombra": "Damage", "symmetra": "Damage", "torbjorn": "Damage", "torbjörn": "Damage",
    "tracer": "Damage", "vendetta": "Damage", "vendetta[5]": "Damage", "venture": "Damage",
    "widowmaker": "Damage",

    "ana": "Support", "baptiste": "Support", "brigitte": "Support", "illari": "Support",
    "jetpack-cat": "Support", "jetpackcat": "Support", "juno": "Support", "kiriko": "Support",
    "lifeweaver": "Support", "lucio": "Support", "lúcio": "Support", "mercy": "Support",
    "mizuki": "Support", "moira": "Support", "wuyang": "Support", "zenyatta": "Support",
}

TIERS = ["MASTER", "GRANDMASTER_AND_CHAMPION"]
REGIONS = ["AMER", "EU", "ASIA", "KOREA"]


def hero_role(slug):
    key = slug.lower().replace(" ", "").replace("_", "-").replace(":", "")
    return HERO_ROLES.get(key, "Damage")
