
#
#	This origranne started on 2025-02-14 system argumants for insterment identifaction
#

import sys
import pyvisa as visa
import re                                           #   REGEX has use case for selecting multiple commands through further selectivity

#child of ossic Test-01 as 

def InstraSel(con):
    for I in range(len(con)):                       #  gathers all the insterments and Identifys them

        #who=rm.open_resource(con[I])
        #print("who you =",Resource.open_resource(con[I]).query( "*IDN?" ))
        who = int(Resource.open_resource(con[I]).query( "*IDN?" ).find(sys.argv[1]))
        
        if who >= 0:                                #   confirms the location of the insterments
            Inst = Resource.open_resource(con[I])
            return(Inst)


Resource = visa.ResourceManager()					#   List Resources 
con = Resource.list_resources() 				    #   Print listed Resources

FuncGen = InstraSel(con)
if 1:                                               #   This if statments defines the FREQuency & AMPLitude in which the user input
    FREQ =(sys.argv[2])
    AMPL =(sys.argv[3])                             #   Takes the input varble 
    FREQSet=("SOUR1:FREQ "+ str(FREQ))
    AMPLSet=("SOUR1:AMPL "+ str(AMPL))              #   Creats the layout of the statment 
    print(FREQSet)
    print(AMPLSet)
    FuncGen.write('SOUR1:FUNC SIN')                 #   Sets the wave produced to a Sin Wave  
    FuncGen.write(FREQSet)
    FuncGen.write(AMPLSet)
    print("SET SINWAVE")

if 0:
        
    FuncGen.write('SOUR1:APPL:SIN 1000, 6.6, 1')    #   is ment to define the SIN wave frequency and OFFset voltage but does not work
                                                    
FuncGen.write('SOUR1:OUTP ON')                      #   turns on the Output

print("SOUR 1 Output is ",FuncGen.query('SOUR1:APPL?'))
