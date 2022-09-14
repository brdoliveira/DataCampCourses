"""
# Pairing is caring

# Hypotheses
# # Question: Was the percentage of Republican candidate votes lower in 2008 than 2012?
# # H0 : μ2008 - μ2012 = 0
# # HA : μ2008 - μ2012 < 0
# # Set α = 0.05 signicance level.
# # # Data is paired → each voter percentage refers to the same county
# # # # Want to capture voting paerns in model
"""
import matplotlib.pyplot as plt
from scipy.stats import t
import pandas as pd
import numpy as np
import pingouin

repub_votes_potus_08_12 = pd.read_feather('./data/repub_votes_potus_08_12.feather')
print(repub_votes_potus_08_12.head())

# From two samples to one
sample_data = repub_votes_potus_08_12
sample_data['diff'] = sample_data['repub_percent_08'] - sample_data['repub_percent_12']

sample_data['diff'].hist(bins=20)
plt.show()

# Calculate sample statistics of the difference
xbar_diff = sample_data['diff'].mean()

"""
# Revised hypotheses
# # Old hypotheses:
# # H0 : μ - μ = 0
# # HA : μ - μ < 0
# # New hypotheses:
# # H0 : μ = 0
# # HA : μ < 0
"""

# Calculating the p-value
n_diff = len(sample_data)

s_diff = sample_data['diff'].std()
t_stat = (xbar_diff-0) / np.sqrt(s_diff**2/n_diff)

degrees_of_freedom = n_diff - 1

p_value = t.cdf(t_stat, df=n_diff-1)

# Testing differences between two means using ttest()
pingouin.ttest(x=sample_data['diff'],
               y=0,
               alternative="less")

# ttest() with paired=True
pingouin.ttest(x=sample_data['repub_percent_08'],
               y=sample_data['repub_percent_12'],
               paired=True,
               alternative="less")

# Unpaired ttest()
pingouin.ttest(x=sample_data['repub_percent_08'],
               y=sample_data['repub_percent_12'],
               paired=False, # The default
               alternative="less")
# Unpaired t-tests on paired data increases the chances of false negative errors