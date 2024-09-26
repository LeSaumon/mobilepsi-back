from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import ORIGINS
from api import pony, parking, random

# Use on the first launch, to initialize the data inside pony table
# initialize_database()
    
app = FastAPI()
# Used to include all specific API router to the application
app.include_router(pony.router)
app.include_router(parking.router)
app.include_router(random.router)
# Used to bypass the CORS requests
app.add_middleware(CORSMiddleware, allow_origins=ORIGINS, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])