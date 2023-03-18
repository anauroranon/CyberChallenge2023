import random
import time
 
#from secret import FLAG
FLAG = b'FLAG'

# seed = str(round(time.time()))
seed = str(1678207057)
print("seed", seed)
random.seed(seed)

key = []
for i in range(len(FLAG)):
	key.append(random.randrange(256))
        
print("key", key)

ct = [m ^ k for m, k in zip(FLAG + seed.encode(), key + [ord("a")] * len(seed))]
print(ct)

a = FLAG + seed.encode()
print("FLAG + seed", a )
b = key + [ord("a")] * len(seed)
print("key + len", b )
z = zip(a,b)

print("ciphertext", bytes(ct).hex())


# with open("ciphertext.txt", "w") as f:
#     f.write(bytes(ct).hex())
