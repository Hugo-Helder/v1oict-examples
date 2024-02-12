from machine import Pin
import time

gpio_pin = Pin(20, Pin.OUT)


def tatataa(pin, high_time, low_time):
    pin.value(1)
    time.sleep(high_time)
    pin.value(0)
    time.sleep(low_time)


while True:
    tatataa(gpio_pin, 0.2, 0.2)
    tatataa(gpio_pin, 0.2, 0.2)
    tatataa(gpio_pin, 0.2, 0.2)
    tatataa(gpio_pin, 1.0, 10.0)

