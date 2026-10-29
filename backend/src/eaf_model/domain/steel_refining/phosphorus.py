from dataclasses import dataclass

from eaf_model.domain.constants import _element_masses, _oxide_masses
from eaf_model.domain.eaf_charge import RefiningMasses


@dataclass(frozen=True)
class PhosphorusMassBalance:
    p2o5_mass_kg: float
    oxygen_for_p2o5_formation_kg: float


def calculate_phosphorus_mass_balance(refining_masses: RefiningMasses) -> PhosphorusMassBalance:
    if refining_masses.p is None:
        raise ValueError("Invalid information about P refining")

    p2o5_mass_kg = ((_oxide_masses["p2o5"] / 1000) * refining_masses.p * 1000) / (
        2 * _element_masses["p"] / 1000
    )

    oxygen_mass_for_p2o5_formation_kg = ((5 * _element_masses["o"] / 1000) * p2o5_mass_kg) / (
        _oxide_masses["p2o5"] / 1000
    )

    return PhosphorusMassBalance(
        p2o5_mass_kg=p2o5_mass_kg, oxygen_for_p2o5_formation_kg=oxygen_mass_for_p2o5_formation_kg
    )
