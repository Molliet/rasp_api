from fastapi import APIRouter, HTTPException
from datetime import datetime
import random

router = APIRouter(prefix="/api", tags=["sensors"])

# Simulação de dados dos sensores (substitua por leitura real dos sensores)
def get_sensor_readings():
    """Simula leitura dos sensores - substitua pela leitura real do Raspberry Pi"""
    return {
        "ph": {
            "value": round(random.uniform(5.5, 7.0), 2),
            "status": "NORMAL",
            "timestamp": datetime.now().isoformat()
        },
        "ec": {
            "value": round(random.uniform(1.5, 2.0), 2),
            "status": "NORMAL",
            "timestamp": datetime.now().isoformat()
        },
        "temperature": {
            "value": round(random.uniform(20.0, 25.0), 1),
            "status": "NORMAL",
            "timestamp": datetime.now().isoformat()
        },
        "dissolved_oxygen": {
            "value": round(random.uniform(7.0, 9.0), 1),
            "status": "NORMAL",
            "timestamp": datetime.now().isoformat()
        }
    }

@router.get("/sensors")
async def get_all_sensors():
    """Retorna dados de todos os sensores"""
    try:
        return get_sensor_readings()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao ler sensores: {str(e)}")
