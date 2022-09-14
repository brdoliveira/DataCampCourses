"""
# Assumptions not met

# # Parametric tests
# # # z-test, t-test, and ANOVA are all parametric tests
# # # Assume a normal distribution
# # # Require sufficiently large sample sizes
"""
from scipy.stats import rankdata
import pandas as pd
import numpy as np
import pingouin

repub_votes_small = pd.read_feather("./data/repub_votes_potus_08_12.feather")
# print(repub_votes_small.head())

# Results with pingouin.ttest()
# # 5 pairs is not enough to meet the sample size condition for the paired t-test:
# # # At least 30 pairs of observations across the samples.
alpha = 0.01
pingouin.ttest(x=repub_votes_small['repub_percent_08'],
               y=repub_votes_small['repub_percent_12'],
               paired=True,
               alternative="less")

# Non-parametric tests
# # Non-parametric tests avoid the parametric assumptions and conditions
# # Many non-parametric tests use ranks of the data
x = [1, 15, 3, 10, 6]
rankdata(x)

"""
# Non-parametric tests
# # Non-parametric tests are more reliable than parametric tests for small sample sizes and when data isn't normally distributed
# Wilcoxon-signed rank test
# # Developed by Frank Wilcoxon in 1945
# # One of the first non-parametric procedures
"""

# Wilcoxon-signed rank test
# # Works on the ranked absolute differences between the pairs of data
repub_votes_small['diff'] = repub_votes_small['repub _percent _ 08'] - repub_votes_small['repub _percent _ 12'] 
# print(repub_votes_small.head())

repub_votes_small['abs_diff'] = repub_votes_small['diff'].abs()
# print(repub_votes_small.head())

repub_votes_small['rank_abs_diff'] = rankdata(repub_votes_small['abs_diff'])
# print(repub_votes_small.head())

# Incorporate the sum of the ranks for negative and positive dierences
T_minus = 1 + 4 + 5 + 2 + 3
T_plus = 0
W = np.min([T_minus, T_plus])

# Implementation with pingouin.wilcoxon()
alpha = 0.01
pingouin.wilcoxon(x=repub_votes_small['repub_percent_08'],
                  y=repub_votes_small['repub_percent_12'],
                  alternative="less") # Fail to reject H0, since 0.03125 > 0.01