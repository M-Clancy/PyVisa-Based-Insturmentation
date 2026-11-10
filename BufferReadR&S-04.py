
#
#	This origranne started on 2025-01-31 system argumants for insterment identifaction ON R&S
#
import matplotlib.pylab as plt
import cv2 
import sys
import pyvisa as visa

Resource = visa.ResourceManager()
print(Resource.list_resources() ) 		
osc = Resource.open_resource('USB::0x0AAD::0x0119::032993293::INSTR')
print("Oscilloscope = ",Resource.open_resource('USB::0x0AAD::0x0119::032993293::INSTR').query( "*IDN?" ))
#print("header state",osc.query('CHAND0:DATA:HEAD?')) # Start time , stop time, number of samples, samples per interval 

#sys.exit(0)
#print("sets the waveform data encoding method to MSB First",osc.write("FROM:BORD MSBF"))   
#print("sets the waveform data encoding method UINT16",osc.write("FROM:DATA UNIT, 16"))   
    
if 0:
    
    EncodingMethod = osc.query("DATA:ENCDG?")
    print("EncodingMethod = ",EncodingMethod)
    WaveFormPreamble = osc.query("WFMpre?")
    print("WaveFormPreamble = ",WaveFormPreamble)
    NumPoints = osc.query("WFMpre:NR_Pt?")
    print("NumPoints = ",NumPoints)

osc.write('EXPort:WAVeform:SOURce D0')					
osc.write('EXPort:WAVeform:NAME "/USB_REAR/UINT16/TESTDIGITALREAD"')					
#osc.write('EXPort:WAVeform:SAVE')					


osc.write('BUS1:LIN:DATA:SOURce D0')	
WaveForm = osc.query('BUS1:LIN:FRAME1:DATA?')					#no work right
print(WaveForm)
txtVar = "Something Else"
plt.plot(WaveForm, 'r', lw = 0.4, label = "Ch1")
plt.legend( )
plt.title( txtVar )
plt.show()