from flask import Flask
from flask import request
from flask import render_template
import RPi.GPIO as GPIO
import signal
import time
import serial

Pin_LED = 23
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Pin_LED, GPIO.OUT, initial=GPIO.LOW)
ObjSerial = serial.Serial('/dev/ttyACM0', 9600)


def Terminate(n, p):
	GPIO.cleanup()
	print("웹 서비스를 종료합니다...")
	exit()

signal.signal(signal.SIGINT, Terminate)

app = Flask(__name__)

@app.route("/")
def Start():
	return render_template("index.html")

@app.route("/led/on1")
def led_on1():
	try:
		ObjSerial.write('1'.encode())
		return "ok"
	except:
		return "FAIL"

@app.route("/led/on2")
def led_on2():
	try:
		ObjSerial.write('2'.encode())
		return "ok"
	except:
		return "FAIL"

@app.route("/led/on3")
def led_on3():
    try:
        ObjSerial.write('3'.encode())
        return "ok"
    except:
        return "FAIL"

GPIO.setup(26 ,GPIO.OUT)
p = GPIO.PWM(26 ,100)
Frq =[ 262, 294, 330, 349, 440, 493, 523 ]

@app.route("/led/buz")
def buz():
	try:
		ObjSerial.write('4'.encode())
		for i in range(10):
			p.start(10)
			for fr in Frq:
				p.ChangeFrequency(fr)
				time.sleep(0.1)
		p.stop()
		return "ok"
	except:
		return "FAIL"

@app.route("/led/Temp")
def Temp():
	try:
		ObjSerial.write('5'.encode())
		temp=ObjSerial.readline().decode()
		return temp
	except:
		return "FAIL"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
