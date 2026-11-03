from dataclasses import asdict
from pathlib import Path

from eaf_model.application.loaders import (
    load_default_metallic_mix,
    load_default_process_parameters,
    load_default_scrap_catalog,
    load_default_steel_grades,
    load_selected_steel_grade,
)
from eaf_model.domain.eaf_charge import (
    calculate_charged_elements_and_oxides,
    calculate_refining_masses,
)
from eaf_model.domain.slag.slag_volume import calculate_slag_volume
from eaf_model.domain.steel_refining.manganese import calculate_manganese_mass_balance
from eaf_model.domain.steel_refining.phosphorus import calculate_phosphorus_mass_balance
from eaf_model.domain.steel_refining.silicon import calculate_silicon_mass_balance

BACKEND_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BACKEND_DIR / "src" / "eaf_model" / "data"


def main() -> None:

    metallic_mix = load_default_metallic_mix(
        str(DATA_DIR / "default_charged_scraps.json"),
        str(DATA_DIR / "default_charge_constraints.json"),
    )

    scrap_catalog = load_default_scrap_catalog(str(DATA_DIR / "default_scrap_catalog.json"))

    process_parameters = load_default_process_parameters(
        str(DATA_DIR / "default_process_parameters.json")
    )

    eaf_input = calculate_charged_elements_and_oxides(
        metallic_mix, scrap_catalog, process_parameters
    )

    steel_grades = load_default_steel_grades(str(DATA_DIR / "default_steel_grades.json"))

    low_carbon_steel = load_selected_steel_grade(steel_grades)

    refining_masses = calculate_refining_masses(eaf_input, low_carbon_steel)

    print(refining_masses)

    total = sum(eaf_input["elements"].values()) - sum(asdict(refining_masses).values())

    print(total)

    silicon_mass_balance = calculate_silicon_mass_balance(refining_masses)
    manganese_mass_balance = calculate_manganese_mass_balance(refining_masses)
    phosphorus_mass_balance = calculate_phosphorus_mass_balance(refining_masses)

    # materials = load_default_materials(str(DATA_DIR / "default_materials_and_fluxes.json"))

    # teste = calculate_lime_addition(process_parameters, eaf_input, silicon_mass_balance, materials)

    slag_volume = calculate_slag_volume(
        process_parameters,
        eaf_input,
        silicon_mass_balance,
        manganese_mass_balance,
        phosphorus_mass_balance,
    )

    print(slag_volume)


if __name__ == "__main__":
    main()
