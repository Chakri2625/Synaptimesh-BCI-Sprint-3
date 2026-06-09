import os
import time
import pyautogui


def run_explorer_workflow():

    open_file_explorer()

    open_drive()

    create_folder()

    close_file_explorer()


FOLDER_NAME = "Sprint4_Day2_Demo"


def open_file_explorer():

    print(
        "\n[EXECUTING] OPEN_FILE_EXPLORER"
    )

    os.system(
        "explorer"
    )

    time.sleep(2)

    print(
        "[SUCCESS] OPEN_FILE_EXPLORER"
    )


def open_drive():

    print(
        "\n[EXECUTING] OPEN_DRIVE_E"
    )

    pyautogui.hotkey(
        "ctrl",
        "l"
    )

    time.sleep(1)

    pyautogui.write(
        "E:\\"
    )

    pyautogui.press(
        "enter"
    )

    time.sleep(2)

    print(
        "[SUCCESS] DRIVE_OPENED"
    )


def create_folder():

    print(
        "\n[EXECUTING] CREATE_FOLDER"
    )

    pyautogui.hotkey(
        "ctrl",
        "shift",
        "n"
    )

    time.sleep(1)

    pyautogui.write(
        FOLDER_NAME
    )

    pyautogui.press(
        "enter"
    )

    time.sleep(1)

    print(
        f"[SUCCESS] FOLDER_CREATED: {FOLDER_NAME}"
    )


def close_file_explorer():

    print(
        "\n[EXECUTING] CLOSE_FILE_EXPLORER"
    )

    pyautogui.hotkey(
        "alt",
        "f4"
    )

    print(
        "[SUCCESS] CLOSE_FILE_EXPLORER"
    )