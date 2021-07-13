import time
import signal

def smart(number, param):
	print("종료합니다.")
#	exit()

signal.signal(signal.SIGINT, smart)

while 1:
	print("zzz...")
	time.sleep(0.2)

