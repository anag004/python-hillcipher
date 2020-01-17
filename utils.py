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
