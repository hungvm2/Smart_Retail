import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

RELAY = 18
GPIO.setup(RELAY,GPIO.OUT)

GPIO.output(RELAY, False)


