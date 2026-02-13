import sensor as sr
import NaviLo
import onboard as cmp

l=NaviLo.NaviLo(0)

class Missile:

    def __init__(self,x,y,thrust=100,m=1,navigation_law):
        thurst in N, mass in kg
        self.navlo=navigation_law
        self.x = x
        self.y = y
        self.z = 0
        self.vx = 0
        self.vy = 0
        self.vz = 0
        
    def launch(ax=0,ay=0,az=):

        self.ax = 0
        self.ay = 0
        self.az = self.thrust/self.m

    def check_collision(X):
        if z<0:
            return None