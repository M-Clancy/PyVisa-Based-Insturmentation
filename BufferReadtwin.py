
#
#	This origranne started on 2025-01-29 system argumants for insterment identifaction
#
import matplotlib.pylab as plt
import sys
import pyvisa as visa

# Generated from BufferRead-02.py 

Resource = visa.ResourceManager()
print(Resource.list_resources() ) 		
osc = Resource.open_resource('USB0::0x0699::0x0368::C021301::INSTR')
txtVar = (print(Resource.open_resource('USB0::0x0699::0x0368::C021301::INSTR').query( "*IDN?" )))
print("header off",osc.write('HEADER OFF')) 
print("Set Data Source",osc.write("DATA:SOURCE CH1"))              #    Selects the channel to be read
print("Confirm Data Source",osc.query("DATA:SOURCE?"))             #    Confirms the channel selected 
print("sets the waveform data encoding method to MSB",osc.write("DATA:ENCDG RIBINARY"))   
EncodingMethod = osc.query("DATA:ENCDG?")                          #    Confirms the Encoding metod as Read Binary MSB
WaveFormPreamble = osc.query("WFMpre?")                            #    returns the Waveform Preamble 
NumPoints = osc.query("WFMpre:NR_Pt?")                             
#0 read returning info through pyVISA
#1 read turning data usinf rb (readbinary)
#2 decode data usinf the int16 formate
#3 plot on matplot


CH1= osc.query_binary_values('CURV?', datatype='h')					#   WORKS


print("Set Data Source",osc.write("DATA:SOURCE CH2"))               #   Selects the channel to be read 



CH2 = osc.query_binary_values('CURV?', datatype='h')				


plt.plot(CH1,'r', lw = 0.4, label = "Ch1")                          #   Generates a plot from channel 1 that is read and labeled  

plt.plot(CH2,'b', lw = 0.4, label = "Ch2")                          #   generates a Plot that will be produced on the next PLT.show
plt.legend( )                                                       #   Adds a Legend or key to the plot
plt.title( txtVar )                                                 #   Sets the title to the name of the device
plt.show()                                                          #   Creats a plot with all of the above plt. items 