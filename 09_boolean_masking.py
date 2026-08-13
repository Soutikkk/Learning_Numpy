import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 60, 80],
    [100, 120, 150]
])

print("Data:")
print(data)

# Values greater than 50
print("Greater than 50:")
print(data > 50)

# Values between 50 and 100
result = (data > 50) & (data < 100)

print("Between 50 and 100:")
print(result)

# Get actual values
print("Selected values:")
print(data[result])

# Values NOT between 50 and 100
print("Not between 50 and 100:")
print(data[~result])