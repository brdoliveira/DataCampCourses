"""
# Binomial distribution -> Probability distribution of the number of successes in a sequence of independent trials
# # The binomial distribution is a probability distribuition of the number of success in a sequence of independent trials
# Described by n and p
# n -> total number of trials
# p -> probability of success
# Expected value = n * p 

from scipy.stats import stats

# Coin Flip (binary outcome)
# binom.rvs(# of coins, probability of head/success,size=# of trials)
binom.rvs(1 , 0.5 , size=1)

# One flip many times
binom.rvs(1 , 0.5 , size=8)

# Many flips one time
binom.rvs(8 , 0.5 , size=1)

# Other probabilities
binom.rvs(8 , 0.25 , size=1)

# Whats probability of 7 heads?
# binom.pmf(num heads, num trials, prob of heads)
# P(heads = 7)
binom.pmf(7,10,0.5)

# P(heads <= 7)
binom.cdf(7,10,0.5)

# P(heads > 7)
1 - binom.cdf(7,10,0.5)
"""
import numpy as np

# Import binom from scipy.stats
from scipy.stats import binom

# Set random seed to 10
np.random.seed(10)

# Simulate a single deal
print(binom.rvs(1, 0.3, size=1))

# Simulate 1 week of 3 deals
print(print(binom.rvs(3, 0.3, size=1)))

# Simulate 52 weeks of 3 deals
deals = binom.rvs(3,0.3,size=52)

# Print mean deals won per week
print(np.mean(deals))