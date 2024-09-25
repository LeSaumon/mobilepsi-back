from fastapi import APIRouter
import random
from datetime import datetime

router = APIRouter()

@router.get("/random/parking/available")
def get_parking_data() -> bool:
    return False if random.randrange(0,2) == 1 else True

@router.get("/random/parkings")
def random_parkings():
    data = [
        {
            "status": False if random.randrange(0,2) == 1 else True,
            "latitude": random.uniform(47.4, 47.5),
            "longitude": random.uniform(-0.5, -0.6),
            "sensor_id": 1 + i
        } for i in range(0, 20)
    ]
    return data

@router.get("/random/sensors")
def random_sensors():
    data = [
        {
            "name": f"sensor_{random.randint(1, 50)}_{random.randint(51, 100)}",
            "last_data": datetime.now(),
            "longitude": random.uniform(-0.5, -0.6),
        } for i in range(0, 20)
    ]
    return data
    