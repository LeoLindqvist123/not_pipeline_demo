import paho.mqtt.client as mqtt
import json

def on_message(client, userdata, message):
    # needs to decode because original msg is encoded after publshing
    payload = message.payload.decode()
    data = json.loads(payload)

    temperature = float(data["temperature"])
    humidity = float(data["humidity"])
    # code for storing data in to timescaledb
    print(temperature, humidity)



if __name__ == "__main__":
    client = mqtt.Client()
    client.connect("localhost", 1883)
    client.subscribe("home/pico/dht11")
    client.on_message = on_message
    client.loop_forever()