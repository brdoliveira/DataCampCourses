"""
# Simple is as simple does
"""
# pip install pyarrow
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

coffee_ratings = pd.read_feather("./data/coffee_ratings_full.feather")
# print(coffe_rating_full.head())

# print(coffee_ratings.sample(n=5,random_state=19000113))

# Systematic sampling - defining the interval
sample_size = 5

pop_size = len(coffee_ratings)
print(pop_size)

interval = pop_size // sample_size # // -> integer division
print("pop_size // sample_size = ",interval)

# Systematic sampling - selecting the rows
print("*" * 32)

print(coffee_ratings.iloc[::interval])

# The trouble with systematic sampling
# # Systematic sampling is only safe if we don't see a pattern is this scatterplot
coffee_ratings_with_id = coffee_ratings.reset_index()
coffee_ratings_with_id.plot(x="index",y="aftertaste",kind="scatter")
plt.show()

# Making systematic sampling safe
# Shuffling rows + systematic sampling is the same as simple random sampling
shuffled = coffee_ratings.sample(frac=1)
shuffled = shuffled.reset_index(drop=True).reset_index()
shuffled.plot(x="index",y="aftertast",kind="scatter")
plt.show()