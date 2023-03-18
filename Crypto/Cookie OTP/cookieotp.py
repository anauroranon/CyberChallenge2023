from pwn import remote
from Crypto.Util.strxor import strxor
import codecs

address = "cyberchallenge-web"
port = 9004
    

def talk_to_server():
    io = remote(address, port)

    # Send the plaintexts
    io.recvuntil(b"Hello! What's your name? ")
    io.sendline(b"ciao")

    res = io.recv().decode().split("! ")[1].split("\n")[0].encode()

    ct = codecs.decode(res, 'hex')
    pt = b"username=ciao&admin=False"

    key = strxor(pt, ct)
    print(key)

    hack = b"username=ciao&admin=True "
    new_ct = strxor(hack, key)

    io.sendline(codecs.encode(new_ct, 'hex'))
    res = io.recv()
    print(res)





if __name__ == "__main__":
    talk_to_server()