import os
import time
import pyautogui


def run_media_workflow():

    open_video()

    pause_video()

    play_video()

    volume_up()

    volume_down()

    fullscreen()

    exit_fullscreen()

    close_video()


VIDEO_PATH = (
    r"C:\Users\AB Lab 9\Videos\Captures"
    r"\calendar_bci_project.mp4"
)


def open_video():

    print("\n[EXECUTING] OPEN_VIDEO")

    os.startfile(
        VIDEO_PATH
    )

    time.sleep(2)

    print("[SUCCESS] VIDEO_OPENED")


def pause_video():

    print("\n[EXECUTING] PAUSE_VIDEO")

    pyautogui.press("space")

    time.sleep(1)

    print("[SUCCESS] VIDEO_PAUSED")


def play_video():

    print("\n[EXECUTING] PLAY_VIDEO")

    pyautogui.press("space")

    time.sleep(1)

    print("[SUCCESS] VIDEO_PLAYING")


def volume_up():

    print("\n[EXECUTING] VOLUME_UP")

    pyautogui.press(
        "volumeup"
    )

    time.sleep(1)

    print("[SUCCESS] VOLUME_UP")


def volume_down():

    print("\n[EXECUTING] VOLUME_DOWN")

    pyautogui.press(
        "volumedown"
    )

    time.sleep(1)

    print("[SUCCESS] VOLUME_DOWN")


def fullscreen():

    print("\n[EXECUTING] FULLSCREEN")

    pyautogui.press("f11")

    time.sleep(1)

    print("[SUCCESS] FULLSCREEN")


def exit_fullscreen():

    print("\n[EXECUTING] EXIT_FULLSCREEN")

    pyautogui.press("f11")

    time.sleep(1)

    print("[SUCCESS] EXIT_FULLSCREEN")


def close_video():

    print("\n[EXECUTING] CLOSE_VIDEO")

    pyautogui.hotkey(
        "alt",
        "f4"
    )

    print("[SUCCESS] CLOSE_VIDEO")