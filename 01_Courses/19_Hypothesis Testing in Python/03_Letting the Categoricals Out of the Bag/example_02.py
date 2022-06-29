"""
# A sense of proportion

"""
from statsmodels.stats.proportion import proportions_ztest
import pandas as pd
import numpy as np

stack_overflow = pd.read_feather(".\data\stack_overflow.feather")
# print(stack_overflow.head())

# Comparing two proportions
# # H0 : Proportion of hobbyist users is the same for those under thirty as those at least thirty
# # H0 : p >= 30 - p <= 30 = 0
# # HA : Proportion of hobbyist users is different for those under thirty to those at least thirty
# # HA : p >= 30 - p <= 30 ≠ 0
alpha = 0.05

# Getting the numbers for the z-score
p_hats = stack_overflow.groupby("age_cat")['hobbyist'].value_counts(normalize=True)

n = stack_overflow.groupby("age_cat")['hobbyist'].count()

p_hats = stack_overflow.groupby("age_cat")['hobbyist'].value_counts(normalize=True)

p_hat_at_least_30 = p_hats[("At least 30","Yes")]
p_hat_under_30 = p_hats[("Under 30","Yes")]
print(p_hat_at_least_30, p_hat_under_30)

n = stack_overflow.groupby("age_cat")['hobbyist'].count()

n_at_least_30 = n["At least 30"]
n_under_30 = n["Under 30"]
print(n_at_least_30, n_under_30)

p_hat = (n_at_least_30 * p_hat_at_least_30 + n_under_30 * p_hat_under_30) /(n_at_least_30 + n_under_30)
std_error = np.sqrt(p_hat * (1-p_hat) / n_at_least_30 +p_hat * (1-p_hat) / n_under_30)
z_score = (p_hat_at_least_30 - p_hat_under_30) / std_error
print(z_score)

# Proportion tests using proportions_ztest()
age_by_hobbyist = stack_overflow.groupby("age_cat")['hobbyist'].value_counts()
success_counts = np.array([812, 1021])
n = np.array([812 + 238, 1021 + 190])
stat, p_value = proportions_ztest(count=success_counts, nobs=n,
                                  alternative="two-sided")