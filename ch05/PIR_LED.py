#!/usr/bin/env python
#-*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import time

PIR=17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
	while 1:
		State = GPIO.input(PIR)
		print("상태:%d" %State)
		time.sleep(0.5)
		
except KeyboardInterrupt:
	pass

GPIO.cleanup()

