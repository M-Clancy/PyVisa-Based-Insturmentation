#
#			Revised 07/02/2025 made to test theory to test a change in start time when using trigger level
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


print("seting trigger mode normal =",osc.write("TRIG:A:MODE NORM"))
print("seting trigger to ch1 =",osc.write("TRIG:A:SOUR CH1"))

print("trig set to ? =",osc.query("TRIG:A:SOUR?"))


print("triglevel set=",osc.write("TRIG:A:LEV 2E-01"))
print("triglevel set? =",osc.query("TRIGger:A:LEVel?"))

print("triglevel set=",osc.write("TRIG:A:TYPE EDGE:"))

print("Volt/DIV =",osc.write('CHAN1:SCAL 1E-01')) 

print("Volt/DIV =",osc.query('CHAN1:SCAL?')) 


print("Prep for Acquisition=",osc.write("SING"))
sys.exit(0)

if (sys.argv[1]==("SING" or "SINGle")):
	osc.write('SING')
	print("set SINGLe trigger mode")
elif(sys.argv[1]==("CONT" or "CONTinuous")):
    osc.write(' CONT')
    print("set CONTinuous trigger mode")
    
elif(sys.argv[1]==("EXT" or "EXTern")):
	
	osc.write(' EXT')
	print("set EXTern trigger mode")
else:
    print("ERROR TRIGGER MODE not reconised")
    
match sys.argv[2]:
    case ("POSitive" | "POS"):
        osc.write(' POS')
        print("POS set")
    case  ("EITHer" | "EITH"):
        osc.write('PATTern:TRIGger:EXTern:SLOPe EITH')
        print("EITH set")
    case ("NEGative" | "NEG") :
        osc.write('PATTern:TRIGger:EXTern:SLOPe NEG')
        print("NEG set")
    case _:
        print("ERROR TRIGGER MODE slop not reconised")

sys.exit(0)
