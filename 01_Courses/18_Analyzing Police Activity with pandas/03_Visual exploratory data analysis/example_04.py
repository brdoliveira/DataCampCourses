import pandas as pd
import matplotlib.pyplot as plt

ri = pd.read_csv('./data/police.csv')
ri.drop('county_name',axis='columns',inplace=True)
ri.dropna(subset=['stop_date','stop_time'],inplace=True)

"""
apple = pd.read_csv('./data/apple.csv')
print(apple.change.dtype)

mapping = {'up':True , 'down':False}
apple['is_up'] = apple.change.map(mapping)
print(apple.head())

apple.is_up.mean()
"""

search_rate = ri.groupby('violation').search_conducted.mean()

search_rate.sort_values().plot(kind='barh')
plt.show()