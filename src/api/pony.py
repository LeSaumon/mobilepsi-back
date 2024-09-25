from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlmodel import Session
import random

from data.engine import engine, Pony, PonyUpdate

from data.query.pony import get_all_pony, get_pony_by_id
router = APIRouter()

@router.get("/parking/{parking_id}")
def get_parking_data():
    return False if random.randrange(0,2) == 1 else True

@router.get("/bikes/", tags=["bikes"])
def get_bikes_data():
    with Session(engine) as session:
        ponys = get_all_pony(session)
        return {"ponys-data": ponys}
    
@router.get("/bikes/{pony_id}", tags=["bikes"])
def get_bike_data(pony_id: int) -> Pony:
    with Session(engine) as session:
        pony = get_pony_by_id(pony_id=pony_id, session=session)
        print(pony)
        # if pony := get_pony_by_id(pony_id=pony_id, session=session):
        # #     return {"data": pony}
        # else:
        #     raise HTTPException(status_code=404, details="Pony not found!")
        
@router.patch("/bikes/{pony_id}", tags=["bikes"])
def update_bike(pony_id: int, pony: PonyUpdate) -> Pony:
    with Session(engine) as session:
        pony_db = session.get(Pony, pony_id)
        if not pony_db:
            raise HTTPException(status_code=404, details="Pony not found!")
        pony_data = pony.model_dump(exclude_unset=True)
        pony_db.sqlmodel_update(pony_data)
        session.add(pony_db)
        session.commit()
        session.refresh(pony_db)
        return pony_db

