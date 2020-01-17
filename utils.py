from math import sqrt

def read_matrix(filename):
    # Get all the numbers in the file
    l = []
    with open(filename, 'r') as f:
        for line in f:
            l = l + [int(num) for num in line.split()] 
    n = int(sqrt(len(l)))

    # Construct a square matrix from this
    s = []
    ctr = 0
    while(ctr < len(l)):
        tmp = []
        for i in range(n):
            tmp.append(l[ctr])
            ctr+=1
        s.append(tmp)
    return s

# Convert a character to a number mod 26
def char2num(c):
    return ord(c.lower()) - ord('a')

# Convert a number mod 26 to a character 
def num2char(n):
    return chr(n + ord('a'))

def matrix_mult(mat, vec, m):
    n = len(mat)
    assert(len(vec) == n)
    # Create the result vector
    res = [0 for i in range(n)]
    for i in range(n):
        # Create a row sum variable
        row_sum = 0 
        for j in range(n):
            row_sum += mat[i][j] * vec[j]
            row_sum %= m
        res[i] = row_sum
    return res
