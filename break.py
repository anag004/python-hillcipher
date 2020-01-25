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

# Create a diagraph frequency table
freqs = []
idx = {}
num_diagraphs = 0
common_diagraphs = ["th", "he", "in", "er", "an", "re", "nd", "at", "on", "nt", "ha", "es", "st", "en", "ed", "to", "it", "ou"]
trial_length = len(common_diagraphs)
tol = 0.004
ideal_ic = 0.0686

ciphertext = raw_input()

# Create a diagraph array
read_ctr = 0
while(read_ctr < len(ciphertext)):
    diagraph = []
    while(len(diagraph) < 2):
        if (read_ctr >= len(ciphertext)):
            raise IncorrectLength("Length of ciphertext is not multiple of key length")
        if (ciphertext[read_ctr].isalpha()):
            diagraph.append(ciphertext[read_ctr])
        read_ctr += 1
    # Process the diagraph
    diagraph = ''.join(diagraph)
    if (diagraph in idx):
        freqs[idx[diagraph]][0] += 1
    else:
        idx[diagraph] = num_diagraphs
        freqs.append([1, diagraph])
        num_diagraphs += 1

freqs.sort(reverse=True)

num_possibles = 0
found_keys = []
# Try various combinations of diagraphs
for c1 in itertools.combinations(range(trial_length), 2):
    for c2 in itertools.combinations(range(min(trial_length, len(freqs))), 2):
        (key, key_inv, verdict) = get_key(common_diagraphs[c1[0]], common_diagraphs[c1[1]], freqs[c2[0]][1], freqs[c2[1]][1])
        # Uncomment when trying to debug
        # print("Trying: " + str(num_possibles) + ": " + common_diagraphs[c1[0]] + "->" + freqs[c2[0]][1] + ", " + common_diagraphs[c1[1]] + "->" + freqs[c2[1]][1] + ": " + verdict)
        if (key != False):
            plaintext = apply(key_inv, ciphertext, 'z')
            plaintext_ic = friedman(plaintext)
            if (abs(plaintext_ic - ideal_ic) <= tol and (key not in found_keys)):
                # This can be a correct value
                num_possibles += 1
                print("Possible decryption #" + str(num_possibles) + ": " + common_diagraphs[c1[0]] + "->" + freqs[c2[0]][1] + ", " + common_diagraphs[c1[1]] + "->" + freqs[c2[1]][1])
                print("KEY: " + str(key))
                found_keys.append(key)
                print("=" * 50)
                print(plaintext)
                print("=" * 50)