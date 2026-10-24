import json
from dataclasses import dataclass


@dataclass(frozen=True)
class Material:
    id: str
    name: str
    price_usd_per_t: float
    composition_pct: dict[str, float]


@dataclass(frozen=True)
class Scrap:
    id: str
    name: str
    price_usd_per_t: float
    metallic_yield_pct: float
    composition_pct: dict[str, float]


def load_default_materials(path: str) -> list[Material]:
    with open(path) as file:
        raw_data = json.load(file)

    return [
        Material(
            id=item["id"],
            name=item["name"],
            price_usd_per_t=item["price_usd_per_t"],
            composition_pct=item["composition_pct"],
        )
        for item in raw_data
    ]


def load_default_scraps(path: str) -> list[Scrap]:
    with open(path) as file:
        raw_data = json.load(file)

    return [
        Scrap(
            id=item["id"],
            name=item["name"],
            price_usd_per_t=item["price_usd_per_t"],
            metallic_yield_pct=item["metallic_yield_pct"],
            composition_pct=item["composition_pct"],
        )
        for item in raw_data
    ]
