'''
Problem: Write a function sum_all that can take any number of numerical arguments and return their total sum.
'''
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

# Function Call
result = sum_all(10, 20, 30, 40)
print(f"Sum: {result}") 
# Output: Sum: 100
