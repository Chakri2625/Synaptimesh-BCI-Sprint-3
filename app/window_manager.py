# app/window_manager.py
import pygetwindow as gw
import pyautogui
import time
import os

# Open a window (launch an application)
def open_window(app_path: str):
    print(f"\n[EXECUTING] OPEN_WINDOW: {app_path}")
    try:
        os.startfile(app_path)
        time.sleep(3)
        print(f"[SUCCESS] WINDOW_OPENED: {app_path}")
    except Exception as e:
        print(f"[FAILED] OPEN_WINDOW: {e}")

# Close a window by its title
def close_window(window_title: str):
    print(f"\n[EXECUTING] CLOSE_WINDOW: {window_title}")
    try:
        window = gw.getWindowsWithTitle(window_title)
        if window:
            window[0].close()
            time.sleep(1)
            print(f"[SUCCESS] WINDOW_CLOSED: {window_title}")
        else:
            print(f"[FAILED] WINDOW NOT FOUND: {window_title}")
    except Exception as e:
        print(f"[FAILED] CLOSE_WINDOW: {e}")

# Minimize a window by its title
def minimize_window(window_title: str):
    print(f"\n[EXECUTING] MINIMIZE_WINDOW: {window_title}")
    try:
        window = gw.getWindowsWithTitle(window_title)
        if window:
            window[0].minimize()
            time.sleep(1)
            print(f"[SUCCESS] WINDOW_MINIMIZED: {window_title}")
        else:
            print(f"[FAILED] WINDOW NOT FOUND: {window_title}")
    except Exception as e:
        print(f"[FAILED] MINIMIZE_WINDOW: {e}")

# Maximize a window by its title
def maximize_window(window_title: str):
    print(f"\n[EXECUTING] MAXIMIZE_WINDOW: {window_title}")
    try:
        window = gw.getWindowsWithTitle(window_title)
        if window:
            window[0].maximize()
            time.sleep(1)
            print(f"[SUCCESS] WINDOW_MAXIMIZED: {window_title}")
        else:
            print(f"[FAILED] WINDOW NOT FOUND: {window_title}")
    except Exception as e:
        print(f"[FAILED] MAXIMIZE_WINDOW: {e}")

# Restore a minimized window
def restore_window(window_title: str):
    print(f"\n[EXECUTING] RESTORE_WINDOW: {window_title}")
    try:
        window = gw.getWindowsWithTitle(window_title)
        if window:
            window[0].restore()
            time.sleep(1)
            print(f"[SUCCESS] WINDOW_RESTORED: {window_title}")
        else:
            print(f"[FAILED] WINDOW NOT FOUND: {window_title}")
    except Exception as e:
        print(f"[FAILED] RESTORE_WINDOW: {e}")

# Switch to a window (bring it to front)
def switch_window(window_title: str):
    print(f"\n[EXECUTING] SWITCH_WINDOW: {window_title}")
    try:
        window = gw.getWindowsWithTitle(window_title)
        if window:
            window[0].activate()
            time.sleep(1)
            print(f"[SUCCESS] SWITCHED_TO_WINDOW: {window_title}")
        else:
            print(f"[FAILED] WINDOW NOT FOUND: {window_title}")
    except Exception as e:
        print(f"[FAILED] SWITCH_WINDOW: {e}")