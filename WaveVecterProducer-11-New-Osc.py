
#
#	This origranne started on 2025-02-14 system argumants for insterment identifaction
#

import matplotlib.pylab as plt
import numpy as np
import sys
import pyvisa as visa
import time                                                                 #   for delays and time test
import re                                                                   #   Not needed for this program       

import os

#has in heritance from WaveVectorProducter-10-updatedVaribles added automated selecting and more varables 

if not os.path.exists("C:/Users/micha/instCtrl/commands/"+time.strftime("%Y-%m-%d")+"/"):       #       Confirms the Existance of a folder of the following name  
   os.makedirs("C:/Users/micha/instCtrl/commands/"+time.strftime("%Y-%m-%d")+"/")               #       and then Creats it if it does not exists
#tick=time.strftime("%H,%M,%S")
def InstraSel(con):                                                                             #       Perviously disscribed 
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


Resource = visa.ResourceManager()					                                      
con = Resource.list_resources() 			
FuncGen = Resource.open_resource('ASRL5::INSTR')
osc = Resource.open_resource('USB0::0x2A8D::0x039B::CN61381361::INSTR')
if 1:                                                               #       used system argumants as there are a lot of them as such defaults are needed     
    try:
        StartFREQ =(sys.argv[1])
        StartFREQ =int(StartFREQ)
        StopFREQ=(sys.argv[2])
        StopFREQ =int(StopFREQ)
        FREQSteps =(sys.argv[3])
        FREQSteps =int(FREQSteps)
        AVER=(sys.argv[4])
        AVER =int(AVER)
    except: 
        StartFREQ = (10000)
        StopFREQ = (5000000)
        FREQSteps = 10000                                            #       checks at a frequency of what evers below the line 
        AVER = 2
    #add Osc channel                                                #       Add line for selecting OSC scope channel

#osc.write('MEASUREMENT:IMMED:TYPE PHA')                            #       Sets IMMED measurement type PHAse
#print("Measured Units=",osc.query('MEASUrement:IMMed:UNIts?'))     #       Asks what are the Units returned in
FuncGen.write('SOUR1:FUNC SIN')

FREQ=StartFREQ

StartAMPL=2
AMPL=StartAMPL
AMPLSteps=1
AMPLinc=0
wait=0.0001

#incFREQ=(StartFREQ/StopFREQ)*FREQSteps+1
#incFREQ=StopFREQ/FREQSteps                                         #       Pervious ways of incrementing between the frequencies

#osc.write('CH1:SCALE 5')
FREQSet=("SOUR1:FREQ "+ str(FREQ))
osc.write(':CHANnel1:OFFSet 0')
TBCommand=(":TIM:SCAL ")
scaleCommand=('CHAN1:SCALE ')
scaleyn = True
FuncGen.write(FREQSet)      
print("incramenting at ",FREQSteps)

osc.write('MEASUREMENT:IMMED:TYPE PK2')  
sig2=[]                                                             #       Lists used to extract data in a fast and easy manner
sig=[]
siginfo=[]
phasig=[]


for i in range(AMPLSteps):
    AMPLSet=("SOUR1:AMPL "+ str(AMPL))
    FuncGen.write(AMPLSet) 
    AMPL = AMPL + AMPLinc
    #print("inc up =",AMPL)    
    for j in range(StartFREQ,StopFREQ,FREQSteps):                    #      Move J from StartFREQ to StopFREQ in size of FREQSteps
        FREQSet=("SOUR1:FREQ "+ str(FREQ))
        #print("FREQ changed to =",FREQSet)
        FuncGen.write(FREQSet) 
        if FREQ>=StopFREQ:                                           #      Is added as i was confirming the if the same error seen when reciveing the CURV query was consistent here
            print("end")
            break
        elif FREQ>=10 and FREQ < 250:
            TimeBase=(str(TBCommand)+'25E-3')
            osc.write(TimeBase)                 #  sets the time/base scale when between the set frequencys 
            
            if scaleyn:
                Vscale(str(scaleCommand)+20E-0)
                osc.write(Vscale)                                     #  Sets the SCale of the Voltage to 2 Volts (this is all on channel 1)
        elif FREQ>=250 and FREQ < 1000:
            TimeBase=(str(TBCommand)+'10E-3')
            osc.write(TimeBase)
            if scaleyn:
                osc.write('CHAN1:SCALE 20E-0')
        elif FREQ>=1000 and FREQ < 10000:
            TimeBase=(str(TBCommand)+'250E-6')
            osc.write(TimeBase)
            if scaleyn:
                Vscale(str(scaleCommand)+20E-0)
                osc.write(Vscale)  
        elif FREQ >=10000 and FREQ < 50000:
            if scaleyn:
                osc.write('CHAN1:SCALE 20')
            TimeBase=(str(TBCommand)+'100E-6')
            osc.write(TimeBase)
        elif FREQ >=50000 and FREQ <70000:
        
            if scaleyn:
                Vscale(str(scaleCommand)+12E-0)
                osc.write(Vscale)
            TimeBase=(str(TBCommand)+'100E-6')
            osc.write(TimeBase)
            
        elif FREQ >=70000 and FREQ <200000:
            if scaleyn:
                Vscale(str(scaleCommand)+7.5E-0)
                osc.write(Vscale)  
            TimeBase=(str(TBCommand)+'5E-6')
            osc.write(TimeBase)
        elif FREQ >=200000 and FREQ <500000:
            TimeBase=(str(TBCommand)+'0.0000025')
            osc.write(TimeBase)
            if scaleyn:
                Vscale(str(scaleCommand)+3E-0)
                osc.write(Vscale)
                osc.write(':CHANnel1:OFFSet 3')
            #set vertical positions here for OSC if below 5 v scaling 
        elif FREQ >=500000 and FREQ < 2000000:
            TimeBase=(str(TBCommand)+'0.0000025')
            osc.write(TimeBase)
            if scaleyn:
                Vscale(str(scaleCommand)+3E-0)                      #      not need to increase at this point higher
                osc.write(Vscale)
                osc.write(':CHANnel1:OFFSet 3.75')                         
        elif FREQ >=2000000 and FREQ < 3000000:
            TimeBase=(str(TBCommand)+'500E-9')
            osc.write(TimeBase)
            #print(TimeBase)
            #osc.write('CH1:POS -1.5')
            if scaleyn:
                Vscale(str(scaleCommand)+2)
                osc.write(Vscale)
                osc.write(':CHAN1:OFFSet 10')
        elif FREQ >=3000000 and FREQ < 5000000:
            TimeBase=(str(TBCommand)+'250E-9')
            osc.write(TimeBase)
            if scaleyn:
                Vscale(str(scaleCommand)+2E-0)
                osc.write(Vscale)
                #osc.write('CH1:POS -1.5')
            
        FREQ = FREQ+FREQSteps                          #    Would require an exponently to get better readings
        time.sleep(wait)
        #print(j)
        if 1:
            
            #print("Set Data Source",osc.write("DATA:SOURCE CH1"))          #       I can run this as I've already defined the output settings in Buffer read
            #CH1 = osc.query_binary_values('CURV?', datatype='h')	
            #MAX= np.max(CH1)
            #MIN=np.min(CH1)      
            
            #osc.write("MEASUrement:IMMed:SOUrce1 CH1")                      #       Sets the channel thst is being read 
            for x in range(0,AVER):
                VP2P=osc.query(':MEAS:VPP? CHAN1')                  #       the actual value in volage that i want  
                x=x+1
            AVout= np.mean(np.array(float(VP2P)))                           #       Averages out the P2P voltage returned to try to improve accuracy                     
            #osc.write("MEASUrement:IMMed:SOUrce1 CH2")
            x=0
            for x in range(0,AVER):
                VP2PIN=float(osc.query('MEAS:VPP? CHAN2'))
                x=x+1
            x=0
            AVin= np.mean(np.array(VP2PIN))
            sig2.extend([AVin])                                             #       adds the new data to the list sig2 which is connected to channel 2 or the input
            #print("Set Data Source",osc.write("DATA:SOURCE CH2"))  
            #CH2 = osc.query_binary_values('CURV?', datatype='h')
            #VPeak=(float(VP2P)/2)
            #TRIGLEV=("TRIG1:A:LEV2"+ str(0.0))
            #osc.write(TRIGLEV))
            
            #print("Measured Units=",osc.query('MEASUrement:IMMed:UNIts?'))
            #print("VP =",VP2P)
            siginfo.extend([FREQ])                                          #       This list is used to get the fequency that is being measured at this point 
            sig.extend([AVout])                                             #       Gets the average voltage of the P2P Voltage on the output
            
            #osc.write('MEASUREMENT:IMMED:TYPE PHA')  
            #Phase=osc.query('MEASUrement:IMMed:VALue?')
            #phasig.extend([float(Phase)])
           
            
            
            if 0:
                plt.plot(CH2, lw = 0.5, label = str(FREQ)+"Hz")
                plt.plot(CH1, lw = 0.5, label = str(FREQ)+"Hz")
                FigName=("C:/Users/micha/instCtrl/commands/"+time.strftime("%Y-%m-%d")+'/'+str(j)+"At"+str(AMPL)+"Vand"+str(FREQ)+"Hz.jpg")
                
                #plt.legend( )
                plt.savefig(str(FigName))
                
    

MAX=np.amax(sig)                                                            #       AMAX is more accurate (not rounding)
print("max =",MAX)                                                          #       Displays the MAXimum value of the 
aver= np.mean(np.array(sig))                                                #       Gets the mean from the list sig which must be defined as a array for this to work        
print("aver =",aver)
MIN=np.min(np.array(sig))                                                   #       Gets the MINimum value from the sig list which must be fined as an array for this to work -- check
print("MIN =",MIN)

if 1:
    plt.plot(siginfo, sig, 'RED' , lw = 0.4, label = "Ch1")         #       Plots the data from the list sets its colour defines its width and lables it 
    plt.plot(siginfo,sig2, 'BLUE', lw = 0.4, label = "Ch2")
    #plt.plot(siginfo,phasig,'BLUE', lw = 0.4)
    plt.xlabel('Frequency')             #       Add an x-label to the Axes.
    plt.ylabel('Voltage Peak to Peak')  #        Add a y-label to the Axes.
    plt.title(str(StartAMPL)+"Amp input")
    plt.xlim([StartFREQ, StopFREQ])     #       sets the limit of the x axis 
    plt.legend()
    plt.yscale('log')                   #       Sets that axis of the Plot to Logoritmic
    plt.xscale('log')
    #plt.ylim( [0, MAX+1])
    plt.grid(True)
    FigName=("C:/Users/micha/instCtrl/commands/"+time.strftime("%Y-%m-%d")+'/'+time.strftime("%H-%M")+"Dev-3-LessWires-Keysite-"+str(StartAMPL)+"V-P2PVoltsfrom"+str(StartFREQ)+"-"+str(StopFREQ)+"Hz.jpg")
    plt.savefig(str(FigName))           #       Adds the file to the location defined in the FIGname which is the date and time of creation of folder and figure
    plt.show()                          #       Displaying the Plot should be done after saving the Plot
    sys.exit(0)
    #print("test output",sig[1])


POS=1
for i in range(len(sig)):
    if POS >= len(sig):
        print("do")
        break
    else:
        plt.plot(siginfo,sig[POS-1],'RED', lw = 0.4, label = "Ch1")
        plt.plot(siginfo,sig[POS],'BLUE', lw = 0.4, label = "Ch2")
        plt.xlabel('Frequency')  # Add an x-label to the Axes.
        plt.ylabel('Voltage Peak to Peak')  # Add a y-label to the Axes.
        plt.title(str(StartAMPL)+"Amp input")
        plt.xlim([StartFREQ, StopFREQ])
        plt.legend( )
        plt.yscale('log')
        plt.xscale('log')
    
        plt.grid(True)
        FigName=("C:/Users/micha/instCtrl/commands/"+time.strftime("%Y-%m-%d")+'/'+time.strftime("%H-%M")+"Dev-1-LessWires-NoGain-"+str(StartAMPL)+"V-P2PVoltsfrom"+str(StartFREQ)+"-"+str(StopFREQ)+"Hz.jpg")
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
