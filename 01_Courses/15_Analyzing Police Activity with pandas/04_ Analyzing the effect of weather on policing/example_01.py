import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv('./data/weather.csv')
print(weather.head())

print('*' * 30)
print(weather[['AWND','WSF2']].head())

print('*' * 30)
print(weather[['AWND','WSF2']].describe())

weather[['AWND','WSF2']].plot(kind='box')
plt.show()

weather['WDIFF'] = weather.WSF2 - weather.AWND
weather.WDIFF.plot(kind='hist',bins=20)
plt.show()