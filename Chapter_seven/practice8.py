# Pyramid Pattern
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    # Print spaces
    print(" " * (n - i), end="")
    # Print stars
    print("*" * (2 * i - 1))
'''
Enter a number: 4
   *
  ***
 *****
*******
'''
