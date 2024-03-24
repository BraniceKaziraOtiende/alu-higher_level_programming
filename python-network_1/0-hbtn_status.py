#!/usr/bin/env python3

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        print(f'Body response:\n\t- type: {type(response.read())}\n\t-'
              f' content: {response.read()}\n\t- utf8 content: {response.read().decode("utf-8")}')
