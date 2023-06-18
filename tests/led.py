from gpiozero import LED
from time import sleep

red = LED(21)
yellow = LED(20)

while True:
    red.on()
    yellow.off()
    sleep(1)
    red.off()
    yellow.on()
    sleep(1)