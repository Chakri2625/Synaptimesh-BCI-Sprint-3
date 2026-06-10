import os
import time
import pyautogui


FILE_NAME = "day3_demo.py"


def run_vscode_workflow():

    open_vscode()

    create_new_file()

    write_python_program()

    save_python_file()

    run_program()

    close_vscode()


def open_vscode():

    print("\n[EXECUTING] OPEN_VSCODE")

    os.system("start code")

    time.sleep(5)

    print("[SUCCESS] OPEN_VSCODE")


def create_new_file():

    print("\n[EXECUTING] CREATE_NEW_FILE")

    pyautogui.hotkey(
        "ctrl",
        "n"
    )

    time.sleep(2)

    print("[SUCCESS] CREATE_NEW_FILE")


def write_python_program():

    print("\n[EXECUTING] WRITE_PYTHON_PROGRAM")

    program = '''
print("BCI Sprint 4 Day 3")

for i in range(5):
    print("Counter =", i)
'''

    pyautogui.write(
        program,
        interval=0.02
    )

    time.sleep(1)

    print("[SUCCESS] WRITE_PYTHON_PROGRAM")


def save_python_file():

    print("\n[EXECUTING] SAVE_FILE")

    pyautogui.hotkey(
        "ctrl",
        "s"
    )

    time.sleep(2)

    pyautogui.write(
        FILE_NAME
    )

    pyautogui.press(
        "enter"
    )

    time.sleep(2)

    print(
        f"[SUCCESS] FILE_SAVED: {FILE_NAME}"
    )


def run_program():

    print("\n[EXECUTING] RUN_PROGRAM")

    pyautogui.hotkey(
        "ctrl",
        "`"
    )

    time.sleep(3)

    pyautogui.write(
        f"python {FILE_NAME}"
    )

    pyautogui.press(
        "enter"
    )

    time.sleep(5)

    print("[SUCCESS] PROGRAM_EXECUTED")


def close_vscode():

    print("\n[EXECUTING] CLOSE_VSCODE")

    pyautogui.hotkey(
        "alt",
        "f4"
    )

    time.sleep(2)

    print("[SUCCESS] CLOSE_VSCODE")