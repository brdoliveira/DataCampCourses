import pandas as pd

ri = pd.read_csv('./data/police.csv') # ri -> rode island
print(ri.head())

print("*" * 30)

ri.isnull() # show the null values
print(f'How many null values have? \n{ri.isnull().sum()}')

print(ri.shape())

ri.drop('county_name',axis='columns',inplace=True) # all values is NaN

ri.dropna(subset=['stop_date','stop_time'],inplace=True)