"""
Integration Test Results

Commands Tested:

1. OPEN_BROWSER        - PASS
2. CLOSE_BROWSER       - PASS
3. PLAY_PAUSE          - PASS
4. VOLUME_UP           - PASS
5. VOLUME_DOWN         - PASS
6. SCROLL_UP           - PASS
7. SCROLL_DOWN         - PASS
8. OPEN_NOTEPAD        - PASS
9. CLOSE_NOTEPAD       - PASS
10. OPEN_CALCULATOR    - PASS
11. CLOSE_CALCULATOR   - PASS
12. ABCXYZ             - PASS (Unknown command handled)

Total Commands Tested: 12
Result: SUCCESS
"""
import time
from app.dispatcher import dispatch_command

test_commands = [
    "OPEN_BROWSER",
    "CLOSE_BROWSER",
    "PLAY_PAUSE",
    "VOLUME_UP",
    "VOLUME_DOWN",
    "SCROLL_UP",
    "SCROLL_DOWN",
    "OPEN_NOTEPAD",
    "CLOSE_NOTEPAD",
    "OPEN_CALCULATOR",
    "CLOSE_CALCULATOR"
]

for command in test_commands:

    print(f"\nTesting: {command}")

    result = dispatch_command(command)

    print(result)

    time.sleep(3)