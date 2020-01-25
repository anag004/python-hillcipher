# Break the Hill Cipher
from utils import *
import sys
import itertools
from copy import deepcopy

class IncorrectLength(Exception):
    pass

class IncorrectFormat(Exception):
    pass

def get_key_length():
    if (len(sys.argv) != 2 or int(sys.argv[1]) > 3):
        raise IncorrectFormat("Correct format - python break.py <2 | 3>")
        exit()
    else:
        return int(sys.argv[1])

key_length = get_key_length()

# Create a ngraph frequency table
freqs = []
idx = {}
num_ngraphs = 0
common_ngraphs = []
common_ngraphs.append(["th", "he", "in", "er", "an", "re", "nd", "at", "on", "nt", "ha", "es", "st", "en", "ed", "to", "it", "ou"])
common_ngraphs.append(["the", "and", "ing", "ent", "ion", "her", "for", "tha", "nth", "int", "ere", "tio", "ter", "est", "ers", "ati", "hat", "ate", "all", "eth", "hes", "ver", "his", "oft", "ith", "fth", "sth", "oth", "res", "ont"])
trial_length = len(common_ngraphs[key_length - 2])
tol = 0.004
ideal_ic = 0.0686

ciphertext = raw_input()

# Create a diagraph array
read_ctr = 0
while(read_ctr < len(ciphertext)):
    ngraph = []
    while(len(ngraph) < key_length):
        if (read_ctr >= len(ciphertext)):
            raise IncorrectLength("Length of ciphertext is not multiple of key length")
        if (ciphertext[read_ctr].isalpha()):
            ngraph.append(ciphertext[read_ctr])
        read_ctr += 1
    # Process the diagraph
    ngraph = ''.join(ngraph)
    if (ngraph in idx):
        freqs[idx[ngraph]][0] += 1
    else:
        idx[ngraph] = num_ngraphs
        freqs.append([1, ngraph])
        num_ngraphs += 1

freqs.sort(reverse=True)

def get_mapping(c1, c2):
    s = ""
    for i in range(len(c1)):
        s += common_ngraphs[key_length - 2][c1[i]] + "->" + freqs[c2[i]][1] + ", "
    return s

num_possibles = 0
found_keys = []
# Try various combinations of diagraphs
for c1 in itertools.combinations(range(trial_length), key_length):
    for c2 in itertools.combinations(range(min(trial_length, len(freqs))), key_length):
        (key, key_inv, verdict) = get_key([common_ngraphs[key_length - 2][c1[i]] for i in range(key_length)], [freqs[c2[i]][1] for i in range(key_length)])
        # Uncomment when trying to debug
        # print("Trying: " + str(num_possibles) + ": " + get_mapping(idx, freqs, c1, c2))
        if (key != False):
            plaintext = apply(key_inv, ciphertext, 'z')
            plaintext_ic = friedman(plaintext)
            if (abs(plaintext_ic - ideal_ic) <= tol and (key not in found_keys)):
                # This can be a correct value
                num_possibles += 1
                print("Possible decryption #" + str(num_possibles) + ": " + get_mapping(c1, c2))
                print("KEY: " + str(key))
                found_keys.append(key)
                print("=" * 50)
                print(plaintext)
                print("=" * 50)