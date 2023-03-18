import os
#from secret import FLAG

FLAG = b'srdnlen{'

for i in range(42):
    FLAG = FLAG + b'i'

FLAG = FLAG + b'}'


assert FLAG.startswith(b"srdnlen{")
assert FLAG.endswith(b"}")
assert len(FLAG) == 51


def xor(key, data):
    # Xor-ing the key with the data. The key is keylength*datalength size. 8 * datalength
    b = bytes(x ^ y for x, y in zip(key * len(data), data))
    print("xoring key:", key, "with data:", data, ": \n", b)
    print("length of b: ", len(b))
    return b


def viscrypt(data):
    # xoring data with data minus first element plus random end element
    return xor(data, data[1:] + b"\xaa")


def round(key, rawdata):
    # viscrypting the xor between key and raw data.
    return viscrypt(xor(key, rawdata))

# 1. Xor between key and flag. the flag is 51 while the key is 8.
# 2. xor between key^flag and key^flag -1 +1.
# 3. hex the ciphertext.


key = os.urandom(8)
print("key: ", key)
print("keylength: ", len(key))


pt = FLAG
print("flag:", FLAG)
print("flag length:", len(FLAG))

ct = round(key, pt)
print("ct:", ct)
print("ct:", len(ct))


# with open("ciphertext.txt", "w") as f:
#     f.write(ct.hex())

print("cthex", ct.hex())
print("cthex length", len(ct.hex()))
