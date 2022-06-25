"""
# Venus infers

# Confidence intervals
# # "Values within one standard deviation of the mean" includes a large number of values from each of these distributions
# # We'll define a related concept called a confidence interval

"""
# pip install pyarrow
import matplotlib.pyplot as plt
from scipy.stats import norm
import pandas as pd
import numpy as np

coffee_ratings = pd.read_feather("./data/coffee_ratings_full.feather")
# print(coffe_rating_full.head())

mean_flavor_5000 = []

for i in range(5000):
    mean_flavor_5000.append(
        np.mean(coffee_ratings.sample(frac=1,replace=True)['flavor'])
    )

bootstrap_distn = mean_flavor_5000

# Bootstrap distribution histogram
plt.hist(bootstrap_distn,bins=15)
plt.show()

# mean of the resample
np.mean(bootstrap_distn)
np.mean(bootstrap_distn) - np.std(bootstrap_distn,ddof=1)
np.mean(bootstrap_distn) + np.std(bootstrap_distn,ddof=1)

# Quantile method for confidence intervals
np.quantile(bootstrap_distn,0.025)
np.quantile(bootstrap_distn,0.925)

# Inverse cumulative distribution function
# # PDF: The bell curve
# # CDF: Integrate to get area under bell curve
# # Inv. CDF: flip x and y axes
quantile=0.25
norm.ppf(quantile,loc=0,scale=1)

# Standard error method for confidence interval
point_estimate = np.mean(bootstrap_distn)
std_error = np.std(bootstrap_distn,ddof=1)

lower = norm.ppf(0.025,loc=point_estimate,scale=std_error)
upper = norm.ppf(0.975,loc=point_estimate,scale=std_error)
print((lower,upper))