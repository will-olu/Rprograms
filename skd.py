import os
from Bio import SeqIO
from Bio import Entrez

Entrez.email = "aoluajeigbe@luc.edu"

filename = "MouseReference"

if not os.path.isfile(filename):
    net_handle = Entrez.efetch(db = "nucleotide", id = " AL732615.15", rettype = "gb", retmode = "text")
    out_handle = open(filename,'w')
    out_handle.write(net_handle.read())
    out_handle.close()
    net_handle.close()


record
