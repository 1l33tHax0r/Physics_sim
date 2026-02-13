import matplotlib.pyplot as plt

def graph(coord):

    x = [i[0][0] for i in coord]
    y = [i[0][1] for i in coord]
    z = [i[0][2] for i in coord]
    t = [i[-1] for i in coord]

    fig, (ax1,ax2)=plt.subplots(2,1)

    ax1.plot(t,y)
    ax2.plot(t,z)
    plt.tight_layout()
    plt.show()