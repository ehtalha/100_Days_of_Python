'''
Problem: Given a $5 \times 5$ matrix of random numbers, replace all values that are greater than 0.5 with the value 1, and all values less than or equal to 0.5 with 0.
'''
import numpy as np

# Create 5x5 matrix with values from a uniform distribution (0 to 1)
matrix = np.random.rand(5, 5)
print("Original Matrix:")
print(matrix)

# Use np.where(condition, value_if_true, value_if_false)
processed_matrix = np.where(matrix > 0.5, 1, 0)

print("\nBinarized Matrix (Threshold 0.5):")
print(processed_matrix)
# output
'''
[[1 0 1 1 0]
 [1 1 1 1 0]
 [0 0 1 1 1]
 [0 1 0 1 1]
 [0 0 0 0 0]]
 '''
