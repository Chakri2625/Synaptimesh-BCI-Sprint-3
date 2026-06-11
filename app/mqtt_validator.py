# app/mqtt_validator.py

REQUIRED_FIELDS = [

    "timestamp",

    "command_name",

    "confidence",

    "threshold"
]


def validate_payload(payload):

    for field in REQUIRED_FIELDS:

        if field not in payload:

            print()

            print(
                f"[VALIDATOR] Missing Field: {field}"
            )

            return False

    print()

    print(
        "[VALIDATOR] Payload Valid"
    )

    return True