import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr)

print(arr[0])   # First element
print(arr[1])   # Second element

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))

print(arr.shape)

import numpy as np

# Zeros array
arr = np.zeros((3, 4))
print(arr)

# Ones array
arr = np.ones((2, 3))
print(arr)

# Array using arange
arr = np.arange(1, 11)
print(arr)

