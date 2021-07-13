#-*- coding: utf-8 -*-

#필요한 모듈을 불러옵니다.
import RPi.GPIO as GPIO
import time

#사용할 GPIO핀의 번호를 선정합니다.(BCM모드)
LED=3                #GPIO 3

#불필요한 warnig 제거
GPIO.setwarnings(False)

#GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)

#LED 핀의 IN/OUT 설정
GPIO.setup(LED, GPIO.OUT)

input("Enter...")

GPIO.cleanup()
