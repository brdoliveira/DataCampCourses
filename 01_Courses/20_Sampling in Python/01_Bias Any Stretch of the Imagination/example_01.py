"""
# Living the sample life

# # Estimate the population of France
# # # A census asks every household how many people live there.
# # There a lots of people in France
# # # Census are really expensive
# # Sampling households
# # # Cheaper to ask a small number of households and use statistics to estimate the population

# The population is the complete dataset
# # Doesn't have to refer to people
# # Typically, don't know what the whole population is

# The sample is the subset of data you calculate on
"""
# pip install pyarrow
import pandas as pd
import numpy as np

coffee_ratings = pd.read_feather("./data/coffee_ratings_full.feather")
# print(coffe_rating_full.head())

pts_vs_flavor_pop = coffee_ratings[["total_cup_points","flavor"]]
pts_vs_flavor_samp = pts_vs_flavor_pop.sample(10)

# A population parameter is a calculation made on the population dataset
np.mean(pts_vs_flavor_pop["total_cup_points"])
pts_vs_flavor_pop["flavor"].mean()

# A point estimate or sample statistics is a calculation made on the sample dataset
np.mean(pts_vs_flavor_samp)
pts_vs_flavor_samp["flavor"].mean()