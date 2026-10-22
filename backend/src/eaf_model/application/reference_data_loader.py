import json

from eaf_model.domain.constraints import ChargeConstraint, ScrapLimit
from eaf_model.domain.materials import Material, Scrap
from eaf_model.domain.steel_grades import ElementLimit, Steel


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


def load_default_steel_grades(path: str) -> list[Steel]:
    with open(path) as file:
        raw_data = json.load(file)

        return [
            Steel(
                id=item["id"],
                name=item["name"],
                element_limits=[
                    ElementLimit(
                        element=limit["element"], max_pct=limit["max_pct"], min_pct=limit["min_pct"]
                    )
                    for limit in item["element_limits"]
                ],
            )
            for item in raw_data
        ]


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
