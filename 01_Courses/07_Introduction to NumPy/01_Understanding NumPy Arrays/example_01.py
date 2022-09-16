"""
# Introducing Arrays
"""
import numpy as np

python_list = [3,2,5,8,4,9,7,6,1]
array = np.array(python_list)

print(array)

# 2D
python_list_of_lists = [[3,2,5],
                        [9,7,1],
                        [4,3,6]]
np.array(python_list_of_lists)

# Python -> Can contain many different data types
python_list = ["beep",False,56,.945,[3,2,5]]

# Numpy -> Can contain only a single data types, use less memory
numpy_boolean_array = [[True,False], [True,True], [False,True]]
numpy_float_array = [1.9,5.4,8.8,3.6,3.2]

"""
np.zeros((5,3))
np.random.random((2,4))
np.arange(-3,4)
np.arange(4)
np.arange(-3,2,4)
"""