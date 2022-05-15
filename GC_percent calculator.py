from Bio.Seq import Seq
from Bio import SeqIO

#I need a thing to read in the files
path = "C:\Users\willi\AppData\Local\Programs\Python\Python38-32"
handle = open( path + "rosalind_gc.txt", "r")


#I then need something to parse the function and return GC percentages
for record in SeqIO.parse(handle,"fasta"):
    print(record.id)
    print(record.seq)
    identity = record.id
    sequence = record.seq
    count = sequence.count.("G")+sequence.count("C")
    content = count/len(sequence)*100
    for largest in

print
    
def gc(sequence):
#function to calc GC content '''
    count = sequence.count("G")+sequence.count("C")
    content = count/len(sequence)*100
    return content
    print(gc(record.seq)

#I then need something that will look over the values that I got for the id and compare then until it prints out a max
handle.close()
