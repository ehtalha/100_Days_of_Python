'''
Anagram Checker
Problem: Two strings are anagrams if they contain the same characters in a different order.
Write a script to check this
'''
str1 = "listen"
str2 = "silent"

# Logic: If sorted characters are equal, they are anagrams
is_anagram = sorted(str1.lower()) == sorted(str2.lower())

print(f"Are they anagrams? {is_anagram}")
# Output: Are they anagrams? True
