# pip install tables
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nsfg = pd.read_hdf('./data/nsfg.hdf5','nsfg')

pounds = nsfg['birthwgt_lb1']
pounds = pounds.replace([98,99],np.nan)

ounces = nsfg['birthwgt_oz1']
ounces.replace([98,99],np.nan,inplace=True)

birth_weight = pounds + ounces / 16.0

plt.hist(birth_weight.dropna(), bins=30)

plt.xlabel('Birth weight (lb)')
plt.ylabel('Fraction of births')

plt.show()

# Premature
preterm = nsfg['prglngth'] < 37
print(f'Preterm babys = {preterm.sum()}')

print(f'Mean (Preterm babys) = {preterm.mean() * 100}%')

preterm_weight = birth_weight[preterm]
preterm_weight.mean()

full_term_weight = birth_weight[~preterm]
print(full_term_weight.mean())