from pydantic import BaseModel

class EEGCommand(BaseModel):
    command: str
    confidence: float