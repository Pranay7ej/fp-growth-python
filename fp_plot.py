from fpalgo import *
from fptree1 import *

import pandas as pd

data = pd.read_csv('C:\\Users\\Teja\\Desktop\\LearningSystemsFall22\\garments_worker_productivity.csv')
data = data.fillna(0)
print(data)

# plotting the values in a graph
import matplotlib.pyplot as plt

x = [1,1.5,2,3,4]  # minSup
y = [6526,4738,4691,2920,2305]  # LenoffreqItemSets_ortime
plt.plot(x, y, color='b', linestyle='dotted', linewidth=2, marker='*', markerfacecolor='black', markersize=10)
plt.xlabel('Minimum Support')
plt.ylabel('Time(ms)')
plt.title("Visualizing Balloons Dataset")
plt.show()
