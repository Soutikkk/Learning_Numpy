import numpy as np

a = np.ones((2, 3))
b = np.full((3, 2), 2)

print("Matrix A:")
print(a)

print("Matrix B:")
print(b)

# Matrix multiplication
result = np.matmul(a, b)

print("Matrix multiplication:")
print(result)

# Identity matrix
c = np.identity(3)

# Determinant
det = np.linalg.det(c)

print("Determinant:", det)