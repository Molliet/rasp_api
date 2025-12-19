
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class PumpStatus(str, Enum):
    ON = "on"
    OFF = "off"
    AUTO = "auto"

class LightMode(str, Enum):
    ON = "on"
    OFF = "off"
    SCHEDULE = "schedule"

class PumpControl(BaseModel):
    status: PumpStatus
    duration_seconds: Optional[int] = None

class NutrientDosing(BaseModel):
    nutrient_type: str
    ml_amount: float
    target_ec: Optional[float] = None

class LightControl(BaseModel):
    mode: LightMode
    brightness: Optional[int] = Field(None, ge=0, le=100)
    schedule_on: Optional[str] = None
    schedule_off: Optional[str] = None

