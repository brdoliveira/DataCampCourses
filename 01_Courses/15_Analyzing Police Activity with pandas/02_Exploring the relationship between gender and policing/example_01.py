import pandas as pd

ri = pd.read_csv('./data/police.csv')
ri.drop('county_name',axis='columns',inplace=True)
ri.dropna(subset=['stop_date','stop_time'],inplace=True)

print(f'value counts : \n{ri.stop_outcome.value_counts()}')

print('*' * 30)
print(f'value counts : \n{ri.stop_outcome.value_counts(normalize=True)}')

print('*' * 30)
print(f'value counts (sum) : {ri.stop_outcome.value_counts().sum()}')
print(f'shape dataframe : {ri.shape}')

print('*' * 30) 
print(ri.driver_race.value_counts())


print('*' * 30)
white = ri[ri.driver_race == 'White']
print(f'White: \n{white.stop_outcome.value_counts(normalize=True)}')

print('*' * 30)
asian = ri[ri.driver_race == 'Asian']
print(f'Asian: \n{asian.stop_outcome.value_counts(normalize=True)}')