from Bio import Seq
from Bio import SeqIO

handle = (r'C:/Users/willi/Downloads/rosalind_gc.txt', 'r')
records = list (SeqIO.parse(handle, "fasta"))
def parse_fasta(handle):
    results = {}
    strings = records.strip().split('>')

    for records in strings:
        if len(records) == 0:
            continue

        parts = records.split()
        label = parts[0]
        bases = ''.join(parts[1:])

        results[label] = bases
        
    return results


def gc_content(records):
    n = len(records)
    m = 0

    for c in records:
        if c == 'G' or c == 'C':
            m += 1

    return 100 * (float(m) / n)


if __name__ == "__main__":


    large_dataset = open("C:/Users/willi/Downloads/rosalind_gc.txt", "r")
    results = parse_fasta(large_dataset)
    results = dict([(k, gc_content(v)) for k, v in results.iteritems()])

    highest_k = None
    highest_v = 0

    for k, v in results.iteritems():
        if v > highest_v:
            highest_k = k
            highest_v = v

    print (highest_k)
    print ('%f%%' % highest_v)
