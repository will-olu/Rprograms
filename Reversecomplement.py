from Bio.Seq import Seq


seq = open('C:/Users/willi/Downloads/rosalind_revc (2).txt', 'r')
seq = seq.readlines()

#seq = Seq(seq)

#seq = 'GTCGGCCTGATCATATTGACTAGTGGAATACTAAACCGTACATCCCTTCCGTAGAGGGGCTGTGCAATGAATCGACAGACCTACTCCATGCGAGCGCCTTGGCGGCGTGTTATGCTTGCGTTAAGTCCGCTTTCGACAGACCAAAGCTTAGATAGGCTCATACGGTCGACTGCTCCCGGTGATGCATGCGGGTTTGGCTAAACCGATATTACAGGTGAACGGCACGAGCATAGATTAAACCCATCCAGAAATTGTTGCGGCCCTCATAAGTCTGGTGCGCGAGGCAGGCCCTGATCCCTATTGAAGGCCTACGCGGACGCTGGTCATCGATCTCGTCAGCCTACCGAGGCTGTATCATATGTCCCCTAATCACTGCCAGTTGAAAATGTACTAAGATATTACTTCCCGATCGGAAGATTTCTACCTATATTAGAGCTATTTCCTTATATCATGTACGATTTCGGTCGAGTCAAATTGTCTTTACCCCCCGCCGAATCGAAGTACGTGCAACCGTTGTTCGCTTAATTATTTTATACTCTGTTCACCCTTGAGCGCAGTGAACCAAAGTGACCATGGCAATCATATAGCGTGCCAAGTGTTTAAAGAGATGCGAGGCAGAGATGACGGTACGAAATGTTCACGGGTTCAGCTGTTGAACTATCAAAGCAAAACAACCAAACCGTTGTTATTGGCTAGACTGTTTATTATGTAACACGCGAAAGCTGACGGCACTTGGGGGATGTGTATTTTTAAGCGCGAAGTACGCTATCTGGCCTCATAATCCGAACTGGTGCCAGCCACTGACAGAGTCTCTACGAGACGACTGGTACACATTCGCGTCCTCCAATGTGAGTCTAACCTCGTCATAAAGGGTTTACCCCGGGTGTACTATGGCTACATTGGATCTGACTCGTCTTTCATAACCCGGCAATCAAGTACTATAGTTTATCGCAACGTGTGG'

#seq = Seq(seq)
#seq = seq.reverse_complement()
#seq = (str(seq))





#print(seq[::-1])
outfile = open("C:/Users/willi/Downloads/reversecomplementsssx.txt", 'w')
outfile.write(str(seq))
outfile.close()


input = "GTCA"
complement = { "A" : "T", "T" : "A", "C" : "G", "G" : "C"}
result = [] 
for i in reversed(input): 
    result.append(complement[i])
print (''.join(result))





string = "CACGTTACTTTA"
#print (string)
string = string[::-1] #reverse string
string = string.replace("A", "t")
string = string.replace("C", "g")
string = string.replace("T", "a")
string = string.replace("G", "c")
print (string.upper())







from sys import argv


response = ""
translate = {"A":"T","T":"A","G":"C","C":"G"}
for nuc in open(argv[1]).read():
    response = translate[nuc] + response
print (response)



nucleotides = file('C:/Users/willi/Downloads/rosalind_revc.txt').read() # read the nucleotides
D = {'A':'T' , 'C':'G', 'G':'C' , 'T':'A' } # this is a 'translation' dictionnary
solution = "".join([D.get(c,'') for c in nucleotides]) # translate the nucleotides
solution = solution[::-1] # Mirror, mirror on the wall...
open('rosalind_revc_sol.txt','w').write(solution) # write the solution


#fasta file bash line to take the reverse complement
#grep -v "^>" r.fasta | tr -d "\n"  | rev  | tr ATCG TAGC

