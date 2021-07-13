#!/usr/bin/env python
#-*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import time

def button_callback(channel):
	print("버튼 눌림!!")

Button=15

GPIO.setmode(GPIO.BCM)
GPIO.setup(Button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(Button, GPIO.RISING, callback=button_callback, bouncetime=300)
#GPIO.add_event_detect(Button, GPIO.FALLING, callback=button_callback, bouncetime=300)

try:
	while 1:
		time.sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()
