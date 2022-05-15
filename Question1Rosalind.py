from Bio.Seq import Seq
from Bio import SeqIO


#GC content Counter

handle = open(r'C:/Users/willi/Downloads/rosalind_gc (4).txt', "r")

records = ((SeqIO.parse(handle, "fasta")))
sequence = handle.read()

handle.close()

#name = records[0].id

sequence = list(sequence)

#initialize length value at 0
length = 0

#create
for seq in sequence:

    if sequence[length] == '>':

        #del sequence[length:length + 14] #this is another way of slicing off the FASTA header sequence.

        length = length + 1
    
        sequence = ''.join(sequence)


total_bp = sequence.count('A') + sequence.count('T') + sequence.count('G') + sequence.count('C')

total_GC = sequence.count('G') + sequence.count('C')

GC_content = (float(total_GC) / float(total_bp)) * 100


print(GC_content)



from utils import read_fasta, gc_content


if __name__ == '__main__':
    sequences = read_fasta('C:/Users/willi/Downloads/rosalind_gc (4).txt')

    max_gc = 0
    max_id = None

    for id, s in sequences.items():
        gc = gc_content(s)

        if gc > max_gc:
            max_gc = gc
            max_id = id

    print (max_id)
    print (max_gc * 100)


