import pyautogui
import time


def left_click(x=None, y=None):

    print("\n[EXECUTING] LEFT_CLICK")

    pyautogui.click(
        x=x,
        y=y
    )

    time.sleep(1)

    print("[SUCCESS] LEFT_CLICK")


def right_click(x=None, y=None):

    print("\n[EXECUTING] RIGHT_CLICK")

    pyautogui.rightClick(
        x=x,
        y=y
    )

    time.sleep(1)

    print("[SUCCESS] RIGHT_CLICK")


def double_click(x=None, y=None):

    print("\n[EXECUTING] DOUBLE_CLICK")

    pyautogui.doubleClick(
        x=x,
        y=y
    )

    time.sleep(1)

    print("[SUCCESS] DOUBLE_CLICK")


def drag_and_drop(
    start_x,
    start_y,
    end_x,
    end_y
):

    print(
        "\n[EXECUTING] DRAG_AND_DROP"
    )

    pyautogui.moveTo(
        start_x,
        start_y
    )

    pyautogui.dragTo(
        end_x,
        end_y,
        duration=1
    )

    time.sleep(1)

    print(
        "[SUCCESS] DRAG_AND_DROP"
    )


def scroll_up(amount=500):

    print(
        "\n[EXECUTING] SCROLL_UP"
    )

    pyautogui.scroll(
        amount
    )

    time.sleep(1)

    print(
        "[SUCCESS] SCROLL_UP"
    )


def scroll_down(amount=500):

    print(
        "\n[EXECUTING] SCROLL_DOWN"
    )

    pyautogui.scroll(
        -amount
    )

    time.sleep(1)

    print(
        "[SUCCESS] SCROLL_DOWN"
    )


def get_mouse_position():

    position = pyautogui.position()

    print(
        f"\n[MOUSE_POSITION] {position}"
    )

    return position