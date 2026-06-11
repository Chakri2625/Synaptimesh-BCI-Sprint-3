# app/command_router.py

from app.domain_classifier import classify_command

# Mapping domain -> module handler
DOMAIN_MODULE_MAP = {
    "APPLICATION_DOMAIN": "application_controller",
    "WINDOW_DOMAIN": "window_controller",
    "KEYBOARD_DOMAIN": "keyboard_controller",
    "MOUSE_DOMAIN": "mouse_controller"
}

def route_command(command, payload=None):
    """
    Determines which module handles the command based on domain classification.
    Returns module name as string.
    """
    domain = classify_command(command)

    module = DOMAIN_MODULE_MAP.get(domain, None)

    if not module:
        print(f"[ROUTER] Command '{command}' has UNKNOWN_DOMAIN")
        return None

    print(f"[ROUTER] Command '{command}' routed to '{module}'")
    return module