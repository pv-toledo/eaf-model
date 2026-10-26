from eaf_model.domain.metrics import (
    calculate_charged_elements_and_oxides,
    load_default_metallic_mix,
)


def test_metrics() -> None:
    metallic_mix = load_default_metallic_mix(
        "src/eaf_model/data/default_charged_scraps.json",
        "src/eaf_model/data/default_charge_constraints.json",
    )
    charged_elements_and_oxides = calculate_charged_elements_and_oxides(
        "src/eaf_model/data/default_scrap_catalog.json", metallic_mix
    )

    assert len(charged_elements_and_oxides) == 2
