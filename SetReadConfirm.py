
#
#	This origranne started on 2025-01-30 Read and verify form Power supply to Oscilloscope. both ROHDE & SCHWARZ
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

PSU.write("INST OUT1")
print("channel =",PSU.query("INST:SEL?"))
#---
if 1:
            
    print("Set channel output is =",PSU.write("OUTP 1"))
    print("channel state ? =",PSU.query("OUTP?"))

    incV = 0.2
    acc = 0
    
    print("Setting to 0 = ",PSU.write('APPL "0,0"'))
    #sys.exit(0)
    for i in range(30):
        
        acc = acc + incV
        APPLY=('APPL "'+ str(acc) +',0.1"')
        PSU.write(APPLY)                                                                           # 'APPL "2 MIN1, 1"' requires the formate of "" around the values being sent this is currently unque
        print("Reading =",PSU.query("APPL?"), "\nAPPL is = ", APPLY)                               #  APPL responeds in the same formate as it is requested in "" but in the manual this is not show 
        time.sleep(0.5)
        


if 0:
    #print("RAMP =",PSU.query("VOLT:EASY?"))                                                      #print("RAMP =",PSU.query("VOLT:EASY:STAT?"))

    print("RAMP  DURation?=",PSU.write("VOLT:EASY:TIME 10000"))
    print("RAMP TIME? =",PSU.query("VOLT:EASY:TIME?"))

    print("RAMP Stat change =",PSU.write("VOLT:EASY 0"))
    print("RAMP state ? =",PSU.query("VOLT:EASY?"))   

    #print("RAMP  DURation?=",PSU.query("VOLT:RAMP:DUR?"))
#---
if 0:
    print("Generate arditaty valuse=",PSU.write("ARB:DATA 2,1,200,4,1,200,6,1,200"))
    print("ARBitrary REPeations = 5",PSU.write("ARB:REP 3"))
    print("Arbitary data = ",PSU.query("ARB:REP?"))
    print("Arbitary DATA POINTs = ",PSU.query("ARB:POIN?"))
    print("Arbitary State Change = ",PSU.write("ARB 1"))
    print("Arbitary State is = ",PSU.query("ARB?"))

#print("Set channel output is =",PSU.write("OUTP ON"))
#print("channel state ? =",PSU.query("OUTP?"))

#print("channel output state =",PSU.query("OUTP?"))
#print("Set channel OFF =",PSU.write("OUTP 0"))

if 0:
    print("channel Sel?=",PSU.query("INST:NSEL?"))
    print("Set channel Sel =",PSU.write("INST:NSEL 2"))
    print("Set Voltage and Current =",PSU.write('APPL "4.2, 1e-02"'))                             # 'APPL " , "' requires the formate of " " and a comma for multiple values
    print("Read Voltage and Current =",PSU.query("APPL?"))      
    print("channel output state =",PSU.query("OUTP?"))
    print("channel selected ?=",PSU.query("INST:NSEL?"))                                                


if 0:
    print("Volt/DIV =",osc.write('CHAN2:SCAL 2E-0')) 
    print("Volt/DIV query=",osc.query('CHAN2:SCAL?'))                                           #   time/div works on tek

    print("time/div Roh =",osc.write('TIM:SCAL 5E-7'))                                          #   Time scale set
    print("time/div Roh query =",osc.query('TIM:SCAL?'))  
    print("CHANnel set =",osc.write('CHAN 2'))  
    #print("CHANnel set ? =",osc.query('CHAN?')) 
    print("tigger Roh =",osc.query('TRIG:A:LEV?'))                                              #   works to test Trigger level ALso requires ""
    print("tigger Roh =",osc.write('TRIG:A:LEV1:VAL 0.5'))                                      #   Trigger Level Works

    print("tigger Roh =",osc.query('TRIG:A:LEV?')) 