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
