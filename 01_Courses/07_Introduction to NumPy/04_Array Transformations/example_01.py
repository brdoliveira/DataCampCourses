"""
# Saving and loading arrays
"""
import matplotlib.pyplot as plt
import numpy as np

# RGB arrays
rgb = np.array([
    [[255,0,0],[255,0,0],[255,0,0]],
    [[0,255,0],[0,255,0],[0,255,0]],
    [[0,0,255],[0,0,255],[0,0,255]],
])

plt.imshow(rgb)
plt.show()

"""
# Loading .npy files
"rb" -> read binary
"write binary" -> write binary
with open("logo.npy","rb") as f:
    logo_rgb_array = np.load(f)
plt.imshow(logo_rgb_array)
plt.show()
"""
help(np.unique)
help(np.ndarray.flatten)
