#master is ESP32 sending RP Pico 2 binary time delay

from machine import UART, Pin
from time import sleep

uart = UART(2, 9600, tx=Pin(23, Pin.OUT))
led = Pin(2, Pin.OUT)
ledDelay = b'001'

while True:
    uart.write(ledDelay)
    sleep(int(ledDelay,2))
    led.on()
    sleep(int(ledDelay,2))
    led.off()
