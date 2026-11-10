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


print("seting trigger mode normal =",osc.write("TRIG:A:MODE AUTO"))
print("seting trigger to ch1 =",osc.write("TRIG:A:SOUR CH1"))

print("trig set to ? =",osc.query("TRIG:A:SOUR?"))


print("triglevel set=",osc.write("TRIG:A:LEV 0.15"))
print("triglevel set? =",osc.query("TRIGger:A:LEVel?"))

print("Volt/DIV =",osc.write('CHAN1:SCAL 0.6')) 
print("Volt/DIV =",osc.query('CHAN1:SCAL?')) 

print("time/div Roh =",osc.write('TIM:SCAL 2'))                                          #   Time scale set
print("time/div Roh query =",osc.query('TIM:SCAL?'))  

print("trig type set=",osc.write("TRIG:A:TYPE WIDT"))
print("trig type set confirm?=",osc.query("TRIG:A:TYPE?"))
if 1:
    print("set width to Range within=",osc.write("TRIG:A:WIDT:RANG with"))
    print("Rang set to ??=",osc.query("TRIG:A:WIDT:RANG?"))

    print("set range type=",osc.write("TRIG:A:WIDT:WIDT 10"))
    print("Rang set to sec ??=",osc.query("TRIG:A:WIDT:WIDT?"))

    print("DELTa Width is ?=",osc.query("TRIG:A:WIDT:DELT?"))


print("Prep for Acquisition=",osc.write("SING"))
sys.exit(0)

if (sys.argv[1]==("EDGE" or "edge")):
	osc.write('TRIG:A:TYPE EDGE')
	print("set Edge trigger mode")
elif(sys.argv[1]==("WIDT" or "WIDTh")):
    osc.write('TRIG:A:TYPE WIDT')
    print("set Width trigger mode")
elif(sys.argv[1]==("TV" or "TV:")):
	osc.write(' TRIG:A:TYPE TV')
	print("set Video trigger mode")
elif(sys.argv[1]==("LOG" or "LOGic")):
    osc.write('TRIG:A:TYPE LOG')
    print("set LOGIC trigger mode")
elif(sys.argv[1]==("BUS" or "BUS:")):
	osc.write(' TRIG:A:TYPE BUS')
	print("set Bus trigger mode")
    
    
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
