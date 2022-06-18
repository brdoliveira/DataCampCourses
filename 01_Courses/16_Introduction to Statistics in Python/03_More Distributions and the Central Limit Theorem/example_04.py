"""
# More probability distribuition

# Exponential distribuition
# # Probability of time between Poisson events
# # Examples
# # # Probability of > 1 day between adoptions
# # # Probability of < 10 minutes between restaurant arrivals
# # # Probability of 6 - 8 months between earthquakes
# # Also uses lambda (rate)
# # Continuous (time)

# (Students distribution) t-distribution
# # Similar shape as the normal distribution
# # Degress of freedom
# # # Has parameter degress of freedom (df) which affects the thiclness of the tails
# # # Lower df = thicker tails, higher standard deviation 
# # # Higher df =  closer to normal distribution 

# Log-normal distribution
# # Variable whose logarithm is normally 
# # Examples: 
# # # Length of chess games 
# # # Adult blood presure
# Number of hospitalizations in the 2003 SARS outbreak
"""
from scipy.stats import expon

# P(wait < 1 min)
expon.cdf(1,scale=0.5)

# P(wait > 1 min)
1 - expon.cdf(3,scale=0.3)

# P(1 min < wait < 3 min)
expon.cdf(3,scale=0.3) - expon.cdf(1, scale=0.5)