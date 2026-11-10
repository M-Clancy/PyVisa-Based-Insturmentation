
#
#	This origranne started on 2025-01-30 Read and verify form Power supply to Oscilloscope. both ROHDE & SCHWARZ
#


import sys
import pyvisa as visa

Resource = visa.ResourceManager()
print(Resource.list_resources() ) 		
PSU = Resource.open_resource('USB::0x0AAD::0x0197::5601.3800k03-112017::INSTR') #               --NGE100 PSU

print("\nPower Supply = ",PSU.query( "*IDN?" ))

Sel=(sys.argv[1])
Sel=("INST:NSEL "+ str(Sel))
PSU.write(Sel)
print("channel =",PSU.query("INST:SEL?"))

print("channel Sel?=",PSU.query("INST:NSEL?"))
#print("Set channel Sel =",PSU.write("INST:NSEL 1"))
print("Set Voltage and Current =",PSU.write('APPL "15, 2.5e-02"'))                             # 'APPL " , "' requires the formate of " " and a comma for multiple values
print("Read Voltage and Current =",PSU.query("APPL?"))      
print("channel output state =",PSU.query("OUTP?"))
print("channel selected ?=",PSU.query("INST:NSEL?")) 

OUT=("OUTP + str(sys.argv[1])+")
print("Set channel output is =",PSU.write("OUTP 1"))
print("channel state ? =",PSU.query("OUTP?"))
