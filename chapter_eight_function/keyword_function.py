'''
Problem: Create a function build_profile that accepts a first name and last name, but also allows any number of other "key-value" details (like age, job, or city) to be stored in a dictionary.
'''
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# Function Call
user = build_profile("Alice", "Smith", location="Dhaka", job="Engineer")
print(user)
# Output: {'location': 'Dhaka', 'job': 'Engineer', 'first_name': 'Alice', 'last_name': 'Smith'}
