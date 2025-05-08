import sys
import serial
ser = serial.Serial('/dev/ttyUSB0')
ser.write(b'F')

n = len(sys.argv)

if (n > 1):
	mm_to_steps_factor = 157.4803149606
	speed_mm = int(sys.argv[1])
	speed_steps = speed_mm * mm_to_steps_factor
	print(str(speed_mm) + " mm/sec is " +  str(speed_steps) + " steps/sec")
	if (speed_steps < 1):
		print("Speed must be no less than 1 step/sec and no greater than 6000 steps/sec.")
		int_speed_steps = 1
	elif (speed_steps > 6000):
		print("Speed must be no less than 1 step/sec and no greater than 6000 steps/sec.")
		int_speed_steps = 6000
	else:
		int_speed_steps = int(speed_steps)
	command = b'C U6, S1M' + str(int_speed_steps).encode() + b', R'
	print(command)
	ser.write(command)
	actual_speed_mm = int_speed_steps / mm_to_steps_factor
	print("Speed set to " + str(int_speed_steps) + " steps/sec (" + str(actual_speed_mm) + " mm/sec).")
	print("I am Ready.")
else:
	print("Optional: one may pass the desired motor speed (in steps per second) as a parameter when calling this function")
	print("I am Ready.")
