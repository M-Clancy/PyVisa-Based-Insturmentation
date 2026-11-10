
#
#	This origranne started on 2025-01-31 system argumants for insterment identifaction ON R&S
#
import matplotlib.pylab as plt
import sys
import pyvisa as visa
import numpy as np



Resource = visa.ResourceManager()
print(Resource.list_resources() ) 		
osc = Resource.open_resource('USB0::0x0AAD::0x0119::104517::INSTR')
print("Oscilloscope = ",Resource.open_resource('USB0::0x0AAD::0x0119::104517::INSTR').query( "*IDN?" ))


if 0:
    HEAD=osc.query('CHAN1:DATA:HEAD?') # Start time , stop time, number of samples, samples per interval 
    print(HEAD)
    HEAD=HEAD.split(",")
    data = osc.query('CHAN1:DATA?')	
    sys.exit(0)
    StartT=(HEAD[0].replace("E","*10^"))
    StopT=(HEAD[1].replace("E","*10^"))
    s1,s2 = HEAD[0].split('E', 1)
    print(s1,s2)
    print(StopT)
    SampleRate=HEAD[2]
    duration = len(data) / int(SampleRate)
    time = np.arange(0, duration, 1/int(SampleRate))
    print(SampleRate)

    start_index = float(StartT) * int(SampleRate)
    stop_index = int(StopT * SampleRate)
        
    time_segment = osc.query_binary_values('CHAN1:DATA:ENV:XINC?', datatype='h')
    data_segment = osc.query_binary_values('CHAN1:DATA:ENV:YINC?', datatype='h')

osc.write('FORM UINT,16')
print("data form is =",osc.query('FORM?')) #sends the form of data 
waveform = osc.query_binary_values('CHAN1:DATA?', datatype='h')


if 0:
    #sys.exit(0)
    print("sets the waveform data encoding method to MSB First",osc.write("FROM:BORD MSBF"))   
    print("sets the waveform data encoding method UINT16",osc.write("FROM:DATA UNIT, 16"))   

    EncodingMethod = osc.query("DATA:ENCDG?")
    print("EncodingMethod = ",EncodingMethod)
    WaveFormPreamble = osc.query("WFMpre?")
    print("WaveFormPreamble = ",WaveFormPreamble)
    NumPoints = osc.query("WFMpre:NR_Pt?")
    print("NumPoints = ",NumPoints)
    

        

            #no work right
#plt.plot(time_segment, data_segment)
txtVar = "Something Else"
plt.plot(waveform, 'r', lw = 0.4, label = "Ch1")
plt.legend( )
plt.title( txtVar )
plt.show()


