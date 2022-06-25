"""
# Statistically significant other

# p-value recap
# # p-values quantify evidence for the null hypothesis
# # Large p-value -> fail to reject null hypothesis
# # Small p-value -> reject null hypothesis
# Where is the cutoff point?

# Significance level
# # The signicance level of a hypothesis test(α) is the threshold point for "beyond a reasonable doubt"
# # # Common values of α are 0.2 , 0.1 , 0.05 , and 0.01 
# # # If p≤ α , reject H , else fail to reject H
# # # α should be set prior to conducting the hypothesis test

"""
from scipy.stats import norm
import pandas as pd
import numpy as np

stack_overflow = pd.read_feather(".\data\stack_overflow.feather")
# print(stack_overflow.head())


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

# # Caculating
alpha = 0.05
prop_child_samp = (stack_overflow['age_first_code_cut'] == "child").mean()
prop_child_hyp = 0.35
std_error = np.std(so_boot_distn,ddof=1)

z_score = (prop_child_samp - prop_child_hyp) / std_error
p_value = 1 - norm.cdf(z_score,loc=0,scale=1)

# # Making a decision
alpha = 0.05
print(p_value) 

print(p_value <= alpha) # Reject H0 in favor of HA

# Confidence intervals
# # For asignicance level of α, it's common to choose a confidence interval level of 1-α 
# # # α= 0.05 → 95% confindence interval

lower = np.quantile(so_boot_distn, 0.025)
upper = np.quantile(so_boot_distn, 0.975)
print((lower, upper))

# Possible errors in our example
# # If p ≤ α, we reject H: A false positive (Type I) error: data scientists didn't start coding as children at a higher rate 
# # If p > α, we fail to reject H: A false negative (TypeII) error: data scientists started coding as children at a higher rate
