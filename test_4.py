import matplotlib.pyplot as plt

def func_A():
    x = range(0,20)
    y = [i*i for i in x]
    
    plt.plot(x,y)
    plt.show()
    plt.close()