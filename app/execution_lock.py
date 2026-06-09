execution_lock = {}


def acquire_lock(command):

    if execution_lock.get(command):

        print(
            f"[BLOCKED] {command} already running"
        )

        return False

    execution_lock[command] = True

    print(
        f"[LOCK ACQUIRED] {command}"
    )

    return True


def release_lock(command):

    execution_lock[command] = False

    print(
        f"[LOCK RELEASED] {command}"
    )