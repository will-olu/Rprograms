f = open("C:/Users/willi/Downloads/rosalind_lcsm (4).txt", "r")

mat = []
str1 = f.read()
str1 = str1.replace("Rosalind_", "")
str1 = str1.replace("\n", "")
str1 = ''.join([i for i in str1 if not i.isdigit()])
mat = str1.split(">")
mat.remove("")

min = mat[0]
for i in mat:
    if len(i) < len(min):
        min = i

submat = []
for i in range (0, len(min)):
    for j in range (i, len(min)+1):
        submat.append(min[i:j])
submat.remove('')

works = []
for i in submat:
    sub = [x for x in mat if i in x]
    if (sub == mat):
        works.append(i)
print(works)

max = works[0]
for i in works:
    if len(i) >= len(max):
        max = i

print(max)
print(i)

f.close()
