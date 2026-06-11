from app.mqtt_validator import (
    validate_payload
)

print()

print("=" * 50)

print(
    "MQTT VALIDATION TEST"
)

print("=" * 50)

print()

valid_payload = {

    "timestamp":
    "2026-06-11 10:00:00",

    "command_name":
    "OPEN_NOTEPAD",

    "confidence":
    0.95,

    "threshold":
    0.70
}

invalid_payload = {

    "command_name":
    "OPEN_NOTEPAD",

    "confidence":
    0.95
}

print()

print(
    "VALID PAYLOAD TEST"
)

validate_payload(
    valid_payload
)

print()

print(
    "INVALID PAYLOAD TEST"
)

validate_payload(
    invalid_payload
)