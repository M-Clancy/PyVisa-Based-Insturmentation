
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
FREQ =(sys.argv[2])
AMPL =(sys.argv[3])
APPLY=('"SOUR1:FREQ '+ str(FREQ) +'"')
APPLY=('"SOUR1:AMPL '+ str(AMPL) +'"')
FuncGen = InstraSel(con)

FuncGen.write('SOUR1:FUN SIN')
FuncGen.write('SOUR1:FREQ 1000')
FuncGen.write('SOUR1:AMPL 2')
print("SET SINWAVE")
if 0:
    APPLY=('SOUR[1]:APP:SIN+ str(sys.argv[2])+')
    FuncGen.write(APPLY)

FuncGen.write('SOUR1:FUNC SIN')

print("SOUR 1 Output is ",FuncGen.query('SOUR1:APPL?'))
