import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

brfss = pd.read_hdf('./data/brfss.hdf5','brfss')
height = brfss['AGE'] + np.random.normal(0,0.5,size=len(brfss))
weight = brfss['WTKG3'] + np.random.normal(0,2,size=len(brfss))

data = brfss.dropna(subset=['AGE','WTKG3'])
sns.violinplot(x='AGE',y='WTKG3',data=data,inner=None)
plt.show()

sns.boxplot(x='AGE',y='WTKG3',data=data,whis=10)
plt.show()

sns.boxplot(x='AGE',y='WTKG3',data=data,whis=10)
plt.yscale('log')
plt.show()