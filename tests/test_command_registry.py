# tests/test_command_registry.py

from app.command_registry import (
    COMMAND_REGISTRY
)

print()

print("=" * 50)

print(
    "COMMAND REGISTRY TEST"
)

print("=" * 50)

print()

for command in COMMAND_REGISTRY:

    print(command)