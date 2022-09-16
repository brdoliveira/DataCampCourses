"""
# Summarizing data

# Aggregating methods
# # .sum()
# # .min()
# # .max()
# # .mean()
# # .cumsum()

"""
import matplotlib.pyplot as plt
import numpy as np

security_breaches = np.array([
                            [0,5,1],
                            [0,2,0],
                            [1,1,2],
                            [2,2,1],
                            [0,0,0]
                            ])

# Sum
print(security_breaches.sum())
print(security_breaches.sum(axis=0))
print(security_breaches.sum(axis=1))

# Min and max values
print(security_breaches.min())
print(security_breaches.max())
print(security_breaches.min(axis=1))

# Finding the mean
print(security_breaches.min())
print(security_breaches.mean(axis=1))

# The keepdims argument
print(security_breaches.sum(axis=1))
print(security_breaches.sum(axis=1, keepdims= True))

# Cumulative sums
print(security_breaches.cumsum(axis=0))

# Graphing summary values
cum_sums_by_client = security_breaches.cumsum(axis=0)
plt.plot(np.arange(1,6), cum_sums_by_client[:,0], label="Client 1")
plt.plot(np.arange(1,6), cum_sums_by_client.mean(axis=1), label="Average")
plt.legend()
plt.show()