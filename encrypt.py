from utils import *

key_filename = "key.in"
plaintext_filename = "plaintext.in"
ciphertext_filename = "ciphertext.out"

# Read the key as a matrix
key = read_matrix("key.in")
key_length = len(key)

# Create file handles for plaintext and ciphertext
plaintext_fh = open(plaintext_filename, 'r')
ciphertext_fh = open(ciphertext_filename, 'w')

# Read the plaintext
plaintext = plaintext_fh.read()
plaintext_fh.close()

# Create an empty ciphertext character array
ciphertext = []

# Iterate over the plaintext
curr_idx = 0
while curr_idx < len(plaintext):
    # Create the string to be processed with x's
    curr_text = [24 for i in range(key_length)]
    # Keep track of the positions at which character should be inserted into the ciphertext
    insert_positions = []
    # Count the number of characters read from the plaintext
    read_ctr = 0
    # Build up curr_text
    while(read_ctr < key_length and curr_idx < len(plaintext)):
        if (plaintext[curr_idx].isalpha()):
            # This is a character
            curr_text[read_ctr] = char2num(plaintext[curr_idx])
            # Put a dummy character into the ciphertext
            ciphertext.append('x')
            insert_positions.append(curr_idx)
            # Increment both counters
            read_ctr += 1
            curr_idx += 1
        else:
            # Copy the plaintext character into the ciphertext
            ciphertext.append(plaintext[curr_idx])
            curr_idx += 1

    # Do matrix multiplication mod 26 and get encrypted text
    encrypted_text = matrix_mult(key, curr_text, 26)

    # Place the text into the ciphertext
    for i in range(read_ctr):
        ciphertext[insert_positions[i]] = num2char(encrypted_text[i])
    
    # Append the residual ciphertext
    for i in range(read_ctr, key_length):
        ciphertext.append(num2char(encrypted_text[i]))

# Convert the ciphertext to a string
ciphertext = ''.join(ciphertext)

# Write the ciphertext to file
ciphertext_fh.write(ciphertext)
ciphertext_fh.close()

    







