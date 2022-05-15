    
def topSort(dictSet, initialize, newSet=[]):  #function
    q = [initialize]  #tthis is where q will be initialized
    while q: #while condition
        v = q.pop(-1)  #variable poping out last node
        if v not in newSet:  #if condition
            newSet = newSet + [v]  #creating a set of values
            q = dictSet[v] + q  #adding values to the set for dict
    return newSet  #return output
dictSet = {   #store values in our set of dictionary items
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['d'],
    'd': ['e'],
    'e': []
}
print("The sorted set is :")  #print statement
print(topSort(dictSet, 'a'))  #call function and print the dictionary set
