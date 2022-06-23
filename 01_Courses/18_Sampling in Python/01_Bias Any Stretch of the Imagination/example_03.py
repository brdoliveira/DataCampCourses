"""
# How does Sue do sampling?

# What does random mean?
# # {adjective} made, done, happening, or chosen without method or conscious decision.

# True random numbers
# # Generated from physical processes, like flipping coins
# # Hotbits uses radioactive decay
# # RANDOM.ORG uses atmospheric noise
# # True randomness is expensive

# Pseudo-random number generation
# # Pseudo-random number generation is CHEAP and FAST
# # Next "random" number calculated from previous "random" number
# # The first "random" number calculated from a seed
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(20000229)

randoms = np.random.beta(a=2,b=2,size=5000)
print(randoms)

plt.hist(randoms, bins=np.arange(0,1,0.05))
plt.show()

np.random.normal(loc=2,scale=1.5,size=2)
np.random.normal(loc=2,scale=1.5,size=2)

# Generate random numbers from a Uniform(-3, 3)
uniforms = np.random.uniform(low=-3,high=3,size=5000)

# Print uniforms
print(uniforms)

# Plot a histogram of uniform values, binwidth 0.25
plt.hist(uniforms,bins=np.arange(-3,3.25,0.25))
plt.show()

normals = np.random.normal(loc=5,scale=2,size=5000)

# Print normals
print(normals)

# Plot a histogram of normal values, binwidth 0.5
plt.hist(normals,bins=np.arange(-2,13.5,0.5))
plt.show()