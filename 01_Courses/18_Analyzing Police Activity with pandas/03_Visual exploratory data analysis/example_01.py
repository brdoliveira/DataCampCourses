import pandas as pd
import matplotlib.pyplot as plt

ri = pd.read_csv('./data/police.csv')
ri.drop('county_name',axis='columns',inplace=True)
ri.dropna(subset=['stop_date','stop_time'],inplace=True)

'''
apple = pd.read_csv('./data/apple.csv')

print(apple.dtypes)
print(apple.date_and_time.dt.month)

apple.set_index('date_and_time',inplace=True)
print(apple.index)
print(apple.index.month)

print(f'Apple mean price : {apple.price.mean()}')
print(f'Apple mean price (month): {apple.groupby(apple.index.month).price.mean()}')

monthly_price = apple.groupby(apple.index.month).price.mean()
montly_price.plot()

plt.xlabel('Month')
plt.ylabel('Price)
plt.title('Monthly mean stock price for Apple)

plt.show()
'''