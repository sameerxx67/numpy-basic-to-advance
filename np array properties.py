# # SHAPE
# when working with multi dimesional data shape is helpful  for understanding how many rows and columns and return a integer
import numpy as np
arr_2d = np.array ([[1,3,3,90],
                    [4, 5, 8, 99],
                    [55,66,66,99]
                    ])
print(arr_2d.reshape(4,3))  # reshaping the array to 4 rows and 3 columns
print(arr_2d.shape)  # returns the shape of the array

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.size)
# returns the shape of the array, which 
import numpy as np
arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr_1d.ndim)  # returns the number of dimensions of the array
print(arr_2d.ndim)  # returns the number of dimensions of the array
print(arr_3d.ndim)  # returns the number of dimensions of the array