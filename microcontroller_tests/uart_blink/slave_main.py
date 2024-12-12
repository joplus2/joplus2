# slave is RP Pico 2 trying to read UART

from machine import UART, Pin
from time import sleep

uart = UART(1, 9600, rx=Pin(5, Pin.IN))
led = Pin(25, Pin.OUT)

while True:
    try:
        time = int(uart.read(),2)
    except:
        pass
    else:
        led.on()
        sleep(time)
        led.off()
