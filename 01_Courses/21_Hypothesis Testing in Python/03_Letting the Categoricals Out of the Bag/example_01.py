"""
# Difference strokes for proportions, folks

# Standardized test statistic for proportions
# # p : population proportion (unknown population parameter)
# # p^: sample proportion (sample statistic)
# # p0: hypothesized population proportion
# # Assuming H is true, p = p , so

# Why z instead of t?
# # T = (x child - x adult) / sqrt((s^2 child / n child) + (s^2 adult / n adult))
# # s is calculated from x
# # # x estimates the population mean
# # # s estimates the population standard deviation
# # # ↑ uncertainty in our estimate of the parameter
# # t-distribution - fatter tails than a normal distribution
# # p^ only appears in the numerator, so z-scores are fine
"""
from scipy.stats import norm
import pandas as pd
import numpy as np

stack_overflow = pd.read_feather(".\data\stack_overflow.feather")
# print(stack_overflow.head())

# Stack Overflow age categories
# # H0 : Proportion of Stack Overow users under thirty = 0.5
# # HA : Proportion of Stack Overow users under thirty ≠ 0.5
alpha = 0.01
stack_overflow['age_cat'].value_counts(normalize=True)

# Variables for z
p_hat = (stack_overflow['age_cat'] == "Under 30").mean()
p_0 = 0.50

n = len(stack_overflow)

# Calculating the z-score
numerator = p_hat - p_0
denominator = np.sqrt(p_0 * (1 - p_0) / n)
z_score = numerator / denominator

# Calculating the p-value
# # Left-tailed ("less than"):
p_value = norm.cdf(z_score)
# # Right-tailed ("greater than"):
p_value = 1 - norm.cdf(z_score)
# # Two-tailed ("not equal"):
p_value = norm.cdf(-z_score) + (1 - norm.cdf(z_score))
p_value = 2 * (1 - norm.cdf(z_score))
print(p_value <= alpha)