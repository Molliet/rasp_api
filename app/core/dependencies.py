
from typing import Dict, List
from datetime import datetime

# In-memory storage (replace with database later)
sensor_data: Dict[str, List] = {
    "ph": [],
    "ec": [],
    "temperature": [],
    "dissolved_oxygen": []
}

system_state: Dict = {
    "water_pump": "off",
    "air_pump": "on",
    "lights": "off",
    "last_dosing": None,
    "start_time": datetime.now()
}

def get_sensor_data():
    return sensor_data

def get_system_state():
    return system_state

