import base64
import json
import os
import time

from curl_cffi import requests

from config import HERO_RELEASE_SEASON, REGIONS, SEASON_MAP, TIERS

API_URL = "https://api.owtics.gg/graphql"
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")

HEADERS = {
    "accept": "application/graphql-response+json,application/json;q=0.9",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "origin": "https://owtics.gg",
    "referer": "https://owtics.gg/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

# OWTics sits behind Cloudflare, so a browser-issued cf_clearance cookie is
# required. Grab one from your own session (devtools -> Application -> Cookies)
# and export it before running this script:
#   export OWTICS_CF_CLEARANCE="..."
COOKIES = {"cf_clearance": os.environ.get("OWTICS_CF_CLEARANCE", "")}

MIDSEASONS = [False, True]

QUERY_DISCOVER_HEROES = """
query GetRolesTopHeroes($input: RolesTopHeroesInput!) {
  rolesTopHeroes(input: $input) {
    ... on RolesTopHeroesAvailable {
      buckets { role entries { hero { id name slug role } } }
    }
  }
}
"""

QUERY_MAP_STATS = """
query GetHeroMapStats($heroId: ID!, $filter: HeroMapStatsFilterInput) {
  heroById(id: $heroId) {
    id
    mapStats(filter: $filter) {
      result {
        __typename
        ... on HeroMapStatsAvailable {
          measurements { map { name slug mode } region winRate pickRate }
        }
        ... on HeroMapStatsUnavailable { reason }
      }
    }
  }
}
"""

session = requests.Session()


def discover_heroes():
    fields = []
    for i in range(1, 65):
        b64_id = base64.b64encode(f"Hero:{i}".encode()).decode()
        fields.append(f'h{i}: heroById(id: "{b64_id}") {{ id name slug role }}')

    query = "query DiscoverAllHeroes {\n  " + "\n  ".join(fields) + "\n}"
    payload = [{"operationName": "DiscoverAllHeroes", "query": query}]

    res = session.post(API_URL, json=payload, headers=HEADERS, cookies=COOKIES, impersonate="chrome120")
    res.raise_for_status()

    heroes = {}
    for hero in res.json()[0]["data"].values():
        if hero and hero.get("name"):
            heroes[hero["name"]] = {"id": hero["id"], "slug": hero["slug"], "role": hero["role"]}
    return heroes


def harvest_hero(hero_name, hero_meta):
    earliest_season = HERO_RELEASE_SEASON.get(hero_name, 1)
    dataset = []

    for concept_season, owtics_season in SEASON_MAP.items():
        if concept_season < earliest_season:
            continue

        for is_mid in MIDSEASONS:
            if concept_season == max(SEASON_MAP) and is_mid:
                continue

            for tier in TIERS:
                for region in REGIONS:
                    payload = [{
                        "operationName": "GetHeroMapStats",
                        "variables": {
                            "heroId": hero_meta["id"],
                            "filter": {
                                "season": {"season": owtics_season, "isMidseason": is_mid},
                                "region": region,
                                "tier": tier,
                            },
                        },
                        "query": QUERY_MAP_STATS,
                    }]

                    try:
                        res = session.post(API_URL, json=payload, headers=HEADERS, cookies=COOKIES, impersonate="chrome120", timeout=10)
                        if res.status_code != 200:
                            continue
                        result = res.json()[0]["data"]["heroById"]["mapStats"]["result"]
                        measurements = result.get("measurements")
                        if measurements:
                            dataset.append({
                                "season": concept_season,
                                "isMidseason": is_mid,
                                "tier": tier,
                                "region": region,
                                "measurements": measurements,
                            })
                        time.sleep(0.1)
                    except Exception as exc:
                        print(f"  {hero_name} / S{concept_season} / {region}: {exc}")

    return dataset


def main():
    if not COOKIES["cf_clearance"]:
        raise SystemExit("Set OWTICS_CF_CLEARANCE before running the harvester.")

    os.makedirs(DATA_DIR, exist_ok=True)

    print("discovering heroes...")
    heroes = discover_heroes()
    print(f"found {len(heroes)} heroes")

    for i, (hero_name, meta) in enumerate(heroes.items(), start=1):
        cache_path = os.path.join(DATA_DIR, f"{meta['slug']}_cache.json")
        if os.path.exists(cache_path):
            print(f"[{i}/{len(heroes)}] {hero_name}: cached, skipping")
            continue

        print(f"[{i}/{len(heroes)}] {hero_name}: fetching...")
        dataset = harvest_hero(hero_name, meta)
        with open(cache_path, "w", encoding="utf-8") as f:
            json.dump(dataset, f)
        print(f"  -> {len(dataset)} slices saved")


if __name__ == "__main__":
    main()
