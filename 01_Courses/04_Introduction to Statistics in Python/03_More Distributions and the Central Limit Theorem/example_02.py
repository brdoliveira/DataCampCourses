"""
# The central limit theorem
# # The sampling distribuition of a statistics becomes closer to the normal distribuition as the number of trials increases.
# # Estimate characteristics of unknown undelying distribution
# # More easily estimate characteristics of large population
# # Sample should be random and independent

"""
from random import sample
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Rolling the dice 5 times
die = pd.Series([1,2,3,4,5,6])

"""
# Roll 5 times
samp_5 = die.sample(5,replace=True)
np.mean(samp_5)
print(samp_5)
"""

times = int(input("How many times rolling the dice: "))

# Rolling the dice 5 times 10 times
sample_means = []

for i in range(times):
    samp_5 = die.sample(5,replace=True)
    sample_means.append(np.mean(samp_5))

# print(sample_means)
plt.hist(sample_means)
plt.show()


"""
# Standard deviation and the CLT
sample_sds = []

for i in range(times):
    samp_5 = die.sample(5,replace=True)
    sample_sds.append(np.std(samp_5))

# print(sample_sds)
plt.hist(sample_sds)
plt.show()
"""

sales_teams = pd.Series(["Amir","Brian","Claire","Damian"])
print(sales_teams.sample(10,replace=True))

# Estimate expected value of die
np.mean(sample_means)

# Estimate proportion of "Claire´s"
np.mean(sales_teams)