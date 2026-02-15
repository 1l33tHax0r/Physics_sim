import numpy as np
import sensor
from math import sin, cos

class Missile:
    missile_list=[]
    def __init__(self,x,mass=1, moment = 1, thrust=100,permitted_forces={}):
        
        self.X = np.array(x,dtype=float) #x,y,z,vx,vy,vz...
        self.mass = mass
        self.moment = moment
        self.thrust = thrust
        self.call=permitted_forces
        self.call['thrust'] = ()
        self.old = 0

        Missile.missile_list.append(self)
    def return_values(self):
        
        return (self.X.copy())

    def measure(self,target):
        measurement = sensor.distance_sensor(target,self)
        return measurement
    
    def complex_measure(self,target):

        measurement = sensor.map_sensor(target,self)
        return measurement
    

    def local_axis(self,y):

        x=self.x[0:3]/np.linalg.norm(self.x[0:3])
        y=y/np.linalg.norm(y)
        z = np.cross(x,y)
        return (x,y,z)

    def complex_thrust(self,signal,kp,kd,dt=0.01):

        reference = [0,0,0]
        own_axis = self.local_axis(signal)
        v,y,z = own_axis
        T_hat_def = -v
        error_s = signal-reference

        

        P = signal*kp





    def simple_thrust(self,signal,kp,kd,dt=0.01):
        
        



        thrust_signal = signal*kp+kd*(signal-kd)/dt
        print(thrust_signal)
        if thrust_signal < 0:

            thrust_signal=0
            
        elif thrust_signal > 1:

            thrust_signal = 1
        
        ret = self.thrust*thrust_signal
        self.call['thrust']=tuple([ret])
        self.old=ret



