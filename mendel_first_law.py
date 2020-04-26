# Mendel's law of segregation
# Mendel beleived that rather than looking at traits as continuous processes, they
# should be divided into discrete building blocks called factors

import numpy

def mendel_first_law(k,m,n):
    mat = numpy.zeros((3,3))
    ls = [k,m,n]

    for i in range(3):
        for j in range(3):
            mat[i][j] = ls[i]/t* 
    return(k/t*((k-1)/(t-1) + m/(t-1) + n/(t-1)) + m/t*(k/(t-1) + (m-1)/(t-1)) + n/t*(k/(t-1)))

print(mendel_first_law(2,2,2))
