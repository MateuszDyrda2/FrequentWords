import sys
import re

inName = "Resources/AliceInWonderland.txt"
outName = "Resources/output.txt"

if len(sys.argv) == 2:
    inName = str(sys.argv[1])
    if len(sys.argv) > 2:
        outName = str(sys.argv[2])


f = open(inName, 'r', encoding="utf8")

words = dict()
for line in f:
    res = re.findall(r'[a-zA-Z]+', line)
    for word in res:
        word = word.lower()
        words[word] = words.get(word, 0) + 1
f.close()

fo = open(outName, 'w')
for word in sorted(words, key=words.get, reverse=True):
    fo.write(word + '\n')

fo.close()
