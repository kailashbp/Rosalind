with open("rosalind_subs.txt") as fh:
    l = ""
    s = []
    for line in fh:
        line = line.strip("\n")
        if line[0] == ">":
            s.append(l)
            l = ""
            continue
        else:
            l += line

s.append(l)
s = s[1:]

# Find LCS among the strings s

min_len = 10000000
for i in range(len(s)):
    val = len(s[i])
    index = 0
    if val < min_len:
        min_len = val
        index = i

min_str = s[index]

# Implementation of the LCS (Longest Common Subsequence) algorithm
# NOTE: The following implementation just finds the length of the LCS, it doesn't find the LCS
m, n = len(x), len(y)
def lcs(x,y,m,n):
    if m ==0 or n ==0:
        return 0
    elif x[m-1] == y[n-1]: # m-1, n-1 because we are first taking the last letter of the string
        # Having x[m], y[n] will return as index out of range.
        return 1+lcs(x,y,m-1,n-1)
    else:
        # Moving the string once at a time - to the left and to the right
        return max(lcs(x,y,m-1,n), lcs(x,y,m,n-1))

# Memoization can be used to store the values returned for various LCS so that memory complexity reduces
# Hence the overall time complexity of the algorithm reduces from 2^^n to m X n
# Note that this is a top-down approach, where we begin with the original complete strings

# Using Dynamic Programming a bottom up approach to LCS can be devised where the LCS can be identified,
# not just the length of the LCS

def lcs_dp(X,Y):
    matrix = [["" for i in range(len(y))] for j in range(len(x))]
    lcs = ""
#     X,Y = str(X), str(Y) # Forcing it to be string
    for i in range(len(X)):
        for j in range(len(Y)):
            if X[i] == Y[j]:
                if i==0 or j ==0:
                    matrix[i][j] =  X[i]
                else:
                    matrix[i][j] = matrix[i-1][j-1] + X[i]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], key = len)

    lcs = matrix[-1][-1]
    return lcs

fasta_lcs = []

for i in range(len(s)):
    for j in range(len(s)):
        if i < j:
            print(s[i],s[j])
            fasta_lcs.append(lcs_dp(s[i],s[j]))

print(min(fasta_lcs))
