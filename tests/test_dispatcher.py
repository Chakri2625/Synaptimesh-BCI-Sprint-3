from app.dispatcher import dispatch_command

def test_invalid_command():

    result = dispatch_command("INVALID_COMMAND")

    assert result["status"] == "error"