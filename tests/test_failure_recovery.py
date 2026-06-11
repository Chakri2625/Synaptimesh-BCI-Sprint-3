# tests/test_failure_recovery.py

from app.failure_recovery import (
    handle_unknown_command,
    handle_invalid_payload,
    handle_unknown_domain,
    handle_controller_failure,
    handle_execution_failure
)

print("="*50)
print("FAILURE RECOVERY TEST")
print("="*50)

print(handle_unknown_command("INVALID_CMD"))
print(handle_invalid_payload({"bad": "payload"}))
print(handle_unknown_domain("OPEN_ROBOT"))
print(handle_controller_failure("OPEN_CALCULATOR", "Controller not found"))
print(handle_execution_failure("OPEN_NOTEPAD", "Execution timeout"))