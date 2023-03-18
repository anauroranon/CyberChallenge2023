import codecs
from Crypto.Util.strxor import strxor
from Crypto.Random import get_random_bytes

key = None


def encrypt(pt):
    global key

    key = get_random_bytes(len(pt))
    byte_ct = strxor(key, pt)
    hex_ct = codecs.encode(byte_ct, 'hex')

    return hex_ct


def decrypt(ct):
    global key

    byte_ct = codecs.decode(ct, 'hex')
    pt = strxor(key, byte_ct)

    return pt
