# Matrix transposer
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# Using nested list comprehension
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

print(transpose)
# Output: [[1, 3, 5], [2, 4, 6]]
