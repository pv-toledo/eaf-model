import json
from dataclasses import dataclass

elements_in_steel = ["fe", "c", "si", "mn", "p", "s"]
oxides_in_slag = ["cao", "sio2", "al2o3", "mgo", "feo"]


@dataclass(frozen=True)
class ChargedElements:
    elements: dict[str, float]
    oxides: dict[str, float]


def load_default_metallic_mix(
    charged_scraps_path: str, charged_constraints_path: str
) -> dict[str, float]:
    with (
        open(charged_scraps_path) as charged_scraps,
        open(charged_constraints_path) as charge_constraints,
    ):
        charged_scraps = json.load(charged_scraps)
        charge_constraints = json.load(charge_constraints)

        basket_capacity_t = charge_constraints["basket_capacity_t"]
        metallic_mix = {}

        for item in charged_scraps:
            metallic_mix[item["scrap_id"]] = item["amount_charged_t"] * basket_capacity_t / 100
        return metallic_mix


def calculate_charged_elements_and_oxides(
    scrap_catalog_path: str, metallic_mix: dict[str, float]
) -> ChargedElements:
    with open(scrap_catalog_path) as file:
        scrap_catalog = json.load(file)

        elements = dict.fromkeys(elements_in_steel, 0.0)
        oxides = dict.fromkeys(oxides_in_slag, 0.0)

        for item in scrap_catalog:
            scrap_id = item["id"]

            if scrap_id not in metallic_mix:
                continue

            charged_amount_t = metallic_mix[scrap_id]
            composition_pct = item["composition_pct"]

            for element in elements:
                elements[element] += charged_amount_t * composition_pct[element] / 100

            for oxide in oxides:
                oxides[oxide] += charged_amount_t * composition_pct[oxide] / 100

    return {
        "elements": {element: round(value, 2) for element, value in elements.items()},
        "oxides": {oxide: round(value, 2) for oxide, value in oxides.items()},
    }
