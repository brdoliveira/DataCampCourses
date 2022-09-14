"""
# Is this some kind of test statistic?

# Two-sample problems
# # Compare sample statistics across groups of a variable
# # converted_comp is a numerical variable 
# # age_first_code_cut is a categorical variable with levels ( "child" and "adult" )
# # Are users who rst programmed as a child compensated higher than those that started as adults?

# Hypotheses
# # H0 : The mean compensation (in USD) is the same for those that coded rst as a child and those that coded rst as an adult.
# # H0 : μ child = μ adult
# # H0 : μ child - μ adult = 0
# # HA : The mean compensation (in USD) is greater for those that coded rst as a child compared to those that coded rst as an adult.
# # HA : μ child > μ adult
# # HA : μ child - μ adult > 0
"""
from scipy.stats import norm
import pandas as pd
import numpy as np

stack_overflow = pd.read_feather(".\data\stack_overflow.feather")
# print(stack_overflow.head())

# Calculating groupwise summary statistics
stack_overflow.groupby('age_first_code_cut')['converted_comp'].mean()

"""
# Test statistics
# # s - Sample mean estimates the population mean
# # x - a sample mean
# # x child- sample mean compensation for coding first as a child
# # x adult - sample mean compensation for coding first as an adult
# # x child - x adult - a test statistic
# # z-score - a (standardized) test statistic

# Standardizing the test statistic
# # z = (sample stat - population parameter) / standard error
# # t = (difference in sample stats - difference in population parameters) / standard error
# # t = (x child - x adult) - (μ child - μ adult) / SE(x child - x adult) 
"""

# Calculations assuming the null hypothesis is true
xbar = stack_overflow.groupby('age_first_code_cut')['converted_comp'].mean()

s = stack_overflow.groupby('age_first_code_cut')['converted_comp'].std()

n = stack_overflow.groupby('age_first_code_cut')['converted_comp'].count()

# Calculating the test statistic
numerator = xbar_child - xbar_adult
denominator = np.sqrt(s_child ** 2 / n_child + s_adult ** 2 / n_adult)
t_stat = numerator / denominator