import numpy as np

a = np.array([
    [1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13, 14]
])

print(a)

# Specific element
print("Element:", a[1, 5])

# Specific row
print("First row:", a[0, :])

# Specific column
print("Third column:", a[:, 2])

# Slicing
print("Sliced:", a[0, 1:-1:2])

# Changing an element
a[1, 5] = 20

# Changing a column
a[:, 2] = [1, 2]

print("Modified array:")
print(a)