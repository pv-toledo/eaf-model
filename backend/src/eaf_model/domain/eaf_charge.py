from dataclasses import dataclass
from typing import TypedDict

from eaf_model.domain.materials import Scrap
from eaf_model.domain.steel_grades import Steel

elements_in_steel = ["fe", "c", "si", "mn", "p", "s"]
oxides_in_slag = ["cao", "sio2", "al2o3", "mgo", "feo"]


class ChargedElements(TypedDict):
    elements: dict[str, float]
    oxides: dict[str, float]


@dataclass(frozen=True)
class RefiningMasses:
    c: float
    si: float
    mn: float
    p: float
    s: float


def calculate_charged_elements_and_oxides(
    metallic_mix: dict[str, float],
    scrap_catalog: list[Scrap],
) -> ChargedElements:
    elements = dict.fromkeys(elements_in_steel, 0.0)
    oxides = dict.fromkeys(oxides_in_slag, 0.0)

    for scrap in scrap_catalog:
        charged_amount_t = metallic_mix.get(scrap.id)

        if charged_amount_t is None:
            continue

        metallic_yield = scrap.metallic_yield_pct

        if metallic_yield is None:
            raise ValueError(f"Metallic yield not informed for scrap '{scrap.id}'.")

        composition_pct = scrap.composition_pct
        yield_fraction = metallic_yield / 100

        for element in elements:
            element_pct = composition_pct[element]

            if element_pct is None:
                raise ValueError(f"Element '{element}' not informed for scrap '{scrap.id}'.")

            elements[element] += charged_amount_t * element_pct * yield_fraction / 100

        for oxide in oxides:
            oxide_pct = composition_pct[oxide]

            if oxide_pct is None:
                raise ValueError(f"Oxide '{oxide}' not informed for scrap '{scrap.id}'.")

            oxides[oxide] += charged_amount_t * oxide_pct * yield_fraction / 100

    return {
        "elements": {element: round(value, 2) for element, value in elements.items()},
        "oxides": {oxide: round(value, 2) for oxide, value in oxides.items()},
    }


def calculate_refining_masses(
    eaf_input_masses: ChargedElements,
    steel_grade: Steel,
) -> RefiningMasses:
    input_element_masses = eaf_input_masses["elements"]
    total_input_mass = sum(input_element_masses.values())

    target_eaf_masses: dict[str, float] = {}

    for element_limit in steel_grade.element_limits:
        max_pct = element_limit.max_pct

        if max_pct is None:
            raise ValueError(
                f"Maximum percentage not informed for element '{element_limit.element}'."
            )

        target_eaf_masses[element_limit.element] = max_pct * total_input_mass / 100

    return RefiningMasses(
        **{
            key: input_element_masses[key] - target_mass
            for key, target_mass in target_eaf_masses.items()
        }
    )
