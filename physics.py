import numpy as np
import time

def acceleration(obj,drag=False, k=0.1):
    # a super simplified forces model`
    g=-9.81
    F=np.array([0,0,-9.81],dtype=float)
    if drag==True:
        #returns drag force as k, which represents the 1/2 p r Cd A part
        V=obj.X[3:6]
        V=np.array(V,dtype=float)
        
        vel=(V@V)**(1/2)
        
        if vel!=0:
        
            dirh=-V/vel
            D=k*vel**2
            aD=(D/obj.mass)
            aD_dir=dirh*aD
            F+=aD_dir
        
    return acc

x += v*dt + 0.5*a*dt*dt
a_new = acceleration(x, v, ...)
v += 0.5*(a + a_new)*dt
a = a_new

def apply_translation(obj, ax,ay,az,dt=0.01,drag=False):
    args = acceleration(obj, drag)

    

    for i in range(len(args)):
        #obj.X is a nmpy array
        obj.X[i+3]+=args[i]*dt
        obj.X[i]+=obj.X[i+3]*dt
        
    if obj.X[2]<0:
        return 1

    return 0
