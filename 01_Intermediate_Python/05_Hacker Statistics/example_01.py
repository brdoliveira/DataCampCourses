import numpy as np 

np.random.seed(123) # Starting from a seed
# np.random.rand() # Pseudo-random numbers
coin = np.random.randint(0,2) # Randomly generate 0 or 1
if coin == 0:
    print("heads")
else:
    print("tails")