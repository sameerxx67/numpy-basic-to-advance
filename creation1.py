# creating array from python list
# np.array = [elo1, elo2, elo3]
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)


# creation2
# with default values
# np.array = [elo1, elo2, elo3]
# arr2 = np.array([1, 2, 3, 4, 5], dtype=float)
# print(arr2)
import numpy as np
zeros_array = np.zeros(889)
print(zeros_array)

# CREATION3
import numpy as np
ones_array = np.ones((5,8))
print(ones_array)
# CREATION4
import numpy as np
filled_array = np.full((4,7),99)
print(filled_array)

# CREATING SEQ OF NUMBER IN NUMPY
import numpy as np
arr= np.arange(1,100,10)
print(arr)
# CREATING IDENTITY MARTICES
import numpy as np
identity_matrix = np.eye(4)
print(identity_matrix)