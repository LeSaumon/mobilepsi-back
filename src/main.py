from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import ORIGINS
from api import pony, parking, random

# Use on the first launch, to initialize the databases schemas
# initialize_database()
    
app = FastAPI()
app.include_router(pony.router)
app.include_router(parking.router)
app.include_router(random.router)
app.add_middleware(CORSMiddleware, allow_origins=ORIGINS, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])