from dataclasses import dataclass

from eaf_model.domain.constants import _element_masses, _oxide_masses
from eaf_model.domain.eaf_charge import RefiningMasses


@dataclass(frozen=True)
class SiliconMassBalance:
    sio2_mass_kg: float
    oxygen_for_sio2_formation_kg: float


def calculate_silicon_mass_balance(refining_masses: RefiningMasses) -> SiliconMassBalance:
    if refining_masses.si is None:
        raise ValueError("Invalid information about Si refining")

    sio2_mass_kg = ((_oxide_masses["sio2"] / 1000) * refining_masses.si * 1000) / (
        _element_masses["si"] / 1000
    )

    oxygen_mass_for_sio2_formation_kg = ((2 * _element_masses["o"] / 1000) * sio2_mass_kg) / (
        _oxide_masses["sio2"] / 1000
    )

    return SiliconMassBalance(
        sio2_mass_kg=sio2_mass_kg, oxygen_for_sio2_formation_kg=oxygen_mass_for_sio2_formation_kg
    )
