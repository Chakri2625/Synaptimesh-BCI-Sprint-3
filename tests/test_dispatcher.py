from app.dispatcher import dispatch_command, dispatch

def test_invalid_command():
    result = dispatch_command("INVALID_COMMAND")
    assert result["status"] == "error"

# Sample payload tests
dispatch({
    "command": "OPEN_NOTEPAD",
    "confidence": 0.95
})

dispatch({
    "command": "OPEN_BROWSER",
    "confidence": 0.45
})