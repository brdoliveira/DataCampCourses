"""
# A tail of two z's

#  Criminal trials
# # Two possible true states:
# # # Defendant commited the crime
# # # Defendant did not commit the crime
# # Two possible verdicts:
# # # 1. Guilty
# # # 2. Not guilty
# # Initially the defendant is assumed to be not guilty
# # Prosecution must prevent evidence "beyond reasonable doubt" for a guilty verdict

# Age of first programming experience
# # age_first_code_cut classifies when Stack Overflow user first started programming
# # # "adult" means they started at 14 or older
# # # "child" means they started before 14
# # PREVIOUS RESEARCH: 35% of software developers started programming as children
# # Evidence that a greater proportion of data scientists stanting programming as children?

# Definitions
# # A hypothesis is a statement about an unknown population parameter
# # A hypothesis test is a test of two competing hypotheses
# # # The null hypothesis (H0) is the existing idea
# # # The alternative hypothesis (HA) is the new "challenger" idea of the researcher
# # For our problem:
# # # H0: The proportion of data scientists starting programming as children is 35%
# # # HA: The proportion of data scientists starting programming as children is greater than 35%

# Criminal trials vs. hypothesis testing
# # Either HA or H0 us true (not both)
# # Initially, H0 is assumed to be true
# # The test ends in either "reject H0" or "fail to reject H0"
# # If the evidence from the sample is "significant" tha HA is true, reject H0, else choice H0
# Significance level is "beyond a reasonable doubt" for hypothesis testing

# One-tailed and two-tailed tests
# # Hyphotesis tests check if the sample statistics lie in the tails of null distribution

# #|  TESTS                         | TAILS       |
# #|alternative different from null |two-tailed   |
# #|alternative greater than null   |right-tailed |
# #|alternative less than null      |left-tailed  |

# HA: The proportion of data scientists starting programming as children is greater than 35%
# This is a right-tailed test

# p-values
# # p-values: probability of obtaining a result, assuming the null hypothesis is true
# # # Large p-value, large support for H0
# # # # Statistic likely NOT IN the tail of the null distribution
# # # Small p-value, strong evidence against H0
# # # # Statistic likely in the trail of the null distribution
# # # "p" in p-value -> probability
# # # "small" means "close to zero"
"""
import matplotlib.pyplot as plt
from scipy.stats import norm
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

# Calculating the p-value
# norm.cdf() is normal CDF from scipy.stats.
# # Left-tailed test -> use norm.cdf().
# # Right-tailed test -> use 1 - norm.cdf().

1 - norm.cdf(z_score,loc=0,scale=1)