
from fastapi import APIRouter
from app.models.system import SystemStatus
from app.services.sensor_service import sensor_service
from app.services.pump_service import pump_service
from app.services.light_service import light_service
from app.core.dependencies import get_system_state
from datetime import datetime

router = APIRouter(tags=["System"])

# REMOVIDO: @app.get("/") - agora será servido pelo main.py

@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now()
    }

@router.get("/status", response_model=SystemStatus)
async def get_system_status():
    """Get overall system status"""
    ph_reading = sensor_service.get_ph_reading()
    ec_reading = sensor_service.get_ec_reading()
    temp_reading = sensor_service.get_temperature_reading()
    
    alerts = []
    if ph_reading.status == "warning":
        alerts.append(f"pH out of range: {ph_reading.value}")
    if ec_reading.status == "warning":
        alerts.append(f"EC out of range: {ec_reading.value}")
    if temp_reading.status == "warning":
        alerts.append(f"Temperature out of range: {temp_reading.value}")
    
    system_state = get_system_state()
    uptime = (datetime.now() - system_state["start_time"]).total_seconds() / 3600
    
    return SystemStatus(
        system_name="DWC System 1",
        uptime_hours=round(uptime, 2),
        ph=ph_reading.value,
        ec=ec_reading.value,
        water_temp=temp_reading.value,
        water_level="normal",
        pumps_status=pump_service.get_pump_status(),
        lights_status=light_service.get_light_status()["status"],
        alerts=alerts
    )

@router.get("/alerts")
async def get_alerts():
    """Get active system alerts"""
    status = await get_system_status()
    return {
        "alerts": status.alerts,
        "count": len(status.alerts),
        "timestamp": datetime.now()
    }

@router.get("/api")
async def api_info():
    """API information endpoint"""
    return {
        "message": "DWC Hydroponic System API",
        "version": "1.0.0",
        "status": "running"
    }

