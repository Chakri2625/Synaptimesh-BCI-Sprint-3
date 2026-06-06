import paho.mqtt.client as mqtt

from app.dispatcher import dispatch_command
from app.logger import logger


def on_connect(client, userdata, flags, reason_code, properties):

    logger.info(
        f"MQTT Connected with result code: {reason_code}"
    )

    client.subscribe("eeg/raw")

    logger.info(
        "Subscribed to topic: eeg/raw"
    )


def on_message(client, userdata, msg):

    command = msg.payload.decode()

    logger.info(
        f"Received MQTT message on {msg.topic}: {command}"
    )

    result = dispatch_command(command)

    logger.info(
        f"Dispatch Result: {result}"
    )


client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)

client.on_connect = on_connect
client.on_message = on_message

logger.info(
    "Starting MQTT Subscriber"
)

client.connect(
    "localhost",
    1883,
    60
)

try:

    client.loop_forever()

except KeyboardInterrupt:

    logger.info(
        "MQTT Subscriber Stopped"
    )

    client.disconnect()