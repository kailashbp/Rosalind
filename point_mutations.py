with open('point_mutations.txt') as fh:
    dna = []
    for line in fh:
        line = line.strip()
        dna.append(line)

    count = 0
    for i in range(len(dna[0])):
        if dna[0][i] != dna[1][i]:
            count+=1

    print(count)
