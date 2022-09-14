from scipy.stats import linregress
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
xs = np.linspace(-1,1)
ys = xs ** 2
ys += np.random.normal(0,0.05,len(xs))

# Hypothetical 1
res = linregress(xs,ys)
print(res)

fx = np.array([xs.min(),xs.max()])
fy = res.intercept + res.slope * fx
plt.plot(fx,fy,'-')
plt.show()
'''

brfss = pd.read_hdf('./data/brfss.hdf5','brfss')
subset = brfss.dropna(subset=['WTKG3','HTM4'])

xs = subset['HTM4']
ys = subset['WTKG3']
res = linregress(xs,ys)

fx = np.array([xs.min(),xs.max()])
fy = res.intercept + res.slope * fx
plt.plot(fx,fy,'-')

height = brfss['HTM4']
weight = brfss['WTKG3']
height_jitter = height + np.random.normal(0,2,size=len(brfss))
weight_jitter = weight + np.random.normal(0,2,size=len(brfss))

plt.plot(height_jitter,weight_jitter,'o',markersize=1, alpha=0.02)
plt.axis([140,200,0,160])
plt.ylabel('Height in cm')
plt.xlabel('Weight in kg')
plt.show()


'''
subset = brfss.dropna(subset=['WTKG3','AGE'])
xs = subset['AGE']
ys = subset['WTKG3']

res = linregress(xs,ys)
print(res)
'''