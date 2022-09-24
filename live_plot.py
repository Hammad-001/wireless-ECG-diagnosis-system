import matplotlib.pyplot as plt
import numpy as np
from baseline_wander_removal import filter_signal, band_pass_filter

lead1 = "Lead 2/n2_lead2.txt"
x = np.loadtxt(lead1)
start, end = 0, 500
rng = range(start, end)
temp_x = band_pass_filter(filter_signal(x[start:end]))

plt.figure(figsize=(6,4))
plt.plot(rng, temp_x)
for i in range(1000):
    start += 10
    end += 10
    rng = range(start, end)
    temp_x = band_pass_filter(filter_signal(x[start:end]))
    plt.gca().lines[0].set_xdata(rng)
    plt.gca().lines[0].set_ydata(temp_x)
    plt.gca().relim()
    plt.gca().autoscale_view()
    plt.pause(0.1)
plt.draw()
