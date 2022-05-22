import pandas as pd
import matplotlib.pyplot as plt

ri = pd.read_csv('./data/police.csv')
ri.drop('county_name',axis='columns',inplace=True)
ri.dropna(subset=['stop_date','stop_time'],inplace=True)

print(f'Driver Race Assian and Gender Female (shape):\
 {ri[(ri.driver_race == "Asian") & (ri.driver_gender == "F")].shape}')

table = pd.crosstab(ri.driver_race,ri.driver_gender)

print('*' * 30)
# print(table.head())
print(table.loc['Asian':'Hispanic'])

table = table.loc['Asian':'Hispanic']

table.plot(kind='bar',stacked=True)
plt.show()