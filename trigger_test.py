
##Print trigger for scanner

##Trigger shock machine    
import serial
#import sys, os #only import if this wasn't done previously
from time import sleep
device = 'COM8' #coded to address desired COM port on PC laptop
#ser = serial.Serial(device, 115200, timeout=1)
ser = serial.Serial(device, 57600, timeout=0)


sleep(2)
#ser.read()
ser.write('t\n');# send out pulse
sleep(1)

ser.close()



##from serial.tools import list_ports
##
##
##def serial_ports():
##    """
##    Returns a generator for all available serial ports
##    """
##    #if os.name == 'nt':
##        # windows
##    for i in range(256):
##        try:
##            s = serial.Serial(i)
##            s.close()
##            yield 'COM' + str(i + 1)
##        except serial.SerialException:
##            pass
####    else:
####        # unix
####        for port in list_ports.comports():
####            yield port[0]
##
##
##if __name__ == '__main__':
##    print(list(serial_ports()))
