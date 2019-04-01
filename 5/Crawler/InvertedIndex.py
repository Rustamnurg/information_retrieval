import json


with open('urls.json', 'r') as file_handle:
    data = json.load(file_handle)

inverted_index = {}

for index, filename in enumerate(data):
    index += 1
    f = open(str(index) + "lemmatized.txt", 'r')
    text = f.read()
    f.close()

    lemmas = text.split()

    for lemma in lemmas:
        if lemma not in inverted_index:
            inverted_index[lemma] = [0 for f in data]

        inverted_index[lemma][index - 1] = 1

f = open('inverted_index.json', "w", encoding='utf-8')
json.dump(inverted_index, f)
f.close()

file = open('inverted_index.txt', 'w', encoding='utf-8')
y = 0
for lemma in inverted_index:
    file.write(str.rjust(lemma, 20) + '|')
    for x in range(len(inverted_index[lemma])):
        file.write(str.rjust(str(inverted_index[lemma][x]), 5) + '|')
    y += 1
    file.write('\n')
file.close()
