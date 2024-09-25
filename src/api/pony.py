from data.engine import get_session
from data.query.pony import get_all_pony
from fastapi import APIRouter

router = APIRouter()

@router.get("/bikes/", tags=["bikes"])
def get_bikes_data():
    with get_session() as session:
        ponys = get_all_pony(session)
        return {"ponys-data": ponys}