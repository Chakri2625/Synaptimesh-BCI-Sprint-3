# app/desktop_detector.py
import psutil
import pygetwindow as gw
import time

# List all running applications/windows
def list_running_apps():
    print("\n[EXECUTING] LIST_RUNNING_APPS")
    windows = gw.getAllTitles()
    for w in windows:
        if w.strip():
            print(f"Running Window: {w}")
    print("[SUCCESS] LIST_RUNNING_APPS")
    return windows

# Get the currently active window title
def get_active_window():
    print("\n[EXECUTING] GET_ACTIVE_WINDOW")
    active = gw.getActiveWindow()
    if active:
        print(f"Active Window: {active.title}")
        return active.title
    print("No active window found")
    return None

# Get a list of running processes
def get_foreground_processes():
    print("\n[EXECUTING] GET_FOREGROUND_PROCESSES")
    processes = [p.name() for p in psutil.process_iter()]
    for proc in processes:
        print(f"Process: {proc}")
    print("[SUCCESS] GET_FOREGROUND_PROCESSES")
    return processes

# Check if a window with specific title exists and is visible
def is_window_visible(window_title):
    print(f"\n[EXECUTING] IS_WINDOW_VISIBLE: {window_title}")
    window = gw.getWindowsWithTitle(window_title)
    if window and window[0].isVisible:
        print(f"Window '{window_title}' is visible")
        return True
    print(f"Window '{window_title}' is not visible")
    return False