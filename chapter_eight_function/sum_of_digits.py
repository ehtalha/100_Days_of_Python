'''
Problem: Write a recursive function that takes an integer and returns the sum of its digits (e.g., $123 \rightarrow 1+2+3 = 6$).
'''
def sum_of_digits(n):
    # Base case: if n is a single digit
    if n < 10:
        return n
    # Recursive step: last digit + sum of remaining digits
    return (n % 10) + sum_of_digits(n // 10)

# Function Call
print(f"Sum of digits of 1234: {sum_of_digits(1234)}") 
# Output: Sum of digits of 1234: 10
