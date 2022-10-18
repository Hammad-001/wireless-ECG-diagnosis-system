# import necessary packages
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from baseline_wander_removal import filter_signal, band_pass_filter

# create figure and axes objects
fig, ax = plt.subplots(2)
fig.tight_layout(pad=4.0)
fig.suptitle("ECG Leads Data")
# reading file
# with open('./Lead 1/nabeels_record.txt', 'r') as file:
#     sig1 = file.readlines()
#     sig1 = [int(d.strip()) for d in sig1]
# with open('./Lead 1/nabeels_record2.txt', 'r') as file:
#     sig2 = file.readlines()
#     sig2 = [int(d.strip()) for d in sig2]

df = pd.read_csv("new_tajammul_data_1.txt", names=["I", "II"])

start, end = 1, 501

# df['I'].plot(ax=ax[0])
# df['II'].plot(ax=ax[1])
# plt.show()
def animate(i):
    """ animation function for FuncAnimation"""
    global start, end
    start += 10
    end += 10
    ax[0].clear()
    ax[1].clear()

    ax[0].set_title('Lead-II')
    ax[1].set_title('Lead-III')
    ax[0].grid(True)
    ax[1].grid(True)
    
    x = df['I'].iloc[start:end]
    y = df['II'].iloc[start:end]
    x = band_pass_filter(filter_signal(x))
    y = band_pass_filter(filter_signal(y))
    ax[0].plot(x)
    ax[1].plot(y)
    # df['I'].iloc[start:end].plot(ax=ax[0])
    # df['II'].iloc[start:end].plot(ax=ax[1])
    # print(type(band_pass_filter(filter_signal(df['I'].iloc[start:end]))))
    
    # ax[0].plot(range(start, end), band_pass_filter(filter_signal(df["I"].iloc[start:end])))
    # ax[1].plot(range(start, end), band_pass_filter(filter_signal(df["II"].iloc[start:end])))


# call the animation
ani = FuncAnimation(fig, animate, interval=10)

# show the plot
plt.show()
