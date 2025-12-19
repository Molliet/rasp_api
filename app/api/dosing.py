
from fastapi import APIRouter
from app.models.controls import NutrientDosing
from app.services.dosing_service import dosing_service

router = APIRouter(prefix="/dosing", tags=["Nutrient Dosing"])

@router.post("/nutrients")
async def dose_nutrients(dosing: NutrientDosing):
    """Trigger nutrient dosing"""
    return dosing_service.dose_nutrients(dosing)

@router.get("/last")
async def get_last_dosing():
    """Get last dosing information"""
    return dosing_service.get_last_dosing()

