import numpy as np
from scipy.signal import medfilt
import matplotlib.pyplot as plt
# import seaborn as sns

# sns.set_theme()

BASIC_SRATE = 160


def get_median_filter_width(sampling_rate, duration):
    res = int(sampling_rate*duration)
    res += ((res % 2) - 1)  # needs to be an odd number
    return res
# baseline fitting by filtering
# === Define Filtering Params for Baseline fitting Leads======================
# ms_flt_array = [0.2, 0.6]    #<-- length of baseline fitting filters (in seconds)
# mfa = np.zeros(len(ms_flt_array), dtype='int')
# for i in range(0, len(ms_flt_array)):
#     mfa[i] = get_median_filter_width(BASIC_SRATE,ms_flt_array[i])

# def filter_signal(X):
#     global mfa
#     X0 = X  #read orignal signal
#     for mi in range(0,len(mfa)):
#         X0 = medfilt(X0,mfa[mi]) # apply median filter one by one on top of each other
#         print(X0 - X)
#     X0 = np.subtract(X,X0)  # finally subtract from orignal signal
#     return X0


def filter_signal(X):
    kernel = get_median_filter_width(BASIC_SRATE, 0.4)
    X0 = X  # read orignal signal
    # apply median filter one by one on top of each other
    X0 = medfilt(X0, kernel)
    # print(X0 - X)
    X0 = np.subtract(X, X0)  # finally subtract from orignal signal
    return X0



def band_pass_filter(signal):
    result = None
    sig = signal.copy()
    for index in range(len(signal)):
        sig[index] = signal[index]

        if (index >= 1):
            sig[index] += 2*sig[index-1]

        if (index >= 2):
            sig[index] -= sig[index-2]

        if (index >= 6):
            sig[index] -= 2*signal[index-6]

        if (index >= 12):
            sig[index] += signal[index-12]

    result = sig.copy()
    for index in range(len(signal)):
        result[index] = -1*sig[index]

        if (index >= 1):
            result[index] -= result[index-1]

        if (index >= 16):
            result[index] += 32*sig[index-16]

        if (index >= 32):
            result[index] += sig[index-32]

    # Normalize the result from the high pass filter

    max_val = max(max(result), -min(result))
    result = result/max_val

    return result


if __name__ == '__main__':
    signal = np.loadtxt("./Lead 2/n1_lead2.txt")[:1000]
    signal_bs = filter_signal(signal)
    signal_flt = band_pass_filter(signal_bs)
    plt.figure(figsize=(16, 9))
    plt.subplot(2, 1, 1)
    plt.plot(signal)
    plt.grid(True)
    plt.title("RAW signal")
    plt.subplot(2, 1, 2)
    plt.plot(signal_flt)
    plt.title("baseline removed signal")
    plt.grid(True)
    plt.show()
