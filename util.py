from random import randint, choice

lista = [randint(0, 20) for _ in range(10)]

_listaPreDefinida = ["gato", "cachorro", "livro", "floresta", "computador", "lua", "música", "caneta", "jardim", "mar"]
listaWords = [choice(_listaPreDefinida) for _ in range(5)]