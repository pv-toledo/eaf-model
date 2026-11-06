from dataclasses import dataclass

from eaf_model.domain.constants import _element_masses, _oxide_masses
from eaf_model.domain.eaf_charge import ChargedElements
from eaf_model.domain.process import ProcessParameters


@dataclass(frozen=True)
class IronMassBalance:
    feo_mass_kg: float
    oxygen_for_feo_formation_kg: float


def calculate_iron_mass_balance(
    slag_mass_kg: float, process_parameters: ProcessParameters, eaf_charge: ChargedElements
) -> IronMassBalance:
    fraction_of_feo_in_slag = process_parameters.slag_feo_pct / 100

    total_feo_mass_kg = slag_mass_kg * fraction_of_feo_in_slag

    formed_feo_mass_kg = total_feo_mass_kg - eaf_charge["oxides"]["feo"] * 1000

    oxygen_mass_for_feo_formation_kg = ((_element_masses["o"] / 1000) * formed_feo_mass_kg) / (
        _oxide_masses["feo"] / 1000
    )

    return IronMassBalance(
        feo_mass_kg=formed_feo_mass_kg, oxygen_for_feo_formation_kg=oxygen_mass_for_feo_formation_kg
    )
