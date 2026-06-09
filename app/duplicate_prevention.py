last_command = None

def check_duplicate(command):
    global last_command
    if command == last_command:
        print(f"[REJECTED] Duplicate command detected: {command}")
        return False
    last_command = command
    print(f"[ACCEPTED] {command} executed")
    return True