from utils import *

key_filename = "key.in"
padding_letter = 'z'

# Read the key as a matrix
key = read_matrix("key.in")
key_length = len(key)

plaintext = get_input()

ciphertext = apply(key, plaintext, padding_letter)
print(ciphertext)

    







