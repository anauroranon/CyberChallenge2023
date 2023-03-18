from Crypto.Random import random
from utils import randbits, strxor 

STRING_SIZE = 16

WINS_NEEDED = 1000
TRIES = 1000

def encrypt(pt):
    k = randbits(STRING_SIZE//2) * 2
       
    ct = strxor(k, pt)
    return ct
