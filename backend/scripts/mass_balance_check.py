from pathlib import Path

from eaf_model.application.loaders import (
    load_default_metallic_mix,
    load_default_scrap_catalog,
    load_default_steel_grades,
    load_selected_steel_grade,
)
from eaf_model.domain.eaf_charge import (
    calculate_charged_elements_and_oxides,
    calculate_refining_masses,
)

BACKEND_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BACKEND_DIR / "src" / "eaf_model" / "data"


def main() -> None:

    metallic_mix = load_default_metallic_mix(
        str(DATA_DIR / "default_charged_scraps.json"),
        str(DATA_DIR / "default_charge_constraints.json"),
    )

    scrap_catalog = load_default_scrap_catalog(str(DATA_DIR / "default_scrap_catalog.json"))

    eaf_input = calculate_charged_elements_and_oxides(metallic_mix, scrap_catalog)

    steel_grades = load_default_steel_grades(str(DATA_DIR / "default_steel_grades.json"))

    low_carbon_steel = load_selected_steel_grade(steel_grades)

    refining_masses = calculate_refining_masses(eaf_input, low_carbon_steel)

    # process_parameters = load_default_process_parameters(
    #     str(DATA_DIR / "default_process_parameters.json")
    # )

    # teste = calculate_silicon_mass_balance(refining_masses)

    print(refining_masses)


if __name__ == "__main__":
    main()
