infile = open('rosalind_set.txt', 'r')
outfile = open('OutputforProblem8.txt', 'w')

#reads input into list and splits at new line character
inputList = infile.read().split('\n')
#saves n as separate item
n = inputLIst[0]

#saves each item in first set as a list
Alist = inputList[1][1:-1].split(', ')
#saves each item in second set as a list
Blist = inputList[2][1:-1].split(', ')

#adds items from list A to set A as integers
for item in Alist:
    A.add(int(item))
    
#adds items from list B to set B as integers
for item in Blist:
    B.add(int(item))
    
#method that returns union of two sets
union = A.union(B)
#method that returns the set intersection of two sets
intersection = A.intersection(B)
#method that returns difference between two sets
setDifferenceA = A.difference(B)
setDifferenceB = B.difference(A)

#creates emptry set for full set
fullSet = set()
#adds integers to set from 1 to n
for i in range(1, int(n) +1):
    fullSet.add(i)

#method that returns complement of set from full set
complementA = fullSet.difference(A)
complementB = fullSet.difference(B)

outfile.write(str(union) + '\n' + str(intersection) + '\n' + str(complementA) + '\n' str(complementB))
outfile.close()
