########Based on code received from Daniel Valmassei, December 2023#######

import sys
import serial

ser = serial.Serial('/dev/ttyUSB0')
#print(ser.name)

def limiting_debug(extrema):

	if (extrema == "bottom"):
		x = b'0'
		print("Moving to bottom...")
	elif (extrema == "top"):
		x = b'-0'
		print("Moving to top...")
	else:
		print("Invalid argument: " + extrema)

	command = b'C U6, I1M' + x + b', R'
	#ser.write(command)

	#ser.write(b'G')
	#ser.close()
	print("Movement complete.")

def limit(extrema):
	if(extrema == "bottom"):
		x = b'0'
		print("Moving to bottom...")
	elif(extrema == "top"):
		x = b'-0'
		print("Moving to top...")
	else:
		print("Invalid argument: " + extrema)
	
	command = b'C U6, I1M' + x + b', R'
	ser.write(command)
	ser.write(b'G')
	ser.close()
	print("Movement complete.")
