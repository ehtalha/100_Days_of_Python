'''
Problem: Create an array with some NaN (Not a Number) values.
Write a script that detects the NaN values and replaces them with the mean of the "clean" (non-NaN) data.
'''
import numpy as np

data = np.array([10.0, 20.0, np.nan, 40.0, 50.0, np.nan])

# Create a mask for NaN values
nan_mask = np.isnan(data)

# Calculate mean of non-NaN values
clean_mean = np.nanmean(data)

# Replace NaNs
data[nan_mask] = clean_mean

print(f"Mean used for filling: {clean_mean}")
print(f"Cleaned Array: {data}")

# output
'''
Mean used for filling: 30.0
Cleaned Array: [10. 20. 30. 40. 50. 30.]
'''
