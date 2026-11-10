
#
#	This origranne started on 2025-01-31 TurnOff/ON function Gen INSTEK AFG-2105
#

#    This is the child of FuncGenOFF redesigned for toggling 

import sys
import pyvisa as visa
import time 

Resource = visa.ResourceManager()
print(Resource.list_resources() ) 		
FuncGen = Resource.open_resource('ASRL5::INSTR')
#osc = Resource.open_resource('USB0::0x0AAD::0x0119::104517::INSTR')

print("\nFunction Gen = ",Resource.open_resource('ASRL5::INSTR').query( "*IDN?" ))
#print("Oscilloscope = ",Resource.open_resource('USB0::0x0AAD::0x0119::104517::INSTR').query( "*IDN?" ))
print("ON or OFF not 1 or 0")
try:
    
    OFF=(sys.argv[1])
    
    OFFSel=("OUTP "+ str(OFF))
except:
    print("Toggling Function Gen")
    state = (FuncGen.query("OUTP?"))
    print(state)
    if int(state) == 1:
        OFF = "OFF"
        print("test")
        OFFSel=("OUTP "+ OFF)
        FuncGen.write(OFFSel)
    elif int(state) == 0:
        OFF = "ON" 
        print("test")
        OFFSel=("OUTP "+ OFF)
        FuncGen.write(OFFSel)
    #print("fail")


    
    
#print("outputting ? =",FuncGen.query("OUTP?"))
