#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

LED=26 
LED2=16
BTN=15
Toggle=GPIO.LOW

def Button(channel):
	global Toggle
	if Toggle==GPIO.LOW:
		Toggle=GPIO.HIGH
	else:
		Toggle=GPIO.LOW
	GPIO.output(LED2, Toggle)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(BTN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(BTN, GPIO.RISING, callback=Button, bouncetime=300)

try:
	while 1:
		GPIO.output(LED, 1)
		time.sleep(0.2)
		GPIO.output(LED, 0)
		time.sleep(0.2)
except KeyboardInterrupt:
	pass
GPIO.cleanup()
