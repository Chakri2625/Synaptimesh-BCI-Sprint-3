from app.notepad_controller import run_notepad_workflow
from app.calculator_controller import run_calculator_workflow
from app.browser_controller import run_browser_workflow
from app.media_controller import run_media_workflow
from app.file_explorer_controller import run_explorer_workflow
from app.automations.mouse import (
    mouse_left,
    mouse_right,
    mouse_up,
    mouse_down,
    scroll_up,
    scroll_down
)

COMMAND_REGISTRY = {
    # Applications
    "OPEN_NOTEPAD": run_notepad_workflow,
    "OPEN_CALCULATOR": run_calculator_workflow,
    "OPEN_BROWSER": run_browser_workflow,
    "OPEN_MEDIA": run_media_workflow,
    "OPEN_EXPLORER": run_explorer_workflow,

    # Mouse
    "MOUSE_LEFT": mouse_left,
    "MOUSE_RIGHT": mouse_right,
    "MOUSE_UP": mouse_up,
    "MOUSE_DOWN": mouse_down,

    # Scroll
    "SCROLL_UP": scroll_up,
    "SCROLL_DOWN": scroll_down,

    # Extra keys
    "ENTER": None,
    "ESCAPE": None,
    "SPACE": None
}