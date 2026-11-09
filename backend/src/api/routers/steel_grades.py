from fastapi import APIRouter

from api.schemas.steel_grades import SteelGrade
from eaf_model.application.loaders import load_default_steel_grades

router = APIRouter(tags=["steel_grades"])


@router.get("/steel-grades", response_model=list[SteelGrade])
def list_steel_grades():
    return load_default_steel_grades("src/eaf_model/data/default_steel_grades.json")
