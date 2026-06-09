from app.dispatcher import (
    dispatch
)

commands = [

    {
        "command":
        "OPEN_NOTEPAD",

        "confidence":
        0.95
    },

    {
        "command":
        "OPEN_CALCULATOR",

        "confidence":
        0.92
    },

    {
        "command":
        "OPEN_BROWSER",

        "confidence":
        0.91
    },

    {
        "command":
        "OPEN_MEDIA",

        "confidence":
        0.94
    },

    {
        "command":
        "OPEN_EXPLORER",

        "confidence":
        0.93
    }
]

for command in commands:

    dispatch(
        command
    )