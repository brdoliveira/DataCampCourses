# Loop in Data Structures (part 1)
import numpy as np

world = {"afghanistan":30.55,
         "albania":2.77,
         "algeria":39.21}

## error ! 
# for key, value in world:
#     print(key + " -- " + str(value)) 

for key, value in world.items():
    print(key + " -- " + str(value)) # there´s no order

np_height = np.array([1.73,1.68,1.71,1.89,1.79])
np_weight = np.array([65.4,58.2,63.6,88.4,68.7])
meas = np.array([np_height,np_weight])

for val in meas:
    print(val) 

for val in np.nditer(meas): # get all values
    print(val)

# Dict --> .items()
# Numpy Array --> np.nditer
# Dict require a method and numpy use a function