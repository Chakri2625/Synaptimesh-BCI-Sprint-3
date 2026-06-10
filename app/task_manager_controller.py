# app/task_manager_controller.py

import os
import time
import pyautogui
import pygetwindow as gw

def open_task_manager():
    print("\n[EXECUTING] OPEN_TASK_MANAGER")
    os.system('powershell -Command "Start-Process taskmgr -Verb runAs"')
    time.sleep(5)
    print("[SUCCESS] TASK_MANAGER_OPENED")

def maximize_task_manager():
    print("\n[EXECUTING] MAXIMIZE_TASK_MANAGER")
    windows = gw.getWindowsWithTitle("Task Manager")
    if windows:
        windows[0].maximize()
        time.sleep(2)
    print("[SUCCESS] TASK_MANAGER_MAXIMIZED")

def open_demo_notepad():
    print("\n[EXECUTING] OPEN_DEMO_NOTEPAD")
    os.system("start notepad")
    time.sleep(2)
    print("[SUCCESS] DEMO_NOTEPAD_OPENED")

def focus_task_manager():
    windows = gw.getWindowsWithTitle("Task Manager")
    if windows:
        windows[0].activate()
        time.sleep(2)

def open_performance_tab():
    print("\n[EXECUTING] OPEN_PERFORMANCE_TAB")
    pyautogui.click(95, 58)  # Click Performance tab
    time.sleep(2)
    print("[SUCCESS] PERFORMANCE_TAB_OPENED")

def show_cpu():
    print("\n[EXECUTING] SHOW_CPU")
    pyautogui.click(90, 110)
    time.sleep(2)
    print("[SUCCESS] CPU_DISPLAYED")

def show_memory():
    print("\n[EXECUTING] SHOW_MEMORY")
    pyautogui.click(90, 165)
    time.sleep(2)
    print("[SUCCESS] MEMORY_DISPLAYED")

def show_disk():
    print("\n[EXECUTING] SHOW_DISK")
    pyautogui.click(90, 225)
    time.sleep(2)
    print("[SUCCESS] DISK_DISPLAYED")

def open_processes_tab():
    print("\n[EXECUTING] OPEN_PROCESSES_TAB")
    pyautogui.click(30, 58)
    time.sleep(2)
    print("[SUCCESS] PROCESSES_TAB_OPENED")

def terminate_demo_notepad():
    print("\n[EXECUTING] TERMINATE_NOTEPAD")
    os.system("taskkill /f /im notepad.exe")
    time.sleep(2)
    print("[SUCCESS] NOTEPAD_TERMINATED")

def close_task_manager():
    print("\n[EXECUTING] CLOSE_TASK_MANAGER")
    focus_task_manager()
    pyautogui.hotkey("alt", "f4")
    time.sleep(2)
    print("[SUCCESS] TASK_MANAGER_CLOSED")

def run_task_manager_workflow():
    open_task_manager()
    maximize_task_manager()
    open_demo_notepad()
    focus_task_manager()
    open_performance_tab()
    show_cpu()
    show_memory()
    show_disk()
    open_processes_tab()
    terminate_demo_notepad()
    close_task_manager()