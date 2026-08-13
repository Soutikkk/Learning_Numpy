import numpy as np

a = np.array([1, 2, 3])

# Make a real copy
b = a.copy()

b[0] = 100

print("Original array:", a)
print("Copied array:", b)