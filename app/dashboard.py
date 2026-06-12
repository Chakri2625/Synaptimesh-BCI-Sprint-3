# app/dashboard.py

import json
import os

HISTORY_FILE = "data/automation_history.json"


def load_history():

    if not os.path.exists(
        HISTORY_FILE
    ):
        return []

    try:

        with open(
            HISTORY_FILE,
            "r"
        ) as f:

            return json.load(f)

    except json.JSONDecodeError:

        return []


def show_dashboard():

    history = load_history()

    total_commands = len(
        history
    )

    accepted = sum(

        1

        for c in history

        if c["status"] == "ACCEPTED"
    )

    rejected = sum(

        1

        for c in history

        if c["status"] == "REJECTED"
    )

    blocked = sum(

        1

        for c in history

        if c["status"] == "BLOCKED"
    )

    failed = sum(

        1

        for c in history

        if c["status"] == "FAILED"
    )

    success_rate = (

        accepted
        / total_commands
        * 100

    ) if total_commands else 0

    total_response_time = sum(

        c.get(
            "response_time",
            0
        )

        for c in history
    )

    average_response_time = (

        total_response_time
        / total_commands

    ) if total_commands else 0

    module_count = {}

    for c in history:

        cmd = c["command"]

        module_count[cmd] = (

            module_count.get(
                cmd,
                0
            )
            + 1
        )

    print()

    print("=" * 60)

    print(
        "DESKTOP AUTOMATION DASHBOARD"
    )

    print("=" * 60)

    print(
        f"Total Commands Processed : {total_commands}"
    )

    print(
        f"Successful Commands      : {accepted}"
    )

    print(
        f"Failed Commands          : {failed}"
    )

    print(
        f"Rejected Commands        : {rejected}"
    )

    print(
        f"Blocked Commands         : {blocked}"
    )

    print(
        f"Average Response Time    : {average_response_time:.2f} sec"
    )

    print(
        f"Success Rate             : {success_rate:.2f}%"
    )

    print("-" * 60)

    print(
        "Commands Per Application"
    )

    print("-" * 60)

    for module, count in module_count.items():

        print(
            f"{module:25s} : {count}"
        )

    print("=" * 60)

    print()