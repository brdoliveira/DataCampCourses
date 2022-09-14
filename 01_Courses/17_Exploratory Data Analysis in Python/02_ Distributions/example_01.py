# Probability mass fucntion (PMF)
import pandas as pd
import matplotlib.pyplot as plt

gss = pd.read_hdf('./data/gss.hdf5','gss')
print(gss.head())

educ = gss['educ']
plt.hist(educ.dropna(),label='educ')
plt.show()

'''
pmf_educ = Pmf(educ, normalize = False) # sum normalize = 1
pmf_educ.head()

pmf_educ.bar(label='educ')

plt.xlabel('Years of education')
plt.ylabel('PMF)
plt.show
'''