import os
os.getcwd()
os.chdir("C:\Users\willi\Downloads")
os.getcwd()
mydir = "C:\Users\willi\Downloads\"

#implement a function to read in a FASTA file
def parse_fasta(main, noId = True):
mydir = "C:\Users\willi\Downloads\"

def parse_fasta(main, noId = True):

    #initialize ids and seqs
    ids, seqs = [], []

    #open data file and read in a fasta
    with open(main, 'r') as file:
        for line in file.readlines():
            if line.startswith('>'):
                ids.append(line[1:].strip())
                seqs.append('')
            else:
                seqs[-1] += line.strip()

    #return a dictionary of sequence with associated headers if noID is set to False
    #return a list of sequence only if that is not the previous case
    if noId == True:
        if len(seqs) > 1:
            return seqs
        else:
            return seqs[0]
    else:
        return dict(zip(ids, seqs))

#implement a function that takes two different protein strings
#to calculate the minimum number of edit operations needed to transform s into t
def editDistance(s, t):
    #the two different strings have possible lengths of x and y
    #to return the edit distance between both strings
    x, y = len(s), len(t)

    #initialize the distance matrix to build a matrix
    M = [[0 for j in range(y + 1)] for i in range(x + 1)]
    
