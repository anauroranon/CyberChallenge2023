from Crypto.Random import random
from utils import randbits, strxor 

STRING_SIZE = 16
WINS_NEEDED = 750
TRIES = 1000

# encrypt generates a random bit (0 or 1) and depending on that bit, it can generate two k:
# if b=0: random_vector; if b=1: vector of 0s or 1s
# it computes the xor with this k and the plaintext

def encrypt(pt):
    bp = random.randint(0,1)
    if bp == 0:
        k = randbits(STRING_SIZE)
    else:
        k = randbits(1) * STRING_SIZE
       
    ct = strxor(k, pt)
    return ct
