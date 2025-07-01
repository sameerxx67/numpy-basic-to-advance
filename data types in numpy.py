# Data Types in NumPy
# NumPy is a powerful library for numerical computing in Python, and it provides a variety of data types to work with arrays.
# Understanding data types is crucial for efficient memory usage and performance in numerical computations.
# NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

# Below is a list of all data types in NumPy and the characters used to represent them.

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

import numpy as np
arr_1 = np.array([1, 2, 3, 5])  
arr_2 = np.array([1, 2, 3, 56.9, "hello"])
arr_3 = np.array([1, 2, 3, 56.9])
print(arr_1.dtype)
print(arr_2.dtype)
print(arr_3.dtype) 

# prints the data type of the array

import numpy as np
arr = np.array([1,8, 8.9, 8.98])
int_arr = arr.astype(int)  # converting float to int
print(int_arr)
print(int_arr.dtype)  # prints the data type of the array after conversion