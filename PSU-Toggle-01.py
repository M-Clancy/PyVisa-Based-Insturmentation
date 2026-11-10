
#
#	This origranne started on 2025-01-30 Read and verify form Power supply for Oscilloscope. both ROHDE & SCHWARZ, Tek OSC
#


import sys
import pyvisa as visa

#   Made From BasicPSUContro-04.py as to better fit the naming convention


Resource = visa.ResourceManager()
#print(Resource.list_resources() ) 		
PSU = Resource.open_resource('USB::0x0AAD::0x0197::5601.3800k03-112017::INSTR') #               --NGE100 PSU

#print("\nPower Supply = ",PSU.query( "*IDN?" ))

Chan=1
print(PSU.write("OUTP 1"))


try:
    
    print(Chan)
    #   Sets the channel to what the user has input 
    PSU.write(Sel)
    while 0 :
    sel = PSU.query("INST:SEL?")
    sel=sel.replace("OUTPut","")
    sel=sel.replace(" ","")
    OFFSet=("OUTP 0")
    OFFSel=("INST OUT 0")

    if  int(Chan) == int(sel):
        print("true")
        Chan=Chan+1
        sel=("INST:NSEL "+ str(Chan)) 
        PSU.write(sel)
    else:
        print('false')
        
    sel = PSU.query("INST:SEL?")
    
    OFFSet=("OUTP 0")
    OFFSel=("INST OUT 0")
    print(PSU.query("OUTP?"))
        
    except:
       print("All OFF")
       break
    
if 0:
    APPLY=('APPL "'+ str(Volts) +','+str(Current)+'"')                          #   'APPL " , "' requires the formate of " " and a comma for multiple values      
    print("Set Voltage and Current =",PSU.write(APPLY))    
    #add system error for is APPLY and APPL? not matching                       #   Verification is currently manual tho all it should need is a try except and then compare  
    print("Read Voltage and Current =",PSU.query("APPL?"))                      #   The try except Should try to write to the Inst then query and filter the return with Regex
    print("channel output state =",PSU.query("OUTP?"))
    print("channel selected ?=",PSU.query("INST:NSEL?")) 

    OUT=("OUTP + str(sys.argv[1])+")
    print("Set channel output is =",PSU.write("OUTP 1"))                        #   Turns on the channel by setting the Output to ON
    print("channel state ? =",PSU.query("OUTP?"))
