from eaf_model.application.reference_data_loader import (
    load_default_charge_constraints,
    load_default_materials,
    load_default_process_parameters,
    load_default_scenario,
    load_default_scraps,
    load_default_steel_grades,
)


def test_load_default_materials() -> None:
    materials = load_default_materials("src/eaf_model/data/default_materials_and_fluxes.json")
    assert len(materials) == 5


def test_load_default_scraps() -> None:
    scraps = load_default_scraps("src/eaf_model/data/default_scrap_catalog.json")
    assert len(scraps) == 13


def test_load_default_steel_grades() -> None:
    steel_grades = load_default_steel_grades("src/eaf_model/data/default_steel_grades.json")
    assert len(steel_grades) == 3


def test_load_default_charge_constraints() -> None:
    charge_constraints = load_default_charge_constraints(
        "src/eaf_model/data/default_charge_constraints.json"
    )
    assert len(charge_constraints) == 1


def test_load_default_process_parameters() -> None:
    process_parameters = load_default_process_parameters(
        "src/eaf_model/data/default_process_parameters.json"
    )
    assert len(process_parameters) == 1


def test_load_default_scenario() -> None:
    scenario = load_default_scenario("src/eaf_model/data/default_charged_scraps.json")
    assert len(scenario) == 7
