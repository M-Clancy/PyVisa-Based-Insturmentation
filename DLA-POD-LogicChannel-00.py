
#
#	This origranne started on 2025-04-32 system argumants for insterment identifaction ON R&S
#
import matplotlib.pylab as plt
import cv2 
import numpy as np
import sys
import pyvisa as visa
import os
import time

filepath=("C:/Users/micha/instCtrl/commands/"+time.strftime("%Y-%m-%d")+"/")
if not os.path.exists(filepath):       #       Confirms the Existance of a folder of the following name  
   os.makedirs(filepath)               #       and then Creats it if it does not exists

Resource = visa.ResourceManager()
#print(Resource.list_resources() ) 		
osc = Resource.open_resource('USB::0x0AAD::0x0119::032993293::INSTR')
#print("Oscilloscope = ",Resource.open_resource('USB::0x0AAD::0x0119::032993293::INSTR').query( "*IDN?" ))
osc.write("BUS1:STATe ON")
osc.write('BUS1:TYPE PAR')
if 0:
    print("FORMat = ",osc.query("BUS2:FORMat?")) # is HEX set to BINARY
    print("FORMat change = ",osc.write("BUS2:FORMat BIN"))
    print("FORMat = ",osc.query("BUS2:FORMat?")) # IS not BINARY
if 0:
    osc.write("BUS1:CAN:DATA:SOURce D0")
    osc.query('BUS1:CAN:FRAMe1:STATus?')
    WaveForm=osc.query('BUS1:CAN:FRAME1:DATA?')
    
    
if 0:
    osc.write("BUS2:I2C:CLOCk:SOURce CH2")#Just usingchannel 2 as it can be connected to a prob
    osc.write("BUS2:I2C:DATA:SOURce D0")
    WaveForm = osc.query('BUS2:I2C:FRAME1:DATA?')
    
if 0:
    osc.write("BUS1:SPI:CLOCk:SOURce CH2")#PARallel
    osc.write("BUS1:SPI:DATA:SOURce D0")
    WaveForm = osc.query('BUS1:SPI:FRAME1:DATA?')
if 1:
    #print("Frame Status",osc.query("BUS1:PARallel:STATus?"))
    #osc.write("BUS1:PAR:CLOCk:SOURce CH2")#PARallel
    osc.write("BUS1:PAR:DATA0:SOURce D0")
    if 0:
        try:
            print("Attempting")
            print("Parrallel reading",osc.query("BUS1:PAR:DATA0?"))
        except:
            print("Error list \n",osc.query("SYSTem:ERRor:ALL?"))
    
    osc.write("BUS1:PAR:DATA1:SOURce D1")
    osc.write("BUS1:PAR:DATA2:SOURce D2")
    osc.write("BUS1:PAR:DATA3:SOURce D3")
    #WaveForm = osc.query('BUS1:PARallel:FRAME1:DATA?') #NO FRAME
    WaveForm=osc.query('POD:DATA?')
if 0:
    print("Frame Status",osc.query("BUS1:LIN:FRAME1:STATus?"))    #
    osc.write('BUS1:LIN:DATA:SOURce D0') #Difference in Can and LIN
    osc.write("BUS1:LIN:CLOCk:SOURce CH2")
    #WaveForm = osc.query('BUS1:LIN:FRAME1:DATA?')					#no work right
    
    
if 0:
    osc.write("BUS2:STATe ON")
    osc.write('BUS2:TYPE LIN')
    osc.write('BUS1:LIN:DATA:SOURce D0') #Difference in Can and LIN
    osc.write("BUS1:LIN:CLOCk:SOURce CH2")
    WaveForm = osc.query('BUS1:LIN:FRAME1:DATA?')					#no work right
    
    
if 0:
    osc.write('EXPort:WAVeform:SOURce D0')				## ment to be general	
    osc.write('EXPort:WAVeform:NAME "/USB_REAR/UINT16/TESTDIGITALREAD"')	

if 1:
    #print(WaveForm)
    print("info,",(osc.query('POD:DATA:HEADer?')))
    print("info StartTime,StopTime,Samples,Sample Interval")
    data = []
    print("amount of commas",(WaveForm.count(',')))
    
    print("amount of RTZ&NL",(WaveForm.count('\r\n')))
    
    print("amount of samples",(WaveForm.count('E')))
    
    print('amount of ""',(WaveForm.count('"')))
    
    #print(WaveForm)
    with open(filepath+time.strftime("%H-%M")+".txt", "w") as f:   # Opens file and casts as f 
        f.write("info,"+osc.query('POD:DATA:HEADer?')+"\n"+WaveForm)
    #for "\r\n" in WaveForm:
    #    player, stats, outcome, date = 
    #    (item.strip() for item in WaveForm.split(',', 9))
    #    stats = dict(zip(('Time', '0', '1',"2",'3',"4",'5',"6",'7'), map(int, stats.split('/'))))
    if 0:
        for i in WaveForm:
            if len(i) == 2:
                i = i[:1] + tuple(i[1].count('/r', ""))
            #data.append(tuple(i[1].count('/r')))
            
        #print("info =",data)

    if 0:
        txtVar = "Something Else"
        plt.plot((time), 'r', lw = 0.4, label = "Ch1")
        plt.legend( )
        plt.title( txtVar )
        plt.show()
lst = []

if 0:           #interesting code
    for i, tup in enumerate(data):
        if len(tup) == 2:
            data[i] = tup[:1] + tuple(tup[1].split(' - '))