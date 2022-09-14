"""
# Baby back dist-rib-ution
"""
# pip install pyarrow
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

coffee_ratings = pd.read_feather("./data/coffee_ratings_full.feather")
# print(coffe_rating_full.head())

# Same code, different answer
coffee_ratings.sample(n=30)['total_cup_points'].mean()
coffee_ratings.sample(n=30)['total_cup_points'].mean()
coffee_ratings.sample(n=30)['total_cup_points'].mean()
coffee_ratings.sample(n=30)['total_cup_points'].mean()

mean_cup_points_1000 = []
for i in range(1000):
    mean_cup_points_1000.append(
        coffee_ratings.sample(n=30)['total_cup_points'].mean()
    )

plt.hist(mean_cup_points_1000, bins=150)
plt.show()
# A sampling distribution is a distribution of replicates of point estimates.

