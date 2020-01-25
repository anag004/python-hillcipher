# Break the Hill Cipher
from utils import *
import sys
import itertools

def get_key_length():
    if (len(sys.argv) != 2):
        print("Incorrect format. Correct format - python break.py <key length>")
        exit()
    else:
        return int(sys.argv[1])

key_length = get_key_length()

# Create a diagraph frequency table
freqs = []
idx = {}
num_diagraphs = 0
trial_length = 10
common_diagraphs = ["th", "he", "in", "er", "an", "re", "nd", "at", "on", "nt"]
tol = 0.003
ideal_ic = 0.0686

ciphertext = raw_input().replace(" ", '')
if (len(ciphertext) % key_length != 0):
    print("Ciphertext length not a multiple of key length")
    exit()

# Create a diagraph array
for i in range(0, len(ciphertext), 2):
    diagraph = ciphertext[i : i + 2]
    if (diagraph in idx):
        freqs[idx[diagraph]][0] += 1
    else:
        idx[diagraph] = num_diagraphs
        freqs.append([1, diagraph])
        num_diagraphs += 1
    
freqs.sort(reverse=True)

def get_key(d1, d2, e1, e2):
    mat1 = construct_matrix([d1, d2])
    mat2 = construct_matrix([e1, e2])
    mat1_inv = []
    try:
        mat1_inv = matrix_inverse(mat1, 26)
    except InverseError:
        return (False, False)
    key = matrix_mult2(mat2, mat1_inv, 26)
    key_inv = []
    try:
        key_inv = matrix_inverse(key, 26)
    except InverseError:
        return (False, False)
    return (key, key_inv)

(key, key_inv) = get_key("sp", "ea", "zs", "kk")

# Try various combinations of diagraphs
for c1 in itertools.combinations(range(trial_length), 2):
    for c2 in itertools.combinations(range(trial_length), 2):
        print("Trying " + common_diagraphs[c1[0]] + "->" + freqs[c2[0]][1] + " and " + common_diagraphs[c1[1]] + "->" + freqs[c2[1]][1])
        (key, key_inv) = get_key(common_diagraphs[c1[0]], common_diagraphs[c1[1]], freqs[c2[0]][1], freqs[c2[1]][1])
        if (key):
            plaintext = apply(matrix_inverse(key, 26), ciphertext, 'z')
            plaintext_ic = friedman(plaintext)
            if (abs(plaintext_ic - ideal_ic) <= tol):
                # This can be a correct value
                print("=" * 50)
                print(plaintext)
                print("=" * 50)