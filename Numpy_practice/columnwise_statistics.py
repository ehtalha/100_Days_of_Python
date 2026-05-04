'''
Problem: Create a $4 \times 3$ matrix of random floats. 
Find the sum of each row, the average of each column, and the maximum value of the entire matrix.
'''
import numpy as np

matrix = np.random.rand(4, 3)

row_sums = matrix.sum(axis=1)    # axis=1 operates across columns (row-wise)
col_means = matrix.mean(axis=0)  # axis=0 operates across rows (column-wise)
grand_max = matrix.max()

print(f"Matrix:\n{matrix}")
print(f"Row Sums: {row_sums}")
print(f"Column Means: {col_means}")
print(f"Global Max: {grand_max}")

#output
'''
Matrix:
[[0.80991781 0.21112364 0.08711155]
 [0.37297552 0.67521146 0.26636915]
 [0.72125286 0.56040391 0.89456807]
 [0.44077341 0.39664361 0.05468922]]
Row Sums: [1.10815301 1.31455614 2.17622485 0.89210625]
Column Means: [0.5862299  0.46084566 0.3256845 ]
Global Max: 0.894568073662215
'''
