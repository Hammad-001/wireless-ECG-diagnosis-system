# import necessary packages
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from baseline_wander_removal import filter_signal, band_pass_filter

# create figure and axes objects
fig, ax = plt.subplots(2)
fig.tight_layout(pad=4.0)
fig.suptitle("ECG Leads Data")

# reading file
with open('./Lead 1/nabeels_record.txt', 'r') as file:
    sig1 = file.readlines()
    sig1 = [int(d.strip()) for d in sig1]
with open('./Lead 1/nabeels_record2.txt', 'r') as file:
    sig2 = file.readlines()
    sig2 = [int(d.strip()) for d in sig2]

start, end = 0, 500

def animate(i):
    """ animation function for FuncAnimation"""
    global start, end
    start += 10
    end += 10
    ax[0].clear()
    ax[1].clear()

    ax[0].set_title('Lead-II')
    ax[1].set_title('Lead-III')

    ax[0].plot(range(start, end), band_pass_filter(filter_signal(sig1[start:end])))
    ax[1].plot(range(start, end), band_pass_filter(filter_signal(sig2[start:end])))


# call the animation
ani = FuncAnimation(fig, animate, interval=10)

# show the plot
plt.show()
