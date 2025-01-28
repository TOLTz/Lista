from util import lista

print(lista)

filtered = list(filter(lambda x: x%2 == 0, lista))
print(filtered)