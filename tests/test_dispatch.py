import time
from app.dispatcher import dispatch_command

test_commands = [
    "OPEN_BROWSER",
    "CLOSE_BROWSER",
    "PLAY_PAUSE",
    "VOLUME_UP",
    "VOLUME_DOWN",
    "SCROLL_UP",
    "SCROLL_DOWN",
    "OPEN_NOTEPAD",
    "CLOSE_NOTEPAD",
    "OPEN_CALCULATOR",
    "CLOSE_CALCULATOR"
]

for command in test_commands:

    print(f"\nTesting: {command}")

    result = dispatch_command(command)

    print(result)

    time.sleep(3)