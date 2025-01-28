from util import listNumbers

def evenOrOdd(listNumber):
    pairCheck = list(filter(lambda x: x%2 == 0, listNumber))
    oddCheck = list(filter(lambda x: x%2 != 0, listNumber))
    return {'par': pairCheck, 'impar': oddCheck}

print(listNumbers)
    
print(evenOrOdd(listNumbers))