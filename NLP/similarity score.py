import nltk
from nltk.corpus import wordnet

# Download required WordNet resources (only needed once)
nltk.download('wordnet')
nltk.download('omw-1.4')

def similarity_score(word1, word2):
    synsets1 = wordnet.synsets(word1)
    synsets2 = wordnet.synsets(word2)

    if not synsets1 or not synsets2:
        print("No synsets found for one or both words.")
        return 0

    # Use the first synset of each word (most common meaning)
    sim = synsets1[0].wup_similarity(synsets2[0])
    
    if sim is not None:
        print(f"Similarity between '{word1}' and '{word2}': {sim:.4f}")
        return sim
    else:
        print("No similarity could be computed.")
        return 0

# Example usage
w1 = input("Enter first word: ")
w2 = input("Enter second word: ")
similarity_score(w1, w2)
