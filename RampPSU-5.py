
#
#	This origranne started on 2025-02-2 system argumants for insterment identifaction
#
#child of RampPSU-4
import sys
import pyvisa as visa
import numpy as np
import time 
import os

import matplotlib.pylab as plt

if not os.path.exists("C:/Users/micha/instCtrl/commands/"+time.strftime("%Y-%m-%d")+"/"):       #       Confirms the Existance of a folder of the following name  
   os.makedirs("C:/Users/micha/instCtrl/commands/"+time.strftime("%Y-%m-%d")+"/")               #       and then Creats it if it does not exists
#tick=time.strftime("%H,%M,%S")

Resource = visa.ResourceManager()
print(Resource.list_resources() ) 
PSU = Resource.open_resource('USB::0x0AAD::0x0197::5601.3800k03-112017::INSTR')

osc = Resource.open_resource('USB0::0x0699::0x0368::C021141::INSTR')

txtVar = (print(Resource.open_resource('USB0::0x0699::0x0368::C021141::INSTR').query( "*IDN?" )))
print("\nPower Supply = ",Resource.open_resource('USB::0x0AAD::0x0197::5601.3800k03-112017::INSTR').query( "*IDN?" ))
#print("Oscilloscope = ",Resource.open_resource('USB0::0x0AAD::0x0119::104517::INSTR').query( "*IDN?" ))

PSU.write("INST OUT1")
print("channel =",PSU.query("INST:SEL?"))

print("Trigger Level ",osc.query("TRIGger:MAIn?"))
osc.write("TRIGger:MAIn:PULSE:SOUrce {CH1}")
print("Source",osc.query("TRIGger:MAIn:PULSE:SOUrce?"))
osc.write("TRIGger:MAIn SETLevel 0.5")
osc.write("TRIGger:MAIn:MODe {NORMal}")

print("Pulse WIdth ",osc.query("TRIGger:MAIn:PULse:WIDth?"))
osc.write("TRIGger:MAIn:PULse:WIDth:POLarity {POSITIVe}") #sets to Rising edge
osc.write("TRIGger:MAIn:PULse:WIDth:WHEN INSIDE")#set in side range of

osc.write("TRIGger:MAIn:PULse:WIDth:WIDth 0.05")
print("WIDth is between ",osc.query("TRIGger:MAIn:PULse:WIDth:WIDth?"))
print("Mode is set to ",osc.query("TRIGger:MAIn:MODe?"))
print("Trigger Level ",osc.query("TRIGger:MAIn?"))

if 1:
            
    print("Set channel output is =",PSU.write("OUTP 1"))
    print("channel state ? =",PSU.query("OUTP?"))

    incV = 0.5
    acc = 0
    
    print("Setting to 0 = ",PSU.write('APPL "0,0"'))
    #sys.exit(0)
    for i in range(6):
        
        acc = acc + incV
        APPLY=('APPL "'+ str(acc) +',0.1"') #Voltage and Amplitude
        PSU.write(APPLY)                                                                           # 'APPL "2 MIN1, 1"' requires the formate of "" around the values being sent this is currently unque
        print("Reading =",PSU.query("APPL?"), "\nAPPL is = ", APPLY)                               #  APPL responeds in the same formate as it is requested in "" but in the manual this is not show 
        time.sleep(0.001)
    
osc.write('HEADER OFF')
osc.write("DATA:SOURCE CH1")
#print("Confirm Data Source",osc.query("DATA:SOURCE?"))
Source=osc.query("DATA:SOURCE?")  
osc.write("DATA:ENCDG RIBINARY")
if 0:
    EncodingMethod = osc.query("DATA:ENCDG?")
    print("EncodingMethod = ",EncodingMethod)
    WaveFormPreamble = osc.query("WFMpre?")
    print("WaveFormPreamble = ",WaveFormPreamble)
    NumPoints = osc.query("WFMpre:NR_Pt?")
    print("NumPoints = ",NumPoints)

CH1= osc.query_binary_values('CURV?', datatype='h')					#WORKS


print("Set Data Source",osc.write("DATA:SOURCE CH2"))  



plt.plot(CH1,'r', lw = 0.4, label = "Ch1")

plt.legend( )
plt.title( txtVar )
FigName=("C:/Users/micha/instCtrl/commands/"+time.strftime("%Y-%m-%d")+'/'+time.strftime("%H-%M")+"RampFunction.jpg")
plt.savefig(str(FigName))
plt.show()


# Open a text file in write mode ('w' = overwrite, 'a' = append)
with open("C:/Users/micha/instCtrl/commands/"+time.strftime("%Y-%m-%d")+'/'+time.strftime("%H-%M")+"output.txt", "w") as file:
    file.write(str(CH1)+"\n")  # Add a newline after each item

print("Data successfully written to output.txt")
#Scan mode only active below certen time --10ms