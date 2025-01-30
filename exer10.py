from functools import reduce

def weightedAverage(gradeStudents):
    grades = {}
    for students, gradesW in gradeStudents.items():
        grade = gradesW[:-1]
        weight = gradesW[-1]
        
        sumWeighted = reduce(lambda y, x: y + x[0] * x[1], zip(grade, weight), 0)
        
        totalWeight = sum(weight)
        
        gradeTotal = sumWeighted/totalWeight
        
        grades[students] = gradeTotal
        
    return grades

'''
    Primeiro recebe um argumento com um dicionario contendo os nomes (chaves), notas e pesos (valores)
    na segunda linha ja e criado um novo dicionario para salvar os "novos" dados
    em seguida e criado um laco for para separar os dados students (nomes) e gradesW (notas e pesos).
    logo apos eu criei uma variavel separando as notas (retirando o ultimo elemento no caso a lista com os pesos, [:-1]) e 
    os pesos (retirando os ultimos elementos, mas dessa vez salvando-os em outra variavel weight, [-1])
    apos foi criada a variavel sumWeighted, serve para somar as notas podenderadas (professor, eu nsabia como calculava, ent tive q
    pesquisar e perguntar ao gpt, mas de resto foi eu q fiz!), com a funcao lambda que salva um acumulador e faz a multiplicacao
    da nota com o peso. Apos isso eu utilizei o zip q serve para salvar os dados juntos e o 0 no final seria o valor inicial do 
    acumulador.
    ex: zip([10, 20 , 30], [2, 3, 1]) -> [(10,2), (20, 3), (30, 1)]
    a variavel totoalWeight serve para somar os pesos.
    gradeTotal serve para fazer as medias ponderadas.
    e por fim a ultima linha antes do retorno, serve para salvar os dados no dicionario criado anteriormente
    retornando por fim as notas.
'''




  
notas = {
    "João": [4, 8.5, 6, 8, [7, 3, 7, 3]],
}

print(weightedAverage(notas))
