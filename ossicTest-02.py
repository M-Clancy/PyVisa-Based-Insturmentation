
#
#	This origranne inherits from Rev01 on 2025-01-22 incorporates ..
#

import sys
import time
import pyvisa as visa

Resource = visa.ResourceManager()					#	list Resources 
osc = Resource.open_resource("USB::0x0699::0x0362::C104603::INSTR")	#	Oscilloscope
print( "osc =", osc.query( "*IDN?" ) )					#	gives details of device

sys.exit( 0 )


print(Resource.list_resources()) #Print listed Resources
print("test")
#osc = Resource.open_resource('ASRL5::INSTR') #Oscilloscope
#Assigns a value to the open resource for the visa Resource
#print( "osc =", osc.query( "*IDN?" ) ) # gives details of device

