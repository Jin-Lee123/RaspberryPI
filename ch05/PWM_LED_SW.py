#!/usr/bin/env python
#-*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import time

LED     = 26
Button1 = 17
Button2 = 27
Duty    = 0
PObj    = 0

def button_callback1(channel):
	global Duty
	Duty = Duty + 10
	if Duty > 100:
		Duty = 100
	PObj.ChangeDutyCycle(Duty)
	print("증가")
def button_callback2(channel):
	global Duty
	Duty = Duty - 10
	if Duty < 0:
		Duty = 0
	PObj.ChangeDutyCycle(Duty)
	print("감소")


GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(Button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(Button1, GPIO.RISING, callback=button_callback1, bouncetime=300)
GPIO.add_event_detect(Button2, GPIO.RISING, callback=button_callback2, bouncetime=300)

PObj = GPIO.PWM(LED, 50)
PObj.start(Duty)

try:
	while 1:
		time.sleep(0.1)
except KeyboardInterrupt:
	pass

PObj.stop()
GPIO.cleanup()
