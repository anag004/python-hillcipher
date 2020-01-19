# Python Hill Cipher
> Python scripts for encryption, decryption and cryptanalysis of the Hill Cipher

1. Inputs are given via files. `key.in` contains an invertible (modulo 26) square matrix of integers. 
2. `plaintext.in` contains the string to be encrypted
3. Running `python encrypt.py` creates the file `ciphertext.out` which is the encrypted plaintext
4. The file `ciphertext.in` contains the ciphertext which is to be decrypted
5. Running `python decrypt.py` creates a file `plaintext.out` which contains the decrypted ciphertext.
