import numpy as np

# Creating 1D array
a = np.array([1, 2, 3], dtype="int32")
print("Array:", a)

# Creating 2D array
b = np.array([
    [9.0, 8.0, 7.0],
    [6.0, 5.0, 4.0]
])
print("2D Array:")
print(b)

# Dimension
print("Dimension:", a.ndim)

# Shape
print("Shape:", b.shape)

# Data type
print("Data type:", a.dtype)

# Size of one element
print("Item size:", a.itemsize)

# Total memory used
print("Total bytes:", a.nbytes)

# Number of elements
print("Number of elements:", a.size)