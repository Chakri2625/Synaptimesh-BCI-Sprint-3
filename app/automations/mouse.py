import pyautogui

pyautogui.FAILSAFE = True


def scroll_up():
    pyautogui.scroll(500)


def scroll_down():
    pyautogui.scroll(-500)


def mouse_left():
    pyautogui.moveRel(-100, 0)


def mouse_right():
    pyautogui.moveRel(100, 0)


def mouse_up():
    pyautogui.moveRel(0, -100)


def mouse_down():
    pyautogui.moveRel(0, 100)