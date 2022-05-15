from  Bio import SeqIO

#create a directory
mydir = "/Users/willi/Downloads/"
myhandle = open(mydir + "rosalind_edta.txt")


def traceback(mat, s, t):
    #empty string for s
    S = ""
    #empty string for t
    T = ""
    #length of m
    n = len(s)
    #length of m is t
    m = len(t)
    #initialize the i as n
    i = n
    #initialize the j as m
    j = m
    #initialize inds as n - 1
    inds = n - 1
    #initialize indt as m - 1
    indt = m - 1
    #while the cell is not empty
    while(mat[i][j] != ""):

        if(mat[i][j] == 'd'):
            i = i-1
            j = j-1
            S = s[inds] + S
            T = t[indt] + T
            inds = inds - 1
            indt = indt - 1

        elif(mat[i][j] == "h"):
            j = j - 1    
            S = "-" + S
            T = t[indt] + T
            indt = indt - 1

        elif(mat[i][j] == "v"):
            i = i - 1
            T = "-" + T
            S = s[inds] + S
            inds = inds - 1
    return S + '\n' + \
           T

def align(handle):
    records = list(SeqIO.parse(handle, "fasta"))
    s = records[0].seq
    t = records[1].seq
    n = len(s)
    m = len(t)
    mat = [[0 for i in range(m + 1)] for j in range(n + 1)]
    back = [["" for i in range(m + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        mat[i][0] = i
    for j in range(1, m + 1):
        mat[0][j] = j

#initialize backtrack matrix top ro
    for i in range(1, n + 1):
        back[i][0] = "v"
    for j in range(1, m + 1):
        back[0][j] = "h"
#calculate the edit distnce and fill matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
#calculate match or mismatch,ms,  through comparison
            if s[i - 1] == t{j - 1]:
                ms = 0

            else:
                ms = 1

            p = 1
            #calculating diagonal
            diagonal = mat[i - 1][j - 1] + ms
            #calculating horizontal
            horizontal = mat[i][j - 1] + p
            #calculating vertical
            vertical = mat[i - 1][j] + p

#takes in the minimum value for each calculation  of the d, h, or v
            mat[i][j] = min(diagonal,
                            horizontal,
                            vertical)



            if(min(diagonal, horizontal, vertical) == diagonal):
                back[i][j] = "d"
            elif(min(diagonal, horizontal, vertical) == horizontal):
                back[i][j] = "h"
            elif(min(diagonal, horizontal, vertical) == vertical):
                back[i][j] = "v"
    distance = str(mat[n][m])
    alignment = traceback(back, s, t)

    return distance + '\n' + \
           alignment

print(align(myhandle))
