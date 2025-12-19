
from app.models.controls import LightControl, LightMode
from app.core.dependencies import get_system_state
from datetime import datetime

class LightService:
    def __init__(self):
        self.system_state = get_system_state()
    
    def control_lights(self, control: LightControl):
        """Control grow lights"""
        self.system_state["lights"] = control.mode
        # TODO: Add actual GPIO control when on Raspberry Pi
        return {
            "message": f"Lights set to {control.mode}",
            "mode": control.mode,
            "brightness": control.brightness,
            "schedule": {
                "on": control.schedule_on,
                "off": control.schedule_off
            } if control.mode == LightMode.SCHEDULE else None,
            "timestamp": datetime.now()
        }
    
    def get_light_status(self):
        """Get current light status"""
        return {
            "status": self.system_state["lights"]
        }

light_service = LightService()

