'''
Problem: Write a recursive function factorial(n) to calculate the product of all integers from 1 to $n$.
'''
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n <= 1:
        return 1
    # Recursive step: n * (n-1)!
    return n * factorial(n - 1)

# Function Call
print(f"Factorial of 5: {factorial(5)}") 
# Output: Factorial of 5: 120
