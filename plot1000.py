import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

lead1 = "Lead 1/nabeels_record.txt"

lead2 = "Lead 2/t3_lead2_bw_removed.txt"
x = np.loadtxt(lead1)
y = np.loadtxt(lead2)

plt.figure(figsize=(16,9))
plt.plot(stats.zscore(x[500:750]))
plt.plot(stats.zscore(y[500:750]))
plt.show()

# start = 2191
# plt.plot(stats.zscore(x[start - 128: start + 128]))
# plt.show()