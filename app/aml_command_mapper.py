# app/aml_command_mapper.py

AML_COMMANDS = {

    "PUSH":
    "OPEN",

    "PULL":
    "CLOSE",

    "LEFT":
    "PREVIOUS_APPLICATION",

    "RIGHT":
    "NEXT_APPLICATION",

    "UP":
    "START_AUTOMATION",

    "DOWN":
    "STOP_AUTOMATION"
}


def map_command(command):

    return AML_COMMANDS.get(
        command,
        "UNKNOWN"
    )