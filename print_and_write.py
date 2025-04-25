#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 21:29:02 2025

@author: danielvalmassei
"""

import serial
import csv
import time

def convert_voltage(voltage):
    if voltage >= 4.94:
        a = 100.624
        b = -0.37679
        c = -20.5623
        d = 0.0348656
        
        numerator = a + c*voltage
        denom = 1 + b*voltage + d*voltage**2
        
        return numerator/denom
    
    elif voltage >= 2.842:
        a = 0.1031
        b = -0.3986
        c = -0.02322
        d = 0.07438
        e = 0.07229
        f = -0.006866
        
        numerator = a + c*voltage + e*voltage**2
        denom = 1 + b*voltage + d*voltage**2 + f*voltage**3
        return numerator/denom
    
    elif voltage >= 0.375:
        a = -0.02585
        b = 0.03767
        c = 0.04563
        d = 0.1151
        e = -0.04158
        f = 0.008737
        return a + b*voltage + c*voltage**2 + d*voltage**3 + e*voltage**4 + f*voltage**5
    
    
    else: #something went wrong. return an unreasonable value
        return 1000
    
    
def main():
    # Adjust these parameters
    port = '/dev/tty.usbmodemF0F5BD5329182'  # Replace with your Arduino's port
    baud_rate = 9600
    output_file = 'out.csv'
    
    
    # Initialize serial connection
    ser = serial.Serial(port, baud_rate, timeout=1)
    time.sleep(2)  # Wait for connection
    
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
    
        print('Collecting data... Press Ctrl+C to stop.')
        try: 
            while True:
                line = ser.readline().decode('utf-8').strip().split(', ')
                print(line[0],convert_voltage(line[1]))
                writer.writerow(line)
                
        except KeyboardInterrupt:
            print('Data collection stopped.')
        finally:
            ser.close()

if __name__ == '__main__':
    main()
