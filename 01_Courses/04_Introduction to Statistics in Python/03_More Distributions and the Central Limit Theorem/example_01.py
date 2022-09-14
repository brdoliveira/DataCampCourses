from scipy.stats import norm
import matplotlib.pyplot as plt

"""
# The normal distribution
# # Curve never hits 0 

# What percent of women are shorter than 154 cm?
norm.cdf(154, 161,7) # number interest (154), mean (161)

# What percent of women are taller than 154 cm? 
1 - norm.cdf(154,161,7)

# What percent of women are 154-157 cm?
norm.cdf(157,161,7) - norm.cdf(154,161,7)

# What height are 90% of women shorter than?
norm.ppf(0.9,161,7)

# What height are 90% of women taller than?
norm.ppf((1-0.9),161,7)

# Generating random numbers
# # Generate 10 random numbers
norm.rvs(161, 7, size=10)
"""

# Probability of deal < 7500
prob_less_7500 = norm.cdf(7500,5000,2000)
print(prob_less_7500)

# Probability of deal > 1000
prob_over_1000 = 1- norm.cdf(1000,5000,2000)
print(prob_over_1000)

# Probability of deal between 3000 and 7000
prob_3000_to_7000 = norm.cdf(7000,5000,2000) - norm.cdf(3000,5000,2000)
print(prob_3000_to_7000)

# Calculate amount that 25% of deals will be less than
pct_25 = norm.ppf(0.25,5000,2000)
print(pct_25)


# Calculate new average amount
new_mean = 5000 * 1.2

# Calculate new standard deviation
new_sd = 2000 * 1.3

# Simulate 36 new sales
new_sales = norm.rvs(new_mean, new_sd, size=36)

# Create histogram and show
plt.hist(new_sales)
plt.show()