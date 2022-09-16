"""
# NumPy data types
"""
import numpy as np

# Numpy vs. Python data types
# # Samples Python data types:
# # # int
# # # float
# # Samples Numpy data types:
# # # np.int64
# # # np.int32
# # # np.float64
# # # np.float32

# The .dtype attribute
np.array([1.32, 5.78, 175.55]).dtype

# Default data types
int_array = np.array([[1,2,3],[4,5,6]])
int_array.dtype # int64

# String data
np.array(["Introduction","to","NumPy"]).dtype # <U12

# Dtype as an argument
float32_array = np.array([1.32,5.78,175.55], dtype=np.float32)

# Type conversion
boolean_array = np.array([[True,False],[False,False]], dtype=np.bool_)
boolean_array.astype(np.int32)

# Type coercion
np.array([True,"Boop",42,42.45])

# Type coercion hierarchu
# # Adding a float to an array of integers will change all into floats:
np.array([0,42,42.42]).dtype
# # Adding a float to an array of boolean will change all into integers:
np.array([True,False,42]).dtype

