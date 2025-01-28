from functools import reduce
from util import lista

print(lista)

added = reduce(lambda x, y: x+y, lista)

print(added)