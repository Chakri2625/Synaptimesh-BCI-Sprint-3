from fastapi import FastAPI
from app.schemas.eeg import EEGCommand

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "BCI Backend Running"
    }

@app.post("/receive-command")
def receive_command(data: EEGCommand):
    return {
        "status": "received",
        "command": data.command
    }