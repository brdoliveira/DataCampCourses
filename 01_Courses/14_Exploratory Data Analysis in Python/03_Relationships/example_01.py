import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

brfss = pd.read_hdf('./data/brfss.hdf5','brfss')
height = brfss['HTM4']
weight = brfss['WTKG3']

plt.plot(height,weight,'o',markersize=1,alpha=0.02)
plt.ylabel('Height in cm')
plt.xlabel('Weight in kg')
plt.show()

height_jitter = height + np.random.normal(0,2,size=len(brfss))
weight_jitter = weight + np.random.normal(0,2,size=len(brfss))

plt.plot(height_jitter,weight_jitter,'o',markersize=1, alpha=0.02)
plt.axis([140,200,0,160])
plt.show()