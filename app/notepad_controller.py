import os
import time
import pyautogui


def run_notepad_workflow():

    open_notepad()

    write_project_report()

    select_all()

    copy_text()

    paste_text()

    save_file(
        "BCI_Project_Report.txt"
    )

    close_notepad()


def open_notepad():

    print("\n[EXECUTING] OPEN_NOTEPAD")

    os.system("start notepad")

    time.sleep(2)

    print("[SUCCESS] OPEN_NOTEPAD")


def write_project_report():

    print("\n[EXECUTING] WRITE_PROJECT_REPORT")

    content = """
Brain Computer Interface Project

Sprint 4 Day 2 Automation Demo

Python Team Activities:

1. Duplicate Prevention Engine
2. Cooldown Management System
3. Command Queue Framework
4. Session Tracking System
5. Enhanced Logging System

Applications Automated:

1. Notepad Automation
2. Calculator Automation
3. Browser Automation
4. Media Automation
5. File Explorer Automation

This file was generated automatically
using Python automation.
"""

    pyautogui.write(
        content,
        interval=0.02
    )

    print("[SUCCESS] PROJECT_REPORT_WRITTEN")


def select_all():

    print("\n[EXECUTING] SELECT_ALL")

    pyautogui.hotkey(
        "ctrl",
        "a"
    )

    time.sleep(1)

    print("[SUCCESS] SELECT_ALL")


def copy_text():

    print("\n[EXECUTING] COPY_TEXT")

    pyautogui.hotkey(
        "ctrl",
        "c"
    )

    time.sleep(1)

    print("[SUCCESS] COPY_TEXT")


def paste_text():

    print("\n[EXECUTING] PASTE_TEXT")

    pyautogui.press("end")

    pyautogui.press("enter")

    pyautogui.press("enter")

    pyautogui.hotkey(
        "ctrl",
        "v"
    )

    time.sleep(1)

    print("[SUCCESS] PASTE_TEXT")


def save_file(filename):

    print("\n[EXECUTING] SAVE_FILE")

    pyautogui.hotkey(
        "ctrl",
        "s"
    )

    time.sleep(2)

    pyautogui.write(
        filename
    )

    time.sleep(1)

    pyautogui.press("enter")

    time.sleep(2)

    print(
        f"[SUCCESS] SAVED: {filename}"
    )


def close_notepad():

    print("\n[EXECUTING] CLOSE_NOTEPAD")

    pyautogui.hotkey(
        "alt",
        "f4"
    )

    time.sleep(1)

    print("[SUCCESS] CLOSE_NOTEPAD")