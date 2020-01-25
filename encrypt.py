from utils import *

key_filename = "key.in"
padding_letter = 'z'

# Read the key as a matrix
key = read_matrix("key.in")
key_length = len(key)

plaintext = raw_input()

ciphertext = apply(key, plaintext, padding_letter)
print(friedman(plaintext))
print(friedman(ciphertext))
print(ciphertext)

    







