import nltk

# Download required resources (only needed once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos_tagging(text):
    # Tokenize the sentence
    tokens = nltk.word_tokenize(text)
    # Apply POS tagging
    tagged = nltk.pos_tag(tokens)
    # Print the result
    for word, tag in tagged:
        print(f"{word} -> {tag}")

# Example usage
sentence = input("Enter a sentence for POS tagging: ")
pos_tagging(sentence)



# NN – Noun (e.g., "dog", "car")

# VB – Verb (base form)

# JJ – Adjective

# RB – Adverb

# DT – Determiner (e.g., "the", "a")

# IN – Preposition

# PRP – Pronoun