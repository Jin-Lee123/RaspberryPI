from flask import Flask
import RPi.GPIO as GPIO
import signal
import time

Pin_LED=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(Pin_LED, GPIO.OUT, initial=GPIO.LOW)

def Terminate(n, p):
	GPIO.cleanup()
	print("웹 서비스를 종료합니다.")
	exit()

signal.signal(signal.SIGINT, Terminate)

app = Flask(__name__)

@app.route("/")
def Start():
	return "여기는LED TEST Page입니다..."

@app.route("/led/<Param>")
def Test1(Param):
	if Param=="on":
		GPIO.output(Pin_LED, GPIO.HIGH)
		return "LED ON..."
	elif Param=="blink":
		for i in range(10):
			GPIO.output(Pin_LED, 1)
			time.sleep(1)
			GPIO.output(Pin_LED, 0)
			time.sleep(1)
		return "LED 10번 깜빡..."
	else :
		GPIO.output(Pin_LED, GPIO.LOW)
		return "LED OFF..."	

if __name__ == "__main__":
	app.run(host="0.0.0.0",  port=80 )

