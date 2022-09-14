"""
# Does this dress make my fit look good?
"""
from scipy.stats import chisquare
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pingouin

stack_overflow = pd.read_feather(".\data\stack_overflow.feather")
# print(stack_overflow.head())

# Purple links
# # You search for a coding solution online and the rst result link is purple because you alreadyvisited it. How do you feel ?
purple_link_counts = stack_overflow['purple_link'].value_counts()
purple_link_counts = purple_link_counts.rename_axis('purple_link').reset_index(name='n')

# Declaring the hypotheses
hypothesized = pd.DataFrame({'purple_link': ['Hello, old friend','Amused','Indifferent','Annoyed'],
                             'prop': [1/2, 1/6, 1/6, 1/6]})

# # H0 : The sample matches with the hypothesized distribution
# # HA : The sample does not match with the hypothesized distribution

# χ2 measures how far observed results are from expectations in each group
alpha = 0.01

# Hypothenized counts by category
n_total = len(stack_overflow)
hypothesized['n'] = hypothesized["prop"] * n_total

# Visualizing counts
plt.bar(purple_link_counts['purple_link'], purple_link_counts['n'],color="orange", alpha=0.5)
plt.scatter(hypothesized['purple_link'], hypothesized['n'], color="purple")
plt.show()

# chi-square goodness of fit test
print(hypothesized)
chisquare(f_obs=purple_link_counts['n'],f_exp=hypothesized['n'])