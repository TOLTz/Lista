listTuple = [(2, 8), (4, 5, 6), (1, 2, 1, 2)]

def overall(listT):
    averageMap = map(lambda x: (x, sum(x) / len(x)), listT)
    averageFiltered = filter(lambda x: x[1] >= 5, averageMap)
    return [x[0] for x in averageFiltered]

'''
    Na variavel averageMap, mas especificamente na lambda, foi escrito (x, sum(x) / len(x)), pois o x sozinho esta salvando a tupla
    pra depois retornar (o uso fica explicito no x[0] que esta puxando o primeiro item de cada tupla que e maior que 5).
'''

print(overall(listTuple))

