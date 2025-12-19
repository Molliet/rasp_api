
from app.models.controls import PumpControl
from app.core.dependencies import get_system_state
from datetime import datetime

class PumpService:
    def __init__(self):
        self.system_state = get_system_state()
    
    def control_water_pump(self, control: PumpControl):
        """Control water circulation pump"""
        self.system_state["water_pump"] = control.status
        # TODO: Add actual GPIO control when on Raspberry Pi
        return {
            "message": f"Water pump set to {control.status}",
            "status": control.status,
            "duration": control.duration_seconds,
            "timestamp": datetime.now()
        }
    
    def control_air_pump(self, control: PumpControl):
        """Control air pump for oxygenation"""
        self.system_state["air_pump"] = control.status
        # TODO: Add actual GPIO control when on Raspberry Pi
        return {
            "message": f"Air pump set to {control.status}",
            "status": control.status,
            "timestamp": datetime.now()
        }
    
    def get_pump_status(self):
        """Get current pump statuses"""
        return {
            "water_pump": self.system_state["water_pump"],
            "air_pump": self.system_state["air_pump"]
        }

pump_service = PumpService()

