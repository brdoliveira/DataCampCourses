"""
# Filtering arrays
"""
import numpy as np

sudoku_game = np.load('./data/sudoku_game.npy')

# Two way to filter
# # 1. Masks and fancy indexing
# # 2. np.where()

# Boolean masks
one_to_five = np.arange(1,6)
print(one_to_five)

mask = one_to_five % 2 == 0
print(mask)

# Filtering with fancy indexing
one_to_five = np.arange(1,6)
mask = one_to_five % 2 == 0
one_to_five[mask]

# 2D fancy indexing
classroom_ids_and_sizes = np.array([[1, 22],[2, 21],[3, 27],[4, 26]])
print(classroom_ids_and_sizes)

classroom_ids_and_sizes[:, 1] % 2 == 0
classroom_ids_and_sizes[:, 0][classroom_ids_and_sizes[:, 1] % 2 == 0]

# Fancy indexing vs. np.where()
# # Fancy indexing
# # # Returns array of elements
# # np.where()
# # # Returns array of indices
# # # Can create an array base on whether elements do or don't meet condition

# Filtering with np.where()
print(classroom_ids_and_sizes)
np.where(classroom_ids_and_sizes[:,1] % 2 == 0)

# A tuples od indices
row_ind, column_ind = np.where(sudoku_game == 0)
print(row_ind)
print(column_ind)

# Find and replace
np.where(sudoku_game == 0, "", sudoku_game)