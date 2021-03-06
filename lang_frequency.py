import re
import os
import sys
import string
from collections import Counter


def load_data(filepath):
    with open(filepath) as file:
        text_from_file = file.read()
    return text_from_file


def remove_punctuation(text):
    regex = re.compile('[{}]'.format(re.escape(string.punctuation)))
    clean_text = regex.sub('', text)
    return clean_text


def get_most_frequent_words(text):
    top_words = 10
    return Counter(text.lower().split()).most_common(top_words)


def print_results(results):
    for word in results:
        print(word[0],'=', word[1])


def main(filepath):
    text_from_file = load_data(filepath)
    clean_text = remove_punctuation(text_from_file)
    most_frequent_words = get_most_frequent_words(clean_text)
    print_results(most_frequent_words)


if __name__ == '__main__':

    if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
        filepath = sys.argv[1]
        main(filepath)        
    else:
        print("File not found.")
        print("Example launch: python lang_frequency.py <filename>")
