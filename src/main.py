from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data.main import get_free_bikes_data

app = FastAPI() 
origins = [
    "http://localhost:8081",
]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/free-bikes")
def read_root():
    data = get_free_bikes_data()
    return {"data": data}
