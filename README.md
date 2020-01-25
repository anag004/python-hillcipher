# Python Hill Cipher
> Python scripts for encryption, decryption and cryptanalysis of the Hill Cipher

# Encryption
Write the encryption key in the file `key.in`. The script `encrypt.py` encrypts plaintext passed through STDIN and prints the answer to STDOUT

# Decryption
Write the encryption key in the file `key.in`. The script `decrypt.py` decrypts plaintext passed through STDIN and prints the answer to STDOUT. 

# Cryptanalysis
To break the hill cipher, run `python break.py <key-length>` and pass the ciphertext through STDIN. The program will print possible keys on STDOUT. If there is no result, consider increasing the tolerance value `tol` inside the script. 

