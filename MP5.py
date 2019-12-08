import matplotlib.pyplot as mpp
from math import *
import numpy as np

print('        Machine Problem 5 (Python):          ')
print('Program should be tested using the equation below: ')
print('                                                  "MPx(np.sin((3*pi*B)/100))" ')

B = np.linspace(0,199,200)
def MP5x(Equationx):
    Equationy = np.zeros(200)
    for A in B:
        A = int(A)
        if A == 0:
            Equationy[A] = -1.5*Equationx[A] + 2*Equationx[A+1] - 0.5*Equationx[A+2]
        elif ((0 < A) and (A < 199)):
            Equationy[A] = 0.5*Equationx[A+1] - 0.5*Equationx[A-1]
        elif A == 199:
            Equationy[A] = 1.5*Equationx[A] - 2*Equationx[A-1] + 0.5*Equationx[A-2]
    mpp.plot(B,Equationx,label = 'Equationx(B)')
    mpp.plot(B,Equationy,label = 'Equationy(B)')
    mpp.legend()