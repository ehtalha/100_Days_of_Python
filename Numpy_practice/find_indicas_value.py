'''
Problem: In an array of 20 random integers (0-100), find the indices (positions) of all values that are greater than 75. 
Then, extract those specific values into a new array.
'''
import numpy as np

arr = np.random.randint(0, 101, 20)

# Find indices where condition is met
indices = np.where(arr > 75)

# Extract values using the indices
high_values = arr[indices]

print(f"Array: {arr}")
print(f"Indices of values > 75: {indices[0]}")
print(f"The values: {high_values}")

#output
'''
Array: [88 20  6 89  5 58 60  1 13 57 68 50 29 36 66 58  7 19 95 95]
Indices of values > 75: [ 0  3 18 19]
The values: [88 89 95 95]
'''
