from app.domain_classifier import (
    classify_command
)

print()

print("=" * 50)

print(
    "DOMAIN CLASSIFIER TEST"
)

print("=" * 50)

print()

commands = [

    "OPEN_NOTEPAD",
    "OPEN_VSCODE",
    "COPY",
    "LEFT_CLICK",
    "MAXIMIZE_WINDOW",
    "INVALID_COMMAND"

]

for command in commands:

    result = classify_command(
        command
    )

    print(
        f"{command} --> {result}"
    )