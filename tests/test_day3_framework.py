# tests/test_day3_framework.py

import time
from app.window_manager import *
from app.keyboard_controller import *
from app.mouse_controller import *
from app.desktop_detector import *

print("\n=== STARTING DAY 3 FRAMEWORK TEST ===")

# ---------------------------
# 1. Test Window Manager
# ---------------------------
print("\n--- Window Manager Tests ---")
open_window("notepad.exe")
time.sleep(1)
switch_window("Untitled - Notepad")
time.sleep(1)
minimize_window("Untitled - Notepad")
time.sleep(1)
maximize_window("Untitled - Notepad")
time.sleep(1)
restore_window("Untitled - Notepad")
time.sleep(1)
close_window("Untitled - Notepad")

# ---------------------------
# 2. Test Keyboard Controller
# ---------------------------
print("\n--- Keyboard Controller Tests ---")
type_text("print('Hello BCI Framework')")
time.sleep(1)
select_all()
paste()
undo()
redo()
save()
alt_tab()

# ---------------------------
# 3. Test Mouse Controller
# ---------------------------
print("\n--- Mouse Controller Tests ---")
left_click()
time.sleep(0.5)
right_click()
time.sleep(0.5)
double_click()
time.sleep(0.5)
scroll_up(200)
time.sleep(0.5)
scroll_down(200)
pos = get_mouse_position()
print(f"Mouse position: {pos}")

# ---------------------------
# 4. Test Desktop Detector
# ---------------------------
print("\n--- Desktop Detector Tests ---")
list_running_apps()
active = get_active_window()
print(f"Active window: {active}")
processes = get_foreground_processes()
print(f"Number of processes running: {len(processes)}")
visible = is_window_visible("Task Manager")
print(f"Task Manager visible? {visible}")

print("\n=== FRAMEWORK TEST COMPLETE ===")