"""
# This bears a striking resample-lance

# # With or without
# # # Sampling without replacement: Playing cards
# # # Sampling with replacement("resampling"): Dice

# # Why sample with replacement?
# # # coffee_ratings: a sample of a larger population of all coffees
# # # Each coffee in our sample represents many different hypothetical population coffees
# # # Sampling with replacement is a proxy
"""
# pip install pyarrow
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

coffee_ratings = pd.read_feather("./data/coffee_ratings_full.feather")
# print(coffe_rating_full.head())

coffee_focus = coffee_ratings[["variety","country_of_origin","flavor"]]
coffee_focus = coffee_focus.reset_index()

# Resampling with .sample()
coffee_resamp = coffee_focus.sample(frac=1,replace=True)

# Missing coffees
num_unique_coffes = len(coffee_resamp.drop_duplicates(subset="index"))
len(coffee_ratings) - num_unique_coffes # comparing with the total

# Bootstrapping
# # The opposite of sampling from a population

# Sampling: going from a population to a smaller sample
# Bootstrapping: building up a theorical population from the sample
# # Bootstrappind use case:
# # # Develop understanding of sampling variability using a single sample
# # # Bootstrapping proccess
# # # # 1. Make a resample of the size as the original sample
# # # # 2. Calculating the statistic of interest for this bootstrap sample
# # # # 3. Repeat steps 1 and 2 many times
# # # The resulting statistics are bootstrap statistics, and they form a bootstrap distribution

mean_flavor_1000 = []

for i in range(1000):
    mean_flavor_1000.append(
        np.mean(coffee_focus.sample(frac=1,replace=True)['flavor'])
    )

# Bootstrap distribution histogram
plt.hist(mean_flavor_1000)
plt.show()