import os
import binascii

# Ciphertexy
ct = '5e904cfb42a18e054f9b04a057ab81421b9c18b046a59b1f48914de312e58b011dc25bfe15e6d75f54941cb04abc8112569534'

# Creating pseudo flag
# FLAG = b'sdrnlen{'

# for i in range(42):
#     FLAG = FLAG + b'i'

# FLAG = FLAG + b'}'

# print (len(FLAG))
# print(FLAG)


# Transforming from hex to bytes
unhex = binascii.unhexlify(ct)

# Obtaining the key xored with the flag
