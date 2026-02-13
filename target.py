#creates a simple, non evading target and updates it's position
import numpy as np




class Rocket:

    
    def __init__(self,x,y,z, vx=0,vy=0,vz=0,mass=1):
        
        self.X = np.array([x,y,z,vx,vy,vz],dtype=float)
        self.mass = mass
    def print_values(self):

        if time()%10==0:
            print("-"*10)
            
            for i in range(int(len(self.X)/2)):
                
                print(f"{self.X[i]} in {chr(105+i)}, and it's velocity {self.X[i+3]}")

            print("-"*10)
    
    def return_values(self):
        
        return (self.X.copy())
