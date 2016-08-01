# Generates the heatmap from data in a 2D matrix

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

ctr = [16,32,64,128,256,512]
intervals = [25,50,100,200,300,400,500]

data = np.zeros([7,6])

data[0] = [36.66,36.23,36.68,37.63,38.28,39.01] # Intrvl 25
data[1] = [36.96,36.46,36.22,36.88,37.69,37.85] # Intrvl 50
data[2] = [37.81,36.79,36.43,36.39,37.10,37.76] # Intrvl 100
data[3] = [38.88,37.70,36.74,36.48,36.51,37.19] # Intrvl 200
data[4] = [39.55,38.33,37.19,36.60,36.46,36.75] # Intrvl 300
data[5] = [40.02,38.78,37.63,36.78,36.55,36.60] # Intrvl 400
data[6] = [40.40,39.16,37.98,37.01,36.51,36.56] # Intrvl 500

for y in range(data.shape[0]):
    for x in range(data.shape[1]):
        plt.text(x+0.5, y+0.5, "%.2f" % data[y,x], horizontalalignment='center', verticalalignment='center')

plt.pcolor(data, cmap='Greys')
plt.yticks(np.arange(0.5, len(intervals), 1), intervals)
plt.xticks(np.arange(0.5, len(ctr), 1), ctr)
plt.xlabel("# of MEA Counters")
plt.ylabel("Interval Length (us)")
plt.colorbar()

pp2 = PdfPages('C:/Users/prodr/Documents/UCSD/MigrationResearch/MemPod/paper/figures/revised/new/DSE.pdf')
pp2.savefig()
pp2.close()