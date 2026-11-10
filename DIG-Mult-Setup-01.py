
#
#	This origranne started on 2025-03-27 testing the Agilent Digital multmeter for improved understanding
#


import sys
import pyvisa as visa
import matplotlib.pylab as plt

#   Made From BasicPSUContro-04.py as to better fit the naming convention


Resource = visa.ResourceManager()
print(Resource.list_resources() ) 		
Mult = Resource.open_resource('USB0::0x0957::0x0607::MY53001075::INSTR') #               --NGE100 PSU

print("\nDigital-Multimeter= ",Mult.query( "*IDN?" ))
print("Last",Mult.query("DATA:LAST?"))
#print("DATA:COPY NVMEM, RDG_STORE")
print("Help = \n", Mult.query('SYSTem:HELP:DATA:FEED?'))
#SYSTem:BEEPer:STATE
#Mult.write("TRIG:COUN ") # Trigger count to ten readings
Mult.write('CALCulate:STAT ON}')
Mult.query("CALCulate:STAT?") # starts gathering data for Calculations
Mult.write('CALCulate:FUNCtion AVERage') #
MultAVER=Mult.query('CALCulate:AVERage:AVERage?') 
# returns all the data gathered since data began to be gathered and provides the average of this data
MultMAX=Mult.query("CALC:AVER:MAX?")
MultMIN=Mult.query('CALCulate:AVERage:MINimum?')
if 0:
    data=Mult.query('DATA:POINts?')
    print(data)
    #plt.plot( data, 'RED' , lw = 0.4)

    #plt.grid(True)
    #plt.show() 