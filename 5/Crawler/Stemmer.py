from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("russian")

count = 102


index = 1
while index < count:

  with open(str(index) + '.txt') as f:
    lines = f.read()
    stemmed_words = [stemmer.stem(word) for word in lines.split()]
    file = open(str(index) + 'stemmer' + '.txt', 'w')
    file.write(str(stemmed_words))
    file.close()
    index += 1
