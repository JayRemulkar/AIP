# Write program to perform the following on signal
# 1.Create a triangle signal and plot a 3-period segment.
# 2.For a given signal, plot the segment and compute the correlation between them.

from scipy import signal
from matplotlib import pyplot as plot
import numpy as np

# linspace(start,stop,num,endpoint)
# return evenly spaced numbers(num) between the specified interval(start,end).
t = np.linspace(0, 1, 1000, endpoint=True)
p = np.linspace(0, 1.01, 1000, endpoint=True)

# Plot the sawtooth wave
# plot(x,y) returns a list of lines representing plotted data
# sawtooth() return a periodic tringle wavwform.
a = plot.plot(t, signal.sawtooth(2 * np.pi * 5 * t))
b = plot.plot(p, signal.sawtooth(2 * np.pi * 4 * t))
#print(a)
#print(b)

# Give x, y, title axis label
plot.xlabel('Time')
plot.ylabel('Amplitude')
plot.title('Sawtooth Signal')
plot.axhline(y=0, color='k')

# Display
plot.show()

# correlat = signal.correlate(t,p)
# plot.plot(correlat)

# correlate() returns corrlation.
correlation = np.correlate(t, p, mode='same')
print(correlation)
plot.plot(correlation)
plot.show()