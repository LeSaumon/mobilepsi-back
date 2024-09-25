from fastapi import APIRouter
import random

router = APIRouter()

@router.get("/parking/{parking_id}")
def get_parking_data() -> bool:
    return False if random.randrange(0,2) == 1 else True