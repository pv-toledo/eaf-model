from eaf_model.domain.eaf_charge import ChargedElements
from eaf_model.domain.materials import Material
from eaf_model.domain.process import ProcessParameters
from eaf_model.domain.steel_refining.silicon import SiliconMassBalance


def calculate_lime_addition(
    process_parameters: ProcessParameters,
    eaf_charged_elements: ChargedElements,
    silicon_mass_balance: SiliconMassBalance,
    materials: list[Material],
):
    target_basicity = process_parameters.slag_bascity

    charged_cao_kg = eaf_charged_elements["oxides"]["cao"] * 1000
    charged_sio2_kg = eaf_charged_elements["oxides"]["sio2"] * 1000

    total_sio2_kg = charged_sio2_kg + silicon_mass_balance.sio2_mass_kg

    cao_for_addition_kg = total_sio2_kg * target_basicity - charged_cao_kg

    calcitic_quicklime: Material = next(
        material for material in materials if material.id == "calcitic_quicklime"
    )

    amount_of_calcitic_quicklime_added_kg = cao_for_addition_kg / (
        calcitic_quicklime.composition_pct["cao"] / 100
    )

    return amount_of_calcitic_quicklime_added_kg
