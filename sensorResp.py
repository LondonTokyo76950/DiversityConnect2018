import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.IN)

while True:
    time.sleep(0.25)
    if GPIO.input(8):
        print("Pin 8 is HIGH")
    else:
        print("Pin 8 is LOW")
