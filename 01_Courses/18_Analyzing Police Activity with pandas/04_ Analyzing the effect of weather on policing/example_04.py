import pandas as pd

weather = pd.read_csv('./data/weather.csv')
# print(weather.head())

ri = pd.read_csv('./data/police.csv')
ri.drop('county_name',axis='columns',inplace=True)
ri.dropna(subset=['stop_date','stop_time'],inplace=True)
# print(ri.head())

print(ri.groupby('driver_gender').search_conducted.mean())

print('*' * 30)
search_rate = ri.groupby(['violation','driver_gender']).search_conducted.mean()
print(search_rate)
print(f'search_rate (type) : {type(search_rate)}')
print(f'search_rate.index (type) : {type(search_rate.index)}')

# search_rate.loc['Equipment']
# search_rate.loc['Equipment','M']
print('*' * 30)
print(search_rate.unstack())
print(f'search_rate.unstack (type) : {type(search_rate.unstack)}')

print('*' * 30)
print(ri.pivot_table(index='violation',columns='driver_gender',values='search_conducted'))