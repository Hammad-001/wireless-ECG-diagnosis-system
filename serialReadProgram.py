import sys
import serial
import numpy as np
import matplotlib.pyplot as plt

num_args = len(sys.argv)
if num_args < 2:
    print("COM port not selected.")
    exit()

com_port = sys.argv[1]
print("-"*50)
print(f"You have selected {com_port} port for communication")
print("-"*50)

try: 
    mcu = serial.Serial(com_port, timeout=1)
except:
    print("COM port failed to open.")
    exit()

res = [] # a cummulative result
chunk = [] # hold a chuck of 500 samples
start = 0
end = 500
threshold = 500
first_time = False
while True:
    try:
        text = mcu.readline().decode()[:-2]
        if text == '':
            continue
        else:
            res.append(float(text))
        if len(res) > threshold:
            chunk = res[start:end]
            if not first_time:
                print("First time")
                first_time = True
                plt.figure(figsize=(6,4))
                plt.plot(range(start, end), chunk)
                plt.draw()
            else:
                plt.gca().lines[0].set_xdata(range(start, end))
                plt.gca().lines[0].set_ydata(chunk)
                plt.gca().relim()
                plt.gca().autoscale_view()
                plt.pause(0.1)
                plt.draw()
            start += 10
            end += 10
            threshold += 10

    except KeyboardInterrupt:
        print(len(res))
        print(len(chunk))

        chunk = np.array(chunk)
        np.savetxt("sine_wave_chunk.txt", chunk)
        print(start, end)
        arr = np.array(res)
        np.savetxt("sine_wave.txt", arr)
        break