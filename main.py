#main

from target import Rocket
import physics as phy
import quick_grapher as gph

def main():
    

    state_vector = [0,0,0,0,0,100,0,0,0,0,0,0] #3 positionals, 3 velocity,3 angles, 3 angular
    


    target_rocket = Rocket(state_vector,mass=1)
    coordinate_rocket=[]
    coordinate_rocket.append((target_rocket.return_values(),0))
    dt=0.01
    t=0
    while True:
        try:
            exit=phy.acceleration(target_rocket, drag=True)
            coords_tar = target_rocket.return_values()
            t+=dt
            coordinate_rocket.append((coords_tar,t))
            
            if exit==1:
                gph.graph(coordinate_rocket)

                break
        except Exception as e:
            print(e)
            break

if __name__=="__main__":
    main()


