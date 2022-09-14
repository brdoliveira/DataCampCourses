"""
# Time for t

# t-distributions
# # t statistic follows a t-distribution
# # Have a parameter named degrees of freedom, or df
# # Look like normal distributions, with fatter tails

# Degrees of freedom
# # Larger degrees of freedom → t-distribution gets closer to the normal distribution
# # Normal distribution → t-distribution with infinite df
# # Degrees of freedom: maximum number of logically independent values in the data sample

# Calculating degrees of freedom
# # Dataset has 5 independent observations
# # Four of the values are 2, 6, 8, and 5
# # The sample mean is 5
# # The last value must be 4
# # Here, there are 4 degrees of freedom
# df = n child + n adult - 2

# Hypotheses
# # H0 : The mean compensation (in USD) is the same for those that coded rst as a child and those that coded first as an adult
# # HA : The mean compensation (in USD) is greater for those that coded rst as a child compared to those that coded first as an adult
# # Use a right-tailed test

# Significance level
# # α = 0.1
# # If p ≤ α then reject H0

"""
from scipy.stats import norm, t
import pandas as pd
import numpy as np

stack_overflow = pd.read_feather(".\data\stack_overflow.feather")
# print(stack_overflow.head())

# Calculating the z-score
prop_child_samp = (stack_overflow['age_first_code_cut'] == "child").mean()
prop_child_hyp = 0.35

# Generating a bootstrap distribution
# Step 3. Repeat steps 1 & 2 many times, appediding to a list
so_boot_distn = []

for i in range(5000):
    so_boot_distn.append(
        # Step 2. Calculate point estimate
        np.mean(
            # Step 1. Resample
            stack_overflow.sample(frac=1,replace=True)['converted_comp']
        )    
    )

std_error = np.std(so_boot_distn,ddof=1)

z_score= (prop_child_samp - prop_child_hyp) / std_error

# Calculating p-values: one proportion vs. a value
1 - norm.cdf(z_score)
# # z-statistic: needed when using one sample statistic to estimate a population parameter
# # t-statistic: needed when using multiple sample statistics to estimate a population parameter

# Calculating p-values: two means from different groups
numerator = xbar_child - xbar_adult
denominator = np.sqrt(s_child ** 2 / n_child + s_adult ** 2 / n_adult)
t_stat = numerator / denominator

degrees_of_freedom = n_child + n_adult - 2

# Calculating p-values: two means from different groups
# Use t-distribution CDF not normal CDF
1 - t.cdf(t_stat,df=degrees_of_freedom)
# Evidence that Stack Overow data scientists who started coding as a child earn more.