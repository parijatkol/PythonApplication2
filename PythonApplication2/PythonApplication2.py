from math import radians
import numpy as np     # installed with matplotlib
import matplotlib.pyplot as plt


def addition(a,b):
    return (a+b)

def subtraction(a,b):
    if(a>b):
        return a-b
    else:
        return b-a

def main():
    x = np.arange(0, radians(1800), radians(12))
    plt.plot(x, np.cos(x), 'b')
    plt.show()

main()
