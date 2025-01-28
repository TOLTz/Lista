from util import listNumbers

print(listNumbers)

filtered = list(filter(lambda x: x%2 == 0, listNumbers))
print(filtered)