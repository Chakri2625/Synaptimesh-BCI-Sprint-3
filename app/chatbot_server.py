from flask import Flask
from flask import render_template
from flask import redirect

from app.dispatcher import dispatch_command
from app.final_integration import run_final_integration
from app.ai_assistant import open_ai_assistant

app = Flask(__name__)


@app.route("/")
def home():

    return render_template(
        "chatbot_dashboard.html"
    )


@app.route("/start_notepad")
def start_notepad():

    dispatch_command(
        "OPEN_NOTEPAD"
    )

    return redirect("/")


@app.route("/start_calculator")
def start_calculator():

    dispatch_command(
        "OPEN_CALCULATOR"
    )

    return redirect("/")


@app.route("/start_explorer")
def start_explorer():

    dispatch_command(
        "OPEN_EXPLORER"
    )

    return redirect("/")


@app.route("/start_vscode")
def start_vscode():

    dispatch_command(
        "OPEN_VSCODE"
    )

    return redirect("/")


@app.route("/start_calendar")
def start_calendar():

    dispatch_command(
        "OPEN_CALENDAR"
    )

    return redirect("/")


@app.route("/start_outlook")
def start_outlook():

    dispatch_command(
        "OPEN_OUTLOOK"
    )

    return redirect("/")


@app.route("/open_ai")
def open_ai():

    open_ai_assistant()

    return redirect("/")


@app.route("/start_final")
def start_final():

    run_final_integration()

    return redirect("/")


if __name__ == "__main__":

    app.run(
        debug=True
    )