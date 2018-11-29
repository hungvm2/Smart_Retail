from gpiozero import LED
from gpiozero import Button
from time import sleep

relay = LED(21)
sensor = Button(25)

while True:     
      relay.on()
      sleep(2)
      relay.off()
      sleep(2)
