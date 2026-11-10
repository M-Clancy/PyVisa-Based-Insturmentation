
#
#	This origranne started on 2025-02-14 system argumants for insterment identifaction
#

import matplotlib.pylab as plt
import sys
import pyvisa as visa
import time                                                                 #   for delays and time test
import re

#child of SinWaveFuncGenInstAFG-04 as child and based on RampPSU

def InstraSel(con):
    for I in range(len(con)):                                                               #  gathers all the insterments and Identifys them

        try :
            
            print( "\n is this in list", I,"insterment is",con[I])
            print("who you =",Resource.open_resource(con[I]).query( "*IDN?" ))
            
            who = int(Resource.open_resource(con[I]).query( "*IDN?" ).find(sys.argv[1]))
            
            
        except:
            print("no response form",con[I])
            
        if who >= 0:                                                                        #   confirms the location of the insterments
            Inst = Resource.open_resource(con[I])
            return(Inst)
        else:
            print("ERROR ",sys.argv[1], " not found in list  did it respond ")
            sys.exit(0)


Resource = visa.ResourceManager()					                                        #   List Resources 
con = Resource.list_resources() 			
FuncGen = Resource.open_resource('ASRL5::INSTR')
osc = Resource.open_resource('USB0::0x0699::0x0368::C021301::INSTR')
if 0:
    StartFREQ =(sys.argv[2])
    StopFREQ=(sys.argv[3])
    FREQSteps =(sys.argv[4])
    StartFREQ =(sys.argv[5])
    StopFREQ=(sys.argv[6])
    FREQSteps =(sys.argv[7])
    
FuncGen.write('SOUR1:FUNC SIN')
StartFREQ = (100000)
FREQ=StartFREQ
StopFREQ=(1000000)
AMPL =(3)
AMPLSteps=1
AMPLinc=0
wait=2
FREQSteps=20
incFREQ=StopFREQ/FREQSteps
print(incFREQ)

sig=[]
for i in range(AMPLSteps):
    
    
    AMPLSet=("SOUR1:AMPL "+ str(AMPL))
    FuncGen.write(AMPLSet) 
    AMPL = AMPL + AMPLinc
    #print("inc up =",AMPL)
    print(AMPLSet)
    FREQ=StartFREQ
    
    for j in range(FREQSteps):
        FREQSet=("SOUR1:FREQ "+ str(FREQ))
        print("FREQ changed to =",FREQSet)
        FuncGen.write(FREQSet)      
        if FREQ>=StopFREQ:
            print("end")
            break
        FREQ = FREQ + incFREQ                                      #    APPL responeds in the same formate as it is requested in "" but in the manual this is not show 
        time.sleep(wait)
        print(j)
        if 1:
            print("Set Data Source",osc.write("DATA:SOURCE CH1"))  #    I can run this as I've already defined the output settings in Buffer read
            CH1= osc.query_binary_values('CURV?', datatype='h')	

            print("Set Data Source",osc.write("DATA:SOURCE CH2"))  
            CH2 = osc.query_binary_values('CURV?', datatype='h')
            
            sig.extend([CH1,CH2])

X=6         #j
Y=3         #i
print("this should be 40 or 20 ",len(sig))
figure, axis = plt.subplots(Y, X)
POS=0
print(POS)
for i in range(Y):
    for j in range(X):
        if POS >= len(sig):
            break
        else:
            axis[i, j].plot(sig[POS-1],'b', lw = 0.4, label = "Ch2")
            axis[i, j].plot(sig[POS],'r', lw = 0.4, label = "Ch1")
            axis[i, j].set_title("Sine Function")
            POS=(2+POS)
        print("position 2 =",POS)
plt.legend( )
plt.title( "yes this is here test" )
plt.show()
sys.exit(0)
FuncGen.write(FREQSet)
FuncGen.write(AMPLSet)
print("SET SINWAVE")

if 0:
        
    FuncGen.write('SOUR1:APPL:USER 1000, 6.6, 1')
    
FuncGen.write('SOUR1:OUTP ON')

print("SOUR 1 Output is ",FuncGen.query('SOUR1:APPL?'))
