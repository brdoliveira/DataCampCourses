"""
# To the lab for testing

# # A/B Testing
# # # In 2013, Eletronic Arts (EA) released SimCity 5
# # # They wanted to increase pre-orders of the game
# # # They used A/B testing to test different adversing scenarios
# # # This envolves splitting users into control and treatment groups
# # # RETAIL WEBPAGE A/B TEST (WITH AD AND NO AD)

# # A/B Test results
# # # The treatment group (no ad) got 43.4% more purchases than the control group (with ad)
# # # Intuition thar "showing an ad would increase sales" was false
# # # Was this result statically significant or just chance?
# # # Need EA's data to determine this
# # # Techiques from Sampling in pythom + this course to do so
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

stack_overflow = pd.read_feather(".\data\stack_overflow.feather")
# print(stack_overflow.head())

# Hypothezing about the mean
# # A hypothesis:
# # # The mean annual compensation of the population of data scientists is $110,000
# # The point estimate (sample statistic):
mean_comp_samp = stack_overflow['converted_comp'].mean()

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

# Visualing the bootstrap distribution
plt.hist(so_boot_distn, bins=50)
plt.show()

# Standard error
std_error = np.std(so_boot_distn,ddof=1)

# Z-SCORES
# # standardized_mean = (value - mean) / standard deviation
# # z-scores = sample stat - hypoth.param.value / standard error
mean_comp_hyp = 110000
z_scores = (mean_comp_samp - mean_comp_hyp) / std_error

# Testing the hypothesis
# # Is 1.707 a high or a low number?
# # This is the goal of the course!

# Hypothesis testing use case:
# # Determine whether sample statistics are close to or far awat from expected (or "hypothesized" values)

# Standard normal (z) distribution
# # Standard normal distribution: normal distribution with MEAN = 0 + STANDARD DEVIATION = 1