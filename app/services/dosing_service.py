
from app.models.controls import NutrientDosing
from app.core.dependencies import get_system_state
from datetime import datetime

class DosingService:
    def __init__(self):
        self.system_state = get_system_state()
    
    def dose_nutrients(self, dosing: NutrientDosing):
        """Trigger nutrient dosing"""
        self.system_state["last_dosing"] = datetime.now()
        # TODO: Add actual dosing pump control when on Raspberry Pi
        return {
            "message": f"Dosed {dosing.ml_amount}ml of {dosing.nutrient_type}",
            "nutrient_type": dosing.nutrient_type,
            "amount_ml": dosing.ml_amount,
            "target_ec": dosing.target_ec,
            "timestamp": datetime.now()
        }
    
    def get_last_dosing(self):
        """Get last dosing timestamp"""
        return {
            "last_dosing": self.system_state["last_dosing"]
        }

dosing_service = DosingService()

