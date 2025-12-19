from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(prefix="/api", tags=["lights"])

# Estado atual das luzes
light_state = "OFF"

class LightCommand(BaseModel):
    command: str  # "ON", "OFF", ou "SCHEDULE"

@router.get("/lights")
async def get_lights_status():
    """Retorna status das luzes de crescimento"""
    return {
        "device": "grow_lights",
        "status": light_state,
        "timestamp": datetime.now().isoformat()
    }

@router.post("/lights")
async def control_lights(command: LightCommand):
    """Controla as luzes de crescimento"""
    global light_state

    try:
        if command.command not in ["ON", "OFF", "SCHEDULE"]:
            raise HTTPException(status_code=400, detail="Comando inválido. Use: ON, OFF ou SCHEDULE")

        light_state = command.command

        # Aqui você adicionaria o código para controlar o GPIO do Raspberry Pi
        # Exemplo: GPIO.output(LIGHTS_PIN, GPIO.HIGH if command.command == "ON" else GPIO.LOW)

        return {
            "device": "grow_lights",
            "status": light_state,
            "message": f"Luzes de crescimento {command.command}",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao controlar luzes: {str(e)}")
