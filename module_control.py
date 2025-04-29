import sys
import serial
import vxmMove
import vxmLimit

n = len(sys.argv)

if (n < 2):
	print("No command passed.")
	print("~~~~~~~~~~~~~~~~~~")
	print("Available commands:")
	print("\t limit [destination]")
	print("\t\t top: Carriage moves up toward the motor end of the UniSlide")
	print("\t\t bottom: Carriage moves down away from the motor to the far side of the track")
	print("\t move [displacement (mm)]")
	print("\t\t Carriage moves +/- by the chosen displacement.")
	
else:
	s = str(sys.argv[1])
	print(s)
	if (s == "limit"):
		if (n < 3):
			print("Error: Destination limit not specified")
		else:
			z = str(sys.argv[2])
			if ((z == "top") | (z == "bottom")):
				vxmLimit.limit(z)
			else:
				print("Error: Invalid limit destination.")
				print("~~~~~~~~~~~~~~~~~~~")
				print("\t\t top: Carriage moves up toward the motor end of the UniSlide")
				print("\t\t bottom: Carriage moves down away from the motor to the far side of the track")
	elif (s == "move"):
		if (n < 3):
			print("Error: Travel displacement unspecified")	
		else:
			v = float(sys.argv[2])
			
			if ((v < 0) | (v > 0)): #### Could work on error handling for this case....
				vxmMove.move(v)
			elif (v == 0):
				print("Error: Non-zero displacement required. To move to the limits, use the limit command.")
			else:
				print("Error: Move command requires an integer displacement (in millimeters)")
			#When I have a more robust script that monitors the track's knowledge of its position, I could
			#	(1) Have it report when a limit was unexpectedly reached
			#	(2) Have it announce when the entered move distance is expected to result in reaching a limit.
	else:
		print("Unrecognized command")
		print("~~~~~~~~~~~~~~~~~~~~")
		print("Available commands:")
		print("\t limit [destination]")
		print("\t\t top: Carriage moves up toward the motor end of the UniSlide")
		print("\t\t bottom: Carriage moves down away from the motor to the far side of the track")
		print("\t move [displacement (mm)]")
		print("\t\t Carriage moves +/- by the chosen displacement.")
		
