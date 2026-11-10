import sys
import time
import pyvisa as visa
import numpy as np 
import matplotlib.pylab as plt
import re #pip install regex

Resource = visa.ResourceManager() #list Resources 
print(Resource.list_resources()) #Print listed Resources
tds2012C = Resource.open_resource("USB::0x0699::0x0368::C021301::INSTR")
#tds2012C = Resource.open_resource('USB::0x0699::0x0368::C021141::INSTR') #Oscilloscope
#Assigns a value to the open resource for the visa Resource 
if 1: #Data Logging Commands set if to 1 to run page 31
    print("showing general info ")
    print( "Tektronix MSO2012 =",tds2012C.query( "*IDN?" ) ) # gives details of device
    print("\n Tektronix MSO2012 info  =",tds2012C.query('ID?'))
    
if 1: #what commands work (with 1052B-EDU)
    tds2012C.write("MEASUrement:IMMed:SOUrce1 CH1")
    print("reading source =",tds2012C.query("MEASUrement:IMMed:SOUrce1?"))
    tds2012C.write('MEASUREMENT:IMMED:TYPE MEAN')  
    print("Measured Units=",tds2012C.query('MEASUrement:IMMed:UNIts?'))
    print("Measured Value=",tds2012C.query('MEASUrement:IMMed:VALue?'))
    print("Measure MEAN =",tds2012C.query('MEASUREMENT:IMMED:TYPE?'))
    tds2012C.write('MEASUREMENT:IMMED:TYPE FREQ')  
    print("Measure FREQ=",tds2012C.query('MEASUREMENT:IMMED:TYPE?'))
    print("Measured Units=",tds2012C.query('MEASUrement:IMMed:UNIts?'))
    print("Measured Value=",tds2012C.query('MEASUrement:IMMed:VALue?'))
    tds2012C.write('MEASUREMENT:IMMED:TYPE PERI')  
    print("Measure PERIod =",tds2012C.query('MEASUREMENT:IMMED:TYPE?'))
    print("Measured Units=",tds2012C.query('MEASUrement:IMMed:UNIts?'))
    print("Measured Value=",tds2012C.query('MEASUrement:IMMed:VALue?'))
    tds2012C.write('MEASUREMENT:IMMED:TYPE PK2')  
    print("Measure PKSpk =",tds2012C.query('MEASUREMENT:IMMED:TYPE?'))
    print("Measured Units=",tds2012C.query('MEASUrement:IMMed:UNIts?'))
    print("Measured Value=",tds2012C.query('MEASUrement:IMMed:VALue?'))
    tds2012C.write('MEASUREMENT:IMMED:TYPE MAXI')  
    print("Measure Max =",tds2012C.query('MEASUREMENT:IMMED:TYPE?'))
    print("Measured Units=",tds2012C.query('MEASUrement:IMMed:UNIts?'))
    print("Measured Value=",tds2012C.query('MEASUrement:IMMed:VALue?'))
    tds2012C.write('MEASUREMENT:IMMED:TYPE MINI')  
    print("Measure Mini=",tds2012C.query('MEASUREMENT:IMMED:TYPE?'))
    print("Measured Units=",tds2012C.query('MEASUrement:IMMed:UNIts?'))
    print("Measured Value=",tds2012C.query('MEASUrement:IMMed:VALue?'))
    tds2012C.write('MEASUREMENT:IMMED:TYPE RIS')  
    print("Measure RISE =",tds2012C.query('MEASUREMENT:IMMED:TYPE?'))
    print("Measured Units=",tds2012C.query('MEASUrement:IMMed:UNIts?'))
    print("Measured Value=",tds2012C.query('MEASUrement:IMMed:VALue?'))
    
    tds2012C.write('MEASUREMENT:IMMED:TYPE FALL')  
    print("Measure Fall=",tds2012C.query('MEASUREMENT:IMMED:TYPE?'))
    print("Measured Units=",tds2012C.query('MEASUrement:IMMed:UNIts?'))
    print("Measured Value=",tds2012C.query('MEASUrement:IMMed:VALue?'))
    
    
if 0: #that commands might work (with 1052B-EDU)
    tds2012C.write("MEASUrement:IMMed:SOUrce1 CH1")
    print("reading source =",tds2012C.query("MEASUrement:IMMed:SOUrce1?"))
    tds2012C.write('MEASUREMENT:IMMED:TYPE DEL')  
    print("Measure DELay =",tds2012C.query('MEASUREMENT:IMMED:TYPE?'))
    tds2012C.write('MEASUREMENT:IMMED:TYPE NWI')  
    print("Measure NWIdth =",tds2012C.query('MEASUREMENT:IMMED:TYPE?'))
    tds2012C.write('MEASUREMENT:IMMED:TYPE PDU')  
    print("Measure PDUty =",tds2012C.query('MEASUREMENT:IMMED:TYPE?'))
    tds2012C.write('MEASUREMENT:IMMED:TYPE PHA')  
    print("Measure Phase =",tds2012C.query('MEASUREMENT:IMMED:TYPE?'))
    tds2012C.write('MEASUREMENT:IMMED:TYPE AM')  
    print("Measure AMplitude =",tds2012C.query('MEASUREMENT:IMMED:TYPE?'))
    