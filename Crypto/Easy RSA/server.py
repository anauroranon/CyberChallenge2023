from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime
import os

FLAG = os.environ['FLAG']

print("Welcome to my super secure communication server")

nbits = 512
e = 65537

p, q = getPrime(nbits), getPrime(nbits)
N = p*q

print("\nMy public key is:")
print(f"\te: {e}")
print(f"\tN: {N}")

print("\nPlease send me your public modulus (please use 512bits primes):")
N_user = int(input())
if len(bin(N_user)[2:]) < nbits - 24:
    print("nope")
    exit(-1)

print("\nPlease send me this encrypted phrase so I can understand it:")
print('''"Give me the flag" (caps sensitive)''')
ct = int(input())

if ct == pow(bytes_to_long(b"Give me the flag"), e, N):
    print(f"GG, here is your flag: {pow(bytes_to_long(FLAG), e, N_user)}")
else:
    print("I can't understand what you sent me")
