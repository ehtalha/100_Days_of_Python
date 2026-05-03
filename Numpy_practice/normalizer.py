'''
Problem: Create a 1D array of 10 random integers between 1 and 50. Then, 
normalize the data so that all values fall between 0 and 1 using the formula:
$$x_{norm} = \frac{x - x_{min}}{x_{max} - x_{min}}$$
'''
import numpy as np

# Generate random data
data = np.random.randint(1, 51, size=10)
print(f"Original Array: {data}")

# Calculate min and max
d_min = data.min()
d_max = data.max()

# Vectorized normalization
normalized = (data - d_min) / (d_max - d_min)

print(f"Normalized Array: \n{normalized}")
