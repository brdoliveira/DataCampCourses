"""
# Array dimensionality
"""
import numpy as np

# 3D Arrays
array_1_2d = np.array([[1,2],[5,7]])
array_2_2d = np.array([[8,9],[5,7]])
array_3_2d = np.array([[1,2],[5,7]])
array_3d = np.array([array_1_2d,array_2_2d,array_3_2d])

# 4d Arrays
array_3d = np.array([array_3d,array_3d,array_3d,array_3d])

# Matrix and tensor arrays
# # A matrix has two dimensions
# # A tensor has three or mode dimensions

# Shapeshifting
# # Array attribute:
# # # .shape
# # Array methods:
# # # .flatten()
# # # .reshape()


# Finding an array's shape
array = np.zeros((3,5))
print(array)

array.shape # (3,5)

# Rows and columns
# # In 2d arrays ...
# # # Rows are the first dimension
# # # Columns are the second dimension

# Flattening an array
array = np.array([1, 2],[5, 7],[6, 6]) # 3 array to 1 array
array.flatten()

# Reshaping an array
array = np.array([1,2],[5,7],[6,6])
array.reshape((2,3))