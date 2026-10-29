from dataclasses import dataclass

from eaf_model.domain.constants import _element_masses, _oxide_masses
from eaf_model.domain.eaf_charge import RefiningMasses


@dataclass(frozen=True)
class ManganeseMassBalance:
    mno_mass_kg: float
    oxygen_for_mno_formation_kg: float


def calculate_manganese_mass_balance(refining_masses: RefiningMasses) -> ManganeseMassBalance:
    if refining_masses.mn is None:
        raise ValueError("Invalid information about Mn refining")

    mno_mass_kg = ((_oxide_masses["mno"] / 1000) * refining_masses.mn * 1000) / (
        _element_masses["mn"] / 1000
    )

    oxygen_mass_for_mno_formation_kg = ((_element_masses["o"] / 1000) * mno_mass_kg) / (
        _oxide_masses["mno"] / 1000
    )

    return ManganeseMassBalance(
        mno_mass_kg=mno_mass_kg, oxygen_for_mno_formation_kg=oxygen_mass_for_mno_formation_kg
    )
