#serialCom.py

import serial
import time

# Configure the serial port
ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # Wait for the connection to establish

# Continuously read data from the port
while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode('utf-8', errors='ignore').rstrip()
        print(data)