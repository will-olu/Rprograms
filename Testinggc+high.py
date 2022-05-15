import operator
from Bio.Seq import Seq
from Bio import SeqIO

handle = open(r'C:/Users/willi/Downloads/rosalind_gc (4).txt')
records = ((SeqIO.parse(handle, "fasta")))
setsoffastas = handle.read()

setsoffastas = list(setsoffastas)

newlistsofnames = []
def getlistofnames(setsoffastas):
    for line in setsoffastas:
        if line.startswith(">"):
            newlistofnames.append(line)
            print(newlistofnames)
        else:
            print("gc_content")

    return("sigh")



            
getlistofnames(setsoffastas)
