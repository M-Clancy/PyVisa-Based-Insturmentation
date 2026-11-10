import sys
import pyvisa as visa
import numpy as np
import time 


Resource = visa.ResourceManager()
print(Resource.list_resources() ) 
PSU = Resource.open_resource('USB::0x0AAD::0x0197::5601.3800k03-112017::INSTR')
DIGMULT = Resource.open_resource('USB0::0x0957::0x0607::MY53001075::INSTR')
print("\nPower Supply = ",Resource.open_resource('USB::0x0AAD::0x0197::5601.3800k03-112017::INSTR').query( "*IDN?" ))
#print("Oscilloscope = ",Resource.open_resource('USB0::0x0AAD::0x0119::104517::INSTR').query( "*IDN?" ))

PSU.write("INST OUT1")
print("channel =",PSU.query("INST:SEL?"))

if 1:
            
    print("Set channel output is =",PSU.write("OUTP 1"))
    print("channel state ? =",PSU.query("OUTP?"))

    incV = 0.1
    acc = 0
    sig=[]
    print("Setting to 0 = ",PSU.write('APPL "0,0"'))
    #sys.exit(0)
    for i in range(30):
        
        acc = acc + incV
        APPLY=('APPL "'+ str(acc) +',0.1"')
        PSU.write(APPLY)                                                                           # 'APPL "2 MIN1, 1"' requires the formate of "" around the values being sent this is currently unque
        print("Reading =",PSU.query("APPL?"), "\nAPPL is = ", APPLY)                               #  APPL responeds in the same formate as it is requested in "" but in the manual this is not show 
        time.sleep(0.05)
        Volt=DIGMULT.query("MEAS:VOLT:DC? 10,0.01") 
        print("REad VOltage = ",Volt)
        sig.append(Volt)
        time.sleep(0.05)
    print(sig)
    # Sample data to write
