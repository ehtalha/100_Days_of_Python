'''
Problem: In a dataset of 10 values, ensure that no value is smaller than 20 and no value is larger than 80.
Any value outside this range should be "clipped" to the nearest boundary.
'''
import numpy as np

# Raw data with some "outliers"
raw_data = np.array([5, 25, 50, 75, 95, 12, 88, 40, 20, 80])

# np.clip(array, min_limit, max_limit)
cleaned_data = np.clip(raw_data, 20, 80)

print(f"Raw Data:     {raw_data}")
print(f"Clipped Data: {cleaned_data}")

# output
'''
Raw Data:     [ 5 25 50 75 95 12 88 40 20 80]
Clipped Data: [20 25 50 75 80 20 80 40 20 80]
'''
