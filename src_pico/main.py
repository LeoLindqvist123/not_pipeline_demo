import time
from wifi import connect_to_wifi
from machine import Pin

led = Pin(15, Pin.OUT)


if connect_to_wifi():
    led.value(1)