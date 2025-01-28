from util import listNumbersInt

def groupNumbers(listN):
    positive = list(filter(lambda x: x > 0, listN))
    negative = list(filter(lambda x: x < 0, listN))
    zero = list(filter(lambda x: x == 0, listN))
    return {'positvos': positive, 'negativos': negative, 'zeros': zero}
    
    
print(listNumbersInt)

print(groupNumbers(listNumbersInt))