# app/domain_classifier.py

APPLICATION_DOMAIN = [
    "OPEN_NOTEPAD",
    "OPEN_CALCULATOR",
    "OPEN_EXPLORER",
    "OPEN_VSCODE",
    "OPEN_CALENDAR"
]

WINDOW_DOMAIN = [
    "OPEN_WINDOW",
    "CLOSE_WINDOW",
    "MINIMIZE_WINDOW",
    "MAXIMIZE_WINDOW",
    "RESTORE_WINDOW",
    "SWITCH_WINDOW"
]

KEYBOARD_DOMAIN = [
    "COPY",
    "PASTE",
    "SAVE",
    "UNDO",
    "REDO",
    "SELECT_ALL",
    "ALT_TAB"
]

MOUSE_DOMAIN = [
    "LEFT_CLICK",
    "RIGHT_CLICK",
    "DOUBLE_CLICK",
    "SCROLL_UP",
    "SCROLL_DOWN"
]


def classify_command(command):

    if command in APPLICATION_DOMAIN:
        return "APPLICATION_DOMAIN"

    if command in WINDOW_DOMAIN:
        return "WINDOW_DOMAIN"

    if command in KEYBOARD_DOMAIN:
        return "KEYBOARD_DOMAIN"

    if command in MOUSE_DOMAIN:
        return "MOUSE_DOMAIN"

    return "UNKNOWN_DOMAIN"