import random as rd
import time
rd.seed()
noise = rd.randint(1,10)/rd.randint(1,100)



def getfrom_sensor(x,y,z):
    
    noise = rd.randint(1,10)/rd.randint(1,100)
    x+= rd.randint(1,10)/rd.randint(1,100)
    y+=rd.randint(1,10)/rd.randint(1,100)
    z+= rd.randint(1,10)/rd.randint(1,100)

    return (x,y,z)



print(getfrom_sensor(10,10,1000))