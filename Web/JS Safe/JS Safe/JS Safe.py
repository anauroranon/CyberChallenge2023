Uint8Array = bytearray([159, 134, 208, 129, 136, 76, 125, 101, 154, 47, 234, 160, 197, 90, 208, 21, 163, 191, 79, 27, 43, 11, 130, 44, 209, 93, 108, 21, 176, 240, 10, 8]).hex()
#de-hash it with crackstation. RESULT: the SHA256 hash of what we entered
print(Uint8Array)

Uint8Array2 = bytearray([230, 104, 96, 84, 111, 24, 205, 187, 205, 134, 179, 94, 24, 181, 37, 191, 252, 103, 247, 114, 198, 80, 206, 223, 227, 255, 122, 0, 38, 250, 29, 238]).hex()
#de-hash it with crackstation. RESULT: the SHA256 hash of 'Passw0rd!'
print(Uint8Array2)