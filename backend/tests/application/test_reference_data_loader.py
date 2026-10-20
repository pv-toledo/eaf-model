from eaf_model.application.reference_data_loader import load_default_materials, load_default_scraps


def test_load_default_materials() -> None:
    materials = load_default_materials("src/eaf_model/data/default_materials_and_fluxes.json")
    assert len(materials) == 5


def test_load_default_scraps() -> None:
    scraps = load_default_scraps("src/eaf_model/data/default_scrap_catalog.json")
    assert len(scraps) == 13
