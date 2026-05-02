'''
Character Mapping (Cipher)
Problem: Create a simple Caesar Cipher. Shift every letter in a string by a fixed number (e.g., 1).
For simplicity, we’ll assume lowercase and no wrapping around 'z'.
'''
text = "hello"
shift = 1
encrypted = ""

for char in text:
    # ord() gets ASCII, chr() converts ASCII back to char
    new_char = chr(ord(char) + shift)
    encrypted += new_char

print(encrypted)
# Output: 'ifmmp'
