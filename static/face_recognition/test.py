import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(14, GPIO.OUT)

while 1 :
 
    GPIO.output(14, 1)
    time.sleep(2)
    GPIO.output(14, 0)
    time.sleep(2)
