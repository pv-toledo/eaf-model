from dataclasses import asdict, dataclass

from eaf_model.domain.constants import _element_masses, _oxide_masses
from eaf_model.domain.eaf_charge import ChargedElements, RefiningMasses
from eaf_model.domain.steel_refining.iron import IronMassBalance


@dataclass(frozen=True)
class SteelComposition:
    steel_mass_t: float
    elements_t: dict[str, float]


elements_in_steel = ("fe", "c", "si", "mn", "p", "s")


def calculate_steel_composition(
    eaf_charge: ChargedElements,
    refining_masses: RefiningMasses,
    iron_mass_balance: IronMassBalance,
):

    elements_t: dict[str, float] = dict.fromkeys(
        elements_in_steel,
        0.0,
    )

    for element in elements_in_steel:
        if element != "fe":
            elements_t[element] = eaf_charge["elements"][element] - asdict(refining_masses)[element]

    fe_removed_from_steel_t = (iron_mass_balance.feo_mass_kg / 1000) * (
        _element_masses["fe"] / _oxide_masses["feo"]
    )

    elements_t["fe"] = eaf_charge["elements"]["fe"] - fe_removed_from_steel_t

    steel_mass_t = sum(elements_t.values())

    return SteelComposition(steel_mass_t=steel_mass_t, elements_t=elements_t)
