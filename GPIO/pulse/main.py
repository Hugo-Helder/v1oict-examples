from machine import Pin
import time

gpio_pin = Pin(20, Pin.OUT)


def pulse(pin, high_time, low_time):
    pin.value(1)
    time.sleep(high_time)
    pin.value(0)
    time.sleep(low_time)


while True:
    pulse(gpio_pin, 1, 1)
