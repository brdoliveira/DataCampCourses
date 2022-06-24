"""
# Straight to the point (estimate)
"""

# pip install pyarrow
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

coffee_ratings = pd.read_feather("./data/coffee_ratings_full.feather")
# print(coffe_rating_full.head())

top_counted_countries = ["Mexico","Colombia","Guatemala","Brazil","Taiwan","United States (Hawaii)"]

subset_condition = coffee_ratings["country_of_origin"].isin(top_counted_countries)
coffee_ratings_top = coffee_ratings[subset_condition]

coffee_ratings_srs = coffee_ratings_top.sample(frac=1/3, random_state=2021)
print(coffee_ratings_srs.shape)

# Review of stratified sampling
coffee_ratings_strat = coffee_ratings_top.groupby("country_of_origin")\
    .sample(frac=1/3,random_state=2021)
print(coffee_ratings_strat.shape)

# Review of cluster sampling
top_countries_samp = random.sample(top_counted_countries,k=2)
top_condition = coffee_ratings_top["country_of_origin"].isin(top_countries_samp)

coffee_ratings_cluster = coffee_ratings_top[top_condition]
coffee_ratings_cluster['country_of_origin'] = coffee_ratings_cluster['country_of_origin']\
    .cat.remove_unused_categories()

coffee_ratings_clust = coffee_ratings_cluster.groupby("country_of_origin")\
    .sample(n=len(coffee_ratings_top) // 6)

print(coffee_ratings_clust.shape)

# Calculating mean cup points
# # Population
coffee_ratings_top['total_cup_points'].mean()
# # Stratified sample
coffee_ratings_strat['total_cup_points'].mean()
# # Simple random sample
coffee_ratings_srs['total_cup_points'].mean()
# # Cluster sample
coffee_ratings_clust['total_cup_points'].mean()

# Mean cup points by country: simple random
# # Population:
coffee_ratings_top.groupby("country_of_origin")\
    ["total_cup_points"].mean()
# # Stratified sample:
coffee_ratings_strat.groupby("country_of_origin")\
    ["total_cup_points"].mean()
# # Simple random sample:
coffee_ratings_srs.groupby("country_of_origin")\
    ["total_cup_points"].mean()
# # Cluster sample:
coffee_ratings_clust.groupby("country_of_origin")\
    ["total_cup_points"].mean()