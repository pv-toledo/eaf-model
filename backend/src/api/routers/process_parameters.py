from fastapi import APIRouter

from api.schemas.process_parameters import ProcessParameters
from eaf_model.application.loaders import load_default_process_parameters

router = APIRouter(tags=["process_parameters"])


@router.get("/process-parameters", response_model=ProcessParameters)
def list_process_parameters():
    return load_default_process_parameters("src/eaf_model/data/default_process_parameters.json")
