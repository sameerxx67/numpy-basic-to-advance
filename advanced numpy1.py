import numpy as np
arr = np. array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr)
new_arr = np.insert(arr, 5, 100)  # Insert 100 at index 5
print(new_arr)
# insert in 2d

import numpy as np
arr_2d = np.array([[1, 2 ],[ 7, 9]])

print(arr_2d)
new_arr_2d = np.insert(arr_2d, 1, [10, 20], axis=None)  # Insert a new row at index 1
print(new_arr_2d)

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
new_arr = np.append(arr, 6)
print(new_arr)
# Append 6 to the end of

# concatenate
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 9 ])
concatenated_arr = np.concatenate((arr1, arr2))
print(concatenated_arr)

# DELETE FUNCTION
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
new_arr = np.delete(arr, 2)  # Delete the element at index 2        
print(new_arr)