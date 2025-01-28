from util import listNumbers

squared = list(map(lambda x: x**2, listNumbers))
ordered = sorted(squared)
print(ordered)