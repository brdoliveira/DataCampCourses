import pandas as pd

weather = pd.read_csv('./data/weather.csv')

'''
apple.reset_index(inplace=True)
high = high_low[['DATE','HIGH']]
apple_high = pd.merge(left=apple,right=high,
                      left_on='date',right_on='DATE',
                      how='left')
apple_high.set_index('date_and_time',inplace=True)
print(apple_high.head())
'''