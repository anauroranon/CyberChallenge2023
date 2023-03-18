import random
import binascii

ciphertext = 'a789762ed8eaf24212ba038a86652a9e913ac911050d9f6d69fad7e0a63173560d029650575657585154515959'

# Transforming from hex to bytes
unhex = binascii.unhexlify(ciphertext)

# From bytes to dec
ct_list = [x for x in unhex]

# Splitting ct in two parts
seedXOR97 = ct_list[-10:] #Taking last 10 elements
keyXORflag = ct_list[:-10] #Taking all elements except last 10


# Key length
key_length = flag_length = len(keyXORflag)

# Obtaining the seed
seed_list = []

for el in seedXOR97:
    seed_list.append(el^97)

seed = str(int(bytes(seed_list)))


# Creating key
random.seed(seed)
key = []

for i in range(key_length):
    key.append(random.randrange(256))
        
    
# Decryption
flag = []

for i in range(key_length):
      flag.append(chr(key[i] ^ keyXORflag[i]))

flag = ' '.join(str(el) for el in flag)

# Printing result
print("flag:", flag)
      


