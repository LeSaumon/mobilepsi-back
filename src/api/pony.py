from fastapi import APIRouter, HTTPException
from sqlmodel import Session

from data.engine import engine, Pony, PonyUpdate

from data.query.pony import get_all_pony, get_pony_by_id
router = APIRouter()

@router.get("/bikes/", tags=["bikes"])
def get_bikes_data() -> Pony | None:
    with Session(engine) as session:
        ponys = get_all_pony(session)
        return ponys
    
@router.get("/bike/{id}", tags=["bikes"])
def get_bike_data(id: int = 0) -> Pony:
    with Session(engine) as session:
        if pony:= get_pony_by_id(session=session, pony_id=id):
            return pony
        else:
            raise HTTPException(status_code=404, details="Pony not found!")
                    
@router.patch("/bike/update/{pony_id}", tags=["bikes"])
def update_bike(pony_id: int, pony: PonyUpdate) -> Pony:
    with Session(engine) as session:
        if pony_db := session.get(Pony, pony_id):
            pony_data = pony.model_dump(exclude_unset=True)
            pony_db.sqlmodel_update(pony_data)
            session.add(pony_db)
            session.commit()
            session.refresh(pony_db)
        else:
            raise HTTPException(status_code=404, details="Pony not found!")

@router.delete("/bike/{id}")
def delete_bike(id: int = 0) -> None:
    with Session(engine) as session:
        if pony:= get_pony_by_id(session, id):
            session.delete(pony)
            session.commit()
            return True
        else:
            raise HTTPException(status_code=404, details="Pony not found!")