import sys
import time
import pyvisa as visa
import numpy as np 
import matplotlib.pylab as plt

Resource = visa.ResourceManager() #list Resources 
print(Resource.list_resources()) #Print listed Resources
print("test")
#HMO1002 = Resource.open_resource('USB::0x0AAD::0x0119::032993293::INSTR') #Oscilloscope
#Assigns a value to the open resource for the visa Resource
#print( "HMO1002 =", HMO1002.query( "*IDN?" ) ) # gives details of device

#HMO1002.write( "AUTOSET EXECUTE" ) #Autoset done as a Execute
if 0:
    #print( "ROHDE&SCHWARZ HMO1002  reads =", HMO1002.query( "*AUTOSet:SIGNAL?" ) )
    print( "Rohde&Schwarz HMO1002  saids =", HMO1002.write( "*AUToscale" ) )
    #Autoset done as a Query wrong


if 0:
    print( "Rohde&Schwarz HMO1002  reads Current Settings =",HMO1002.query( "ACQuire?" ) )
    #Returns current acquisition settings. not all querys require *
    print( "Rohde&Schwarz HMO1002  reads Current Mode =", HMO1002.query( "ACQuire:MODe?" ) )

if 0: 
    #HMO1002.write("CHANnel<1>:STATe<ON>")
    #HMO1002.write("ACQuire:STATe")#
    
    #HMO1002.write("MEASurement<m>:AON")
    #HMO1002.write("MEASurement<1>[:ENABle] <ON>")#allows for the measurements of FREQ
    print("HMO1002 reads FREQ =", HMO1002.query("MEASurement<1>:ARESult?"))#expected frequency from channel 1 
    #un-like the tek 2012C the measurements are set as numbers and not by name so its less interpratatable. 

#print( "ROHDE&SCHWARZ HMO1002  reads Current Mode =", HMO1002.query( "ACQuire:NUMACq?" ) )
if 0: 
    #HMO1002.write("CHANnel<0>:STATe<ON>")
    #HMO1002.write("ACQuire:STATe")#
    
    #HMO1002.write("MEASurement<1>:AON")
    HMO1002.write("MEASurement<1>[:ENABle]<ON>")#allows for the measurements of FREQ
    print("HMO1002 reads FREQ =", HMO1002.query("MEAS<1>:RES?[FREQ]"))#expected frequency from channel 1 
    #un-like the tek 2012C the measurements are set as numbers and not by name so its less interpratatable. 

