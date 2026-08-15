import numpy as np

b = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("3D Array:")
print(b)

# Access specific element
print("Specific element:", b[0, 1, 1])

# Change values
b[0, 1, :] = [9, 9]

print("Modified array:")
print(b)