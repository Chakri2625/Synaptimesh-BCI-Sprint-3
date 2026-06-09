from app.cooldown_manager import (
    check_cooldown
)

import time

check_cooldown(
    "OPEN_BROWSER"
)

check_cooldown(
    "OPEN_BROWSER"
)

time.sleep(6)

check_cooldown(
    "OPEN_BROWSER"
)