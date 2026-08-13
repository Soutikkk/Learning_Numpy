import numpy as np

a = np.array([1, 2, 3, 4])

print("Original:", a)

print("Addition:", a + 2)
print("Subtraction:", a - 2)
print("Multiplication:", a * 2)
print("Division:", a / 2)

b = np.array([1, 0, 1, 0])

print("Array addition:", a + b)

print("Square:", a ** 2)

print("Cosine:", np.cos(a))
print("Sine:", np.sin(a))