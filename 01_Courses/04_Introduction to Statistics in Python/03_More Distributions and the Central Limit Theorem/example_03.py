"""
# The Poisson distribution
# # Events appear to happen at a certain rate, but completely at random
# # Examples :
# # # Number of animals adopted from an animal shelter per week  
# # # Number of people arriving at a restaurant per hour
# # # Number of earthquakes in California per year
# # The unit is irrelevant, as long a you use the same unit when talking about the same situation
# # ´Probability of some # of events ocurring over a fixed period a time
# # Examples:
# # # Probability of >= 5 animals adopted from an animal shelter per week
# # # Probability of 12 people arriving at a restaurant per hour
# # # Probability < 20 earthquakes in California per year

# Lambda = average number of events per time interval
# # Avarage number of adoptions per week = 8
"""
from scipy.stats import poisson

# Probability of a single value
# # If the average number of adoptions per week is 8, what is P (# adoptions in a week = 5)?
poisson.pmf(5,8)

# Probability of less than or equal to
# # If the average number of adoptions per week is 8, what is P (# adoptions in a week <= 5)?
poisson.cdf(5,8)

# # If the average number of adoptions per week is 8, what is P (# adoptions in a week > 5)?
1 - poisson.cdf(5,8)

# Sampling from a Poisson distribution
poisson.rvs(8,size=10)