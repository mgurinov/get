#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)

ldr = 6
GPIO.setup(ldr, GPIO.IN)

while True:
    GPIO.output(led, GPIO.input(ldr))
