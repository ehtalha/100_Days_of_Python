'''
Problem: Create a 1D array of 12 elements (0 to 11).
Reshape it into a $3 \times 4$ matrix, then transpose it so it becomes a $4 \times 3$ matrix.
'''
import numpy as np

# Create 1D array
arr = np.arange(12)

# Reshape to 3x4
matrix_3x4 = arr.reshape(3, 4)

# Transpose (flip axes)
matrix_4x3 = matrix_3x4.T

print(f"Original: {arr}")
print(f"Reshaped (3x4):\n{matrix_3x4}")
print(f"Transposed (4x3):\n{matrix_4x3}")

# output
'''
Original: [ 0  1  2  3  4  5  6  7  8  9 10 11]
Reshaped (3x4):
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
Transposed (4x3):
[[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]
'''
