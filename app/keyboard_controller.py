# app/keyboard_controller.py
import pyautogui
import time
from typing import List

# Type text with optional delay between characters
def type_text(text: str, interval: float = 0.03):
    print(f"\n[EXECUTING] TYPE_TEXT")
    pyautogui.write(text, interval=interval)
    print("[SUCCESS] TEXT_TYPED")

# Copy selected content (Ctrl + C)
def copy():
    print("\n[EXECUTING] COPY")
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.5)
    print("[SUCCESS] COPIED")

# Paste content (Ctrl + V)
def paste():
    print("\n[EXECUTING] PASTE")
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    print("[SUCCESS] PASTED")

# Select all content (Ctrl + A)
def select_all():
    print("\n[EXECUTING] SELECT_ALL")
    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.5)
    print("[SUCCESS] ALL_SELECTED")

# Save current file (Ctrl + S)
def save():
    print("\n[EXECUTING] SAVE")
    pyautogui.hotkey("ctrl", "s")
    time.sleep(1)
    print("[SUCCESS] FILE_SAVED")

# Undo action (Ctrl + Z)
def undo():
    print("\n[EXECUTING] UNDO")
    pyautogui.hotkey("ctrl", "z")
    time.sleep(0.5)
    print("[SUCCESS] UNDO_DONE")

# Redo action (Ctrl + Y)
def redo():
    print("\n[EXECUTING] REDO")
    pyautogui.hotkey("ctrl", "y")
    time.sleep(0.5)
    print("[SUCCESS] REDO_DONE")

# Switch between windows (Alt + Tab)
def alt_tab():
    print("\n[EXECUTING] ALT_TAB")
    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    print("[SUCCESS] SWITCHED_WINDOW")

# Run a list of shortcut keys
def run_shortcut(keys: List[str]):
    print(f"\n[EXECUTING] SHORTCUT: {' + '.join(keys)}")
    pyautogui.hotkey(*keys)
    time.sleep(0.5)
    print("[SUCCESS] SHORTCUT_EXECUTED")