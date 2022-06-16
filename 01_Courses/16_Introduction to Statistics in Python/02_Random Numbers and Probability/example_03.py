"""
from scipy.stats import uniform
# Continuous Distribuitions
# # wait for a bus that passes every 15 minutes

# # Probability still = area
# # what is the probability of waiting between 4 to 7 minutes?
# (4 - 7) = 3 * 1/12 = 3/12 > 25%
# OR
uniform.cdf(7,0,12) - uniform.cdf(4,0,12) # 25% 


uniform.cdf(7,0,12) # 58 % ( < 7)
# inferior limit -> 0
# upper limit -> 12

# ( > 7)
1 - uniform.cdf(7,0,12)

# Generating random numbers according to uniform distribuition
uniform.rvs(0,5,size=10) # max value , min value, random values

"""

# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30

# Import uniform from scipy.stats
from scipy.stats import uniform

# Calculate probability of waiting less than 5 mins
prob_less_than_5 = uniform.cdf(5,min_time,max_time)
print(prob_less_than_5)

# Calculate probability of waiting more than 5 mins
prob_greater_than_5 = 1 - uniform.cdf(5,min_time,max_time)
print(prob_greater_than_5)

# Calculate probability of waiting 10-20 mins
prob_between_10_and_20 = uniform.cdf(20,min_time,max_time) - uniform.cdf(10,min_time,max_time)
print(prob_between_10_and_20)