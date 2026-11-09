from fastapi import APIRouter

from api.schemas.materials import Scrap
from eaf_model.application.loaders import load_default_scrap_catalog

router = APIRouter(tags=["materials"])


@router.get("/scraps", response_model=list[Scrap])
def list_scraps():
    return load_default_scrap_catalog("src/eaf_model/data/default_scrap_catalog.json")
