# Write program to perform the following on signal
# 1.Create a triangle signal and plot a 3-period segment.
# 2.For a given signal, plot the segment and compute the correlation between them.

from scipy import signal
from matplotlib import pyplot as plt 
import numpy as np

# 1.Create a triangle signal and plot a 3-period segment.
def TriangleSignal(t,p):

    plt.plot(t,signal.sawtooth(2*np.pi*5*t))
    plt.plot(p,signal.sawtooth(2*np.pi*4*t))

    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("Sawtooth Signal")
    plt.axhline(y=0,color="k")

    plt.show()

# 2.For a given signal, plot the segment and compute the correlation between them.
def PSeg(t,p):
    correlation = np.correlate(t,p,mode="same")
    print(correlation)
    plt.plot(correlation)
    plt.show()

def main():
    t = np.linspace(0, 1, 1000, endpoint=True)
    p = np.linspace(0, 1.01, 1000, endpoint=True)
    
    TriangleSignal(t,p)
    PSeg(t,p)
    
if __name__ == "__main__":
    main()