from app.enhanced_logger import log_command
import time
import pyautogui
import webbrowser

CALENDAR_URL = "https://calendar.google.com"

EVENT_DATE = "2026-06-15"

EVENT_TITLE = "BCI Synaptimesh Sprint 5 Start"

EVENT_START = "10:00 AM"

EVENT_END = "11:00 AM"


def open_calendar():

    log_command(
        "[EXECUTING] OPEN_CALENDAR"
    )

    webbrowser.open(
        CALENDAR_URL
    )

    time.sleep(5)

    log_command(
        "[SUCCESS] CALENDAR_OPENED"
    )


def go_to_date(date_str):

    log_command(
        f"[EXECUTING] GO_TO_DATE: {date_str}"
    )

    pyautogui.press("g")

    time.sleep(2)

    pyautogui.write(
        date_str,
        interval=0.10
    )

    time.sleep(1)

    pyautogui.press("enter")

    time.sleep(5)

    log_command(
        f"[SUCCESS] DATE_SELECTED: {date_str}"
    )


def create_event(

    title=EVENT_TITLE,

    start_time=EVENT_START,

    end_time=EVENT_END

):

    log_command(
        f"[EXECUTING] CREATE_EVENT: {title}"
    )

    pyautogui.press("c")

    time.sleep(5)

    pyautogui.write(
        title,
        interval=0.08
    )

    time.sleep(2)

    pyautogui.press("tab")

    time.sleep(1)

    pyautogui.write(
        start_time,
        interval=0.10
    )

    time.sleep(2)

    pyautogui.press("tab")

    time.sleep(1)

    pyautogui.write(
        end_time,
        interval=0.10
    )

    time.sleep(2)

    pyautogui.press("enter")

    time.sleep(5)

    log_command(
        f"[SUCCESS] EVENT_CREATED: {title}"
    )


def close_calendar():

    log_command(
        "[EXECUTING] CLOSE_CALENDAR"
    )

    pyautogui.hotkey(
        "alt",
        "f4"
    )

    time.sleep(2)

    log_command(
        "[SUCCESS] CALENDAR_CLOSED"
    )


def run_calendar_workflow():

    log_command(
        "=== STARTING CALENDAR WORKFLOW ==="
    )

    open_calendar()

    time.sleep(2)

    go_to_date(
        EVENT_DATE
    )

    time.sleep(2)

    create_event()

    time.sleep(3)

    close_calendar()

    log_command(
        "=== CALENDAR WORKFLOW COMPLETE ==="
    )