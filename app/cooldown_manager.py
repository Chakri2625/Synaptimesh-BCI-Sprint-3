import time

last_execution = {}

COOLDOWN_SECONDS = 5


def check_cooldown(command):

    current_time = time.time()

    if command in last_execution:

        elapsed = current_time - last_execution[command]

        if elapsed < COOLDOWN_SECONDS:

            print(
                f"[BLOCKED] {command} is in cooldown"
            )

            return False

    last_execution[command] = current_time

    print(
        f"[EXECUTED] {command}"
    )

    return True