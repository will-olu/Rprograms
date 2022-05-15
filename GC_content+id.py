import operator
#from Bio.Seq import Seq
#from Bio import SeqIO


#GC content Counter

#handle = open(r'C:/Users/willi/Downloads/rosalind_gc (4).txt', "r")
#records = ((SeqIO.parse(handle, "fasta")))
#fp = handle.read()


def returnHighGC(fastaName):
    
    def read_fasta(fp):
        name = None
        seq = []
        for line in fp:
            line = line.rstrip()
            if line.startswith(">"):
                if name: yield (name, ''.join(seq)) #interim genes
                name = line #first name
                seq = [] #first seq
            else:
                seq.append(line)
        if name: yield (name, ''.join(seq)) #yields last gene
    
    genes = {}
    with open(fastaName) as fp:
        for name, seq in read_fasta(fp):
            genes[name] = seq
    gene_gcs = {}
    for gene in genes:
        geneLength = len(genes[gene])
        gORc = genes[gene].count('G') + genes[gene].count('C')
        percentage = (gORc / geneLength) * 100
        gene_gcs[gene] = percentage
    
    sortedByGC = sorted(gene_gcs.items(), key=operator.itemgetter(1), reverse=True)
    return(sortedByGC[0])


print(returnHighGC('C:/Users/willi/Downloads/rosalind_gc (4).txt'))
