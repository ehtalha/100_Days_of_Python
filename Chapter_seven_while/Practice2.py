# Sum until Zero
total = 0
number = 1
while number != 0:
    number = int(input("Enter a number (0 to stop): "))
    total += number
print(f"Total sum: {total}")

'''
Enter a number (0 to stop): 2
Enter a number (0 to stop): 3
Enter a number (0 to stop): 4
Enter a number (0 to stop): 0
Total sum: 9
'''