import pandas as pd
# import numpy as np

ri = pd.read_csv('./data/police.csv')
ri.drop('county_name',axis='columns',inplace=True)
ri.dropna(subset=['stop_date','stop_time'],inplace=True)


# print(ri.isnull().sum())
print(f'Mean Arrested \n{ri.is_arrested.value_counts(normalize=True)}') # equal ri.is_arrested.mean()
# ri.is_arrested.dtype # boolean

print('*' * 30)
print(f'The unique districts {ri.district.unique()}')
for distr in ri.district.unique():
    print(f'{distr}\t {ri[ri.district == distr].is_arrested.mean()} ')

'''
# OR
print('*' * 30)
print(ri.groupby('district').is_arrested.mean()) 
print(ri.groupby(['district','driver_gender']).is_arrested.mean())
print(ri.groupby(['driver_gender','district']).is_arrested.mean())
'''