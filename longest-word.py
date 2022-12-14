import re

# Read the words.txt file - thanks to dwyl's english-words repository for this list
with open('words.txt', 'r') as file:
    words = file.readlines()

# Define a regular expression to exclude words with letters that cannot be displayed on a seven segment display
regex = re.compile(r'[gikmoqsvwxz]')

# Find the longest words in the words.txt file that can be displayed on a seven segment display
longest_words = []
longest_word_length = 0
for word in words:
    if len(word) > longest_word_length and not regex.search(word):
        longest_words = [word]
        longest_word_length = len(word)
    elif len(word) == longest_word_length and not regex.search(word):
        longest_words.append(word)

# Print the longest words
for word in longest_words:
    print(word)