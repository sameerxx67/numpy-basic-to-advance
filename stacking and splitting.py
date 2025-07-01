# vertically
# horizantaly
# vstack row vise
# hstack column vise

import numpy as np
arr1 = ([1, 2, 3, 4, 5])
arrr2 = ([4, 5, 6, 7, 8])
print(np.vstack((arr1, arrr2)))  # Stack arrays vertically (row-wise)
print(np.hstack((arr1, arrr2)))  # Stack arrays horizontally (column-wise)


# STACKING AND SPLITTING
# Stacking arrays vertically and horizontally using vstack and hstack
# Splitting arrays into multiple sub-arrays using split
# Importing NumPy library
import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60])
print(np.split(arr, 3))  # Splitting the array into 3 sub-arrays
# Splitting the array into 3 sub-arrays
# Importing NumPy library

import numpy as np
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 10
result = array_2d + scalar
print(result)  # Adding a scalar to a 2D array

import numpy as np
arr = np.array([100, 200, 400,700,9000, 10000,30000,8000000,9000000,900000000,9000098])
print(np.array_split(arr, 3))  # Splitting the array into 3 sub-arrays
print(arr)
print(np.array_split(arr, 3, axis=0))  # Splitting the array into 3 sub-arrays along the first axis