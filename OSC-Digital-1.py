import pyvisa as visa

#
#	This origrally started on 2025-04-08 for The control of Rohde & Schwarz RTC 1002 Oscilloscope
#


Resource = visa.ResourceManager()					                                      
con = Resource.list_resources() 			
#FuncGen = Resource.open_resource('ASRL5::INSTR')
osc = Resource.open_resource('USB0::0x0AAD::0x0119::104520::INSTR')

print(osc.query("*IDN?"))

