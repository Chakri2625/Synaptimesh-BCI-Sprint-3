from app.command_registry import COMMAND_REGISTRY
from app.logger import logger
from app.exceptions import (
    InvalidCommandError,
    AutomationExecutionError
)
from app.duplicate_prevention import check_duplicate
from app.cooldown_manager import check_cooldown
from app.execution_lock import acquire_lock, release_lock
from app.enhanced_logger import log_command

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

        return {"status": "success", "command": command}

    except Exception as e:
        logger.error(f"Dispatcher Error: {str(e)}")
        return {"status": "error", "message": str(e)}


def dispatch(payload):
    """
    Dispatch a BCI command payload with logging, duplicate prevention,
    cooldown, execution lock, and sequential execution.
    """
    command = payload.get("command")
    confidence = payload.get("confidence", 0)
    threshold = payload.get("threshold", 0.7)

    # Log command received
    log_command(f"COMMAND RECEIVED: {command} | Confidence: {confidence} | Threshold: {threshold}")

    # Threshold check
    if confidence < threshold:
        log_command(f"COMMAND REJECTED: {command} | Reason: Low Confidence")
        print(f"[RESULT] REJECTED - Low Confidence")
        return {"status": "rejected", "reason": "Low Confidence"}

    # Duplicate check
    if not check_duplicate(command):
        log_command(f"COMMAND REJECTED: {command} | Reason: Duplicate Command")
        print(f"[RESULT] REJECTED - Duplicate Command")
        return {"status": "rejected", "reason": "Duplicate Command"}

    # Cooldown check
    if not check_cooldown(command):
        log_command(f"COMMAND BLOCKED: {command} | Reason: Cooldown Active")
        print(f"[RESULT] BLOCKED - Cooldown Active")
        return {"status": "blocked", "reason": "Cooldown Active"}

    # Acquire execution lock
    if not acquire_lock(command):
        log_command(f"COMMAND BLOCKED: {command} | Reason: Lock Active")
        print(f"[RESULT] BLOCKED - Lock Active")
        return {"status": "blocked", "reason": "Lock Active"}

    try:
        # Command accepted
        log_command(f"COMMAND ACCEPTED: {command}")
        print(f"[RESULT] ACCEPTED - Executing {command}")

        # Execute the actual command
        if command not in COMMAND_REGISTRY:
            log_command(f"COMMAND FAILED: {command} | Reason: Unknown Command")
            print(f"[ERROR] Unknown command: {command}")
            return {"status": "error", "reason": "Unknown Command"}

        log_command(f"EXECUTING: {command}")
        COMMAND_REGISTRY[command]()
        log_command(f"SUCCESS: {command}")
        print(f"[RESULT] SUCCESS - {command} executed")

        return {"status": "success"}

    except Exception as e:
        log_command(f"COMMAND FAILED: {command} | Reason: {str(e)}")
        print(f"[RESULT] FAILED - {command} | {str(e)}")
        return {"status": "error", "reason": str(e)}

    finally:
        release_lock(command)
        log_command(f"LOCK RELEASED: {command}")