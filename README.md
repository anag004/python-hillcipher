CPP programs implementing a Hill cryptosystem. 

* How to use *
0. Compile all files by running `make`
1. Inputs are given via files. `key.txt` contains an invertible (modulo 26) square matrix of integers. 
2. `plaintext.in` contains the string to be encrypted
3. Running `./encrypt.o` creates the file `ciphertext.out` which is the encrypted plaintext
4. The file `ciphertext.in` contains the ciphertext which is to be decrypted
5. Running `./decrypt.o` creates a file `plaintext.out` which contains the decrypted ciphertext.
