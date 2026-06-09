import time

session_log = []


def track_command(
    command,
    status,
    module,
    response_time,
    failure_reason=None
):

    session_log.append({

        "command": command,

        "execution_time":
        time.strftime("%H:%M:%S"),

        "status": status,

        "module": module,

        "response_time":
        response_time,

        "failure_reason":
        failure_reason

    })


def print_session_report():

    print()

    print(
        "=" * 40
    )

    print(
        "SESSION REPORT"
    )

    print(
        "=" * 40
    )

    for entry in session_log:

        print(
            f"Command      : {entry['command']}"
        )

        print(
            f"Status       : {entry['status']}"
        )

        print(
            f"Module       : {entry['module']}"
        )

        print(
            f"Response Time: {entry['response_time']} sec"
        )

        if entry["failure_reason"]:

            print(
                f"Failure      : {entry['failure_reason']}"
            )

        print(
            "-" * 40
        )