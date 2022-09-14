# Comparing distributions
import pandas as pd
import matplotlib.pyplot as plt

gss = pd.read_hdf('./data/gss.hdf5','gss')
print(gss.head())

male = gss['sex'] == 1
age = gss['age']

male_age = age[male]
female_age = age[~male]

'''
Pmf(male_age).plot(label='Male')
Pmf(female_age).plot(label='Female')

plt.xlabel('Age (years)')
plt.ylabel('Count')

plt.show()

Cdf(male_age).plot(label='Male')
Cdf(female_age).plot(label='Female')

plt.xlabel('Age (years)')
plt.ylabel('Count')

plt.show()

income = gss['realinc']
pre95 = gss['year'] < 1995

Cdf(income[pre95]).plot(label='Before 1995')
Cdf(income[~pre95]).plot(label='After 1995')

plt.xlabel('Income (1986 USD)')
plt.ylabel('PMF')

plt.show()
'''