import os
import time
import pyautogui


def run_browser_workflow():

    open_browser()

    search_google(
        "Brain Computer Interface"
    )

    search_google(
        "Python Automation"
    )

    search_google(
        "BCI Command Execution"
    )

    refresh_page()

    close_browser()


def open_browser():

    print("\n[EXECUTING] OPEN_BROWSER")

    os.system("start msedge")

    time.sleep(4)

    print("[SUCCESS] OPEN_BROWSER")


def search_google(query):

    print(
        f"\n[EXECUTING] SEARCH: {query}"
    )

    pyautogui.hotkey(
        "ctrl",
        "l"
    )

    time.sleep(1)

    pyautogui.write(
        f"https://www.google.com/search?q={query}"
    )

    pyautogui.press(
        "enter"
    )

    time.sleep(4)

    print(
        f"[SUCCESS] SEARCH COMPLETED: {query}"
    )


def refresh_page():

    print(
        "\n[EXECUTING] REFRESH_PAGE"
    )

    pyautogui.press(
        "f5"
    )

    time.sleep(3)

    print(
        "[SUCCESS] PAGE_REFRESHED"
    )


def close_browser():

    print(
        "\n[EXECUTING] CLOSE_BROWSER"
    )

    pyautogui.hotkey(
        "alt",
        "f4"
    )

    time.sleep(2)

    print(
        "[SUCCESS] CLOSE_BROWSER"
    )