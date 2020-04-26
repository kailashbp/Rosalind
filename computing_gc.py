import numpy as np

with open('computing_gc.txt') as fh:
    id = []
    dna = []
    l = ''
    for line in fh:
        line = line.strip()
        if line.startswith('>'):
            if len(l) != 0:
                dna.append(l)
            l = ''
            id.append(line[1:])
        else:
            l = l + str(line)
    dna.append(l)
    gc = []
    # print(id,dna)
    for i in dna:
        gc.append(100*(i.count('G') + i.count('C'))/len(i))

    index_max = np.argmax(gc)

    print(id[index_max])
    print(max(gc))
    fh.close()
