
#
#	This origranne started on 2025-01-31 system argumants for insterment identifaction ON R&S
#
import matplotlib.pylab as plt
import sys
import pyvisa as visa

Resource = visa.ResourceManager()
print(Resource.list_resources() ) 		
osc = Resource.open_resource('USB0::0x0AAD::0x0119::104517::INSTR')
print("Oscilloscope = ",Resource.open_resource('USB0::0x0AAD::0x0119::104517::INSTR').query( "*IDN?" ))
print("header state",osc.query('CHAN1:DATA:HEAD?')) # Start time , stop time, number of samples, samples per interval 

sys.exit(0)
print("sets the waveform data encoding method to MSB First",osc.write("FROM:BORD MSBF"))   
print("sets the waveform data encoding method UINT16",osc.write("FROM:DATA UNIT, 16"))   
    
if 0:
    
    EncodingMethod = osc.query("DATA:ENCDG?")
    print("EncodingMethod = ",EncodingMethod)
    WaveFormPreamble = osc.query("WFMpre?")
    print("WaveFormPreamble = ",WaveFormPreamble)
    NumPoints = osc.query("WFMpre:NR_Pt?")
    print("NumPoints = ",NumPoints)

WaveForm = osc.query('CHAN1:DATA?')					#no work right
print(WaveForm)
txtVar = "Something Else"
plt.plot(WaveForm, 'r', lw = 0.4, label = "Ch1")
plt.legend( )
plt.title( txtVar )
plt.show()


