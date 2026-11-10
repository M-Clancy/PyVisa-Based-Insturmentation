
#
#	This origranne started on 2025-02-14 system argumants for insterment identifaction
#

import matplotlib.pylab as plt
import numpy as np
import sys
import pyvisa as visa
import time                                                                 #   for delays and time test
import re

import os

#has in heritance from 5 of WaveVectorProducter-05

if not os.path.exists("C:/Users/micha/instCtrl/commands/"+time.strftime("%Y-%m-%d")+"/"):
   os.makedirs("C:/Users/micha/instCtrl/commands/"+time.strftime("%Y-%m-%d")+"/")
#tick=time.strftime("%H,%M,%S")
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
    #add Osc channel 

osc.write("MEASUrement:IMMed:SOUrce1 CH1")
osc.write('MEASUREMENT:IMMED:TYPE PHA')  
print("Measured Units=",osc.query('MEASUrement:IMMed:UNIts?'))
FuncGen.write('SOUR1:FUNC SIN')
StartFREQ = (100)
FREQ=StartFREQ
StopFREQ=(1000000)
AMPL=StartAMPL =(5)
AMPLSteps=1
AMPLinc=0
wait=0
FREQSteps=100 # I've notest some missing steps 
incFREQ=StopFREQ/FREQSteps

FREQSet=("SOUR1:FREQ "+ str(FREQ))
FuncGen.write(FREQSet)      
print("VP2P=",osc.query('MEASUrement:IMMed:VALue?'))
print(incFREQ)

osc.write('MEASUREMENT:IMMED:TYPE PK2')  
sig=[]
siginfo=[]
phasig=[]
for i in range(AMPLSteps):
    AMPLSet=("SOUR1:AMPL "+ str(AMPL))
    FuncGen.write(AMPLSet) 
    AMPL = AMPL + AMPLinc
    print("inc up =",AMPL)    
    for j in range(FREQSteps):
        FREQSet=("SOUR1:FREQ "+ str(FREQ))
        print("FREQ changed to =",FREQSet)
        FuncGen.write(FREQSet)      
        if FREQ>=StopFREQ:
            print("end")
            break
        FREQ = FREQ + incFREQ                                      #    APPL responeds in the same formate as it is requested in "" but in the manual this is not show 
        time.sleep(wait)
        #print(j)
        if 1:
            
            #print("Set Data Source",osc.write("DATA:SOURCE CH1"))  #    I can run this as I've already defined the output settings in Buffer read
            #CH1 = osc.query_binary_values('CURV?', datatype='h')	
            #MAX= np.max(CH1)
            #MIN=np.min(CH1)      
            osc.write('MEASUREMENT:IMMED:TYPE PK2')  
            VP2P=osc.query('MEASUrement:IMMed:VALue?') # the actual value in volage that i want 

            #print("Set Data Source",osc.write("DATA:SOURCE CH2"))  
            #CH2 = osc.query_binary_values('CURV?', datatype='h')
            
            
            #print("Measured Units=",osc.query('MEASUrement:IMMed:UNIts?'))
            #print("VP =",VP2P)
            siginfo.extend([FREQ])
            sig.extend([float(VP2P)])
            
            osc.write('MEASUREMENT:IMMED:TYPE PHA')  
            Phase=osc.query('MEASUrement:IMMed:VALue?')
            phasig.extend([float(Phase)])
           
            
            
            if 0:
                plt.plot(CH2, lw = 0.5, label = str(FREQ)+"Hz")
                plt.plot(CH1, lw = 0.5, label = str(FREQ)+"Hz")
                FigName=("C:/Users/micha/instCtrl/commands/"+time.strftime("%Y-%m-%d")+'/'+str(j)+"At"+str(AMPL)+"Vand"+str(FREQ)+"Hz.jpg")
                
                #plt.legend( )
                plt.savefig(str(FigName))
                
    

MAX=np.amax(sig)                                                            #AMAX is more accurate (not rounding)
print("max =",MAX)
aver= np.mean(np.array(sig))
print("aver =",aver)
MIN=np.min(np.array(sig))
print("MIN =",MIN)

plt.plot(siginfo,sig,'RED', lw = 0.4)
#plt.plot(siginfo,phasig,'BLUE', lw = 0.4)
plt.xlabel('Voltage Peak to Peak')  # Add an x-label to the Axes.
plt.ylabel('Frequency ')  # Add a y-label to the Axes.
plt.title(str(StartAMPL)+"Amp input")
plt.xlim([StartFREQ, StopFREQ])
plt.xscale('linear')
plt.ylim( [0, MAX+1])
plt.grid(True)
#FigName=("C:/Users/micha/instCtrl/commands/"+time.strftime("%Y-%m-%d")+'/'+"peak Voltage-"+str(StartAMPL)+"V-P2PVoltsfrom"+str(StartFREQ)+"-"+str(StopFREQ)+"Hz.jpg")
#plt.savefig(str(FigName))
plt.show()
sys.exit(0)
#print("test output",sig[1])


POS=1
for i in range(len(sig)):
    if POS >= len(sig):
        print("do")
        break
    else:
        plt.plot(sig[POS-1],'RED', lw = 0.4, label = "Ch1")
        #plt.plot(sig[POS],'BLUE', lw = 0.4, label = "Ch2")
        plt.legend()
        FigName=("C:/Users/micha/instCtrl/commands/"+time.strftime("%Y-%m-%d")+'/'+str(j)+"At"+str(siginfo[POS-1])+"Vand"+str(siginfo[POS])+"Hz.jpg")
        plt.savefig(str(FigName))
        plt.show()
        print(POS)
        POS=(2+POS)
        
sys.exit(0)
xn = sine_wave 
hn = np.array( [ -1, 2, 1, -1] )
yn = np.convolve( xn, hn )

if 0:
	plt.plot( yn, 'k', lw = 0.6 )
	plt.show( )

pktSize = 100
B = len(hn-1)
xn1 = xn[0:pktSize] #orginal 
xn2 = xn[pktSize-B:2*pktSize+B]
xn3 = xn[2*pktSize-B:3*pktSize+B]
xn4 = xn[3*pktSize-B:4*pktSize+B]

yn1 = np.convolve( xn1, hn )
yn2 = np.convolve( xn2, hn )
yn3 = np.convolve( xn3, hn )
yn4 = np.convolve( xn4, hn )

yn1 = yn1[0:pktSize]
yn2 = yn2[B:B+pktSize ]
yn3 = yn3[B:B+pktSize ]
yn4 = yn4[B:B*2+pktSize]

yAll = np.concatenate( ( yn1, yn2, yn3, yn4 ) )

if 1:
	plt.plot( yn, 'k', lw = 0.6 )
	plt.plot( yAll, 'r', lw = 0.6 )
	plt.show( )

if 0:
    try:
        X=4         #j
        Y=2         #i
    except:
        X=5         #j
        Y=5         #i
    print("this should be 40 or 20 ",len(sig))
    figure, axis = plt.subplots(Y, X)
    print(POS)
    for i in range(Y):
        for j in range(X):
            if POS >= len(sig):
                break
            else:
                axis[i, j].plot(sig[POS-1],'b', lw = 0.5, label = "Ch2")
                axis[i, j].plot(sig[POS],'r', lw = 0.5, label = "Ch1")
                axis[i, j].set_title("Sine Function")
                POS=(2+POS)
            
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
