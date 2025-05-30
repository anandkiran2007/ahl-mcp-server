from fastapi import APIRouter
from app.services.context_resolver import build_context_bundle
from app.models.context_bundle import MCPBundle

router = APIRouter()

@router.get("/context/{patient_id}", response_model=MCPBundle)
def get_context(patient_id: str):
    return build_context_bundle(patient_id)
