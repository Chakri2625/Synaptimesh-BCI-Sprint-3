from fastapi import FastAPI
from app.schemas.eeg import EEGCommand
from app.validator import is_valid_confidence
from app.dispatcher import dispatch_command

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "BCI Backend Running"
    }


@app.post("/receive-command")
def receive_command(data: EEGCommand):

    if not is_valid_confidence(data.confidence):
        return {
            "status": "rejected",
            "reason": "confidence below threshold"
        }

    return dispatch_command(data.command)