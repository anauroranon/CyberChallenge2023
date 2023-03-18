from utils import randbits, strxor, bitxor 

STRING_SIZE = 16
WINS_NEEDED = 1000
TRIES = 1000

def encrypt(pt):
    kpart = randbits(STRING_SIZE-1)
    klast = [bitxor(kpart)]
    k = kpart + klast 
       
    ct = strxor(k, pt)
    return ct
