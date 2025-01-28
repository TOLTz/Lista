from util import listWords
from functools import reduce


def countedWords(listW):
    words = list(map(lambda x: len(x), listWords))
    counted = reduce(lambda x, y: x + y, words)
    return print(counted)

print(listWords)
countedWords(listWords)

