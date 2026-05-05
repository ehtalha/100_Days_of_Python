'''
Problem: Create an array of 15 random numbers. 
Find the 3 largest values in the array and return them in descending order.
'''
import numpy as np

# Generate random data
data = np.random.randint(1, 100, 15)
print(f"Original Data: {data}")

# Sort the array in ascending order
sorted_data = np.sort(data)
print("Sorted data : ",sorted_data)

# Slice from the end to get the top 3 and reverse them [start:stop:step]
top_3 = sorted_data[-3:][::-1]

print(f"Top 3 Largest Values: {top_3}")

#output
'''
Original Data: [19 28 50 36 64 30 83 97 15 49 58 46 74 73 73]
Sorted data :  [ 2  7 12 16 23 24 42 44 49 76 78 81 84 96 99]
Top 3 Largest Values: [97 83 74]
'''
