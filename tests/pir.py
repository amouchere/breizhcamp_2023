from gpiozero import MotionSensor
from time import sleep

pir = MotionSensor(4)

i = 0
while True:
    pir.wait_for_motion()
    print("Motion detected!",  i)
    sleep(1)
    i +=1