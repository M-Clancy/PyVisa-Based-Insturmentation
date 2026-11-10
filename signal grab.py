import sys
import time
import pyvisa as visa
import numpy as np 
import matplotlib.pylab as plt
visa.ResourceManager('@py')
visa.log_to_screen()
Resource = visa.ResourceManager() #list Resources 
print(Resource.list_resources()) #Print listed Resources
tds2012C = Resource.open_resource('USB::0x0699::0x0368::C021141::INSTR') #Oscilloscope
#Assigns a value to the open resource for the visa Resource
print( "Tektronix MSO2012 =", tds2012C.query( "*IDN?" ) ) # gives details of device

#tds2012C.write( "AUTOSET EXECUTE" ) #Autoset done as a Execute

#print( "Tektronix MSO2012  reads =", tds2012C.query( "*AUTOSet:SIGNAL?" ) )
print( "Tektronix MSO2012  reads =", tds2012C.write( "*AUTOSet" ) )
#Autoset done as a Query


if 0:
    print( "Tektronix MSO2012  reads Current Settings =", tds2012C.query( "ACQuire?" ) )
    #Returns current acquisition settings. not all querys require *
    print( "Tektronix MSO2012  reads Current Mode =", tds2012C.query( "ACQuire:MODe?" ) )


#print( "Tektronix MSO2012  reads Current Mode =", tds2012C.query( "ACQuire:NUMACq?" ) )

