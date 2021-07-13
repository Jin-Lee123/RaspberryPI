#!/usr/bin/env python
#-*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#GPIO.setup(000, GPIO.OUT)
#GPIO.setup(000, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.cleanup()
