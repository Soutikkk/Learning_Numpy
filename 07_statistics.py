import numpy as np

stats = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Array:")
print(stats)

print("Minimum:", np.min(stats))

print("Maximum:", np.max(stats))

print("Maximum of each row:", np.max(stats, axis=1))

print("Sum of each column:", np.sum(stats, axis=0))