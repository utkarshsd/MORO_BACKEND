from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI(
    title="MORO AI",
    version="1.0.0"
)

N8N_WEBHOOK = "http://localhost:5678/webhook/moro-chat"


class ChatRequest(BaseModel):
    user_id: str
    user_message: str

class ChatResponse(BaseModel):
    response: str

@app.get("/")
def home():
    return {
        "status": "running",
        "message": "Welcome to MORO AI Backend"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(data: ChatRequest):
    response = requests.post(
        N8N_WEBHOOK,
        json={
            "user_id": data.user_id,
            "user_message": data.user_message
        }
    )

    return response.json()