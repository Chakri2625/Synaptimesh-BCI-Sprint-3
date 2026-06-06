from app.command_registry import COMMAND_REGISTRY
from app.logger import logger
from app.exceptions import (
    InvalidCommandError,
    AutomationExecutionError
)


def dispatch_command(command):
    """
    Dispatch a command from BCI signals or MQTT messages.
    Logs everything to command_log.txt via logger.
    """
    try:
        # Log every received command
        logger.info(f"Received command: {command}")

        if command not in COMMAND_REGISTRY:
            logger.error(f"Unknown command: {command}")
            raise InvalidCommandError(f"Unknown command: {command}")

        action = COMMAND_REGISTRY[command]

        if action:
            try:
                action()
                logger.info(f"Successfully executed: {command}")
            except Exception as e:
                logger.error(f"Automation failed for {command}: {str(e)}")
                raise AutomationExecutionError(str(e))

        return {
            "status": "success",
            "command": command
        }

    except Exception as e:
        logger.error(f"Dispatcher Error: {str(e)}")
        return {
            "status": "error",
            "message": str(e)
        }