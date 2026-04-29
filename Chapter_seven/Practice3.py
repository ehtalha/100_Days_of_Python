# Count Vowels
text = "hello world"
vowels = "aeiou"
count = 0
for char in text.lower():
    if char in vowels:
        count += 1
print(f"Number of vowels: {count}")
# Number of vowels: 3