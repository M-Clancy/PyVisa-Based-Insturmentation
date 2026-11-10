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
    floats = []
    with open(filename, 'r') as file:
        for line in file:
            # Find all numbers including decimals using regex
            found = re.findall(r"[-+]?\d*\.\d+|\d+", line)
            # Convert found strings to floats
            floats.extend([float(num) for num in found])
    return floats

# Example usage
file_path = 'C:/Users/micha/instCtrl/commands/2025-04-23/15-43.txt'
numbers = extract_floats_from_file(file_path)
print("Extracted numbers as floats:", numbers)
print("LEnght of x ", len(numbers))
#for i in range(0,len(numbers),2):
    
    
sys.exit(0)
plt.plot(numbers, 'RED' , lw = 0.4, label = "Ch1")         #       Plots the data from the list sets its colour defines its width and lables it 
#plt.plot(siginfo,sig2, 'BLUE', lw = 0.4, label = "Ch2")
#plt.plot(siginfo,phasig,'BLUE', lw = 0.4)
plt.xlabel('Time')             #       Add an x-label to the Axes.
plt.ylabel('Voltage')           #        Add a y-label to the Axes.
#plt.title(str(StartAMPL)+"Amp input")
#plt.xlim([StartFREQ, StopFREQ])     #       sets the limit of the x axis 
plt.legend()
#plt.yscale('log')                   #       Sets that axis of the Plot to Logoritmic
#plt.xscale('log')
#plt.ylim( [0, MAX+1])
plt.grid(True)
FigName=("C:/Users/micha/instCtrl/commands/"+time.strftime("%Y-%m-%d")+'/'+time.strftime("%H-%M")+"RampFunction.jpg")
plt.savefig(str(FigName))           #       Adds the file to the location defined in the FIGname which is the date and time of creation of folder and figure
plt.show()                          #       Displaying the Plot should be done after saving the Plot
sys.exit(0)