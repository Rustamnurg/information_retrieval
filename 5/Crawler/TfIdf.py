import json
import math

with open('urls.json', 'r') as file_handle:
    links = json.load(file_handle)

with open('inverted_index.json', 'r') as file_handle:
    inverted_index = json.load(file_handle)


def write_to_file_results(dictionary, title, format):
    with open(title + '.txt', "w") as f:
        f.write("Лемма" + " - " + title)
        f.write("\n")
        for lemma in dictionary.keys():
            f.write(str(lemma) + " - ")
            f.write(format.format(dictionary[lemma]))
            f.write("\n")
        f.close()

tokens_tf = {}
for index, filename in enumerate(links):
    index = +1
    f = open(str(index) + 'stemmer.txt', 'r')
    text = f.read()
    f.close()

    lemmas = text.split()

    for lemma in lemmas:
        if lemma not in tokens_tf:
            tokens_tf[lemma] = 0
        tokens_tf[lemma] += 1
write_to_file_results(tokens_tf, "TF", "{}")

tokens_df = {}
for lemma in inverted_index:
    if lemma not in tokens_df:
        tokens_df[lemma] = 0

    for index, value in enumerate(inverted_index[lemma]):
        tokens_df[lemma] += value
write_to_file_results(tokens_df, "DF", "{}")

tf_idf = {}
doc_count = len(links)
for lemma in inverted_index:
    tf_idf[lemma] = tokens_tf[lemma] * math.log(doc_count / tokens_df[lemma])
write_to_file_results(tf_idf, "TF-IDF", "{:.4f}")
