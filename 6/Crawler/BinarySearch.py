import json
import sys
from pymystem3 import Mystem

if __name__ == '__main__':

    with open('urls.json', 'r') as file_handle:
        links = json.load(file_handle)

    with open('inverted_index.json', 'r') as file_handle:
        inverted_index = json.load(file_handle)

    words_len = len(sys.argv) - 1

    if words_len == 0:
        print("No search")
        exit(-1)
    words = sys.argv[1:]
    indexes = [0 for item in links]

    m = Mystem()
    lemmas_to_search = [m.lemmatize(word.lower())[0] for word in words]
    print(lemmas_to_search)

    for word in lemmas_to_search:
        if word in inverted_index:
            for i, exists in enumerate(inverted_index[word]):
                indexes[i] += int(exists)
        else:
            print(word + " doesn't exist in dictionary")
            words_len -= 1

    print("Results:")
    for i, count_of_words_in_file in enumerate(indexes):
        if count_of_words_in_file == words_len:
            print(links[str(i + 1)])