# Boolean operators
# - and
# - or
# - not
import numpy as np

# AND
print(True and True) # True

print(False and True) # False

print(False and False) # False

x = 12
print(x > 5 and x < 15) # True

# OR
print(True or True) # True

print(False or True) # True

print(False or False) # False

y= 5
print(y < 7 or y > 13)

# NOT

print(not True) # False

print(not False) # True

# NUMPY
np_height = np.array([1.73,1.68,1.71,1.89,1.79])
np_weight = np.array([65.4,58.2,63.6,88.4,68.7])
bmi = np_weight / np_height ** 2

print(bmi > 21)

print(bmi < 21)

# print(bmi > 21 and bmi < 22) -> is ambiguous

# NUMPY
np.logical_and(bmi > 21, bmi < 22)
# array values boolean

np.logical_and[(bmi > 21, bmi < 22)]
# show the elements that are in the condition








