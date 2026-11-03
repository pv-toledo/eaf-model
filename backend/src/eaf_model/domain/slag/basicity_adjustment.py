from eaf_model.domain.eaf_charge import ChargedElements
from eaf_model.domain.materials import Material
from eaf_model.domain.process import ProcessParameters
from eaf_model.domain.steel_refining.manganese import ManganeseMassBalance
from eaf_model.domain.steel_refining.phosphorus import PhosphorusMassBalance
from eaf_model.domain.steel_refining.silicon import SiliconMassBalance


def calculate_slag_additions(
    process_parameters: ProcessParameters,
    eaf_charged_elements: ChargedElements,
    silicon_mass_balance: SiliconMassBalance,
    manganese_mass_balance: ManganeseMassBalance,
    phosphorus_mass_balance: PhosphorusMassBalance,
    materials: list[Material],
):

    target_basicity = process_parameters.slag_bascity

    charged_oxides_kg = sum(eaf_charged_elements["oxides"].values()) * 1000

    charged_feo_kg = eaf_charged_elements["oxides"]["feo"] * 1000
    charged_mgo_kg = eaf_charged_elements["oxides"]["mgo"] * 1000
    charged_cao_kg = eaf_charged_elements["oxides"]["cao"] * 1000
    charged_sio2_kg = eaf_charged_elements["oxides"]["sio2"] * 1000

    cao_for_basicity_correction_kg = (
        (silicon_mass_balance.sio2_mass_kg + charged_sio2_kg) * target_basicity
    ) - charged_cao_kg

    total_oxides_kg = (
        charged_oxides_kg
        + silicon_mass_balance.sio2_mass_kg
        + manganese_mass_balance.mno_mass_kg
        + phosphorus_mass_balance.p2o5_mass_kg
        + cao_for_basicity_correction_kg
        - charged_feo_kg
        - charged_mgo_kg
    )

    preliminary_slag_volume_kg = total_oxides_kg / (
        1 - ((process_parameters.slag_feo_pct + process_parameters.slag_mgo_saturation_pct) / 100)
    )

    calcitic_quicklime: Material = next(
        material for material in materials if material.id == "calcitic_quicklime"
    )

    dolomitic_quicklime: Material = next(
        material for material in materials if material.id == "dolomitic_quicklime"
    )

    mgo_addition_for_slag_saturation_kg = (
        preliminary_slag_volume_kg * process_parameters.slag_mgo_saturation_pct / 100
    ) - charged_mgo_kg

    dolomitic_quicklime_addition_kg = mgo_addition_for_slag_saturation_kg / (
        dolomitic_quicklime.composition_pct["mgo"] / 100
    )

    cao_addition_for_basicity_adjustment_kg = cao_for_basicity_correction_kg - (
        dolomitic_quicklime_addition_kg * dolomitic_quicklime.composition_pct["cao"] / 100
    )

    calcitic_quicklime_addition_kg = cao_addition_for_basicity_adjustment_kg / (
        calcitic_quicklime.composition_pct["cao"] / 100
    )

    total_quicklime_addition_kg = calcitic_quicklime_addition_kg + dolomitic_quicklime_addition_kg

    return total_quicklime_addition_kg
