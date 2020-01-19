from math import sqrt

class InverseError(Exception):
    pass

class IncorrectLength(Exception):
    pass

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

def gcd(a, b):
    if (a == 0 and b == 0):
        raise Exception("Cannot find gcd of zero and zero")
    if (b == 0):
        return [a, 1, 0]
    else:
        arr = gcd(b, a % b)
        q = int(a / b)
        return [arr[0], arr[2], arr[1] - q * arr[2]]

def get_mod(a, m):
    if (a >= 0):
        return a % m
    else:
        return m - ((-a) % m)

def mod_inverse(a, m):
    arr = gcd(a, m)
    if (arr[0]) != 1:
        raise InverseError
    else:
        return get_mod(arr[1], m)

# Swap two rows of a matrix
def swap_row(mat, i, j):
    for k in range(len(mat[i])):
        tmp = mat[i][k]
        mat[i][k] = mat[j][k]
        mat[j][k] = tmp

# Multiply rows of a matrix by some factor
def mult_row(mat, row_idx, mult_factor, m):
    for i in range(len(mat)):
        mat[row_idx][i] *= mult_factor
        mat[row_idx][i] = get_mod(mat[row_idx][i], m)
    
# Add factor * (row j) of the matrix to row i
def add_row(mat, i, j, factor, m):
    for k in range(len(mat)):
        mat[i][k] += (factor * mat[j][k])
        mat[i][k] = get_mod(mat[i][k], m)


def matrix_inverse(mat, m):
    n = len(mat)
    
    # Create a n x n identity matrix
    res = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        res[i][i] = 1

    # Iterate over the rows to find nz_idx
    for row_idx in range(n):
        # Find a non-zero row
        nz_idx = -1
        for i in range(row_idx, n):
            if (gcd(mat[i][row_idx], m)[0] == 1):
                nz_idx = i
                break
    
        if (nz_idx == -1):
            raise InverseError
    
        # Swap out this row with the other one
        swap_row(mat, row_idx, nz_idx)
        swap_row(res, row_idx, nz_idx)

        # Multiply this row with the element to make the head element one
        mult_factor = mod_inverse(mat[row_idx][row_idx], m)
        mult_row(mat, row_idx, mult_factor, m)
        mult_row(res, row_idx, mult_factor, m)

        # Clear out everything above and below
        for i in range(n):
            if (i != row_idx):
                # Clear out this row
                mult_factor = mat[i][row_idx]
                add_row(mat, i, row_idx, -mult_factor, m)
                add_row(res, i, row_idx, -mult_factor, m)

    return res

    

