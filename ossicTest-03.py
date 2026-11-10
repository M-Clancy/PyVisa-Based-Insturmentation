
#
#	This origranne inherits from Rev01 on 2025-01-22 incorporates a test for automation on the selection of Insterments & added HMO introments
#

import sys
import pyvisa as visa

Resource = visa.ResourceManager()					                    #	list Resources 

InstTag =[USB::0x0AAD::0x0119::032993293::INSTR,USB::0x0699::0x0362::C104603::INSTR,USB::0x0699::0x0362::C104603::INSTR]

            
        
#osc = Resource.open_resource("USB::0x0AAD::0x0119::032993293::INSTR")  #   Oscilloscope RH0 HMO1002
#osc = Resource.open_resource("USB::0x0699::0x0362::C104603::INSTR")	#	Oscilloscope TEK 1056B
osc = Resource.open_resource("USB::0x0699::0x0368::C021138::INSTR")	    #	Oscilloscope TEK 1005B
print( "osc =", osc.query( "*IDN?" ) )					                #	gives details of device


sys.exit( 0 )


print(Resource.list_resources()) #Print listed Resources
print("test")
#osc = Resource.open_resource('ASRL5::INSTR') #Oscilloscope
#Assigns a value to the open resource for the visa Resource
#print( "osc =", osc.query( "*IDN?" ) ) # gives details of device

