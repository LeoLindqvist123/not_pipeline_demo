import rp2
import network
import json
import time

rp2.country("SE")

with open("edge_computing/wifi/wifi_cred.json") as file:
    credentials = json.load(file)

def connect_to_wifi(waiting_time=10):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(credentials["WIFI_SSID"], credentials["WIFI_PASSWORD"])

    while not wlan.isconnected():
        print("Connecting to WiFi...")
        time.sleep(1)

    print("Connected to WiFi!")
    print("Network config:", wlan.ifconfig())