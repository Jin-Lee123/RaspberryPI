from flask import Flask
import RPi.GPIO as GPIO
import signal

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

@app.route("/on")
def Test1():
	GPIO.output(Pin_LED, GPIO.HIGH)
	return "LED ON..."


@app.route("/off")
def Test2():
	GPIO.output(Pin_LED, GPIO.LOW)
	return "LED OFF..."

if __name__ == "__main__":
	app.run(host="0.0.0.0",  port=80 )

