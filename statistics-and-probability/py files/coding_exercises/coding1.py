import numpy as np  # Import necessary package

# Create numpy arrays representing the vectors
v = np.array([1, 3, 5])
w = np.array([2, 4, 1])

# vector addition
print(v + w)

# vector multiplication by a scalar
print(2 * v)

# Dot product
print(np.dot(v, w))

# Alternative way to make the dot product
print(v @ w)
