#test

import sys
import time
import pyvisa as visa
import numpy as np 
import matplotlib.pylab as plt


thing1 = visa.ResourceManager()
thing2 = visa.ResourceManager()
print(thing1.list_resources())
#for i in things.list_resources():
    
    #who = (things.list_resources(i))
    #cutter = [j.replace(',','') for j in who]
    #print(who)
    #Th1s = things.open_resource(who)
    #print(Th1s)

Device_1 = thing1.open_resource('ASRL5::INSTR') #Oscilloscope
Device_2 = thing2.open_resource('ASRL6::INSTR') #Ardbitary Generater

Device_1.timeout = 2000
Device_2.timeout = 2000

print(Device_1.query('*IDN?'))
print(Device_2.query('*IDN?'))

sys.exit( 0 )

print(Device_2.query('*IDN?')) #The WHO ARE YOUS
Device_1.write("AUToscale")
#print(Device_2.query("FREQuency?"))
#Device_1.timeout = 2000
print("hello Humies")

sys.exit( 0 )
