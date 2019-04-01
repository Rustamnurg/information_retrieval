from pymystem3 import Mystem

count = 51

m = Mystem()

index = 1
while index < count:

  with open(str(index) + '.txt', 'r') as f:
    lines = f.read()
    lemmatized_words = [m.lemmatize(word.lower()) for word in lines.split()]
    file = open(str(index) + 'lemmatized' + '.txt', 'w+')
    for word in lemmatized_words:
      file.write(word[0] + ' ')
    file.close()
    index += 1
