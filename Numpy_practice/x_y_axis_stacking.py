'''
Problem: Create two different $2 \times 3$ arrays. 
Combine them first vertically (one on top of the other) and then horizontally (side-by-side). 
'''
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [10, 11, 12]])

# Vertical stack (Resulting shape: 4, 3)
v_stack = np.vstack((A, B))

# Horizontal stack (Resulting shape: 2, 6)
h_stack = np.hstack((A, B))

print("Vertical Stack:")
print(v_stack)
print("\nHorizontal Stack:")
print(h_stack)

# Output
'''
Vertical Stack:
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]

Horizontal Stack:
[[ 1  2  3  7  8  9]
 [ 4  5  6 10 11 12]]
 '''
