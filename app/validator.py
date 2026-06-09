CONFIDENCE_THRESHOLD = 0.70

def is_valid_confidence(confidence: float) -> bool:
    return confidence >= CONFIDENCE_THRESHOLD

def validate_threshold(confidence, threshold):
    return confidence >= threshold

def validate_command(payload):
    command = payload["command"]
    confidence = payload["confidence"]

    print("\n====================================")
    print(f"Command    : {command}")
    print(f"Confidence : {confidence}")
    print(f"Threshold  : {CONFIDENCE_THRESHOLD}")

    if confidence >= CONFIDENCE_THRESHOLD:
        print("\nResult     : ACCEPTED")
        print("====================================")
        return True

    print("\nResult     : REJECTED")
    print("Reason     : Low Confidence")
    print("====================================")
    return False