from utils import *

key_filename = "key.in"
padding_letter = 'z'

# Read the key as a matrix
key = read_matrix("key.in")
key_length = len(key)

# Get the inverse of the key
key_inverse = matrix_inverse(key, 26)

# Read the ciphertext
ciphertext = get_input()

# Create an empty plaintext character array
plaintext = []

plaintext = apply(key_inverse, ciphertext, padding_letter)

print(plaintext)
