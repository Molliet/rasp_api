
# config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # API Settings
    API_TITLE: str = "DWC Hydroponic System API"
    API_VERSION: str = "1.0.0"
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    
    # Sensor Thresholds
    PH_MIN: float = 5.5
    PH_MAX: float = 6.5
    PH_OPTIMAL: float = 6.0
    
    EC_MIN: float = 1.5
    EC_MAX: float = 2.5
    EC_OPTIMAL: float = 2.0
    
    TEMP_MIN: float = 18.0
    TEMP_MAX: float = 24.0
    TEMP_OPTIMAL: float = 21.0
    
    DO_MIN: float = 6.0
    
    # GPIO Pins (for Raspberry Pi)
    WATER_PUMP_PIN: int = 17
    AIR_PUMP_PIN: int = 27
    LIGHT_PIN: int = 22
    DOSING_PUMP_PIN: int = 23
    
    class Config:
        env_file = ".env"

settings = Settings()

