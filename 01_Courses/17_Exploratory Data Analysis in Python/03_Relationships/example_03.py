from numpy import linspace
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

brfss = pd.read_hdf('./data/brfss.hdf5','brfss')
columns = ['HTM4','WTKG3','AGE']
subset = brfss[columns]

print(subset.corr()) # correlation matrix

xs = np.linspace(-1,1)
ys = xs ** 2
ys += np.random.normal(0,0.05,len(xs))

plt.plot(xs,ys)
print(np.corrcoef(xs,ys))
plt.show()