import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.connect("localhost", 1883, 60)

result = client.publish(
    "eeg/raw",
    "Hello from BCI Backend"
)

print("Message Published")
print(result)

client.disconnect() 