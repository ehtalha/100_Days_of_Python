'''
Inventory Manager
Problem: You have a dictionary of stock and a list of items sold.
Update the stock and remove the item if it hits zero.
'''
stock = {"apple": 5, "banana": 2, "orange": 8}
sold = ["apple", "apple", "banana", "banana", "grape"]

for item in sold:
    if item in stock:
        stock[item] -= 1
        if stock[item] == 0:
            del stock[item]
    else:
        print(f"Warning: {item} not in stock!")

print(stock)
# Output: Warning: grape not in stock!
# Output: {'apple': 3, 'orange': 8}
