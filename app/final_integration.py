from app.dispatcher import dispatch_command
from app.ai_assistant import open_ai_assistant

import time


def run_final_integration():

    open_ai_assistant()

    COMMANDS = [

        "OPEN_NOTEPAD",

        "OPEN_CALCULATOR",

        "OPEN_EXPLORER",

        "OPEN_VSCODE",

        "OPEN_CALENDAR",

        "OPEN_OUTLOOK"
    ]

    for command in COMMANDS:

        dispatch_command(
            command
        )

        time.sleep(2)