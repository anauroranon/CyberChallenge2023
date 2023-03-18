from Crypto.Random import random

def randbits(n):
    return [random.randint(0,1) for _ in range(n)]

def bitxor(args):
    res = 0
    for arg in args:
        res = int(res) ^ int(arg)
    return res

def strxor(al, bl):
    res = []
    for a, b in zip(al, bl):
        res.append(bitxor([a, b]))
    return res

####

def input_bits(query, STRING_SIZE):
    s = input(query)
    if any(c != '0' and c != '1' for c in s):
        print("Your input must be a bitstring.")
        exit(-1)
    if len(s) != STRING_SIZE:
        print(f"All strings must be of length {STRING_SIZE}.")
        exit(-1)
    bitstring = [int(c) for c in s]
    return bitstring

def bits_to_string(bitstring):
    return "".join(str(b) for b in bitstring)
