import time
import paho.mqtt.client as mqtt

from app.logger import logger


client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)

client.connect(
    "localhost",
    1883,
    60
)

commands = [
    "OPEN_BROWSER",
    "OPEN_YOUTUBE",
    "PLAY_PAUSE",
    "VOLUME_UP",
    "VOLUME_DOWN",
    "SCROLL_UP",
    "SCROLL_DOWN",
    "OPEN_NOTEPAD",
    "CLOSE_NOTEPAD",
    "OPEN_CALCULATOR",
    "CLOSE_CALCULATOR",
    "CLOSE_BROWSER"
]

for command in commands:

    client.publish(
        "eeg/raw",
        command
    )

    logger.info(
        f"Published MQTT command: {command}"
    )

    print(
        f"Published: {command}"
    )

    time.sleep(2)

client.disconnect()