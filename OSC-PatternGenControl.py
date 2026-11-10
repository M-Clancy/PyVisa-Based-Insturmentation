import pyvisa as visa

#
#	This origrally started on 2025-04-04 for The control of Rohde & Schwarz RTC 1002 Oscilloscope
#


Resource = visa.ResourceManager()					                                      
con = Resource.list_resources() 			
#FuncGen = Resource.open_resource('ASRL5::INSTR')
osc = Resource.open_resource('USB0::0x0AAD::0x0119::104520::INSTR')

print(osc.query("*IDN?"))

#osc.write("PGENerator:PATTern:FREQuency 9600")
osc.write("PGENerator:PATTern:STATe OFF")
osc.write("PGENerator:MANual:STATe0 ON")
osc.write("PGENerator:FUNCtion ARBitrary")
#osc.write("PGENerator:PATTern:STATe ON")
print("Manual State = ",osc.query("PGENerator:MANual:STATe0?"))
print(osc.query("PGEN:FUNC?"))

if 0:
    osc.write("PGEN:FUNC ARBitrary")  #Standard Data rate 9600 Bit/s, 115.2 kBit/s and 1 MBit/s 
    #print("ERROR 1 is ",osc.query("SYSTEM:ERROR?"))
    #osc.write("PGENerator:PATTern:STATe ON")
    osc.write("PGENerator:PATTern:ARBitrary:DATA:APPend 333A") #displays bits in Hex code
    #print("ERROR 2 is ",osc.query("SYSTEM:ERROR?"))


