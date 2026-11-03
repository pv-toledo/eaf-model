from dataclasses import dataclass
from typing import TypedDict

from eaf_model.domain.materials import Scrap
from eaf_model.domain.process import ProcessParameters
from eaf_model.domain.steel_grades import Steel

elements_in_steel = ["fe", "c", "si", "mn", "p", "s"]
oxides_in_slag = ["cao", "sio2", "al2o3", "mgo", "feo"]


class ChargedElements(TypedDict):
    elements: dict[str, float]
    oxides: dict[str, float]
    liquid_steel_t: float


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
    process_parameters: ProcessParameters,
) -> ChargedElements:
    elements = dict.fromkeys(elements_in_steel, 0.0)
    oxides = dict.fromkeys(oxides_in_slag, 0.0)

    liquid_steel_t = 0.0

    scrap_by_id = {scrap.id: scrap for scrap in scrap_catalog}

    for scrap_id, charged_amount_t in metallic_mix.items():
        scrap = scrap_by_id.get(scrap_id)

        if scrap is None:
            raise ValueError(f"Scrap '{scrap_id}' not found in scrap catalog.")

        metallic_yield_pct = scrap.metallic_yield_pct

        if metallic_yield_pct is None:
            raise ValueError(f"Metallic yield not informed for scrap '{scrap_id}'.")

        composition_pct = scrap.composition_pct

        scrap_liquid_steel_t = charged_amount_t * metallic_yield_pct / 100

        liquid_steel_t += scrap_liquid_steel_t

        for element in elements:
            element_pct = composition_pct[element]

            if element_pct is None:
                raise ValueError(f"Element '{element}' not informed for scrap '{scrap_id}'.")

            elements[element] += scrap_liquid_steel_t * element_pct / 100

        for oxide in oxides:
            oxide_pct = composition_pct[oxide]

            if oxide_pct is None:
                raise ValueError(f"Oxide '{oxide}' not informed for scrap '{scrap_id}'.")

            oxides[oxide] += charged_amount_t * oxide_pct / 100

    electrode_carbon_pick_up_t = (
        liquid_steel_t * process_parameters.electrode_kg_per_t_liquid / 1000
    )

    elements["c"] += electrode_carbon_pick_up_t
    liquid_steel_t += electrode_carbon_pick_up_t

    return {
        "elements": elements,
        "oxides": oxides,
        "liquid_steel_t": liquid_steel_t,
    }


def calculate_refining_masses(
    eaf_input_masses: ChargedElements, steel_grade: Steel
) -> RefiningMasses:
    input_element_masses = eaf_input_masses["elements"].copy()
    total_input_mass = eaf_input_masses["liquid_steel_t"]

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
            key: max(input_element_masses[key] - target_mass, 0.0)
            for key, target_mass in target_eaf_masses.items()
        }
    )
