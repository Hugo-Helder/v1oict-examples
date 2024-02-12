from machine import ADC, Pin
import time

led = Pin(20, Pin.OUT)
adc = ADC(Pin(26))


def pulse(pin, high_time, low_time):
    """
    Geef een puls op de pin:
    Maak de pin pin_nr hoog, wacht high_time,
    maak de pin laag, en wacht nog low_time
    """
    pin.value(1)
    time.sleep(high_time)
    pin.value(0)
    time.sleep(low_time)


while True:
    # naar rechts is dicht
    adc_value = adc.read_u16()
    pulse_value = (adc_value + 1) / 65535
    pulse(led, pulse_value, pulse_value)
