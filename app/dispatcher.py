from app.command_registry import COMMAND_REGISTRY


def dispatch_command(command):

    if command not in COMMAND_REGISTRY:
        return {
            "status": "error",
            "message": f"Unknown command: {command}"
        }

    action = COMMAND_REGISTRY[command]

    if action:
        action()

    return {
        "status": "success",
        "command": command
    }