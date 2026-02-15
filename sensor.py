import numpy as np
import onboard as cmp

def distance_sensor(obj1,obj2):
    debug=True
    target=obj1.X
    missile = obj2.X

    difference = target[0:3] - missile[0:3]
    sigma = 1 # meters
    noise = np.random.normal(0, sigma, size=3)

    

    if debug==True:
        measured = difference
    else:
        measured = difference+noise

    print(f"+-----------+\n    BEEP\ndifference: {measured}\ncheating! Noise: {noise}+-----------+\n\n\n")
    
    return measured

def map_sensor(obj1,obj2):

    """Given a velocity, maps object two's position on the plane whose normal is parallel to the velocity vector"""

    target = obj1
    missile = obj2

    target_coord = target.X[0:3]
    missile_coord = missile[0:3]
    ret = cmp.plane(missile_coord,target_coord)

    

    return ret



