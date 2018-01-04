import random as rd
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from scipy import misc

fh = open("data/data_lr.csv","r")

x = []
y = []

for line in fh:
    tokens = line.split(",")
    x.append(tokens[0].strip())
    y.append(tokens[1].strip())

plt.plot(x[1:],y[1:],'o')

num_samples = len(x)
#y=1+bx

param_0 = 1
param_1 = round(rd.uniform(4,40),2)

def cost_i(num, x, y):
    return ( 1 / ( 2 * num_samples ) ) * ( ( THETA_0 + (theta_1 * x_i) - y_i ) ** 2 )

num_iters = 1
THETA_0, theta_1, x_i, y_i = symbols('THETA_0 theta_1 x_i y_i', float = True)
cost_i = ( 1 / ( 2 * num_samples ) ) * ( ( THETA_0 + (theta_1 * x_i) - y_i ) ** 2 )
deriv = Derivative(cost_i, theta_1)

alpha = 0.01

for i in range(num_iters):
    change = 0

    for k in range (1,num_samples):
        change+= deriv.doit().subs({THETA_0 : param_0, theta_1 : param_1, x_i : x[k], y_i : y[k] })
    param_1 = param_1 - (alpha * change)


plt.plot(x[1:], param_0 + (x[1:]*param_1))
plt.suptitle('Linear regression by gradient descent')
plt.xlabel('x')
plt.ylabel('y')

plt.show()
