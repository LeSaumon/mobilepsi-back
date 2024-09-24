from typing import Union
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from data.main import get_free_bikes_data
from data.engine import Pony, get_session
from data.query.pony import add_pony, get_all_pony

origins = [
    "http://localhost:8081",
]
app = FastAPI() 
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/init-bikes")
def read_root():
    data = get_free_bikes_data()
    for bike in data["data"]["bikes"]:
        with get_session() as session:
            add_pony(
                Pony(
                    latitude=bike["lat"], 
                    longitude=bike["lon"], 
                    is_available=not bike["is_reserved"]
                    ),
                session=session
                )
    return {"data": f"Added {len(data['data']['bikes'])} to database !"}

@app.get("/bikes-data")
def get_all_bikes_data():
    with get_session() as session:
        ponys = get_all_pony(session)
        return {"ponys-data": ponys}
