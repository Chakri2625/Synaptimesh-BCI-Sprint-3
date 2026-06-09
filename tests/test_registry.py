from app.command_registry import (
    COMMAND_REGISTRY
)

print(
    "\nREGISTERED COMMANDS\n"
)

for command in COMMAND_REGISTRY:

    print(command)