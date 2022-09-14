import pandas as pd

ri = pd.read_csv('./data/police.csv')
ri.drop('county_name',axis='columns',inplace=True)
ri.dropna(subset=['stop_date','stop_time'],inplace=True)

female = ri[ri.driver_gender == 'F']
print(f'Female shape: {female.shape}')

female_and_arrested = ri[(ri.driver_gender == 'F') & (ri.is_arrested == True)]
print(f'Female arrested shape: {female_and_arrested.shape}')

female_or_arrested = ri[(ri.driver_gender == 'F') | (ri.is_arrested == True)]
print(f'Female or arrested shape: {female_or_arrested.shape}')

'''
male = ri[ri.driver_gender == 'M']
print(f'Male shape: {male.shape}')

male_and_arrested = ri[(ri.driver_gender == 'M') & (ri.is_arrested == True)]
print(f'Male arrested shape: {male_and_arrested.shape}')

male_or_arrested = ri[(ri.driver_gender == 'M') | (ri.is_arrested == True)]
print(f'Male or arrested shape: {male_or_arrested.shape}')
'''