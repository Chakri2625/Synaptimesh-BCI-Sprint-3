# app/validator.py

CONFIDENCE_THRESHOLD = 0.70

def is_valid_confidence(confidence: float) -> bool:
    return confidence >= CONFIDENCE_THRESHOLD