#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.IN)

tripCounter = 0

while True:
    time.sleep(0.015)
    if GPIO.input(8):
        print("Pin 8 is HIGH")
        if tripCounter == 0 or tripCounter == 5 or tripCounter == 10:
            print("Alert!")
        elif tripCounter >= 15:
            print("Error!")
        print("Taking Photo")
        subprocess.call("./takePhoto.sh", shell=True)
        tripCounter += 1
        time.sleep(1)
    else:
        tripCounter = 0
        print("Pin 8 is LOW")
