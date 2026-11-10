#
#			made to test theory to test a change in start time when using trigger level
#
import matplotlib.pylab as plt
import sys
import pyvisa as visa
import numpy as np
import time 


Resource = visa.ResourceManager()
print(Resource.list_resources() ) 
osc = Resource.open_resource('USB0::0x0AAD::0x0119::104517::INSTR')

print("Scope is = ",osc.query( "*IDN?" ))


if (sys.argv[1]==("SING" or "SINGle")):
	osc.write('PGEN:PATT:TRIG:MODE SING')
	print("set SINGLe trigger mode")
elif(sys.argv[1]==("CONT" or "CONTinuous")):
    osc.write('PGEN:PATT:TRIG:MODE CONT')
    print("set CONTinuous trigger mode")
    
elif(sys.argv[1]==("EXT" or "EXTern")):
	
	osc.write('PGEN:PATT:TRIG:MODE EXT')
	print("set EXTern trigger mode")
else:
    print("ERROR TRIGGER MODE not reconised")
    
match sys.argv[2]:
    case ("POSitive" | "POS"):
        osc.write('PGENerator:PATTern:TRIGger:EXTern:SLOPe POS')
        print("POS set")
    case  ("EITHer" | "EITH"):
        osc.write('PGENerator:PATTern:TRIGger:EXTern:SLOPe EITH')
        print("EITH set")
    case ("NEGative" | "NEG") :
        osc.write('PGENerator:PATTern:TRIGger:EXTern:SLOPe NEG')
        print("NEG set")
    case _:
        print("ERROR TRIGGER MODE slop not reconised")

sys.exit(0)
