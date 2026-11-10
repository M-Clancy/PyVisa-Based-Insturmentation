
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
except:
    print("Toggling Function Gen")
    if FuncGen.query("OUTP?") == 1;
        OFF = "OFF"
    elif FuncGen.query("OUTP?") == 0;
        OFF = "ON" 
    #print("fail")

OFFSel=("OUTP "+ str(OFF))
FuncGen.write(OFFSel)
    
    
print("outputting ? =",FuncGen.query("OUTP?"))
