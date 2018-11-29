from gpiozero import LED
from gpiozero import Button
from time import sleep

relay = LED(21)


while True:
    output = open("face.txt","r+")
    line1 = output.readline()
    if line1 == "1":
      relay.off()
      print("value 1 ")
    else:
      relay.on()
      print("value 0 ")
