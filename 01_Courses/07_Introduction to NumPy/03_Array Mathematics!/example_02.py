"""
# Vectorized operations
"""
import numpy as np

np.arange(1000000).sum()

array = np.array([[1, 2, 3], [4, 5, 6]])
for row in range(array.shape[0]):
    for column in range(array.shape[1]):
        array[row][column] += 3

array = np.array([[1, 2, 3], [4, 5, 6]])
array + 3

# Multiplying by a scalar
array * 3

# Adding two arrays together
array_a = np.array([[1,2,3],[4,5,6]])
array_b = np.array([[0,1,0],[1,0,1]])
array_a + array_b

# Multiplying two arrays together
array_a * array_b

# Not just for math
array = np.array([[1, 2, 3], [4, 5, 6]])
array > 2

# Vectorize Python code!
array = np.array(["NumPy","is","awesome"])
len(array) > 2

vectorized_len = np.vectorize(len)
vectorized_len(array) > 2