import json
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


def load_default_charge_constraints(path: str) -> list[ChargeConstraint]:
    with open(path) as file:
        raw_data = json.load(file)

        return [
            ChargeConstraint(
                basket_capacity_t=raw_data["basket_capacity_t"],
                scrap_limits=[
                    ScrapLimit(
                        material_id=limit["material_id"],
                        min_pct=limit["min_pct"],
                        max_pct=limit["max_pct"],
                    )
                    for limit in raw_data["scrap_limits"]
                ],
            )
        ]
