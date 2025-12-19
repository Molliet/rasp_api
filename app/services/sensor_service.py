
from app.models.sensors import SensorReading
from app.core.config import settings
from app.core.dependencies import get_sensor_data
from datetime import datetime

class SensorService:
    def __init__(self):
        self.sensor_data = get_sensor_data()
    
    def get_ph_reading(self) -> SensorReading:
        """Get current pH reading - replace with actual sensor code"""
        value = 6.2  # Simulated value
        reading = SensorReading(
            value=value,
            unit="pH",
            status="normal" if settings.PH_MIN <= value <= settings.PH_MAX else "warning"
        )
        self.sensor_data["ph"].append(reading.dict())
        return reading
    
    def get_ec_reading(self) -> SensorReading:
        """Get current EC reading - replace with actual sensor code"""
        value = 1.8  # Simulated value
        reading = SensorReading(
            value=value,
            unit="mS/cm",
            status="normal" if settings.EC_MIN <= value <= settings.EC_MAX else "warning"
        )
        self.sensor_data["ec"].append(reading.dict())
        return reading
    
    def get_temperature_reading(self) -> SensorReading:
        """Get current temperature reading - replace with actual sensor code"""
        value = 22.5  # Simulated value
        reading = SensorReading(
            value=value,
            unit="°C",
            status="normal" if settings.TEMP_MIN <= value <= settings.TEMP_MAX else "warning"
        )
        self.sensor_data["temperature"].append(reading.dict())
        return reading
    
    def get_dissolved_oxygen_reading(self) -> SensorReading:
        """Get current DO reading - replace with actual sensor code"""
        value = 8.2  # Simulated value
        reading = SensorReading(
            value=value,
            unit="mg/L",
            status="normal" if value >= settings.DO_MIN else "warning"
        )
        self.sensor_data["dissolved_oxygen"].append(reading.dict())
        return reading
    
    def get_sensor_history(self, sensor_type: str, limit: int = 100):
        """Get historical sensor data"""
        if sensor_type not in self.sensor_data:
            return None
        return self.sensor_data[sensor_type][-limit:]

sensor_service = SensorService()

