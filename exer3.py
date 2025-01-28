from functools import reduce
from util import listNumbers

print(listNumbers)

added = reduce(lambda x, y: x+y, listNumbers)

print(added)