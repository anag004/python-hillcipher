from utils import *

key_filename = "key.in"
plaintext_filename = "plaintext.out"
ciphertext_filename = "ciphertext.in"

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

# Iterate over the ciphertext
curr_idx = 0
while curr_idx < len(ciphertext):
    # Create the string to be processed with x's
    curr_text = [24 for i in range(key_length)]
    # Keep track of the positions at which character should be inserted into the ciphertext
    insert_positions = []
    # Count the number of characters read from the plaintext
    read_ctr = 0
    # Build up curr_text
    while(read_ctr < key_length and curr_idx < len(ciphertext)):
        if (ciphertext[curr_idx].isalpha()):
            # This is a character
            curr_text[read_ctr] = char2num(ciphertext[curr_idx])
            # Put a dummy character into the ciphertext
            plaintext.append('x')
            insert_positions.append(curr_idx)
            # Increment both counters
            read_ctr += 1
            curr_idx += 1
        else:
            # Copy the plaintext character into the ciphertext
            plaintext.append(ciphertext[curr_idx])
            curr_idx += 1

    # Do matrix multiplication mod 26 and get encrypted text
    decrypted_text = matrix_mult(key_inverse, curr_text, 26)

    # Place the text into the ciphertext
    for i in range(read_ctr):
        plaintext[insert_positions[i]] = num2char(decrypted_text[i])
    
    if read_ctr < key_length:
        raise IncorrectLength("Ciphertext length is not a multiple of key length")

# Convert the plaintext to a string
plaintext = ''.join(plaintext)

# Write the ciphertext to file
plaintext_fh.write(plaintext)
plaintext_fh.close()
