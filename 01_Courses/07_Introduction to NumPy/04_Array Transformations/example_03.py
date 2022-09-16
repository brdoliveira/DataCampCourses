"""
# Stacking and splitting
"""
import numpy as np

rgb = np.array([
    [[255,0,0],[255,255,0],[255,255,255]],
    [[255,0,255],[0,255,0],[0,255,255]],
    [[0,0,0],[0,255,255],[0,0,255]]
])

red_array = rgb[:,:,0]
green_array = rgb[:,:,1]
blue_array = rgb[:,:,2]
print(red_array)

# Splitting arrays
red_array, green_array, blue_array = np.split(rgb, 3, axis=2)
print(red_array)
red_array.shape

# Trainling dimension
red_array_2d = red_array.reshape((3,3))
print(red_array_2d)
red_array_2d.shape

# Array divisions rules
red_array, green_array, blue_array = np.split(rgb, 5, axis=2)