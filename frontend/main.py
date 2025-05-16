from fastapi import FastAPI, Request
from pydantic import BaseModel
from backend.models.trainer import train_user_model
from backend.models.predictor import authenticate_user
from backend.database import save_behavior_data

app = FastAPI()

class LoginRequest(BaseModel):
    username: str
    password: str
    behaviorData: list

@app.post("/authenticate")
async def authenticate(data: LoginRequest):
    result = authenticate_user(data.username, data.behaviorData)
    if result:
        return {"message": "Login Success"}
    else:
        return {"message": "Login Denied (Behavior Mismatch)"}

@app.post("/train")
async def train_user(data: LoginRequest):
    save_behavior_data(data.username, data.behaviorData)
    train_user_model(data.username)
    return {"message": "User trained successfully"}
