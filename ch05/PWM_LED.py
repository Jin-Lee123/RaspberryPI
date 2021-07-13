#!/usr/bin/env python
#-*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import time

LED=18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
pwmObj=GPIO.PWM(18, 50) #PWM객체생성(GPIO:18,주파수:50Hz)
pwmObj.start(0)

try:
	while 1:
		for dc in range(0,101,5):
			pwmObj.ChangeDutyCycle(dc)
			time.sleep(0.1)
		for dc in range(100,-1,-5):
			pwmObj.ChangeDutyCycle(dc)
			time.sleep(0.1)
		time.sleep(1)
except KeyboardInterrupt:
	pass

pwmObj.stop()
GPIO.cleanup()
