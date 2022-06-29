"""
# What do you assume?

# Randomness
# # Assumption
# # # The samples are random subsets of larger populations
# # Consequence
# # # Sample is not representative of population
# # How to check this
# # # Understand how your data was collected
# # # Speak to the data collector/domain expert

#  Independence of observations
# # Assumption
# # # Each observation (row) in the dataset is independent
# # Consequence
# # # Increased chance of false negative/positive error
# # How to check this
# # # Understand how our data was collected

# Large sample size
# # Assumption
# # # The sample is big enough to mitigate uncertainty, so that the Central Limit Theorem applies
# # Consequence
# # # Wider confidence intervals
# # # Increase chance of false negative/positive errors
# # How do check this
# # # It depends on the test

# Large sample size: t-test
# # One sample
# # # At least 30 observations in the sample n ≥ 30
# # # n: sample size

# # Paired samples
# # # At least 30 pairs of observations across the samples
# # # Number of rows in our data ≥ 30

# # Two samples
# # # At least 30 observations in each sample
# # # n ≥ 30, n2 ≥ 30
# # # n : sample size for group i

# # ANOVA
# # # At least 30 observations in each sample
# # # ni ≥ 30 for all values of i

# Large sample size: proportion tests

# # One sample
# # # Number of successes in sample is greater than or equal to 10
# # # n * p^ ≥ 10
# # Number of failures in sample is greater than or equal to 10
# # # n * (1 - ) ≥ 10
# # # n: sample size
# # # p^ : proportion of successes in sample

# # Two samples
# # # Number of successes in each sample is greater than or equal to 10
# # # n * ≥ 10
# # # n * ≥ 10
# # Number of failures in each sample is greater than or equal to 10
# # # n * (1 - p^ 1 ) ≥ 10
# # # n * (1 - p^ 2 ) ≥ 10

# # Large sample size: chi-square tests
# # # The number of successes in each group in greater than or equal to 5
# # # n * ≥ 5 for all values of i
# # # The number of failures in each group in greater than or equal to 5
# # # n * (1 * p^ 1 ) ≥ 5 for all values of i
# # # n : sample size for group i
# # # p^ 1: proportion of successes in sample group i

# # Sanity check
# # # If the bootstrap distribution doesn't look normal, assumptions likely aren't valid
# # # Revisit data collection to check for randomness, independence, and sample size
"""