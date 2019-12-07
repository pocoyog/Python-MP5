import numpy as np
import matplotlib.pyplot as plt 
import math
def MP5x(A):
    return math.sin((3*math.pi*A) / 100)

def MP5y(A):
    if A==0:
        return -1.5*MP5x(A) + 2*MP5x(A+1) - 0.5*MP5x(A+2)
    elif A>0 and A<=198:
        return 0.5*MP5x(A+1) - 0.5*MP5x(A-1)
    elif A==199:
        return 1.5*MP5x(A) - 2*MP5x(A-1) + 0.5*MP5x(A-2)

A_val = list(range(200))
x_val = [MP5x(A) for A in A_val]
y_val = [MP5y(A) for A in A_val]

plt.plot(A_val, x_val, label = 'Value of x(n)')
plt.plot(A_val, y_val, label = 'Value of y(n)')
plt.legend()
plt.show()