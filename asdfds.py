metacentric = ['chr1','chr16','chr19','chr20','chr3']
for c in range(1,23):
    chrom = "chr" + str(c)
    if chrom in metacentric:
        print(chrom)
