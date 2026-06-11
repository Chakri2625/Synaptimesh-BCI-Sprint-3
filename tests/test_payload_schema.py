from app.payload_schema import (
    create_payload
)

payload = create_payload(

    command_name=
    "OPEN_NOTEPAD",

    confidence=
    0.95,

    module_name=
    "APPLICATION_DOMAIN",

    source_identifier=
    "BCI_HEADSET"
)

print()

print("=" * 50)

print(
    "PAYLOAD SCHEMA TEST"
)

print("=" * 50)

print()

for key, value in payload.items():

    print(
        f"{key}: {value}"
    )