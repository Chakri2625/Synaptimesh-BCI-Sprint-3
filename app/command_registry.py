from app.automations.browser import (
    open_browser,
    close_browser,
    open_youtube
)

from app.automations.applications import (
    open_notepad,
    close_notepad,
    open_calculator,
    close_calculator
)

from app.automations.mouse import (
    scroll_up,
    scroll_down,
    mouse_left,
    mouse_right,
    mouse_up,
    mouse_down
)

from app.automations.media import (
    play_pause,
    volume_up,
    volume_down,
    mute
)


COMMAND_REGISTRY = {

    # Browser / Web
    "OPEN_BROWSER": open_browser,
    "CLOSE_BROWSER": close_browser,
    "OPEN_YOUTUBE": open_youtube,

    # Applications
    "OPEN_NOTEPAD": open_notepad,
    "CLOSE_NOTEPAD": close_notepad,
    "OPEN_CALCULATOR": open_calculator,
    "CLOSE_CALCULATOR": close_calculator,

    # Media
    "PLAY_PAUSE": play_pause,
    "VOLUME_UP": volume_up,
    "VOLUME_DOWN": volume_down,
    "MUTE": mute,

    # Mouse
    "MOUSE_LEFT": mouse_left,
    "MOUSE_RIGHT": mouse_right,
    "MOUSE_UP": mouse_up,
    "MOUSE_DOWN": mouse_down,

    # Scroll
    "SCROLL_UP": scroll_up,
    "SCROLL_DOWN": scroll_down,

    # Extra
    "ENTER": None,
    "ESCAPE": None,
    "SPACE": None
}