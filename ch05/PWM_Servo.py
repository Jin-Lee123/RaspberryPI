#!/usr/bin/env python
#-*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import time

SERVO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)
servo = GPIO.PWM(SERVO_PIN, 50)
servo.start(0)

try:
	while True:
		servo.ChangeDutyCycle(7.5)
		time.sleep(1)
		servo.ChangeDutyCycle(12.5)
		time.sleep(1)
		servo.ChangeDutyCycle(2.5)
		time.sleep(1)
except KeyboardInterrupt:
	sevo.stop()
	GPIO.cleanup()
