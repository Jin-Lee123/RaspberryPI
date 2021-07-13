#!/usr/bin/env python
#-*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import time

LED     = 26
Button1 = 17
Button2 = 27
Button3 = 16
Duty    = 0
PObj    = 0

def button_callback1(channel):
	global Duty
	Duty = 60
	PObj.ChangeDutyCycle(Duty)
	print("2단")
def button_callback2(channel):
	global Duty
	Duty = 100
	PObj.ChangeDutyCycle(Duty)
	print("3단")
def button_callback3(channel):
	global Duty
	if Duty == False:
		Duty = 25
		PObj.ChangeDutyCycle(Duty)
		print("작동 1단")
	else:
		Duty = 0
		PObj.ChangeDutyCycle(Duty)
		print("꺼짐")

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(Button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(Button1, GPIO.RISING, callback=button_callback1, bouncetime=600)
GPIO.add_event_detect(Button2, GPIO.RISING, callback=button_callback2, bouncetime=600)
GPIO.add_event_detect(Button3, GPIO.RISING, callback=button_callback3, bouncetime=600)

PObj = GPIO.PWM(LED, 50)
PObj.start(Duty)

try:
	while 1:
		time.sleep(0.1)
except KeyboardInterrupt:
	pass

PObj.stop()
GPIO.cleanup()
