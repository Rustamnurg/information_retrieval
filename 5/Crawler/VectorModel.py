import json
import numpy as np
import sys
from pymystem3 import Mystem


def calculate_tf(lemmas):
    tf = {}
    doc_count = len(lemmas)
    for token in lemmas:
        tf[token] = lemmas.count(token) / doc_count
    return tf


if __name__ == '__main__':

    with open('urls.json', 'r') as file_handle:
        links = json.load(file_handle)

    with open('TF-IDF.json', 'r') as file_handle:
        tf_idf = json.load(file_handle)

    with open('IDF.json', 'r') as file_handle:
        idf = json.load(file_handle)

    vectors = [[] for item in links]

    for lemma in tf_idf:
        for index, item in enumerate(tf_idf[lemma]):
            vectors[index].append(item)

    doc_vec_len = []
    for vector in vectors:
        doc_vec_len.append(np.linalg.norm(vector))

    words_len = len(sys.argv) - 1

    if words_len == 0:
        print("No words to search")
        exit(1)

    words = sys.argv[1:]

    zeros = np.zeros(len(tf_idf), dtype=float)

    m = Mystem()
    lemmas = [m.lemmatize(word.lower())[0] for word in words]
    tf = calculate_tf(lemmas)

    tokens_all = [token for token in idf]

    for token in tf.keys():
        if token in idf:
            zeros[tokens_all.index(token)] = tf[token] * idf[token]
        else:
            print(token + " -- doesn't exist in dictionary")

    search_vec_len = np.linalg.norm(zeros)

    scores = []
    for i, lemma in enumerate(vectors):
        print(i)
        print(lemma)
        print()
        scores.append((np.divide(np.matmul(vectors[i], zeros), (doc_vec_len[i] * search_vec_len)), links[str(i + 1)]))

    scores.sort(reverse=True)
    for i in range(10):
        print(scores[i][1])