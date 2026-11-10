
#
#	This origranne started on 2025-02-14 system argumants for insterment identifaction
#

import sys
import pyvisa as visa
import re                                                                                   #   REGEX has use case for selecting multiple commands through further selectivity

#child of ossic Test-01 as 

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

FuncGen = InstraSel(con)

FREQ =(sys.argv[2])
AMPL =(sys.argv[3])
FREQSet=("SOUR1:FREQ "+ str(FREQ))
AMPLSet=("SOUR1:AMPL "+ str(AMPL))

print(FREQSet)
print(AMPLSet)
FuncGen.write('SOUR1:FUNC RAMP')
FuncGen.write(FREQSet)
FuncGen.write(AMPLSet)
print("SET SINWAVE")

if 0:
        
    FuncGen.write('SOUR1:FUN SIN')
    FuncGen.write('SOUR1:FREQ 1000')
    FuncGen.write('SOUR1:AMPL 2')

print("SOUR 1 Output is ",FuncGen.query('SOUR1:APPL?'))
