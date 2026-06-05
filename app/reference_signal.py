# app/reference_signal.py

REFERENCE_SIGNALS = [

    {
        "signal_id": 1,
        "correlation_id": "BCI_001",
        "command": "OPEN_BROWSER",
        "confidence": 0.95,
        "target": "web"
    },

    {
        "signal_id": 2,
        "correlation_id": "BCI_002",
        "command": "OPEN_YOUTUBE",
        "confidence": 0.96,
        "target": "web"
    },

    # Pause Video
    {
        "signal_id": 3,
        "correlation_id": "BCI_003",
        "command": "PLAY_PAUSE",
        "confidence": 0.94,
        "target": "web"
    },

    # Play Video Again
    {
        "signal_id": 4,
        "correlation_id": "BCI_004",
        "command": "PLAY_PAUSE",
        "confidence": 0.95,
        "target": "web"
    },

    {
        "signal_id": 5,
        "correlation_id": "BCI_005",
        "command": "VOLUME_UP",
        "confidence": 0.91,
        "target": "web"
    },

    {
        "signal_id": 6,
        "correlation_id": "BCI_006",
        "command": "VOLUME_DOWN",
        "confidence": 0.92,
        "target": "web"
    },

    {
        "signal_id": 7,
        "correlation_id": "BCI_007",
        "command": "MUTE",
        "confidence": 0.93,
        "target": "web"
    },

    {
        "signal_id": 8,
        "correlation_id": "BCI_008",
        "command": "SCROLL_DOWN",
        "confidence": 0.91,
        "target": "web"
    },

    {
        "signal_id": 9,
        "correlation_id": "BCI_009",
        "command": "SCROLL_UP",
        "confidence": 0.92,
        "target": "web"
    },

    {
        "signal_id": 10,
        "correlation_id": "BCI_010",
        "command": "OPEN_NOTEPAD",
        "confidence": 0.93,
        "target": "desktop"
    },

    {
        "signal_id": 11,
        "correlation_id": "BCI_011",
        "command": "OPEN_CALCULATOR",
        "confidence": 0.95,
        "target": "desktop"
    },

    {
        "signal_id": 12,
        "correlation_id": "BCI_012",
        "command": "CLOSE_CALCULATOR",
        "confidence": 0.96,
        "target": "desktop"
    },

    {
        "signal_id": 13,
        "correlation_id": "BCI_013",
        "command": "CLOSE_NOTEPAD",
        "confidence": 0.94,
        "target": "desktop"
    },

    {
        "signal_id": 14,
        "correlation_id": "BCI_014",
        "command": "CLOSE_BROWSER",
        "confidence": 0.95,
        "target": "web"
    },

    # Low Confidence Rejection Demo
    {
        "signal_id": 15,
        "correlation_id": "BCI_015",
        "command": "OPEN_BROWSER",
        "confidence": 0.50,
        "target": "web"
    },

    {
        "signal_id": 16,
        "correlation_id": "BCI_016",
        "command": "OPEN_NOTEPAD",
        "confidence": 0.40,
        "target": "desktop"
    }
]