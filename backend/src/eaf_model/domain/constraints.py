from dataclasses import dataclass


@dataclass(frozen=True)
class ScrapLimit:
    material_id: str
    min_pct: float | None
    max_pct: float | None


@dataclass(frozen=True)
class ChargeConstraint:
    basket_capacity_t: float
    scrap_limits: list[ScrapLimit]
