from machine import Pin
import time

led_pin = Pin(20, Pin.OUT)
switch_pin = Pin(19, Pin.IN, pull=Pin.PULL_DOWN)
second_switch = Pin(18, Pin.IN, pull=Pin.PULL_DOWN)

while True:
    if switch_pin.value():
        led_pin.value(1)
    elif second_switch.value():
        led_pin.value(0)
    time.sleep(0.1)
