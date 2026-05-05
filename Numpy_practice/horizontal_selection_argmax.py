'''
Problem: Create a $3 \times 4$ matrix. For each row, find the index of the maximum value.
This is a common task in classification tasks (finding the class with the highest probability).
'''
import numpy as np

# Creating a sample matrix
scores = np.array([
    [0.1, 0.8, 0.05, 0.05], # Max is at index 1
    [0.4, 0.1, 0.45, 0.05], # Max is at index 2
    [0.9, 0.0, 0.05, 0.05]  # Max is at index 0
])

# axis=1 looks across the columns for each row
predicted_classes = np.argmax(scores, axis=1)

print("Scores Matrix:\n", scores)
print("Index of max value per row:", predicted_classes)

#output
'''
Scores Matrix:
 [[0.1  0.8  0.05 0.05]
 [0.4  0.1  0.45 0.05]
 [0.9  0.   0.05 0.05]]
Index of max value per row: [1 2 0]
'''
