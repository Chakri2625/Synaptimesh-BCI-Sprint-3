from flask import Flask, render_template
import json
import os

app = Flask(__name__)

HISTORY_FILE = "data/automation_history.json"


@app.route("/")
def dashboard():

    history = []

    if os.path.exists(HISTORY_FILE):

        with open(HISTORY_FILE, "r") as f:

            history = json.load(f)

    total = len(history)

    accepted = len(
        [
            h for h in history
            if h["status"] == "ACCEPTED"
        ]
    )

    rejected = len(
        [
            h for h in history
            if h["status"] == "REJECTED"
        ]
    )

    blocked = len(
        [
            h for h in history
            if h["status"] == "BLOCKED"
        ]
    )

    success_rate = 0

    if total:

        success_rate = round(
            accepted / total * 100,
            2
        )

    return render_template(
        "dashboard.html",
        history=history,
        total=total,
        accepted=accepted,
        rejected=rejected,
        blocked=blocked,
        success_rate=success_rate
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )