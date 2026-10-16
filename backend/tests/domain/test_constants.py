from eaf_model.domain.constants import ELEMENT_MASSES_G_PER_MOL

def test_fe_molar_mass() -> None:
    assert ELEMENT_MASSES_G_PER_MOL["fe"] == 55.845