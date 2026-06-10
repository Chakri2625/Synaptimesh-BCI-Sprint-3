# app/command_history.py

import json
import time
import os

HISTORY_FILE = "data/automation_history.json"

# Ensure the data folder exists
if not os.path.exists("data"):
    os.makedirs("data")

def add_command_to_history(command, confidence, threshold, status, reason=None):
    """
    Adds a command record to the automation history.
    """
    record = {
        "command": command,
        "confidence": confidence,
        "threshold": threshold,
        "status": status,
        "reason": reason,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    history = []

    try:
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        history = []

    history.append(record)

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

    print(f"[HISTORY] Recorded: {command} | Status: {status}")


def get_command_history():
    """
    Returns the list of all commands in history.
    """
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def print_command_history():
    """
    Prints command history in a readable format.
    """
    history = get_command_history()
    print("\n" + "="*40)
    print("AUTOMATION COMMAND HISTORY")
    print("="*40)
    for entry in history:
        print(f"Command    : {entry['command']}")
        print(f"Confidence : {entry['confidence']}")
        print(f"Threshold  : {entry['threshold']}")
        print(f"Status     : {entry['status']}")
        if entry["reason"]:
            print(f"Reason     : {entry['reason']}")
        print(f"Timestamp  : {entry['timestamp']}")
        print("-"*40)