from app.command_registry import COMMAND_REGISTRY


def dispatch_command(command: str):

    if command not in COMMAND_REGISTRY:
        return {
            "status": "error",
            "message": f"Unknown command: {command}"
        }

    action = COMMAND_REGISTRY[command]

    if action is None:
        return {
            "status": "error",
            "message": f"Command not implemented: {command}"
        }

    try:
        action()

        return {
            "status": "success",
            "command": command
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }