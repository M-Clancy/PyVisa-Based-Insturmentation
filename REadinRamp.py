#
#       this origranne started on 2025-05-23 convert to be read by math plot lib
#
#       Child of Read in to Plt 1
import re
import matplotlib.pylab as plt
import numpy as np
import sys

import time                                                                 #   for delays and time test
import re                                                                   #   Not needed for this program       

import os


if not os.path.exists("C:/Users/micha/instCtrl/commands/"+time.strftime("%Y-%m-%d")+"/"):       #       Confirms the Existance of a folder of the following name  
   os.makedirs("C:/Users/micha/instCtrl/commands/"+time.strftime("%Y-%m-%d")+"/")               #       and then Creats it if it does not exists
#tick=time.strftime("%H,%M,%S")

def extract_floats_from_file(filename):
    time = []
    data = []
    with open(filename, 'r') as file:
        for line in file:
            # Find all numbers including decimals using regex
            Val = re.findall(r",[0|1]",line)
            info = [item.replace(",","") for item in Val]
            
            #info = [item.replace(",","") for item in clean]
            #separate = re.findall(r"[-+]?\d*\.\d+|\d+", data)
            sampletimes = re.findall(r"[-+]?\d*\.\d+E[+-]\d+",line)
            #print(time)
            # Convert found strings to floats
            time.extend([float(times)] for times in sampletimes)
            data.extend([num for num in info])
    return time, data

# Example usage
file_path = "C:/Users/micha/instCtrl/commands/2025-05-27/11-59output.txt"#15-46-D0was touchingD2
Times, Data = extract_floats_from_file(file_path)
lenght=len(Data)-1
#print("Extracted numbers as floats:", Data)
print("LEnght of x ", lenght)

if 0:
    for i in range(lenght):
        #print("test",i)
        if i%8 == 0:
            D0.append(Data[i])
            D1.append(Data[i-1])
            D2.append(Data[i-2])
            D3.append(Data[i-3])
            D4.append(Data[i-4])
            D5.append(Data[i-5])
            D6.append(Data[i-6])
            D7.append(Data[i-7])
        
    

plt.plot(Times, 'RED', lw = 0.5, label = "Mult reading")

plt.xlabel('Time')             #       Add an x-label to the Axes.
plt.ylabel('Voltage')           #        Add a y-label to the Axes.
#plt.title(str(StartAMPL)+"Amp input")
#plt.xlim([Start, Stop])     
plt.legend()
#plt.yscale('log')                   #       Sets that axis of the Plot to Logoritmic
#plt.xscale('log')
#plt.ylim( [0, MAX+1])
plt.grid(True)
FigName=("C:/Users/micha/instCtrl/commands/"+time.strftime("%Y-%m-%d")+'/'+time.strftime("%H-%M")+"RampFunction.jpg")
plt.savefig(str(FigName))           #       Adds the file to the location defined in the FIGname which is the date and time of creation of folder and figure
plt.show()                          #       Displaying the Plot should be done after saving the Plot
sys.exit(0)