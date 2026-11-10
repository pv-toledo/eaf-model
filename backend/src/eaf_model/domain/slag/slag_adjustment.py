from dataclasses import dataclass

import numpy as np

from eaf_model.domain.eaf_charge import ChargedElements
from eaf_model.domain.materials import Material
from eaf_model.domain.process import ProcessParameters
from eaf_model.domain.steel_refining.manganese import ManganeseMassBalance
from eaf_model.domain.steel_refining.phosphorus import PhosphorusMassBalance
from eaf_model.domain.steel_refining.silicon import SiliconMassBalance


@dataclass(frozen=True)
class SlagCalculation:
    calcitic_quicklime_kg: float
    dolomitic_quicklime_kg: float
    slag_mass_kg: float
    oxides_kg: dict[str, float]


def calculate_slag_and_quicklime_additions(
    process_parameters: ProcessParameters,
    eaf_charged_elements: ChargedElements,
    silicon_mass_balance: SiliconMassBalance,
    manganese_mass_balance: ManganeseMassBalance,
    phosphorus_mass_balance: PhosphorusMassBalance,
    materials: list[Material],
) -> SlagCalculation:

    materials_by_id = {material.id: material for material in materials}

    calcitic_quicklime = materials_by_id["calcitic_quicklime"]
    dolomitic_quicklime = materials_by_id["dolomitic_quicklime"]

    calcitic_composition = {
        oxide: content_pct / 100
        for oxide, content_pct in calcitic_quicklime.composition_pct.items()
    }

    dolomitic_composition = {
        oxide: content_pct / 100
        for oxide, content_pct in dolomitic_quicklime.composition_pct.items()
    }

    slag_oxides_kg = {
        oxide: mass_t * 1000 for oxide, mass_t in eaf_charged_elements["oxides"].items()
    }

    slag_oxides_kg["mno"] = manganese_mass_balance.mno_mass_kg

    slag_oxides_kg["p2o5"] = phosphorus_mass_balance.p2o5_mass_kg

    slag_oxides_kg["sio2"] += silicon_mass_balance.sio2_mass_kg

    target_basicity = process_parameters.slag_basicity

    target_feo_fraction = process_parameters.slag_feo_pct / 100

    target_mgo_fraction = process_parameters.slag_mgo_saturation_pct / 100

    base_non_feo_oxides_kg = sum(
        mass_kg for oxide, mass_kg in slag_oxides_kg.items() if oxide != "feo"
    )

    quicklime_oxides = (
        "cao",
        "sio2",
        "al2o3",
        "mgo",
    )

    calcitic_total_oxide_fraction = sum(calcitic_composition[oxide] for oxide in quicklime_oxides)

    dolomitic_total_oxide_fraction = sum(dolomitic_composition[oxide] for oxide in quicklime_oxides)

    coefficient_matrix = np.array(
        [
            [
                calcitic_composition["cao"] - (target_basicity * calcitic_composition["sio2"]),
                dolomitic_composition["cao"] - (target_basicity * dolomitic_composition["sio2"]),
            ],
            [
                (
                    (1 - target_feo_fraction) * calcitic_composition["mgo"]
                    - (target_mgo_fraction * calcitic_total_oxide_fraction)
                ),
                (
                    (1 - target_feo_fraction) * dolomitic_composition["mgo"]
                    - (target_mgo_fraction * dolomitic_total_oxide_fraction)
                ),
            ],
        ],
        dtype=float,
    )

    result_vector = np.array(
        [
            (target_basicity * slag_oxides_kg["sio2"] - slag_oxides_kg["cao"]),
            (
                target_mgo_fraction * base_non_feo_oxides_kg
                - ((1 - target_feo_fraction) * slag_oxides_kg["mgo"])
            ),
        ],
        dtype=float,
    )

    (
        calcitic_quicklime_kg,
        dolomitic_quicklime_kg,
    ) = np.linalg.solve(
        coefficient_matrix,
        result_vector,
    )

    for oxide in quicklime_oxides:
        slag_oxides_kg[oxide] += (
            calcitic_quicklime_kg * calcitic_composition[oxide]
            + dolomitic_quicklime_kg * dolomitic_composition[oxide]
        )

    non_feo_oxides_kg = sum(mass_kg for oxide, mass_kg in slag_oxides_kg.items() if oxide != "feo")

    slag_mass_kg = non_feo_oxides_kg / (1 - target_feo_fraction)

    slag_oxides_kg["feo"] = slag_mass_kg * target_feo_fraction

    return SlagCalculation(
        calcitic_quicklime_kg=float(calcitic_quicklime_kg),
        dolomitic_quicklime_kg=float(dolomitic_quicklime_kg),
        slag_mass_kg=float(slag_mass_kg),
        oxides_kg={oxide: float(mass_kg) for oxide, mass_kg in slag_oxides_kg.items()},
    )
