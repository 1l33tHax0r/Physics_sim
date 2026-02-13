#simple navigation law selector

import math as m



def DumbLaw(rx,ry,rz,tx,ty,tz):

    """No law, just up up and away!"""
    return None

def Pointy(rx,ry,rz,tx,ty,tz):
    """Points the rocket at launch to intercept,
    computes angles, and returns angles"""
    


    theta = m.atan2(tz - rz, tx - rx)
    return theta
    

def return_nav_list():

    return {0:DumbLaw,
    1:Pointy}

def NaviLo(quick_select = True, s=0 ):

    """ALL NAVIGATION LAWS HAVE 6 MANDATORY COORDINATE INPUTS"""
    navigation_laws=return_nav_list()

    if quick_select == True:

        return navigation_laws[s]

    else:
        while True:
            try:

                print("\n"*100)
                
                for key in navigation_laws:
                    print(f"[{key}]. {navigation_laws[key].__name__}")
                s=int(input("Select a law by typing an integer: "))

                return navigation_laws[s]

            except KeyError:
                print("Please elect a valid key from the list.")
            except TypeError:
                print("Please input a valid input (an integer indicating control law number).")

            

