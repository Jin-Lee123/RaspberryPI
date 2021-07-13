#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time as TT

SW=4
LED=26

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED, GPIO.OUT)

try:
	while 1:
		if GPIO.input(SW) == GPIO.HIGH:
			GPIO.output(LED, GPIO.HIGH)
			TT.sleep(1)
			GPIO.output(LED, GPIO.LOW)
		TT.sleep(0.1)
except KeyboardInterrupt:	
	pass
finally:
	GPIO.cleanup()
	print("\b\b종료합니다...")
