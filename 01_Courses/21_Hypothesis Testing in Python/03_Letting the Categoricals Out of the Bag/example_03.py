"""
# Declaration of independence
"""
from statsmodels.stats.proportion import proportions_ztest
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pingouin

stack_overflow = pd.read_feather(".\data\stack_overflow.feather")
# print(stack_overflow.head())

# Revisiting the proportion test
age_by_hobbyist = stack_overflow.groupby("age_cat")['hobbyist'].value_counts()

success_counts = np.array([812, 1021])
n = np.array([812 + 238, 1021 + 190])
stat, p_value = proportions_ztest(count=success_counts, nobs=n,
                                alternative="two-sided")

# Independence of variables
# # Previous hypothesis test result: evidence that hobbyist and age_cat are associated
# # Statistical independence - proportion of successes in the response variable is the sameacross all categories of the explanatory variable
expected, observed, stats = pingouin.chi2_independence(data=stack_overflow, x='hobbyist',y='age_cat', correction=False)
print(stats)

# Job satisfaction and age category
stack_overflow['age_cat'].value_counts()

stack_overflow['job_sat'].value_counts()

# Declaring the hypotheses
# # H0 : Age categories are independent of job satisfaction levels
# # HA : Age categories are not independent of job satisfaction levels
alpha = 0.1
# # Test statistic denoted χ2
# # Assuming independence, how far away are the observed results from the expected values?
props = stack_overflow.groupby('job_sat')['age_cat'].value_counts(normalize=True)
wide_props = props.unstack()
wide_props.plot(kind="bar", stacked=True)
plt.show()

# Chi-square independence test
expected, observed, stats = pingouin.chi2_independence(data=stack_overflow, x="job_sat", y="age_cat")
print(stats)
# Degrees of freedom:
# # (No. of response categories - 1) * (No. of explanatory categories - 1)
# # (2 - 1) * (5 - 1) = 4
props = stack_overflow.groupby('age_cat')['job_sat'].value_counts(normalize=True)
wide_props = props.unstack()
wide_props.plot(kind="bar", stacked=True)
plt.show()

# chi-square both ways
expected, observed, stats = pingouin.chi2_independence(data=stack_overflow, x="job_sat", y="age_cat")
print(stats[stats['test'] == 'pearson'])
# # Ask: Are the variables X and Y independent?
# # Not: Is variable X independent from variable Y?

# What about direction and tails?
# # Observed and expected counts squared must be non-negative
# # chi-square tests are almost always right-tailed

# # Le-tailed chi-square tests are used in statistical forensics to detect if a t is suspiciously good because the
# # data was fabricated. Chi-square tests of variance can be two-tailed. These are niche uses, though.