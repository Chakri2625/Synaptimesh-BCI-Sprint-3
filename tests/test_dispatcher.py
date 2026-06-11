# tests/test_dispatcher.py

from app.dispatcher import (
    dispatch_command
)

COMMANDS = [

    "OPEN_NOTEPAD",

    "OPEN_CALCULATOR",

    "OPEN_EXPLORER",

    "OPEN_VSCODE",

    "OPEN_CALENDAR"
]

for command in COMMANDS:

    print()

    print("=" * 50)

    print(
        f"TESTING: {command}"
    )

    print("=" * 50)

    result = dispatch_command(
        command
    )

    print(result)