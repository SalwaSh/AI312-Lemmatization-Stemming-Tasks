import spacy


def apply_stemming_rules(word, word_count):
    """
    Apply stemming rules to a word based on specific conditions.

    Args:
        word (str): The word to apply stemming rules to.
        word_count (int): The count of words that have been stemmed.

    Returns:
        tuple: A tuple containing the stemmed word and the updated word count.

    """
    # Stem a word based on specific conditions ✂️
    if word.endswith("sses"):  # If the word ends with "sses" 🪓
        word_count += 1
        # Remove "es" and replace with "ss" ✂️
        return word[:-4] + "ss", word_count
    elif word.endswith("ies"):  # If the word ends with "ies" 🪓
        word_count += 1
        # Remove "es" and replace with "i" ✂️
        return word[:-3] + "i", word_count
    elif word.endswith("ss"):  # If the word ends with "ss" 🪓
        word_count += 1
        return word, word_count  # Return the word as is ✅
    elif word.endswith("s"):  # If the word ends with "s" 🪓
        word_count += 1
        return word[:-1], word_count  # Remove the last character "s" ✂️
    else:
        return None, word_count


def read_file(filename):
    """
    Read the content of a file and return it as a string.

    Args:
        filename (str): The name of the file to read.

    Returns:
        str: The content of the file as a string.

    """
    # Read the content of a file and return it as a string 📖
    with open(filename, "r") as file:
        return file.read()


def tokenize_text(text):
    """
    Tokenize the text into words using spaCy.

    Args:
        text (str): The text to tokenize.

    Returns:
        list: A list of tokens (words) extracted from the text.

    """
    # Tokenize the text into words using spaCy 📝
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    return [token for token in doc]


def stem_and_count_words(words):
    """
    Stem each word in the given list based on the stemming rules defined in the function apply_stemming_rules
    and count the stemmed words.

    Args:
        words (list): A list of words to stem.

    Returns:
        tuple: A tuple containing the stemmed words, original words, and the count of stemmed words.

    """
    stemmed_words = []
    original_words = []
    word_count = 0

    for word in words:
        # Stem each word and count them ✂️
        stemmed_word, word_count = apply_stemming_rules(word.text, word_count)
        if stemmed_word is None:
            stemmed_words.append(word.text)
            original_words.append(word.text)
            continue
        stemmed_words.append(stemmed_word)
        original_words.append(word)
        print(f"{word} -> {stemmed_word}")

    return stemmed_words, original_words, word_count


def lemmatize_and_count_words(words):
    """
    Lemmatize each word in the given list and count the lemmatized words.

    Args:
        words (list): A list of words to lemmatize.

    Returns:
        tuple: A tuple containing the lemmatized words, original words, and the count of lemmatized words.

    """
    lemmatized_words = []
    original_words = []
    word_count = 0

    for word in words:
        # Check if the current token's text is different from its lemma (base form) 🔎
        if word.text != word.lemma_:
            # If so, increment the 'changed_words' counter
            word_count += 1
            print(f"{word.text} -> {word.lemma_}")

        lemmatized_words.append(word.lemma_)
        original_words.append(word.text)

    return lemmatized_words, original_words, word_count


def save_results(filename, original_words, modified_words):
    """
    Save the stemmed words and their original counterparts in a file.

    Args:
        filename (str): The name of the file to save the results.
        original_words (list): A list of original words.
        modified_words (list): A list of modified (stemmed or lemmatized) words.

    Returns:
        None

    """
    # Save the stemmed words and their original counterparts in a file 💾
    with open(filename, "w") as file:
        file.write(f"Number of modified words: {len(modified_words)}\n\n")
        for word, stemmed_word in zip(original_words, modified_words):
            file.write(f"{word} -> {stemmed_word}\n")

    print("Output saved to", filename, "file. ✨")
