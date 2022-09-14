"""
# Can't get no stratisfaction
"""
# pip install pyarrow
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

coffee_ratings = pd.read_feather("./data/coffee_ratings_full.feather")
# print(coffe_rating_full.head())

top_counts = coffee_ratings["country_of_origin"].value_counts()
# print(top_counts.head(6))

top_counted_countries = ["México","Colombia","Guatemala","Brazil","Taiwan","United States (Hawaii)"]

top_counted_subset = coffee_ratings['country_of_origin'].isin(top_counted_countries)

coffee_ratings_top = coffee_ratings[top_counted_subset]

# Counts of a simple random sample
coffee_ratings_samp = coffee_ratings_top.sample(frac=0.1,random_state=2021)

coffee_ratings_samp['country_of_origin'].value_counts(normalize=True)

# Proportional stratified sampling
coffee_ratings_strat = coffee_ratings_top.groupby("country_of_origin")\
    .sample(frac=0.1,random_state=2021)

coffee_ratings_strat["country_of_origin"].value_counts(normalize=True)

# Equal counts stratified sampling
coffee_ratings_eq = coffee_ratings_top.groupby("country_of_origin")\
    .sample(n=15,random_state=2021)

coffee_ratings_eq["country_of_origin"].value_counts(normalize=True)

# Weigthted random sampling
# # Specify weights to adjust the relative probability of a row being sampled

import numpy as np

coffee_ratings_weight = coffee_ratings_top
condition = coffee_ratings_weight['country_of_origin'] == "Taiwan"

coffee_ratings_weight['weight'] = np.where(condition,2,1)

coffee_ratings_weight = coffee_ratings_weight.sample(frac=0.1,weights="weight")

# Weighted random sampling results
# # 10% weighted sample:
coffee_ratings_weight["country_of_origin"].value_counts(normalize=True)