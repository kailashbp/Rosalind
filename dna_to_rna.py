# READ Rosalind INTRODUCTION : The Second Nucleic acid

with open('dna_to_rna.txt') as fh:
    dna = ''
    for line in fh:
        line = line.split()
        dna = dna + str(line)

    # Solution 2
    # print('U'.join(fh.read().split('T')))
    fh.close()
print(str(dna[2:len(dna)-2].replace('T','U')))
