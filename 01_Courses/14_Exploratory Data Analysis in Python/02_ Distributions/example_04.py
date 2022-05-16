import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

gss = pd.read_hdf('./data/gss.hdf5','gss')
print(gss.head())

'''
sample = np.random.normal(size=100)
Cdf(sample).plot()
'''

# Perfect cdf
xs = np.linspace(-3,3)
ys = norm(0,1).cdf(xs)
plt.plot(xs,ys,color='gray')
plt.show()

# Perfect curve bell 
xs = np.linspace(-3,3)
ys = norm(0,1).pdf(xs)
plt.plot(xs,ys,color='gray')
plt.show()

# Use CDFs for exploration.
# Use PMFs if there are a small number of unique values.
# Use KDE if there are a lot a values.