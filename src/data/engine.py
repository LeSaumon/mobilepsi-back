from sqlmodel import SQLModel, create_engine
from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel 

class Vehicule(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    type: str
    brand: str
    model: str
    color: str
    user_id: int = Field(default=None, foreign_key="user.id")
    
class Pony(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    latitude: str
    longitude: str
    is_available: bool
    
class PonyUpdate(SQLModel):
    id: int | None = None
    latitude: str | None = None
    longitude: str | None = None
    is_available: bool | None = None
    
class Parking(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    status: str
    latitude: str
    longitude: str
    sensor_id: int = Field(default=None, foreign_key="sensor.id")
    
    
class Rent(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    is_available: bool
    departure_location: str
    arrival_location: str
    departure_timestamp: str
    arrival_location: str
    
    
class Sensor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    last_data: datetime
    parking_id: int = Field(default=None, foreign_key="parking.id")
    
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    password: str
    is_admin: bool
    mail: str
    # carpoolings: List["Carpooling"] = Relationship(back_populates="carpooling")
    
class Carpooling(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    departure_timestamp: datetime
    arrival_timestamp: datetime
    # attendees: List["User"] = Relationship(back_populates="carpoolings")
    
postgres_url = "postgresql://postgres:saumonpass@localhost:5432/postgres"

engine = create_engine(postgres_url, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)
