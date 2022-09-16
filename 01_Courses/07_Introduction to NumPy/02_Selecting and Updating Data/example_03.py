"""
# Adding and removing data
"""
import numpy as np

# Concatenating rows
classroom_ids_and_sizes = np.array([[1, 22],[2, 21],[3, 27],[4,26]])
new_classroms = np.array([[5, 30],[5, 17]])
np.concatenate((classroom_ids_and_sizes, new_classroms))
# # np.concatenate() concatenates along the first axis by default

classroom_ids_and_sizes = np.array([[1, 22],[2, 21],[3, 27],[4,26]])
grade_levels_and_teachers = np.array([[1,"James"],[2,"George"],[3,"Amy"],[3,"Meehir"]])
np.concatenate((classroom_ids_and_sizes,grade_levels_and_teachers), axis=1)

# Creating compatibility
array_1d = np.array([1,2,3])
column_array_2d = array_1d.reshape((3,1))
print(column_array_2d)

row_array_2d = array_1d.reshape((1,3))
print(row_array_2d)

# Deleting with np.delete()
print(classroom_ids_and_sizes)
np.delete(classroom_ids_and_sizes, axis=0)

# Deleting columns
np.delete(classroom_ids_and_sizes,1, axis=1)

# Deleting without an axis
print(classroom_ids_and_sizes)
np.delete(classroom_ids_and_sizes,1)