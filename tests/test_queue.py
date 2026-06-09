from app.command_queue import (
    add_command,
    process_queue
)

add_command(
    "OPEN_NOTEPAD"
)

add_command(
    "OPEN_BROWSER"
)

add_command(
    "OPEN_CALCULATOR"
)

process_queue()