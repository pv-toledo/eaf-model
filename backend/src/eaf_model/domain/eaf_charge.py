from dataclasses import dataclass
from typing import TypedDict

from eaf_model.domain.materials import Scrap
from eaf_model.domain.steel_grades import Steel

elements_in_steel = ["fe", "c", "si", "mn", "p", "s"]
oxides_in_slag = ["cao", "sio2", "al2o3", "mgo", "feo"]


@dataclass(frozen=True)
class ChargedElements(TypedDict):
    elements: dict[str, float]
    oxides: dict[str, float]


def calculate_charged_elements_and_oxides(
    metallic_mix: dict[str, float], scrap_catalog: list[Scrap]
) -> ChargedElements:

    elements = dict.fromkeys(elements_in_steel, 0.0)
    oxides = dict.fromkeys(oxides_in_slag, 0.0)

    for scrap in scrap_catalog:
        charged_amount_t = metallic_mix.get(scrap.id)

        if charged_amount_t is None:
            continue

        composition_pct = scrap.composition_pct
        metallic_yield = scrap.metallic_yield_pct

        for element in elements:
            elements[element] += (
                charged_amount_t * composition_pct[element] * (metallic_yield / 100) / 100
            )

        for oxide in oxides:
            oxides[oxide] += (
                charged_amount_t * composition_pct[oxide] * (metallic_yield / 100) / 100
            )

    return {
        "elements": {element: round(value, 2) for element, value in elements.items()},
        "oxides": {oxide: round(value, 2) for oxide, value in oxides.items()},
    }


def calculte_refining_masses(
    eaf_input_masses: ChargedElements, steel_grade: Steel
) -> dict[str, float]:

    total_input_mass = sum(eaf_input_masses["elements"].values())

    target_eaf_masses = {
        element_limit.element: element_limit.max_pct * total_input_mass / 100
        for element_limit in steel_grade.element_limits
    }

    return {
        key: eaf_input_masses["elements"][key] - target_eaf_masses.get(key)
        for key in target_eaf_masses
    }
