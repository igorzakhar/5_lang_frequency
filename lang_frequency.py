import os
import sys
import string
from collections import Counter


def load_data(filepath):
    with open(filepath) as file:
        text_from_file = file.read()
    return text_from_file

def remove_punctuation(text):
    """ This code remove punctuation mark from text"""
    punct = set(string.punctuation)
    sans_punct = ''.join(symbl for symbl in text if symbl not in punct)
    return sans_punct # return list all words from text

def get_most_frequent_words(text):
    return Counter(text.lower().split()).most_common(10)


if __name__ == '__main__':

    if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
        filepath = sys.argv[1]
        text_from_file = load_data(filepath)
        clean_text = remove_punctuation(text_from_file)
        most_frequent_words = get_most_frequent_words(clean_text)
        
        for word in most_frequent_words:
            print(word[0],'=', word[1])
    else:
        print("File not found.")
        print("Example launch: python lang_frequency.py <filename>")

