# app/command_registry.py

from app.notepad_controller import run_notepad_workflow
from app.calculator_controller import run_calculator_workflow
from app.file_explorer_controller import run_explorer_workflow
from app.vscode_controller import run_vscode_workflow
from app.calendar_controller import run_calendar_workflow
from app.outlook_controller import run_outlook_workflow

from app.enhanced_logger import log_command


COMMAND_REGISTRY = {

    "OPEN_NOTEPAD":
    lambda: (
        log_command(
            "Executing OPEN_NOTEPAD"
        ),
        run_notepad_workflow()
    ),

    "OPEN_CALCULATOR":
    lambda: (
        log_command(
            "Executing OPEN_CALCULATOR"
        ),
        run_calculator_workflow()
    ),

    "OPEN_EXPLORER":
    lambda: (
        log_command(
            "Executing OPEN_EXPLORER"
        ),
        run_explorer_workflow()
    ),

    "OPEN_VSCODE":
    lambda: (
        log_command(
            "Executing OPEN_VSCODE"
        ),
        run_vscode_workflow()
    ),

    "OPEN_CALENDAR":
    lambda: (
        log_command(
            "Executing OPEN_CALENDAR"
        ),
        run_calendar_workflow()
    ),

    "OPEN_OUTLOOK":
    lambda: (
        log_command(
            "Executing OPEN_OUTLOOK"
        ),
        run_outlook_workflow()
    )
}