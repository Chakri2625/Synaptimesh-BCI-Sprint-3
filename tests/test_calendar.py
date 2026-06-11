from app.calendar_controller import run_calendar_workflow

def test_create_event():
    """
    Test the full Google Calendar workflow.
    """
    run_calendar_workflow()
    print("[TEST] Calendar workflow test executed successfully.")

if __name__ == "__main__":
    test_create_event()