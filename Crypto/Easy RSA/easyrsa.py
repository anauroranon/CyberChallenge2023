from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime
from pwn import remote

# Server connection
address = "cyberchallenge-web"
port = 9016

#Info collected from server
message = b'Give me the flag'

# RSA Encryption
nbits = 512
e = 65537

p, q = getPrime(nbits), getPrime(nbits)
Nc = p*q
print("Nc:", Nc)

# Encryption
def encryption(x, e, N):
    return pow(bytes_to_long(x), e, N)

# Decryption
def decryption(x, d, N):
    return long_to_bytes(pow(x, d, N))

def phi(p, q):
    return (p-1)*(q-1)

def privatekey(e, p, q):
    return pow(e, -1, phi(p,q))


Ns = int(input("Ns"))
print("enc: ", encryption(message,e,Ns))
flag = int(input("flag"))
print("dec: ", decryption(flag, privatekey(e, p, q), Nc))

