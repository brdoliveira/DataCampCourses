"""
# Indexing and slicing arrays
"""
import numpy as np

# Indexing 1D arrays
array = np.array([2, 4, 6, 8, 10])
array[3]

sudoku_game = np.load('./data/sudoku_game.npy')
sudoku_game[2,4]
sudoku_game[0]
sudoku_game[:,3]

# Slicing 1D arrays
array = np.array([2, 4, 6, 8, 10])
array[2:4]

# Slicing 2D arrays
sudoku_game[3:6, 3:6]

# Slicing with steps
sudoku_game[3:6:2, 3:6:2]

# Sorting arrays
np.sort(sudoku_game)

# Sorting by axis
np.sort(sudoku_game)
np.sort(sudoku_game, axis=0)