'''
Problem: Write a recursive function to find the $n$-th number in the Fibonacci sequence (where the number is the sum of the two preceding ones: 0, 1, 1, 2, 3, 5, 8...).
'''
def fibonacci(n):
    # Base cases
    if n <= 0: return 0
    if n == 1: return 1
    # Recursive step
    return fibonacci(n - 1) + fibonacci(n - 2)

# Function Call
print(f"7th Fibonacci number: {fibonacci(7)}") 
# Output: 7th Fibonacci number: 13
