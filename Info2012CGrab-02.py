import sys
import time
import pyvisa as visa
import numpy as np 
import matplotlib.pylab as plt
import re #pip install regex

Resource = visa.ResourceManager() #list Resources 
print(Resource.list_resources()) #Print listed Resources
tds2012C = Resource.open_resource('USB::0x0699::0x0362::C104603::INSTR') #Oscilloscope
#Assigns a value to the open resource for the visa Resource 
if 1: #Data Logging Commands set if to 1 to run page 31
    print("showing general info ")
    print( "Tektronix MSO2012 =",tds2012C.query( "*IDN?" ) ) # gives details of device
    print("\n Tektronix MSO2012 info  =",tds2012C.query('ID?'))
if 0: # proof for value interaction simplafied not really useful right now but good to have a small win 
    tds2012C.write('HEADer?') #if i break down the query into write and read allows me to assign values read for the osciloscope
    head = tds2012C.read() # example
    print("\n header status =", tds2012C.query('HEADer?')) #header prints the header of querys  (the first bit) 
     
    print((re.findall(':head 0|(0)',head)))
    if (re.findall(':head 0|(0)',head)): #quoted strings ASCII
        print("\n --activating header to save hands--\n ")
        tds2012C.write('HEADer ON') #remove curly brackets to work ( that too a while)
        #this also adds the header to saved commands ie :HEAD 1 when on & 0 when off
        print("\n header status =", tds2012C.query('HEADer?'))
    elif re.findall((':head 1|1'),head):
        print("\n --header activated hands safe--\n --toggling off--\n")
        tds2012C.write('HEADer OFF') #PLACED HERE TO TEST TOGGLE BETWEEN RUNS ~(TO SEE IF OSC saves that)
    else :
        print("error")
    print("header test =",tds2012C.query('MEASUREMENT?'))
if 0: #Data Logging Commands set if to 1 to run page 31
 print("test")
    
if 0: #MEASUREMENT:IMMED test pg 41
    tds2012C.write("MEASUrement:IMMed:SOUrce1 CH1")
    print("reading source =",tds2012C.query("MEASUrement:IMMed:SOUrce1?")) #MEASUrement:IMMed:SOUrce[1]? IS WRONG THERE IS NO BRACKETS 
    #tds2012C.write('COUNTERFREQ:CH1STATE ON')
    #print("what stste counter freq ? =",tds2012C.query('COUNTERF:CH1S?') ) 
    #print("Reading FREQ =",tds2012C.query("COUNTERFreq?")) #test in collage
    tds2012C.write('MEASUREMENT:IMMED:TYPE FREQ')
    print("Measure FREQ=",tds2012C.query('MEASUREMENT:IMMED:TYPE?'))  #PHA = phase
    #TEST MEASUrement:MEAS<x>:TYPe NEXT (NOT PREFARED WAY) WFFREQ measures using min man high low method
    #print("PAUSE =",tds2012C.write("ACQuire:STATE {RUN}"))
    #print("reading source =",tds2012C.query("MEASUrement:IMMed:SOUrce1?")) #this placed here prevents further errors does not prevent
    print("Measured Units=",tds2012C.query('MEASUrement:IMMed:UNIts?'))
    print("Measured Value=",tds2012C.query('MEASUrement:IMMed:VALue?'))#9.9E37 means error make sure to set channel like on line 37 .... why broken :(
    # adding *ESR? so errors are 16 not 9.9E37 MEASUrement:IMMed:SOUrce[1]?
    # measures frequency and all involved 
    print("Measured How=",tds2012C.query('ACQuire?'))
    tds2012C.write('*CLS')
if 1: #mean
    #tds2012C.write("ACQUIRE:STATE OFF")
    #tds2012C.write("SELECT:CH1 ON")
    #tds2012C.write("HORIZONTAL:RECORDLENGTH 1000")
    #tds2012C.write("ACQUIRE:MODE SAMPLE") 
    tds2012C.write('MEASUREMENT:IMMED:TYPE {MEAN}')
    tds2012C.write("MEASUrement:IMMed:SOUrce1 CH1")
    print("reading source =",tds2012C.query("MEASUrement:IMMed:SOUrce1?"))  
    print("Measure AMP=",tds2012C.query('MEASUREMENT:IMMED:TYPE?'))  #PHA = phase
    
    #TEST MEASUrement:MEAS<x>:TYPe NEXT (NOT PREFARED WAY) WFFREQ measures using min man high low method
    #print("PAUSE =",tds2012C.write("ACQuire:STATE {RUN}"))
    #print("reading source =",tds2012C.query("MEASUrement:IMMed:SOUrce1?")) #this placed here prevents further errors does not prevent
    print("Measured Units=",tds2012C.query('MEASUrement:IMMed:UNIts?'))
    print("Measured Value=",tds2012C.query('MEASUrement:IMMed:VALue?'))#9.9E37 means error make sure to set channel like on line 37 .... why broken :(
    # adding *ESR? so errors are 16 not 9.9E37 MEASUrement:IMMed:SOUrce[1]?
    # measures frequency and all involved 
    

if 1: # what am i measuring and abrevation test
    tds2012C.write('INITIATE_CLEAR')#
    tds2012C.write('DCL')#
    tds2012C.write('USBTMC INITIATE_CLEAR')#
    tds2012C.write('CHECK_CLEAR_STATUS')
    #print("Cleared? = ",tds2012C.query('CHECK_CLEAR_STATUS'))
    tds2012C.write("MEASUrement:IMMed:SOUrce1 CH1")
    print("reading source =",tds2012C.query("MEASUrement:IMMed:SOUrce1?"))
    tds2012C.write('MEASUREMENT:IMMED:TYPE AMPLITUDE')  
    print("Measure NOT FREQ =",tds2012C.query('MEASUREMENT:IMMED:TYPE?'))
    print("Measured Units=",tds2012C.query('MEASUrement:IMMed:UNIts?'))
    print("Measured Value=",tds2012C.query('MEASUrement:IMMed:VALue?'))
    
if 0: # what am i measuring and abrevation test
    print("Measured=",tds2012C.query('MEASUREMENT?'))  #what im measuring (manually) , 
    print("Measured=",tds2012C.query('MEASUrement?'))
    print("Measured=",tds2012C.query('MEASU?'))#testing abrevation
    print("Measured=",tds2012C.query('MEASUrement:IMMed?'))#Do colons break everything ? anser no
    
    
    #TEST MEASUrement:MEAS<x>:TYPe NEXT (NOT PREFARED WAY)
    #print("PLAY =",tds2012C.write("ACQuire:STATE {STOP}"))
    #tds2012C.write("MEASUrement:SNAPSHOT")  #no work on this model 1000B only
if 0: #MEASUREMENT: test pg 41
    print("measured =",tds2012C.write("MEASUREMENT"))
    #print("measured IMMED =",tds2012C.query("MEASUrement:IMMed?"))     #dont query it break but only query ? see page 137 set units to measure first
    #print("measured IMMED Units  =",tds2012C.query("MEASUrement:IMMed:UNIts?")) # error why, no measure?
    #tds2012C.write("MEASUrement:SNAPSHOT")  #no work on this model 1000B only
#if 0: #MEASUREMENT: Source 1 set measurement 
    #tds2012C.write("MEASUrement:SNAPSHOT")  #no work on this model 1000B only

#if 0: #examples form signal grab
#    print( "Tektronix MSO2012  reads Current Settings =", tds2012C.query( "ACQuire?" ) )
    #Returns current acquisition settings. not all querys require *
#    print( "Tektronix MSO2012  reads Current Mode =", tds2012C.query( "ACQuire:MODe?" ) )


#print( "Tektronix MSO2012  reads Current Mode =", tds2012C.query( "ACQuire:NUMACq?" ) )

