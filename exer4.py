from util import listWords

print(listWords)

onlyFive = list(filter(lambda x: len(x) >= 5, listWords))

print(onlyFive)