# WORD frequency dictionary
text = "Python is fun. Python is fast, and Python is easy."
# Clean the string: remove punctuation and lowercase it
clean_text = text.replace(".", "").replace(",", "").lower()
words = clean_text.split()

freq_dict = {}
for word in words:
    freq_dict[word] = freq_dict.get(word, 0) + 1

print(freq_dict)
# Output: {'python': 3, 'is': 3, 'fun': 1, 'fast': 1, 'and': 1, 'easy': 1}
