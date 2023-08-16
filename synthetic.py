# synthetic.py
# --------------
# Copyright : (c) 2019, Germain Haessig <germain@ini.uzh.ch>
# Licence   : BSD3
#
# Generates fake data for the ScarpoCaccia projet.


import time
import numpy as np
import matplotlib.pyplot as plt

def solve_problem(dt):
    A = np.zeros((7,3))
    B = np.zeros(7)
    for i in range(7):
        A[i,0] = 2*(x[0] - x[i+1])
        A[i,1] = 2*(y[0] - y[i+1])
        A[i,2] = -2*c*dt[i]
        B[i] = np.power(c,2)*np.power(dt[i],2) + np.power(x[0],2) + np.power(y[0],2) - np.power(x[i+1],2) - np.power(y[i+1],2)
    sol = np.matmul(np.linalg.pinv(A),B)
    print(sol)
    return (np.arctan2(sol[1], sol[0])+np.pi)*180./np.pi-180.

times = []
positions = [[],[]]


L = 0.3
c = 340.

R = [0.5,1]
alpha = np.linspace(0.,2*np.pi,num=360, endpoint = False)

for r in R:
    for a in alpha:

        u = r*np.cos(a)
        v = r*np.sin(a)

        t = np.zeros(8)
        dt = np.zeros(7)

        x = np.zeros(8)
        y = np.zeros(8)



        for i in range(8):
            x[i] = L*np.cos(i*np.pi/4)
            y[i] = L*np.sin(i*np.pi/4)

        for i in range(8):
            t[i] = np.sqrt( np.power(u-x[i],2) + np.power(v-y[i],2) )/c

        for i in range(7):
            dt[i] = t[i+1]-t[0]

        times.append(t)
        positions[0].append(u)
        positions[1].append(v)


        #print( solve_problem(dt) )
np.save('times',times)
np.save('positions',positions)

print('Fake News')
