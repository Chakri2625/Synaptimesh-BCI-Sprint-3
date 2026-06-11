# app/dispatcher.py
from app.command_registry import COMMAND_REGISTRY
from app.enhanced_logger import log_command
from app.execution_lock import acquire_lock, release_lock

def dispatch_command(command_name):
    """
    Dispatch a command and log all steps to execution.log
    """
    log_command(f"COMMAND RECEIVED: {command_name}")

    if command_name not in COMMAND_REGISTRY:
        log_command(f"COMMAND FAILED: Unknown command: {command_name}")
        return {"status": "error", "command": command_name, "reason": "Unknown command"}

    # Acquire lock
    if not acquire_lock(command_name):
        log_command(f"COMMAND BLOCKED: Lock active for {command_name}")
        return {"status": "blocked", "command": command_name, "reason": "Lock active"}

    try:
        log_command(f"COMMAND ACCEPTED: {command_name}")

        # Execute the command
        result = COMMAND_REGISTRY[command_name]()
        log_command(f"SUCCESS: {command_name}")

        return {"status": "success", "command": command_name, "result": result}

    except Exception as e:
        log_command(f"COMMAND FAILED: {command_name} | {str(e)}")
        return {"status": "error", "command": command_name, "reason": str(e)}

    finally:
        release_lock(command_name)
        log_command(f"LOCK RELEASED: {command_name}")