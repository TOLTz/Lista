from util import listaWords

print(listaWords)

onlyFive = list(filter(lambda x: len(x) >= 5, listaWords))

print(onlyFive)