from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(prefix="/api/pumps", tags=["pumps"])

# Estado atual das bombas (em produção, use um banco de dados ou estado persistente)
pump_states = {
    "water": "OFF",
    "air": "ON"
}

class PumpCommand(BaseModel):
    command: str  # "ON", "OFF", ou "AUTO"

@router.get("/water")
async def get_water_pump_status():
    """Retorna status da bomba de água"""
    return {
        "device": "water_pump",
        "status": pump_states["water"],
        "timestamp": datetime.now().isoformat()
    }

@router.post("/water")
async def control_water_pump(command: PumpCommand):
    """Controla a bomba de água"""
    try:
        if command.command not in ["ON", "OFF", "AUTO"]:
            raise HTTPException(status_code=400, detail="Comando inválido. Use: ON, OFF ou AUTO")

        pump_states["water"] = command.command

        # Aqui você adicionaria o código para controlar o GPIO do Raspberry Pi
        # Exemplo: GPIO.output(WATER_PUMP_PIN, GPIO.HIGH if command.command == "ON" else GPIO.LOW)

        return {
            "device": "water_pump",
            "status": pump_states["water"],
            "message": f"Bomba de água {command.command}",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao controlar bomba de água: {str(e)}")

@router.get("/air")
async def get_air_pump_status():
    """Retorna status da bomba de ar"""
    return {
        "device": "air_pump",
        "status": pump_states["air"],
        "timestamp": datetime.now().isoformat()
    }

@router.post("/air")
async def control_air_pump(command: PumpCommand):
    """Controla a bomba de ar"""
    try:
        if command.command not in ["ON", "OFF", "AUTO"]:
            raise HTTPException(status_code=400, detail="Comando inválido. Use: ON, OFF ou AUTO")

        pump_states["air"] = command.command

        # Aqui você adicionaria o código para controlar o GPIO do Raspberry Pi
        # Exemplo: GPIO.output(AIR_PUMP_PIN, GPIO.HIGH if command.command == "ON" else GPIO.LOW)

        return {
            "device": "air_pump",
            "status": pump_states["air"],
            "message": f"Bomba de ar {command.command}",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao controlar bomba de ar: {str(e)}")
