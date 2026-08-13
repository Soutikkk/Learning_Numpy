import numpy as np

# All zeros
print(np.zeros((2, 3)))

# All ones
print(np.ones((4, 2, 2), dtype="int32"))

# Fill with a number
print(np.full((2, 2), 99))

# Same shape as another array
a = np.array([[1, 2], [3, 4]])
print(np.full_like(a, 4))

# Random decimal numbers
print(np.random.rand(4, 2))

# Random integers
print(np.random.randint(-4, 8, size=(3, 3)))

# Identity matrix
print(np.identity(5))

# Repeat an array
arr = np.array([[1, 2, 3]])
r1 = np.repeat(arr, 3, axis=0)

print(r1)