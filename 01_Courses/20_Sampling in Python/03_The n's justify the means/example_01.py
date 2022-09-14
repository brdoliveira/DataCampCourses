"""
# An ample sample
"""
# pip install pyarrow
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

coffee_ratings = pd.read_feather("./data/coffee_ratings_full.feather")
# print(coffe_rating_full.head())

# Sample size is number of rows
len(coffee_ratings.sample(n=300))
len(coffee_ratings.sample(frac=0.25))

# Various simple size
coffee_ratings['total_cup_points'].mean()
coffee_ratings.sample(n=10)['total_cup_points'].mean()
coffee_ratings.sample(n=100)['total_cup_points'].mean()
coffee_ratings.sample(n=1000)['total_cup_points'].mean()

# Relative errors
# # Population parameter:
population_mean = coffee_ratings['total_cup_points'].mean()

# # Point estimate:
sample_size=5
sample_mean = coffee_ratings.sample(n=sample_size)['total_cup_points'].mean()

# # Relative error as a percentage:
rel_error_pct = 100 * abs(population_mean-sample_mean) / population_mean

# Properties:
# # Really noise, particularly for small samples
# # Amplitude is initially steep, then flattens
# # Relative error decreases to zero (when the sample size = population)

"""
# Generate a simple random sample of 50 rows, with seed 2022
attrition_srs50 = attrition_pop.sample(n=50, random_state=2022)

# Calculate the mean employee attrition in the sample
mean_attrition_srs50 = attrition_srs50['Attrition'].mean()

# Calculate the relative error percentage
rel_error_pct50 = 100 * abs(mean_attrition_pop-mean_attrition_srs50) / mean_attrition_pop

# Print rel_error_pct50
print(rel_error_pct50)
"""