from fastapi import APIRouter

from api.schemas.charged_scraps import ChargedScraps
from eaf_model.application.loaders import load_default_charged_scraps

router = APIRouter(tags=["charged_scraps"])


@router.get("/charged-scraps", response_model=list[ChargedScraps])
def list_charged_scraps():
    return load_default_charged_scraps("src/eaf_model/data/default_charged_scraps.json")
