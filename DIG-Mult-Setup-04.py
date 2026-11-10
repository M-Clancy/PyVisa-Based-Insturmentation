
#
#	This origranne started on 2025-03-27 testing the Agilent Digital multmeter for improved understanding
#


import sys
import pyvisa as visa
import matplotlib.pylab as plt

#   Made From BasicPSUContro-04.py as to better fit the naming convention


Resource = visa.ResourceManager()
print(Resource.list_resources() ) 		
Mult = Resource.open_resource('USB0::0x0957::0x0607::MY53001075::INSTR') #  Agilient 34410A

print("\nDigital-Multimeter= ",Mult.query( "*IDN?" ))
print("Error ",Mult.query("SYSTEM:ERROR?"))
#print("DATA:COPY NVMEM, RDG_STORE")
#print("Help = \n", Mult.query('SYSTem:HELP?'))


Mult.write("TRIG:SLOP NEG")
print("Trigger state =",Mult.query("TRIG:SLOP?"))

print("Setting the multmeter to AC function")
Mult.write('FUNC "VOLT:AC"')
#Mult.write("TRIG:COUN ") # Trigger count to ten readings
print("AC Measurment =",Mult.query("MEASure:VOLTage:AC?"))
Mult.write("VOLT:AC:PEAK:STAT ON")# This Command Does function
# configures the ac voltage measurement function to also produce peak-to-peak measurements, which may be retrieved separately from the main voltage measurement.
print("Measureing P2P Voltage active = ",Mult.query("VOLT:AC:PEAK:STAT?"))
#print("FETCH",Mult.query("FETC?"))
for i in range(0,10):
    print("AC Voltage Peak =",Mult.query("MEASure:VOLTage:AC?"))
    
    #Mult.write("VOLT:AC:PEAK:STAT ON")# This Command Does function
    print("Peak to Peak =",Mult.query("FETCh? ; FETC:VOLT:AC:PTP?"))


if 0:
    Mult.write('CALCulate:STAT ON')            #   Enable the Calculations While clearing Previous data gathered and begins gathering new data 
    Mult.query("CALCulate:STAT?")               #   Confirms the state change and the gathering of calculations
    Mult.write('CALCulate:FUNCtion AVERage')    #   starts gathering data for Calculations
    MultAVER=Mult.query('CALCulate:AVERage:AVERage?') 
    # returns all the data gathered since data began to be gathered and provides the average of this data
    MultMAX=Mult.query("CALC:AVER:MAX?")
    MultMIN=Mult.query('CALCulate:AVERage:MINimum?')
    print("Average = ",MultAVER)
    print("MAX = ",MultMAX)
    print("MIN = ",MultMIN)
if 0:
    data=Mult.query('DATA:POINts?')
    print(data)
    #plt.plot( data, 'RED' , lw = 0.4)

    #plt.grid(True)
    #plt.show() 