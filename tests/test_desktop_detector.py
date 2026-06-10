from app.desktop_detector import *

list_running_apps()
active = get_active_window()
print(f"Active window: {active}")

processes = get_foreground_processes()
print(f"Number of processes: {len(processes)}")

visible = is_window_visible("Task Manager")
print(f"Task Manager visible? {visible}")