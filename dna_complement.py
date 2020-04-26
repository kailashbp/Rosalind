# READ Rosalind INTRODUCTION : The Secondary and Tertiary structures of DNA

with open('dna_complement.txt') as fh:
    dna = ''
    for line in fh:
        line = line.split()
        dna += str(line)

dna = dna[2:len(dna)-2]

c = {'A' : 'T', 'C' : 'G', 'G' : 'C' ,'T' : 'A'}

complement = []
for i in dna:
    complement.append(c[i])

print(''.join(reversed(complement)))
