
# Text Analyzer
# Get user input
text = input("Enter a text to analyze: ")

print("\n--- Original Text ---")
print(text)

# Basic transformations
print("\n--- Transformations ---")
print("Capitalized:", text.capitalize())
print("Lowercase:", text.lower())
print("Uppercase:", text.upper())
print("Stripped (remove spaces at ends):", text.strip())

# Replace and count
old_word = input("\nEnter a word to replace: ")
new_word = input("Enter the new word: ")
replaced_text = text.replace(old_word, new_word)
print("After replacement:", replaced_text)

word_to_count = input("\nEnter a word to count occurrences: ")
print(f"'{word_to_count}' occurs {text.count(word_to_count)} times")

# Find and index
word_to_find = input("\nEnter a word to find: ")
position = text.find(word_to_find)
if position != -1:
    print(f"First occurrence of '{word_to_find}' is at index {position}")
else:
    print(f"'{word_to_find}' not found")

# Index raises an error if not found
try:
    idx = text.index(word_to_find)
    print(f"(Using index) '{word_to_find}' found at {idx}")
except ValueError: 
    print(f"(Using index) '{word_to_find}' not found")

# Check start/end
print("\n--- Starts/Ends With ---")
print("Starts with 'Hello'? ->", text.startswith("Hello"))
print("Ends with '.'? ->", text.endswith("."))

# Split and analyze words
words = text.split()
print("\n--- Words in the text ---")
print(words)
print("Number of words:", len(words))

# Analyze each word
print("\n--- Word-wise analysis ---")
for w in words:
    print(f"'{w}': uppercase={w.upper()}, lowercase={w.lower()}, length={len(w)}")
