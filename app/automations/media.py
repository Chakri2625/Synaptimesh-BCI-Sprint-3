import pyautogui

pyautogui.FAILSAFE = True


def play_pause():
    pyautogui.press("playpause")


def volume_up():
    pyautogui.press("volumeup")


def volume_down():
    pyautogui.press("volumedown")


def mute():
    pyautogui.press("volumemute")