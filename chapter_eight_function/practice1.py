'''
Problem: Create a function calculate_area that takes length and width as arguments and returns the area. If only one argument is provided, assume it is a square (where width = length).
'''
def calculate_area(length, width=None):
    # If width is None, the user only passed one argument
    if width is None:
        return length * length
    return length * width

# Function Calls
print(f"Rectangle Area: {calculate_area(5, 10)}") # Output: Rectangle Area: 50
print(f"Square Area: {calculate_area(7)}")       # Output: Square Area: 49
