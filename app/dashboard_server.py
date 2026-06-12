# app/dashboard_server.py

from flask import Flask
from flask import render_template

import json
import os

app = Flask(__name__)

HISTORY_FILE = "data/automation_history.json"


@app.route("/")
def dashboard():

    history = []

    if os.path.exists(
        HISTORY_FILE
    ):

        with open(
            HISTORY_FILE,
            "r"
        ) as f:

            history = json.load(f)

    total = len(
        history
    )

    accepted = len(

        [
            h

            for h in history

            if h["status"] == "ACCEPTED"
        ]
    )

    rejected = len(

        [
            h

            for h in history

            if h["status"] == "REJECTED"
        ]
    )

    blocked = len(

        [
            h

            for h in history

            if h["status"] == "BLOCKED"
        ]
    )

    failed = len(

        [
            h

            for h in history

            if h["status"] == "FAILED"
        ]
    )

    total_response_time = sum(

        h.get(
            "response_time",
            0
        )

        for h in history
    )

    average_response_time = (

        total_response_time
        / total

    ) if total else 0

    success_rate = (

        accepted
        / total
        * 100

    ) if total else 0

    return render_template(

        "dashboard.html",

        history=history,

        total=total,

        accepted=accepted,

        rejected=rejected,

        blocked=blocked,

        failed=failed,

        average_response_time=round(
            average_response_time,
            2
        ),

        success_rate=round(
            success_rate,
            2
        )
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )