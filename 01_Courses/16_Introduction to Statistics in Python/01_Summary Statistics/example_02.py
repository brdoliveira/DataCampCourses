import numpy as np

"""
### ! SPREAD ! ###

# Calculating Variance

# # 1 - Subtract mean from each data point
dists = msleep['sleep_total'] - np.mean(msleep['sleep_total']) 
print(dists)

# # 2 - Square each distance
sq_dists = dists ** 2
print(sq_dists)

# # 3 - Sum squared distances
sum_sq_dists = np.sum(sq_dists)
print(sum_sq_dists) 

# # 4 - Divide by number of data points - 1
variance = sum_sq_dists / (83 - 1)
print(variance) # the greater the variance, the more dispersed

variance = np.var(msleep['sleep_total'],doff=1) # without ddof = 1, population variance is calculated instead of sample variance

# Standard deviation
np.sqrt(np.var(msleep['sleep_total'], ddof=1))
##
np.std(msleep['sleep_total'], doff=1)

# Mean absolute deviation
dists = msleep['sleep_total'] - mean(msleep$sleep_total)
np.mean(np.abs(dists))

# Quantiles
np.quantile(msleep['sleep_total'],0.5) # 50 % = median
# # Quartiles
np.quantile(msleep['sleep_total'],[0 , 0.25 , 0.5 , 0.75 , 1])
np.quantile(msleep['sleep_total'],np.linspace(0,1,5))


# IQR (Interquartile Range)
# # Height of the box in a boxplot

np.quantile(msleep['sleep_total'],0.75) - np.quantile(msleep['sleep_total'],0.25)

from scipy.stats import iqr
iqr(msleep['sleep_total'])

# All in one go 
msleep['bodywt].describe()
"""