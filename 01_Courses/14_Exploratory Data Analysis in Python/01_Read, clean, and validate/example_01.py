# pip install tables
import pandas as pd

nsfg = pd.read_hdf('./data/nsfg.hdf5','nsfg')
# print(type(nsfg)) # <class 'pandas.core.frame.DataFrame'>

print(nsfg.head())

print(nsfg.shape)

print(nsfg.columns) # name of columns

print("-" * 30)

pounds = nsfg['birthwgt_lb1']
# print(type(pounds)) # pandas.core.series.Series
print(pounds.head()) # name series and type series
