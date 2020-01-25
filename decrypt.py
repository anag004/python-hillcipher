from utils import *

key_filename = "key.in"
plaintext_filename = "plaintext.out"
ciphertext_filename = "ciphertext.in"
padding_letter = 'z'

# Read the key as a matrix
key = read_matrix("key.in")
key_length = len(key)

# Get the inverse of the key
key_inverse = matrix_inverse(key, 26)

# Create file handles for plaintext and ciphertext
plaintext_fh = open(plaintext_filename, 'w')
ciphertext_fh = open(ciphertext_filename, 'r')

# Read the ciphertext
ciphertext = ciphertext_fh.read()
ciphertext_fh.close()

# Create an empty plaintext character array
plaintext = []

plaintext = apply(key_inverse, ciphertext, padding_letter)

# Write the ciphertext to file
plaintext_fh.write(plaintext)
plaintext_fh.close()
