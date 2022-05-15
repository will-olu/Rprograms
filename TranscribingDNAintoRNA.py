#from Bio import SeqIO
#from Bio.Seq import Seq

#easiest solution utilizing file function

seq = open(r'C:/Users/willi/Downloads/rosalind_rna.txt', 'r')
seq = seq.read()
#seq = 'GATGGAACTTGACTACGTAAATT'


for n in seq:
    if n == "T":
        seq = seq.replace("T", "U")

print(seq)


#perl allows  an individual
#second option linux command
#awk '{gsub(/T/,"U");print}' rosalind_rna.txt
#perl -pe 'y/T/U/' rosalind_rna.txt
#perl -p -e 's/T/U/g' rosalind_rna.txt

    
