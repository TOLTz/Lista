from random import randint, choice

listNumbers = [randint(0, 20) for _ in range(10)]
listNumbersInt = [randint(-20, 20) for _ in range(10)]

_listaPreDefinida = ["gato", "cachorro", "livro", "floresta", "computador", "lua", "música", "caneta", "jardim", "mar"]
listWords = [choice(_listaPreDefinida) for _ in range(5)]

