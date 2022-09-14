"""
# A breath of fresh error
"""
# pip install pyarrow
import matplotlib.pyplot as plt
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

"""
# Interpreting the means
# # Bootstrap distribution mean:
# # # Usually close to the sample mean
# # # May not be a good estimate of the population mean
# # BOOTSTRAPPING CANNOT CORRECT BIASES FROM SAMPLING
"""

standard_error = np.std(bootstrap_distn,ddof=1) # Standard error is the standard deviation of the statistic of interest
std_sqrt = standard_error * np.sqrt(500) # Standard error times square root of sample size estimates the population standard deviation

coffee_sample = coffee_ratings.sample(n=10)
original_std = coffee_sample['flavor'].std()
real_std = coffee_ratings['flavor'].std(ddof=0)
print(original_std," and ",std_sqrt," and ",real_std)

# Interpreting the standard errors
# # Estimated standard error -> standard deviation of the bootstrap distribution for a sample statistic