'''
Operating System: Windows 11
Python Version: 3.10.9
Author: Salwa Shamma
ID: 4010405
Description: This code reads the content of a file, tokenizes it into words,
performs stemming on the words, counts the stemmed words, and saves the results
in a file. Stemming is a process of reducing words to their root or base form, 
which helps in normalizing the words and reducing them to a common representation.
'''
from nlp_utilities import read_file, tokenize_text, stem_and_count_words, save_results

# Define input file paths
input_file = "wiki_mountain_def.txt"

# Read the content of the file 📖
text = read_file(input_file)

# Tokenize the content into words using spaCy 📝
words = tokenize_text(text)

# Stem each word and count them ✂️
stemmed_words, original_words, word_count = stem_and_count_words(words)

# Print the number of stemmed words 🔢
print("Stemmed Word Count:", word_count)

# Save the result in a file 💾
save_results("stemmed_words.txt", original_words, stemmed_words)
