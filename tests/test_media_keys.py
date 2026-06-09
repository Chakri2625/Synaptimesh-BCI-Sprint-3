import pyautogui
import time

print(
    "[TEST] PLAY / PAUSE"
)

time.sleep(3)

pyautogui.press(
    "playpause"
)

time.sleep(3)

print(
    "[TEST] VOLUME UP"
)

pyautogui.press(
    "volumeup"
)

time.sleep(2)

print(
    "[TEST] VOLUME DOWN"
)

pyautogui.press(
    "volumedown"
)

time.sleep(2)

print(
    "[TEST] NEXT TRACK"
)

pyautogui.press(
    "nexttrack"
)

time.sleep(2)

print(
    "[TEST] PREVIOUS TRACK"
)

pyautogui.press(
    "prevtrack"
)

print(
    "\nDONE"
)