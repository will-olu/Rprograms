from Bio import Entrez
Entrez.email = "aoluajeigbe@luc.edu"

def parse_input(file):
    i = open(file, 'r')
    items = i.readlines()
    i.close()
    return items

def get_info(items):
    genus = items[0][:-1]
    mn = items[1][:-1]
    mx = items[2][:-1]

    handle = Entrez.esearch(db="nucleotide", term=genus + '[orgn]', datetype ='pdat', mindate=mn, maxdate=mx)
    record = Entrez.read(handle)
    entries = int(record["Count"])
    return entries

def output(out,num):
    o = open(out, 'w')
    o.write(str(num))
    o.close()





