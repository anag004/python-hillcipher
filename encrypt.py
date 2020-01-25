from utils import *

key_filename = "key.in"
plaintext_filename = "plaintext.in"
ciphertext_filename = "ciphertext.out"
padding_letter = 'z'

# Read the key as a matrix
key = read_matrix("key.in")
key_length = len(key)

# Create file handles for plaintext and ciphertext
plaintext_fh = open(plaintext_filename, 'r')
ciphertext_fh = open(ciphertext_filename, 'w')

# Read the plaintext
plaintext = plaintext_fh.read()
plaintext_fh.close()

ciphertext = apply(key, plaintext, padding_letter)
print(ciphertext)

# Write the ciphertext to file
ciphertext_fh.write(ciphertext)
ciphertext_fh.close()

    







