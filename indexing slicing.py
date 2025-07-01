# array [index] #id array
# array [row, column] #2d array
import numpy as np
arr = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
print(arr[0])  # Accessing the first element of the array
print(arr[1])
print(arr[6])# Accessing the second element of the array  


import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(arr[1:5])  # Slicing the first five elements of the array
print(arr[:4])  # Slicing the second to eighth elements of the array
print(arr[::2])   # Slicing from the fourth element to the end of the
print(arr[::-1])