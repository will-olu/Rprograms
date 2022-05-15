from Bio import SeqIO
from Bio.Seq import Seq

handle = "rosalind_splc.txt"

sequence = list(SeqIO.parse(handle,"fasta"))
seqlist = []
for record in sequence:
    x = record.seq
    seqlist.append((x))

#set of rna molecules
rna = seqlist[0]
#searches for all of the introns
introns = seqlist[1:]

#if intron is found replace with a non value
for i in introns:
    rna = str(rna).replace(str(i), "")

#conversion to RNA seq
rna = Seq(rna)

#translate the sequence
coding_dna = rna.translate()
print(coding_dna)
