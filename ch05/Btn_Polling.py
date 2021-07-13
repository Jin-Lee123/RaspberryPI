#-*- coding: utf-8 -*-

#필요한 라이브러리를 불러옵니다.
import RPi.GPIO as GPIO
import time

#사용할 GPIO핀의 번호를 선정합니다.
button_pin=4

#GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)
#버튼 핀의 입력설정, PULL DOWN 설정
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
	while 1:  #무한반복
		if GPIO.input(button_pin) == GPIO.HIGH:
			print("버튼눌림")
		time.sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()
	print("")	
	exit()

