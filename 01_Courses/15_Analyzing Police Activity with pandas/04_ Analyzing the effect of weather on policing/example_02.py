import pandas as pd

weather = pd.read_csv('./data/weather.csv')
# print(weather.head())

# weather.shape
# weather.columns

ri = pd.read_csv('./data/police.csv')
ri.drop('county_name',axis='columns',inplace=True)
ri.dropna(subset=['stop_date','stop_time'],inplace=True)
# print(ri.head())


temp = weather.loc[:,'TAVG':'TMAX']
print(f'Temp shape : {temp.shape}')
print(f'Temp columns :\n{temp.columns}')

print('*' * 30)
print(temp.head())

print('*' * 30)
print(temp.sum())

print('*' * 30)
print(temp.sum(axis='columns').head())

print('*' * 30)
ri.dropna(subset=['stop_duration'],inplace=True)
print(ri.stop_duration.unique())

mapping = {'0-15 Min':'short',
           '16-30 Min':'medium',
           '30+ Min':'long'} 

ri['stop_length'] = ri.stop_duration.map(mapping)
# ri.stop_length.dtype # '0'

print(ri.stop_length.unique())
print(f'Memory usage : {ri.stop_length.memory_usage(deep=True)} MB')

cats = pd.CategoricalDtype(['short','medium','long'],
                            ordered=True)

ri['stop_length'] = ri.stop_length.astype(cats)
print(f'Memory usage (After change type): {ri.stop_length.memory_usage(deep=True)} MB')

print('*' * 30)
print(ri.stop_length.head())

print('Stop Length: ')
# print(ri[ri.stop_length > 'short'].shape) # single
print(ri.groupby('stop_length').is_arrested.mean())