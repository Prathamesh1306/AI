from textblob import TextBlob

def spell_check(text):
    blob = TextBlob(text)
    corrected_text = blob.correct()
    print("Original text: ", text)
    print("Corrected text:", corrected_text)

if __name__ == "__main__":
    text = input("Enter a sentence with possible spelling mistakes: ")
    spell_check(text)


# input :- Ths is an exmple sentense with sme speling erors.