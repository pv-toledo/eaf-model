from eaf_model.domain.eaf_charge import ChargedElements
from eaf_model.domain.process import ProcessParameters
from eaf_model.domain.steel_refining.manganese import ManganeseMassBalance
from eaf_model.domain.steel_refining.phosphorus import PhosphorusMassBalance
from eaf_model.domain.steel_refining.silicon import SiliconMassBalance


def calculate_slag_volume(
    process_parameters: ProcessParameters,
    eaf_charged_elements: ChargedElements,
    silicon_mass_balance: SiliconMassBalance,
    manganese_mass_balance: ManganeseMassBalance,
    phosphorus_mass_balance: PhosphorusMassBalance,
) -> float:

    charged_oxides_kg = sum(eaf_charged_elements["oxides"].values()) * 1000

    charged_feo_kg = eaf_charged_elements["oxides"]["feo"] * 1000
    charged_mgo_kg = eaf_charged_elements["oxides"]["mgo"] * 1000

    total_oxides_kg = (
        charged_oxides_kg
        + silicon_mass_balance.sio2_mass_kg
        + manganese_mass_balance.mno_mass_kg
        + phosphorus_mass_balance.p2o5_mass_kg
        - charged_feo_kg
        - charged_mgo_kg
    )

    slag_volume_kg = total_oxides_kg / (
        1 - ((process_parameters.slag_feo_pct + process_parameters.slag_mgo_saturation_pct) / 100)
    )

    return slag_volume_kg
