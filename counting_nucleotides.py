# READ Rosalind INTRODUCTION : A rapid introduction to Molecular Biology

# Solution 1

with open('counting_nucleotides.txt') as fh:
    dna = ''
    for line in fh:
        line = line.split()
        dna = dna + str(line)
    fh.close()

print(dna.count('A'),'',dna.count('C'),'',dna.count('G'),'',dna.count('T'))

# Solution 2

fh = open('counting_nucleotides.txt','r')
dna = str(fh.read()).replace('\n','')

count = { 'A': 0 , 'C': 0 , 'G': 0 , 'T': 0 }

for i in dna:
    count[i] = count[i] + 1

print(count)
