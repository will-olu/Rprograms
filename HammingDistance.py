
records = open('C:/Users/willi/Downloads/rosalind_hamm (3).txt')

s = records.readlines(1)
s = str(s)

t = records.readlines(2)
t = str(t)

tet = len(t)
ses = len(s)
print("length of t " , tet)
print("length of s " , ses)


#print(s, " , " ,t)   

#s="GAGCCTACTAACGGGAT"
#t="CATCGTAATGACGGCCT"


def countPointMutations(s,t):
    count = 0
    counts = 0
    for i in range(0, len(s)):
        if(s[i] != t[i]):
           count+= 1
    print(count)

    for i in range(0, len(t)):
        if(s[i] != t[i]):
            counts+= 1
    print(counts)




    
print(countPointMutations(s,t))
