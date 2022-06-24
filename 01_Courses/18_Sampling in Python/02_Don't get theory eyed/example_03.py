"""
# What a cluster...

# Stratified sampling vs. cluster sampling
# # Stratified sampling
# # # Split the population int subgroups
# # # Use simple random sampling on every subgroup
# # Cluster Sampling
# # # Use simple random sampling to pick some subgroups
# # # Use simple random sampling on only those subgroups
"""
# pip install pyarrow
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

coffee_ratings = pd.read_feather("./data/coffee_ratings_full.feather")
# print(coffe_rating_full.head())

varieties_pop = list(coffee_ratings['variety'].unique())

# Stage 1: sampling for subgroups
varieties_samp = random.sample(varieties_pop,k=3)

# Stage 2: sampling each group
variety_condition = coffee_ratings['variety'].isin(varieties_samp)
coffee_ratings_cluster = coffee_ratings[variety_condition]

coffee_ratings_cluster['variety'] = coffee_ratings_cluster['variety'].cat.remove_unsed_categories()

coffee_ratings_cluster.groupby("variety")\
    .sample(n=5,random_state=2021)

# Multistage sampling
# # Cluster sampling is a type of multistage sampling
# # Can have > 2 stages
# # E.g., countrywides surveys many sample states, counties, cities, and neighborhoods