import os
import time
import random
import pyautogui


def run_calculator_workflow():

    open_calculator()

    addition()

    subtraction()

    multiplication()

    division()

    clear_calculator()

    close_calculator()


def open_calculator():

    print("\n[EXECUTING] OPEN_CALCULATOR")

    os.system("start calc")

    time.sleep(3)

    print("[SUCCESS] OPEN_CALCULATOR")


def addition():

    a = random.randint(10, 99)
    b = random.randint(10, 99)

    print("\n[EXECUTING] ADDITION")
    print(f"Expression: {a} + {b}")

    pyautogui.write(str(a))
    pyautogui.press("+")

    time.sleep(1)

    pyautogui.write(str(b))
    pyautogui.press("enter")

    time.sleep(1)

    print(
        f"[SUCCESS] RESULT = {a + b}"
    )


def subtraction():

    a = random.randint(100, 999)
    b = random.randint(10, 99)

    print("\n[EXECUTING] SUBTRACTION")
    print(f"Expression: {a} - {b}")

    pyautogui.write(str(a))
    pyautogui.press("-")

    time.sleep(1)

    pyautogui.write(str(b))
    pyautogui.press("enter")

    time.sleep(1)

    print(
        f"[SUCCESS] RESULT = {a - b}"
    )


def multiplication():

    a = random.randint(10, 50)
    b = random.randint(2, 10)

    print("\n[EXECUTING] MULTIPLICATION")
    print(f"Expression: {a} * {b}")

    pyautogui.write(str(a))
    pyautogui.press("*")

    time.sleep(1)

    pyautogui.write(str(b))
    pyautogui.press("enter")

    time.sleep(1)

    print(
        f"[SUCCESS] RESULT = {a * b}"
    )


def division():

    divisor = random.randint(2, 10)

    result = random.randint(
        10,
        50
    )

    dividend = divisor * result

    print("\n[EXECUTING] DIVISION")

    print(
        f"Expression: {dividend} / {divisor}"
    )

    pyautogui.write(str(dividend))
    pyautogui.press("/")

    time.sleep(1)

    pyautogui.write(str(divisor))
    pyautogui.press("enter")

    time.sleep(1)

    print(
        f"[SUCCESS] RESULT = {result}"
    )


def clear_calculator():

    print("\n[EXECUTING] CLEAR")

    pyautogui.press("esc")

    time.sleep(1)

    print("[SUCCESS] CLEAR")


def close_calculator():

    print("\n[EXECUTING] CLOSE_CALCULATOR")

    pyautogui.hotkey(
        "alt",
        "f4"
    )

    print("[SUCCESS] CLOSE_CALCULATOR")