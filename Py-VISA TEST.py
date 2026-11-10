import pyvisa
rm = pyvisa.ResourceManager()
print(rm.list_resources())

#print("\nwho = ",rm.open_resource('ASRL8::INSTR').query( "*IDN?" ))

pyvisa.log_to_screen()