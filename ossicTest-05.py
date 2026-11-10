
#
#	This origranne started on 2025-01-27 time / DIv 
#

import sys
import pyvisa as visa

Resource = visa.ResourceManager()					                    #	list Resources 
con = Resource.list_resources() 	#con for connection
print(con) 			#Print listed Resources

#InstTag =['USB::0x0AAD::0x0119::032993293::INSTR','USB::0x0699::0x0362::C104603::INSTR','USB::0x0699::0x0362::C104603::INSTR']
if 0:
    for I in range(len(con)):# gathers all the insterments and Identifys them

        #who=rm.open_resource(con[I])
        #who = print("osc =",Resource.open_resource(con[I]).query( "*IDN?" ) )
        osc = Resource.open_resource(con[I])			
        
            

#FuncGen = Resource.open_resource("ASRL5::INSTR")
osc = Resource.open_resource("USB0::0x0AAD::0x0119::104517::INSTR'")     #   Oscilloscope RH0 HMO1002
#osc = Resource.open_resource('USB::0x0AAD::0x0119::104517::INSTR')
#osc = Resource.open_resource("USB::0x0699::0x0362::C104603::INSTR")	#	Oscilloscope TEK 1056B
#osc = Resource.open_resource("USB::0x0699::0x0368::C021301::INSTR")     #    Oscilloscope TEK 1005B  --and 1056B

print( "osc =", osc.query( "*IDN?" ) )					                #	gives details of device
#print( "FuncGen =", FuncGen.query("*IDN?"))
#sys.exit(0)
print("Volt/DIV =",osc.write('CHAN1:SCAL 7E-0')) 

#print("time/div tek =",osc.write('HORIZONTAL:MAIN:SCALE 5E-3')) #time/div works on tek

print("time/div Roh =",osc.write('TIM:SCAL 1E-3')) #SWEep:TIME

sys.exit(0)

print(Resource.list_resources()) #Print listed Resources
print("test")
#osc = Resource.open_resource('ASRL5::INSTR') #Oscilloscope
#Assigns a value to the open resource for the visa Resource
#print( "osc =", osc.query( "*IDN?" ) ) # gives details of device

