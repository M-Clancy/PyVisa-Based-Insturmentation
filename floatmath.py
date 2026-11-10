
import sys
import matplotlib.pylab as plt
import numpy as np


x = +18.33216394E-04
y = +9.35694394E-04
Z = -1.33848040E-04

F = float(x)+float(y)
print(F)
if float(x) < float(y) and float(x) > 0:
    
    Diff=float(x)-float(y)
    print(Diff,"DIFF")

F = float(Z)-float(y)

print(F)