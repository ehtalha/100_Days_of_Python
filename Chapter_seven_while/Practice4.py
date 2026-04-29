# Reverse a Number
num = 12345
reversed_num = 0
while num > 0:
    remainder = num % 10
    reversed_num = (reversed_num * 10) + remainder
    num //= 10
print(f"Reversed number: {reversed_num}")

# Reversed number: 54321