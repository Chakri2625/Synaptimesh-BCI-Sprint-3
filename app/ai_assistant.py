import webbrowser

from app.enhanced_logger import log_command


def open_ai_assistant():

    log_command(
        "[EXECUTING] OPEN_AI_ASSISTANT"
    )

    webbrowser.open(
        "https://chat.openai.com"
    )

    log_command(
        "[SUCCESS] AI_ASSISTANT_OPENED"
    )