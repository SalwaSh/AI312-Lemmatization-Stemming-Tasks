'''
Operating System: Windows 11
Python Version: 3.10.9
Author: Salwa Shamma
ID: 4010405
Description: This code reads the content of a file, tokenizes it into words, performs 
lemmatization on the words, counts the lemmatized words, and saves the results in a file.
Lemmatization is a linguistic process where words are reduced to their base or root form.
'''
from nlp_utilities import read_file, tokenize_text, lemmatize_and_count_words, save_results

# Define input file paths
input_file = "wiki_mountain_def.txt"

# Read the content of the file 📖
text = read_file(input_file)

# Tokenize the content into words using spaCy 📝
words = tokenize_text(text)

# Lemmatize each word and count them 🔎
lemmatized_words, original_words, word_count = lemmatize_and_count_words(words)

# Print the number of lemmatized words 🔢
print("Lemmatized Word Count:", word_count)

# Save the result in a file 💾
save_results("lemmatized_words.txt", original_words, lemmatized_words)
