'''
Remove Duplicates (Order Preserved)
Problem: Remove duplicates from a list without using set() (because sets don't maintain order)
'''

numbers = [1, 2, 2, 3, 4, 4, 5, 1]
unique_list = []

for n in numbers:
    if n not in unique_list:
        unique_list.append(n)

print(unique_list)
# Output: [1, 2, 3, 4, 5]
