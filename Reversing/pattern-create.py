#!/usr/bin/python3

import sys



def main():
    size = sys.argv[1]
    first = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    second = "abcdefghijklmnopqrstuvwxyz"
    value = range(0, 10)
    payload = ""
    flag=False
    for x in first:
        for y in second:
            for z in value:
                payload += x+y+str(z)
                if len(payload) >= size:
                    flag = True
                    payload = payload[:200]
                    break
            if flag:
                break
        if flag:
            break

    print(payload)


if __name__ == "__main__":
    main()
