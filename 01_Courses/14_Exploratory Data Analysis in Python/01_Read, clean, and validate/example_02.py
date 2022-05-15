# pip install tables
import pandas as pd
import numpy as np

nsfg = pd.read_hdf('./data/nsfg.hdf5','nsfg')

pounds = nsfg['birthwgt_lb1']
ounces = nsfg['birthwgt_oz1']

print(pounds.value_counts().sort_index())

print(pounds.describe()) # Summary series

print('-' * 30)

pounds = pounds.replace([98,99],np.nan)
print(pounds.describe())
print(f'Mean  \t {pounds.mean()}')

ounces.replace([98,99],np.nan,inplace=True)

print('-' * 30)

birth_weight = pounds + ounces / 16.0
print(birth_weight.head())

print('-' * 30)

print(birth_weight.describe())