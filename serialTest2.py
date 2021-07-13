import serial

ObjSerial = serial.Serial('/dev/ttyACM0', 9600)

#while 1:
#   print(ObjSerial.readline().decode())

while 1:
    Command = input("입력 : ")
    if "on" == Command:
        print("온 입력")
        ObjSerial.write('1'.encode()) # 아두이노에 '1'를 전송
    elif "off" == Command:
        print("오프 입력")
        ObjSerial.write('0'.encode()) # 아두이노에 '0'을 전송
    else:
        print("없는 명령")
