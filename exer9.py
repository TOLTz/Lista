listTuple = [(2, 8), (4, 5, 6), (1, 2, 1, 2)]

def overall(listT):
    
    average = list(filter(lambda x: x>=5, map(lambda x: sum(x)/2, listTuple)))
    return average
    
print(overall(listTuple))