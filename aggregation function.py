# function and what it does
# def aggregation_function(arr, func):
#     """
#     Applies a specified aggregation function to a NumPy array.

#     Parameters:
#     arr (np.ndarray): The input array.
#     func (str): The aggregation function to apply ('sum', 'mean', 'max', 'min').

#     Returns:
#     float: The result of the aggregation function.
#     """
#     import numpy as np

#     if func == 'sum':
#         return np.sum(arr)
#     elif func == 'mean':
#         return np.mean(arr)
#     elif func == 'max':
#         return np.max(arr)
#     elif func == 'min':
#         return np.min(arr)
#     else:
#         raise ValueError("Unsupported aggregation function. Use 'sum', 'mean', 'max', or 'min'.")
    
    
# print(aggregation_function(np.array([1, 2, 3, 4, 5]), 'sum'))   # Output: 15
# print(aggregation_function(np.array([1, 2, 3, 4, 5]), 'mean'))  # Output: 3.0
# print(aggregation_function(np.array([1, 2, 3, 4, 5]), 'max'))   # Output: 5
# print(aggregation_function(np.array([1, 2, 3, 4,    5]), 'min'))   # Output: 1

import numpy as np
arr = np.array([10, 20, 30, 40, 50])

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(np.std(arr))
print(np.var(arr))

# Output: 