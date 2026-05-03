'''
The Problem: Create an $8 \times 8$ matrix filled with 0s and 1s in a checkerboard pattern.
This tests your understanding of slicing with steps.
'''
import numpy as np

# Initialize an 8x8 matrix of zeros
checkerboard = np.zeros((8, 8), dtype=int)

# Use slicing: [start:stop:step]
# Fill rows 1, 3, 5, 7 with 1s starting from column 0
checkerboard[1::2, ::2] = 1

# Fill rows 0, 2, 4, 6 with 1s starting from column 1
checkerboard[::2, 1::2] = 1

print("8x8 Checkerboard:")
print(checkerboard)

#Output
'''
[[0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]]
 '''
