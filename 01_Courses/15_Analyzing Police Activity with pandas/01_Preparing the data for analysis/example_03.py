import pandas as pd

ri = pd.read_csv('./data/police.csv') # ri -> rode island
ri.drop('county_name',axis='columns',inplace=True)
ri.dropna(subset=['stop_date','stop_time'],inplace=True)

print(ri.head(3))

"""
apple.date.str.replace('/','-')

combined = apple.date.str.cat(apple.time,sep=' ')
apple['date_and_time'] = pd.to_datetime(combined)
print(apple.head())

apple.set_index('date_and_time',inplace=True)
print(apple.index)
print(apple.columns)
"""