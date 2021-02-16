import re
import matplotlib.pyplot as plt

file = open("robin.txt", "r+")
text = file.read()



text = text.lower()
words = re.split(r"[^\w']+",text)

print(f"Number of words in text file:  {len(words)}")

d = dict()

for word in words:
    if word in d:
        d[word] +=1
    else:
        d[word] = 1

print(d)

len(d.keys())

d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

plt.figure(figsize=(50,120))
plt.barh(list(d.keys()), d.values(), height=.5, color='g')
plt.ylim(-1, 411)
plt.show()