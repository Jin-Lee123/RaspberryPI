import serial

ObjSerial = serial.Serial('/dev/ttyACM0', 9600)

while 1:
	print (ObjSerial.readline())


