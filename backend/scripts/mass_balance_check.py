from pathlib import Path

from eaf_model.application.loaders import (
    load_default_metallic_mix,
    load_default_scrap_catalog,
    load_default_steel_grades,
)
from eaf_model.domain.metrics import calculate_charged_elements_and_oxides

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

    low_carbon = next(s for s in steel_grades if s.id == "low_carbon")

    total = sum(eaf_input["elements"].values())

    print(total, low_carbon)


if __name__ == "__main__":
    main()
