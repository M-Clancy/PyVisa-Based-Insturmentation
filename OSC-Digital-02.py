import pyvisa as visa

#
#	This origrally started on 2025-04-08 for The control of KeySIght 1052G Oscilloscope
#


Resource = visa.ResourceManager()					                                      
con = Resource.list_resources() 			
#FuncGen = Resource.open_resource('ASRL5::INSTR')
osc = Resource.open_resource('USB0::0x0AAD::0x0119::032993293::INSTR')

print(osc.query("*IDN?"))

