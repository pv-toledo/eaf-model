from eaf_model.application.loaders import (
    load_default_metallic_mix,
    load_default_process_parameters,
    load_default_scrap_catalog,
)
from eaf_model.domain.eaf_charge import calculate_charged_elements_and_oxides


def test_metrics() -> None:
    metallic_mix = load_default_metallic_mix(
        "src/eaf_model/data/default_charged_scraps.json",
        "src/eaf_model/data/default_charge_constraints.json",
    )

    scrap_catalog = load_default_scrap_catalog("src/eaf_model/data/default_scrap_catalog.json")
    process_parameters = load_default_process_parameters(
        "src/eaf_model/data/default_process_parameters.json"
    )
    charged_elements_and_oxides = calculate_charged_elements_and_oxides(
        metallic_mix, scrap_catalog, process_parameters
    )

    assert len(charged_elements_and_oxides) == 3
