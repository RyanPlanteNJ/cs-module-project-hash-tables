import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

texts = words.split(' ')

word_dictionary = {}

for i in range(len(texts)-1):
    if texts[i] not in word_dictionary:
        word_dictionary[texts[i]] = [texts[i+1]]
    else:
        word_dictionary[texts[i]].append(texts[i-1])

start_words = []
stop_words = []

for word in word_dictionary:
    if word[0].isupper() or word[0] == '""':
        start_words.append(word)
    if word[-1] in '.?!':
        stop_words.append(word)
    if len(word)>2:
        if(word[-2] in '.?!') and word[-1] == '"':
            stop_words.append(word)


start = random.choice(list(word_dictionary))

for i in range(5):
    if start in stop_words:
        continue
    else:
        start = random.choice(word_dictionary[start])
        for value in word_dictionary[start]:
            print(value, end=' ')


# TODO: construct 5 random sentences
# Your code here

