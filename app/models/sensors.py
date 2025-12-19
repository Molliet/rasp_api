
from pydantic import BaseModel, Field
from datetime import datetime

class SensorReading(BaseModel):
    value: float
    unit: str
    timestamp: datetime = Field(default_factory=datetime.now)
    status: str = "normal"

class AllSensorsResponse(BaseModel):
    ph: SensorReading
    ec: SensorReading
    temperature: SensorReading
    dissolved_oxygen: SensorReading
    timestamp: datetime

