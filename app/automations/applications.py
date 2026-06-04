import subprocess


def open_notepad():
    subprocess.Popen("notepad.exe")


def close_notepad():
    subprocess.run(
        ["taskkill", "/F", "/IM", "notepad.exe"],
        capture_output=True,
        text=True
    )


def open_calculator():
    subprocess.Popen("calc.exe")


def close_calculator():
    subprocess.run(
        ["taskkill", "/F", "/IM", "CalculatorApp.exe"],
        capture_output=True,
        text=True
    )