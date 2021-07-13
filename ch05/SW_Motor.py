#!/usr/bin/env python
#-*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import time

SW=17
Pan=26

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Pan, GPIO.OUT)
GPIO.output(Pan , GPIO.LOW)

try:
	while 1:
		State = GPIO.input(SW)
		print("기울기 상태:%d" %State)
		time.sleep(0.5)
		
		if State  == 1 :
			GPIO.output(Pan, GPIO.HIGH)
		time.slee(0.5)
except KeyboardInterrupt:
	pass

GPIO.cleanup()

