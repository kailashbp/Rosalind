with open('point_mutations.txt') as fh:
    dna = []
    for line in fh:
        line = line.strip()
        dna.append(line)

def find_hamming_distance(seq1, seq2):
    count = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            count+=1
    return(count)


dna = ["ATCGTGGTACTG", "CCGGAGAACTAG", "AACGTACTACTG", "ATGGTGAAAGTG",  "CCGGAAGACTTG",  "TGGCCCTGTATC"]

for i in dna:
    for j in dna:
        print(find_hamming_distance(i,j))
