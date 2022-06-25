"""
# Err on the side of Gaussian

# Consequences of the central limit theorem
# # Averages of independent samples have approximately NORMAL DISTRIBUTIONS.
# As the sample size increases,
# #  The distribution of the avarages gets closer to being normally distributed
# #  The width of the sampling distribution gets narrower
"""
# pip install pyarrow
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

coffee_ratings = pd.read_feather("./data/coffee_ratings_full.feather")
# print(coffe_rating_full.head())

# Population & sampling distribution means
coffee_ratings['total_cup_points'].mean()

# Population & sampling distribution means
coffee_ratings['total_cup_points'].std(ddof=0) # when ddof=0 when calling .std() on populations
                                               # when ddof=1 when calling .std() on samples or sampling distributions

# Standard error
# # Standard deviation of the sampling distribution
# # Important tool in undestanding sampling variability