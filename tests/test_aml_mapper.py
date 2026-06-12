from app.aml_command_mapper import (
    map_command
)

COMMANDS = [

    "PUSH",

    "PULL",

    "LEFT",

    "RIGHT",

    "UP",

    "DOWN"
]

for command in COMMANDS:

    print()

    print(
        f"{command} --> {map_command(command)}"
    )