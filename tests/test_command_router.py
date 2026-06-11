# tests/test_command_router.py

from app.command_router import route_command

print()
print("="*50)
print("COMMAND ROUTER TEST")
print("="*50)
print()

commands = [
    "OPEN_NOTEPAD",
    "OPEN_VSCODE",
    "COPY",
    "LEFT_CLICK",
    "MAXIMIZE_WINDOW",
    "INVALID_COMMAND"
]

for cmd in commands:
    module = route_command(cmd)
    print(f"{cmd} --> Routed to: {module}")