from Bio.Seq import Seq  #helps find the revers complement

file = open('rosalind_dbru.txt')

DNA_strings = file.read().strip().split('\n')

reverse_complements = []

for DNA_string in DNA_strings:
    mySeq = Seq(DNA_string) #looks at the reverse complement of a Seq object
    reverse_complement = str(mySeq.reverse_complement()) #find revese complement
    reverse_complements.append(reverse_complement) #add reverse complement to list of reverse complements



S_U_Src = set() #this is the union of the DNA string and the their reverses

#add DNA to set

for DNA_string in DNA_strings:
    S_U_Src.add(DNA_string)


#add reverse complements to set
for reverse_complement in reverse_complements:
    S_U_Src.add(reverse_complement)
    #print(reverse_complement)

outfile = open('output.txt' ,'w')

for r in S_U_Src:
    outfile.write('(' +r[:-1] + ',' + r[1:] + ')' + '\n') #creates an edge for each kmer from the SuSrc set
    #print('(' + r[:-1] + ',' + r[1:] + ')')

outfile.close()





    
