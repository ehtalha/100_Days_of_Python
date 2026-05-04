'''
Problem: Create a $2 \times 3$ matrix ($A$) and a $3 \times 2$ matrix ($B$). 
Perform a formal matrix multiplication. 
'''
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8], [9, 10], [11, 12]])

# for dotr @ operator or np.dot()
result = A @ B

print(f"Matrix A (2x3):\n{A}")
print(f"Matrix B (3x2):\n{B}")
print(f"Result (2x2):\n{result}")

#output
'''
Matrix A (2x3):
[[1 2 3]
 [4 5 6]]
Matrix B (3x2):
[[ 7  8]
 [ 9 10]
 [11 12]]
Result (2x2):
[[ 58  64]
 [139 154]]
 '''
