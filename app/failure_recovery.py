# app/failure_recovery.py

def handle_unknown_command(command):
    print(f"[FAILURE] Unknown command received: {command}")
    return {"status": "error", "reason": "Unknown Command"}

def handle_invalid_payload(payload):
    print(f"[FAILURE] Invalid payload received: {payload}")
    return {"status": "error", "reason": "Invalid Payload"}

def handle_unknown_domain(command):
    print(f"[FAILURE] Command has unknown domain: {command}")
    return {"status": "error", "reason": "Unknown Domain"}

def handle_controller_failure(command, exception):
    print(f"[FAILURE] Controller failed for {command}: {exception}")
    return {"status": "error", "reason": str(exception)}

def handle_execution_failure(command, exception):
    print(f"[FAILURE] Execution failed for {command}: {exception}")
    return {"status": "error", "reason": str(exception)}