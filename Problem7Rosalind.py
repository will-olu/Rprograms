import re
from Bio import SeqIO
import itertools

filename = "C:\\path to file"

file = SeqIO.read(filename, 'fasta')
seq = str(file.seq)

#seq = ""

#using itertools to find possible k-mers
#first kmer in list in alphabetical order
start = "ACGT"
#the itertools go through the permutations and then find the repeats
#and kmers have to be 4 values
permutations = itertools.product(start, repeat =4)

kmers = []
for temp, temp2 in enumerate(list(list(permutations))):
    kmer = ""
    for i in temp2:
        kmer += str(i)
    kmers.append(kmer)
                            

val = []
#for loop for each value in the kmer list
for kmer in kmers:
    #this gives us an initial value for the counter
    count = 0
    #regex is an expression to find the kmer
    for i in re.findall(regex, seq):
        count += 1
    val.append(count)

#added space seperation to format
print(*val, sep = ' ')

                             
