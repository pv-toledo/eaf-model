from dataclasses import dataclass

from eaf_model.domain.constants import _element_masses, _gas_masses
from eaf_model.domain.eaf_charge import RefiningMasses
from eaf_model.domain.process import ProcessParameters


@dataclass(frozen=True)
class CarbonMassBalance:
    co_mass_kg: float
    co2_mass_kg: float
    oxygen_for_co_generation_kg: float
    oxygen_for_co2_generation_kg: float
    total_oxygen_for_carbon_adjustment: float


def calculate_carbon_mass_balance(
    refining_masses: RefiningMasses,
    process_parameters: ProcessParameters,
) -> CarbonMassBalance:
    if refining_masses.c is None:
        raise ValueError("Invalid information about C refining")

    co_mass_kg = ((_gas_masses["co"] / 1000) * refining_masses.c * 1000) / (
        _element_masses["c"] / 1000
    )

    oxygen_mass_for_co_formation_kg = ((_element_masses["o"] / 1000) * co_mass_kg) / (
        _gas_masses["co"] / 1000
    )

    co2_mass_kg = (
        (_gas_masses["co2"] / 1000)
        * (co_mass_kg * process_parameters.post_combustion_pct / 100)
        / (_gas_masses["co"] / 1000)
    )

    oxygen_mass_for_co2_formation_kg = ((_element_masses["o"] / 1000) * co2_mass_kg) / (
        _gas_masses["co2"] / 1000
    )

    total_oxygen_for_carbon_adjustment = (
        oxygen_mass_for_co_formation_kg + oxygen_mass_for_co2_formation_kg
    )

    return CarbonMassBalance(
        co_mass_kg=co_mass_kg * (1 - process_parameters.post_combustion_pct / 100),
        co2_mass_kg=co2_mass_kg,
        oxygen_for_co_generation_kg=oxygen_mass_for_co_formation_kg,
        oxygen_for_co2_generation_kg=oxygen_mass_for_co2_formation_kg,
        total_oxygen_for_carbon_adjustment=total_oxygen_for_carbon_adjustment,
    )
