from Bio.Seq import Seq
from Bio import SeqIO


handle = open(r"C:/Users/willi/Downloads/rosalind_dna (3).txt" , "r")

records = ((SeqIO.parse(handle, "fasta")))
sequence = handle.read()


adenosine = sequence.count('A')
tyrosine = sequence.count('T')
cytosine = sequence.count('C')
guanine = sequence.count('G')
    
   
    
           

print(adenosine, tyrosine, cytosine, guanine)

