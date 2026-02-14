import matplotlib.pyplot as plt

def graph(coord):

    x = [i[0][0] for i in coord]; vx = [i[0][3] for i in coord]
    y = [i[0][1] for i in coord]; vy = [i[0][4] for i in coord]
    z = [i[0][2] for i in coord]; vz = [i[0][5] for i in coord]
    t = [i[-1] for i in coord]

    fig, (AX)=plt.subplots(3,2)

    AX[0,0].set_title("x vs t")
    AX[1,0].set_title("y vs t")
    AX[2,0].set_title("z vs t")

    AX[0,0].plot(t,x,label = "X")
    AX[0,0].plot(t,vx,label = "Velocity X")
    AX[1,0].plot(t,y,label = "Y")
    AX[1,0].plot(t,vy, label = "Velocity y")
    AX[2,0].plot(t,z, label = "Z")
    AX[2,0].plot(t,vz, label="Velocity z")


    AX[2,0].legend()
    plt.tight_layout()
    plt.show()



