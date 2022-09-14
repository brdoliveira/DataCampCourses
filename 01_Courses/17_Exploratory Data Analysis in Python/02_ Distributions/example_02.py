# Cumulative distribution functions (CDF)
import pandas as pd
import matplotlib.pyplot as plt


gss = pd.read_hdf('./data/gss.hdf5','gss')
print(gss.head())

'''
cdf = Cdf(gss['age'])
cdf.plot()

plt.xlabel('Age')
plt.ylabel('CDF')
plt.show()
'''