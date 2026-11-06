from dataclasses import dataclass

from eaf_model.domain.constants import _element_masses
from eaf_model.domain.steel_refining.carbon import CarbonMassBalance
from eaf_model.domain.steel_refining.iron import IronMassBalance
from eaf_model.domain.steel_refining.manganese import ManganeseMassBalance
from eaf_model.domain.steel_refining.phosphorus import PhosphorusMassBalance
from eaf_model.domain.steel_refining.silicon import SiliconMassBalance


@dataclass(frozen=True)
class OxygenMassBalance:
    oxygen_mass_for_refining_kg: float
    o2_volume_for_refining_nm3: float


def calculate_oxygen_mass_balance(
    carbon_mass_balance: CarbonMassBalance,
    manganese_mass_balance: ManganeseMassBalance,
    silicon_mass_balance: SiliconMassBalance,
    phosphorus_mass_balance: PhosphorusMassBalance,
    iron_mass_balance: IronMassBalance,
) -> OxygenMassBalance:
    oxygen_mass_for_refining_kg = (
        carbon_mass_balance.oxygen_for_co_formation_kg
        + carbon_mass_balance.oxygen_for_co2_formation_kg
        + manganese_mass_balance.oxygen_for_mno_formation_kg
        + silicon_mass_balance.oxygen_for_sio2_formation_kg
        + phosphorus_mass_balance.oxygen_for_p2o5_formation_kg
        + iron_mass_balance.oxygen_for_feo_formation_kg
    )

    mols_of_o2_for_refining = oxygen_mass_for_refining_kg / (2 * _element_masses["o"] / 1000)

    o2_volume_for_refining_nm3 = mols_of_o2_for_refining * 0.0224

    return OxygenMassBalance(
        oxygen_mass_for_refining_kg=oxygen_mass_for_refining_kg,
        o2_volume_for_refining_nm3=o2_volume_for_refining_nm3,
    )
