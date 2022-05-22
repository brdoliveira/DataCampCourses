import pandas as pd
import matplotlib.pyplot as plt

ri = pd.read_csv('./data/police.csv')
ri.drop('county_name',axis='columns',inplace=True)
ri.dropna(subset=['stop_date','stop_time'],inplace=True)

'''
apple = pd.read_csv('./data/apple.csv')

apple.groupby(apple.index.month).price.mean()

monthly_price = apple.price.resample('M').mean()
monthly_volume = apple.volume.resample('M').mean()

monthly = pd.concat([monthly_price, monthly_volume],
                    axis='columns')

monthly.plot(subplots=True) # different scales
monthly.show()
'''