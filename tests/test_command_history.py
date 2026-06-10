# tests/test_command_history.py

from app.command_history import (
    add_command_to_history,
    print_command_history,
    get_command_history
)

# -------------------------------
# Sample Test Commands
# -------------------------------

test_commands = [
    {"command": "OPEN_NOTEPAD", "confidence": 0.85, "threshold": 0.7, "status": "ACCEPTED", "reason": None},
    {"command": "OPEN_VSCODE", "confidence": 0.65, "threshold": 0.7, "status": "REJECTED", "reason": "Low Confidence"},
    {"command": "OPEN_BROWSER", "confidence": 0.90, "threshold": 0.7, "status": "ACCEPTED", "reason": None},
    {"command": "OPEN_TASK_MANAGER", "confidence": 0.80, "threshold": 0.7, "status": "ACCEPTED", "reason": None}
]

# Add commands to history
for cmd in test_commands:
    add_command_to_history(
        cmd["command"],
        cmd["confidence"],
        cmd["threshold"],
        cmd["status"],
        cmd["reason"]
    )

# Print the command history
print_command_history()

# Optional: Get the history as a list
history_list = get_command_history()
print("\nTotal commands recorded:", len(history_list))