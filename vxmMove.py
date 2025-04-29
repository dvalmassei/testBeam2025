#####Based on code received from Daniel Valmassei, December 2023######

import serial
import time

def pause(ser):
    while True:
       # print(ser.in_waiting)
        if ser.in_waiting > 0:
            break

def moving_debug(y):

    #displacement = sys.argv[1]
    displacement = str(y)

    # 200 steps per 0.1" revolution.
    # The screw actually advances by half-steps, so there are 4000 half-steps per 1-inch advance.
    # 0.00025" per step -> 0.00635mm per step, so 157.4803149606...half-steps per millimeter
    
    mm_to_steps_factor = 157.4803149606
    travel = mm_to_steps_factor * y
    print(displacement + "mm is " + str(travel) + " half-steps")
    steps = str(round(travel))
    
    
    print("Moving " + displacement + " mm (" + steps + " half-steps) ...")

    #displacement_bin = displacement.encode()
    #print(displacement_bin)

    command = b'C U6, I' + steps.encode() + b', R'
    print(command)

    #ser = serial.Serial('/dev/ttyUSB0')
    #print(ser.name)

    #ser.write(b'C U6, I1M25, R')
    #ser.write(command)

    #ser.write(b'G')
    #ser.close()

    print("Movement complete.")
    
def move(y):
    
    if (y > 0):
        direction = "(downward)"
    else:
        direction = "(upward)"
    displacement = str(y)
    
    # 200 steps per 0.1" revolution.
    # The screw actually advances by half-steps, so there are 4000 half-steps per 1-inch advance.
    # 0.00025" per step -> 0.00635mm per step, so 157.4803149606...half-steps per millimeter	
    
    mm_to_steps_factor = 157.4803149606
    travel = mm_to_steps_factor * y
    
    print(displacement + "mm is " + str(travel) + " half-steps")
    steps = str(round(travel))

    print("Moving " + displacement + " mm " + direction + " (" + steps + " half-steps) ...")
    command = b'C U6, I' + steps.encode() + b', R'

    ser = serial.Serial('/dev/ttyUSB0')
    ser.write(command)
    
    done = 0
    
    while (done == 0): #while the program is running
        pause(ser)
        print ("line 28")
        input = ser.read()
        print ("line 30")
        if input == b'^':
            print('program complete')
            done = 1
            break 
        elif input == b'W':
            ser.write(b'X') #send command to VXM to send back position
            pause(ser)
            data_start = ser.read(size = ser.in_waiting) #read data from buffer
            print(data_start)
            
            start_steps = str(data_start)[3:10]
            start_mm = int(start_steps) / mm_to_steps_factor 
            print("Start: " + str(start_mm) + " mm (" + start_steps + " steps)")
            ser.write(b'G') #send go command to VXM, so it may continue

            data_before = data_start
            done = 0
            while (done == 0):
            #    print("still true")
                ser.write(b'X')
                pause(ser)
                data_after = ser.read(size = ser.in_waiting)
             #   print("Data Before: ")
              #  print(data_before)
               # print("Data After: ")
                #print(data_after)
                #print("--------------------")
                if (data_before == data_after):
                    done = 1
                #    print("MATCH")
                #    print("-------------------")
                else:
                    data_before = data_after
                #    print("still waiting")
                
            #print("Data Start:")
            #print(data_start)
            #print("Data End:")
            #print(data_after)
            
            #start_steps = str(data_start)[3:10]
            end_steps = str(data_after)[3:10]
            #print("Moved from " + start_steps + " steps to " + end_steps + " steps")
            
            #start_mm = int(start_steps) / mm_to_steps_factor
            end_mm = int(end_steps) / mm_to_steps_factor
            #print("Moved from " + str(start_mm) + " mm to " + str(end_mm) + " mm.")
            print("End:   " + str(end_mm) + " mm (" + end_steps + " steps)")
            
        else:
            print('error: unexpected input')
            print(input)
            break
    
    ser.close()
    
    print("Movement complete.")
