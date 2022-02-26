import numpy as np
# Basic comparisons

print(2<3)

print(2==3)

print(2<=3)

print(3<=3)

print("carl" < "chris")

# print(3 < "chris") --> error the 1° variable is int 
# and 2° variable is string 

# Other comparions
np_height = np.array([1.73,1.68,1.71,1.89,1.79])
np_weight = np.array([65.4,58.2,63.6,88.4,68.7])
bmi = np_weight / np_height ** 2

print(bmi > 23) # we can compare list