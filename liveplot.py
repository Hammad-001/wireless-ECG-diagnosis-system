# import necessary packages
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from baseline_wander_removal import filter_signal, band_pass_filter

# create figure and axes objects
fig, ax = plt.subplots()

# reading file
with open('./Lead 1/nabeels_record.txt', 'r') as file:
    data = file.readlines()
    data = [int(d.strip()) for d in data]

start, end = 0, 500


def animate(i):
    """ animation function for FuncAnimation"""
    global start, end
    start += 10
    end += 10
    ax.clear()
    ax.set_title('ECG Wave Plot')
    ax.plot(range(start, end), band_pass_filter(
        filter_signal(data[start:end])))


# call the animation
ani = FuncAnimation(fig, animate, interval=10)

# show the plot
plt.show()
