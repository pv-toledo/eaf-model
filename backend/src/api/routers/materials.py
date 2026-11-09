from fastapi import APIRouter

from api.schemas.materials import AlloysAndFluxes, Scrap
from eaf_model.application.loaders import load_default_materials, load_default_scrap_catalog

router = APIRouter(tags=["materials"])


@router.get("/scraps", response_model=list[Scrap])
def list_scraps():
    return load_default_scrap_catalog("src/eaf_model/data/default_scrap_catalog.json")


@router.get("/materials", response_model=list[AlloysAndFluxes])
def list_materials():
    return load_default_materials("src/eaf_model/data/default_materials_and_fluxes.json")
