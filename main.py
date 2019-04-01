import serial
import config


ser = serial.Serial(config.port, config.baudrate)

while 1:
	data=ser.readline()
	print(data)

