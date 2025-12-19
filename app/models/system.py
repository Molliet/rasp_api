
from pydantic import BaseModel
from typing import List

class SystemStatus(BaseModel):
    system_name: str
    uptime_hours: float
    ph: float
    ec: float
    water_temp: float
    water_level: str
    pumps_status: dict
    lights_status: str
    alerts: List[str]

class HealthCheck(BaseModel):
    status: str
    timestamp: str

