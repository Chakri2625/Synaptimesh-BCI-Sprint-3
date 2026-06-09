from app.session_tracker import (
    track_command,
    print_session_report
)

track_command(
    command="OPEN_NOTEPAD",
    status="SUCCESS",
    module="applications",
    response_time=0.15
)

track_command(
    command="OPEN_BROWSER",
    status="FAILED",
    module="browser",
    response_time=0.30,
    failure_reason="Browser Not Found"
)

print_session_report()