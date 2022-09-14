import pandas as pd
import numpy as np
import statistics as st

"""
amir_deals = pd.read_csv("./data/amir_deals.csv")
# print(amir_deals.head())

print("Mean num user = " , np.mean(amir_deals.num_users))
print("Median num user = " , np.median(amir_deals.num_users.sort_values()))
print("Mode num user = ", st.mode(amir_deals.num_users))

print("*" * 32)
print(amir_deals.num_users.agg([np.mean,np.median,st.mode]))
"""

food_consumption = pd.read_csv('./data/food_consumption.csv')

# Subset for Belgium and USA only
be_and_usa = food_consumption[(food_consumption["country"] == "Belgium") | (food_consumption["country"] == "USA")]

# Group by country, select consumption column, and compute mean and median
print(be_and_usa.groupby('country')['consumption'].agg([np.mean,np.median]))

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# Histogram of co2_emission for rice and show plot
plt.hist(rice_consumption['co2_emission'])
plt.show()