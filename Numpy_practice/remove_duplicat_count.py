'''
Problem: You have a list of "category IDs" (integers) assigned to products. 
Identify all unique categories present in the dataset and count how many times each category appears.
'''
import numpy as np

# Array with repeated values
category_ids = np.array([1, 2, 2, 3, 1, 4, 2, 5, 3, 1, 1, 2])

# np.unique can return counts if requested
unique_cats, counts = np.unique(category_ids, return_counts=True)

print(f"Unique Categories: {unique_cats}")
print(f"Occurrences:       {counts}")
# Creating a quick dictionary-like view
print(f"Summary: {dict(zip(unique_cats, counts))}")



'''
Unique Categories: [1 2 3 4 5]
Occurrences:       [4 4 2 1 1]
Summary: {np.int64(1): np.int64(4), np.int64(2): np.int64(4), np.int64(3): np.int64(2), np.int64(4): np.int64(1), np.int64(5): np.int64(1)}
'''
