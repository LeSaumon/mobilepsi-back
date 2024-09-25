import requests
from sqlmodel import Session
from typing import Dict
import random
from data.query.pony import add_pony
from data.query.parking import add_parking
from data.engine import engine, Pony, Parking

def get_free_bikes_data() -> Dict[str, str]:
    response = requests.get("https://gbfs.getapony.com/v1/Angers/en/free_bike_status.json")
    return response.json()

def initialize_database() -> None:
    data = get_free_bikes_data()
    for bike in data["data"]["bikes"]:
        with Session(engine) as session:
            add_pony(
                Pony(
                    latitude=bike["lat"], 
                    longitude=bike["lon"], 
                    is_available=not bike["is_reserved"]
                    ),
                session=session
                )
    print(f"Added {len(data['data']['bikes'])} to database !")