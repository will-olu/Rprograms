
from Bio import Entrez

#put in given from Rosalind
organism = 'Pagyris'
start = '2002/07/06'
end = '2011/05/15'

Entrez.email = 'aoluajeigbe@luc.edu'

#looks at the organism and goes through the publication start-end date
#PDAT is search tag for publication date

handle = Entrez.esearch(db = 'nucleotide', term = '"' + organism + '"[Organism] AND ("' + start + '"[PDAT] : "' + end + '"[PDAT])"')
record = Entrez.read(handle)

#print the number of records between start/end dates
print(record['Count'])

