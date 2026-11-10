
#
#	This origranne started on 2025-01-29 system argumants for insterment identifaction
#

import sys
import pyvisa as visa
import re                                                                                   #   REGEX has use case for selecting multiple commands through further selectivity


def InstraSel(con):
    for I in range(len(con)):                                                               #  gathers all the insterments and Identifys them

        #who=rm.open_resource(con[I])
        print("who you =",Resource.open_resource(con[I]).query( "*IDN?" ))
        who = int(Resource.open_resource(con[I]).query( "*IDN?" ).find(sys.argv[1]))
        
        if who >= 0:                                                                        #   confirms the location of the insterments
            Inst = Resource.open_resource(con[I])
            return(Inst)


Resource = visa.ResourceManager()					                                        #   List Resources 
con = Resource.list_resources() 	                                                        #   Con for connection
print(Resource.list_resources() ) 			                                                                        #   Print listed Resources

osc = InstraSel(con)

#FuncGen = Resource.open_resource("ASRL5::INSTR")
#osc = Resource.open_resource("USB0::0x0AAD::0x0119::104517::INSTR")                       #   Oscilloscope RH0 HMO1002
#osc = Resource.open_resource('USB::0x0AAD::0x0119::104517::INSTR')
#osc = Resource.open_resource("USB::0x0699::0x0362::C104603::INSTR")	                    #	Oscilloscope TEK 1056B
#osc = Resource.open_resource("USB::0x0699::0x0368::C021301::INSTR")                        #   Oscilloscope TEK 1005B  --and 1056B

print( "osc =", osc.query( "*IDN?" ) )					                                    #	gives details of device
#print( "FuncGen =", FuncGen.query("*IDN?"))
#sys.exit(0)
print("Volt/DIV =",osc.write('CHAN1:SCAL 7E-0')) 

#print("Volt/DIV =",osc.write('CH1:SCAL 7E-0')) # works on tek
print("Volt/DIV query=",osc.query('CHAN1:SCAL?'))                                           #   QUERY THE VOLTAGE

print("time/div tek =",osc.write('HORIZONTAL:MAIN:SCALE 5E-3'))                            #   time/div works on tek

print("time/div Roh =",osc.write('TIM:SCAL 1E-3'))                                          #   Time scale set
print("time/div Roh query =",osc.query('TIM:SCAL?'))  


print("tigger Roh =",osc.query('TRIG:A:LEV?'))                                              #   works to test Trigger level
print("tigger Roh =",osc.write('TRIG1:A:LEV2 4.5'))                                           #   error sets value that i have not set acts like auto set ?
#'TRIG1:LEV2 4.5' no work -- 'TRIG:A:LEV 1 16.59' works as autoset
print("tigger Roh =",osc.query('TRIG:A:LEV?'))                                              #   returns correct value\

sys.exit(0)

print(Resource.list_resources())                                                            #   Print listed Resources
print("test")
#osc = Resource.open_resource('ASRL5::INSTR') #Oscilloscope
#Assigns a value to the open resource for the visa Resource
#print( "osc =", osc.query( "*IDN?" ) ) # gives details of device

