"""
# Broadcasting

# Compatibility rules
# # NumPy compares sets of array dimensions from right to left
# # Two dimensions are compatible when...
# # # One of them has  length of one or
# # # They are of equal lengths
# # All dimension sets must be compatible

# Broadcastable or not?
# # Broadcastable shapes:
# # # (10,5) and (10,1)
# # # (10,5) and (5,)
# # Shapes which are not broadcastable:
# # # (10, 5) and (5, 10)
# # # (10, 5) and (10,)
"""
from array import array
import numpy as np

array = np.arange(10).reshape((2,5))
array + np.array([0,1,2,3,4])

array = np.arange(10).reshape((2,5))
array + np.array([0,1]).reshape((2,1))
