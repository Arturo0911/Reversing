#!/usr/bin/python3


buffer = "\x55" * (1040 - 100 - 150 - 4)
nops = "\x90" * 100
shellcode = "\x44" * 150
eip = "\x66" * 4
print(buffer)
print(len(buffer))


print(f"buffer lenght {len(buffer)} buffer: {buffer}")

print(f"nops lenght {len(nops)} nops {nops}")

print(f"shellcode lenght {len(shellcode)} shellcode: {shellcode}")

print(f"eip lenght {len(eip)} eip: {eip}")
