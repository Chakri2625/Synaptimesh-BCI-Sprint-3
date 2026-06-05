import os
import webbrowser


def open_browser():
    os.system("start msedge")


def close_browser():
    os.system("taskkill /F /IM msedge.exe")


def open_youtube():
    webbrowser.open(
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    )