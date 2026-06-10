# app/dashboard.py

import json
import os

HISTORY_FILE = "data/automation_history.json"

def load_history():
    """Load command history from JSON file"""
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def show_dashboard():
    """Print automation dashboard summary"""
    history = load_history()

    total_commands = len(history)
    accepted = sum(1 for c in history if c["status"] == "ACCEPTED")
    rejected = sum(1 for c in history if c["status"] == "REJECTED")
    blocked = sum(1 for c in history if c["status"] == "BLOCKED")

    success_rate = (accepted / total_commands * 100) if total_commands else 0

    # Count commands per application/module
    module_count = {}
    for c in history:
        cmd = c["command"]
        module_count[cmd] = module_count.get(cmd, 0) + 1

    print("\n" + "="*50)
    print("AUTOMATION DASHBOARD")
    print("="*50)
    print(f"Total Commands      : {total_commands}")
    print(f"Accepted Commands   : {accepted}")
    print(f"Rejected Commands   : {rejected}")
    print(f"Blocked Commands    : {blocked}")
    print(f"Success Rate        : {success_rate:.2f}%")
    print("-"*50)
    print("Commands per Application/Module:")
    for module, count in module_count.items():
        print(f"{module:20s} : {count}")
    print("="*50 + "\n")