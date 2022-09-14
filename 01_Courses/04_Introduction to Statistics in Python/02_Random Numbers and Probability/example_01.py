"""
# P(event) = # ways event can happen / total # of possible outcome

# Example: a coin flip 
# P(event) = # ways event can happen / total # of possible outcome -> 1/2 -> 50%

# Sampling from a DataFrame
print(sales_counts)
print(sales_counts.sample()) # random choice

np.random.seed(10) # setting a random seed
print(sales_counts.sample())

print(sales_counts.sample(2)) # sampling twice in python
print(sales_counts.sample(5, replace = True)) # sampling with/without replacement in Python

# Depends events -> Two events are dependent if the probability of the second event is affected by the outcome of the first event.
"""
import pandas as pd
import numpy as np

amir_deals = pd.read_csv("./data/amir_deals.csv")

# Count the deals for each product
counts = amir_deals['product'].value_counts()

# Calculate probability of picking a deal with each product
probs = counts / amir_deals.shape[0]
print(probs)

# Set random seed
np.random.seed(24)

# Sample 5 deals without replacement
sample_without_replacement = amir_deals.sample(5)
print(sample_without_replacement)

# Sample 5 deals with replacement
sample_with_replacement = amir_deals.sample(5,replace=True)
print(sample_with_replacement)