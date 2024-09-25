from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import ORIGINS
from api import pony

app = FastAPI()
app.include_router(pony.router)
app.add_middleware(CORSMiddleware, allow_origins=ORIGINS, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])