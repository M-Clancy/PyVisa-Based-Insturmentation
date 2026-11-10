
#
#	This origranne started on 2025-01-30 Read and verify form Power supply for Oscilloscope. both ROHDE & SCHWARZ, Tek OSC
#


import sys
import pyvisa as visa

#   Made From BasicPSUContro-01.py 


Resource = visa.ResourceManager()
print(Resource.list_resources() ) 		
PSU = Resource.open_resource('USB::0x0AAD::0x0197::5601.3800k03-112017::INSTR') #               --NGE100 PSU

print("\nPower Supply = ",PSU.query( "*IDN?" ))

Sel=(sys.argv[1])
Sel=("INST:NSEL "+ str(Sel))                                                #   Sets the channel to what the user has input 
PSU.write(Sel)
print("channel =",PSU.query("INST:SEL?"))

print("channel Sel?=",PSU.query("INST:NSEL?"))
#print("Set channel Sel =",PSU.write("INST:NSEL 1"))

Volts=(sys.argv[2])                                                         #   Takes in the Voltage for the system input 
try:
    Current=(sys.argv[3])                                                   #   Tries to assign a system Varable to Current    
except:
    Current=(8.0e-02)
    print("Current out of range defalting to ", Current)                      #   If that assignment fails then Set it to a Defalting value     
    
    
APPLY=('APPL "'+ str(Volts) +','+str(Current)+'"')                          #   'APPL " , "' requires the formate of " " and a comma for multiple values      
print("Set Voltage and Current =",PSU.write(APPLY))    
#add system error for is APPLY and APPL? not matching                       #   Verification is currently manual tho all it should need is a try except and then compare  
#print("Read Voltage and Current =",PSU.query("APPL?"))                      #   The try except Should try to write to the Inst then query and filter the return with Regex
#print("channel output state =",PSU.query("OUTP?"))
#print("channel selected ?=",PSU.query("INST:NSEL?")) 

OUT=("OUTP + str(sys.argv[1])+")
print("Set channel output is =",PSU.write("OUTP 1"))                        #   Turns on the channel by setting the Output to ON
print("channel state ? =",PSU.query("OUTP?"))
