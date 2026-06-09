from app.execution_lock import (
    acquire_lock,
    release_lock
)

acquire_lock(
    "OPEN_NOTEPAD"
)

acquire_lock(
    "OPEN_NOTEPAD"
)

release_lock(
    "OPEN_NOTEPAD"
)

acquire_lock(
    "OPEN_NOTEPAD"
)