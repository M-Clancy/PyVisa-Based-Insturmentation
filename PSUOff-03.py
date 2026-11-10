
#
#	This origranne started on 2025-01-31 Turnoff PSU
#

import sys
import pyvisa as visa
import time 

Resource = visa.ResourceManager()
print(Resource.list_resources() ) 		
PSU = Resource.open_resource('USB::0x0AAD::0x0197::5601.3800k03-112017::INSTR')
#osc = Resource.open_resource('USB0::0x0AAD::0x0119::104517::INSTR')

print("\nPower Supply = ",Resource.open_resource('USB::0x0AAD::0x0197::5601.3800k03-112017::INSTR').query( "*IDN?" ))
#print("Oscilloscope = ",Resource.open_resource('USB0::0x0AAD::0x0119::104517::INSTR').query( "*IDN?" ))


OFF =(sys.argv[1])
OFFSet=("INST OUT "+ str(OFF))
print(OFFSet)
PSU.write(OFFSet)
#PSU.write("INST OUT2")
print("channel =",PSU.query("INST:SEL?"))
print("Set channel output is =",PSU.write("OUTP 0"))
print("channel state ? =",PSU.query("OUTP?"))
print("Setting to 0 = ",PSU.write('APPL "0,1"'))