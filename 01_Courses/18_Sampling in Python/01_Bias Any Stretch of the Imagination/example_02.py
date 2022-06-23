"""
# A little too convenient

# The Literary Digest election prediction (1936)
# # Prediction: Landon gets 57%; Roosevelt gets 43%
# # Actual results: Landon got 38%, Roosevelt got 62%
# # # Sample not representative of population, causing sample bias
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

coffee_ratings = pd.read_feather("./data/coffee_ratings_full.feather")
# print(coffe_rating_full.head())

coffee_ratings["total_cup_points"].mean()

coffee_ratings_first10 = coffee_ratings.head(10)
coffee_ratings_first10["total_cup_points"].mean()

coffee_ratings["total_cup_points"].hist(bins=np.range(59,93,2))
plt.show()

coffee_ratings_first10["total_cup_points"].hist(bins=np.range(59,93,2))
plt.show()

coffee_sample = coffee_ratings.sample(n=10)
coffee_sample["total_cup_points"].hist(bins=np.arange(59,93,2))
plt.show()