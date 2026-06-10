import time

from app.vscode_controller import (
    run_vscode_workflow
)

from app.task_manager_controller import (
    run_task_manager_workflow
)

print()

print("=" * 50)

print(
    "SPRINT 4 DAY 3 FINAL INTEGRATION TEST"
)

print("=" * 50)

print()

print(
    "\n--- VS CODE AUTOMATION ---"
)

run_vscode_workflow()

time.sleep(2)

print(
    "\n--- TASK MANAGER AUTOMATION ---"
)

run_task_manager_workflow()

time.sleep(2)

print()

print("=" * 50)

print(
    "DAY 3 INTEGRATION COMPLETED"
)

print("=" * 50)

print()