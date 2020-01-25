# Python Hill Cipher
> Python scripts for encryption, decryption and cryptanalysis of the Hill Cipher

1. Inputs are given via files. `key.in` contains an invertible (modulo 26) square matrix of integers. 
2. `plaintext.in` contains the string to be encrypted
3. Running `python encrypt.py` creates the file `ciphertext.out` which is the encrypted plaintext
4. The file `ciphertext.in` contains the ciphertext which is to be decrypted
5. Running `python decrypt.py` creates a file `plaintext.out` which contains the decrypted ciphertext.

# # Try various combinations of diagraphs
# for c1 in itertools.combinations(range(trial_length), 2):
#     for c2 in itertools.combinations(range(trial_length), 2):
#         print("Trying " + common_diagraphs[c1[0]] + "->" + freqs[c2[0]][1] + " and " + common_diagraphs[c1[1]] + "->" + freqs[c2[1]][1])
#         (key, key_inv) = get_key(common_diagraphs[c1[0]], common_diagraphs[c1[1]], freqs[c2[0]][1], freqs[c2[1]][1])
#         if (key):
#             print(key)
#             plaintext = apply(matrix_inverse(key, 26), ciphertext, 'z')
#             plaintext_ic = friedman(plaintext)
#             if (abs(plaintext_ic - ideal_ic) <= tol):
#                 # This can be a correct value
#                 print("=" * 50)
#                 print(plaintext)
#                 print("=" * 50)